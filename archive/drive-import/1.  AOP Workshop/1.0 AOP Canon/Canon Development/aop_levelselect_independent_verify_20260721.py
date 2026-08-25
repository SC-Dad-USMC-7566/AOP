#!/usr/bin/env python3
"""Independent verification of the AOP section 13a level-selection model.

Built from the work-order specification, not from phaseD1_levelselect.py.

Model
-----
N nodes in two equal complete modules.  Intra-module edges have weight a=1,
inter-module edges weight b, L is the weighted graph Laplacian, and
Sigma = (I + g L)^(-1), with g=1.

Every unordered, non-trivial bipartition is enumerated exactly.  Three MIP
selectors are compared:
  raw       I(A;B)
  size      I(A;B) / min(|A|, |B|)
  entropy   I(A;B) / min(h(A), h(B))
where h is Gaussian differential entropy in nats.
"""

from __future__ import annotations

import argparse
import itertools
import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Partition:
    left: tuple[int, ...]
    right: tuple[int, ...]


def partitions(n: int) -> list[Partition]:
    """Enumerate unordered bipartitions once, canonically placing node 0 left."""
    nodes = tuple(range(n))
    out: list[Partition] = []
    for r in range(1, n):
        for left in itertools.combinations(nodes, r):
            if 0 not in left:
                continue
            right = tuple(i for i in nodes if i not in left)
            out.append(Partition(left, right))
    assert len(out) == 2 ** (n - 1) - 1
    return out


def covariance(n: int, b: float, a: float = 1.0, g: float = 1.0) -> np.ndarray:
    if n % 2:
        raise ValueError("N must be even")
    half = n // 2
    weights = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(i + 1, n):
            same_module = (i < half) == (j < half)
            weights[i, j] = weights[j, i] = a if same_module else b
    laplacian = np.diag(weights.sum(axis=1)) - weights
    return np.linalg.inv(np.eye(n) + g * laplacian)


def logdet(matrix: np.ndarray) -> float:
    sign, value = np.linalg.slogdet(matrix)
    if sign <= 0:
        raise ArithmeticError("Expected a positive-definite covariance submatrix")
    return float(value)


def marginal_entropy(sigma: np.ndarray, part: tuple[int, ...]) -> float:
    sub = sigma[np.ix_(part, part)]
    k = len(part)
    return 0.5 * (k * math.log(2.0 * math.pi * math.e) + logdet(sub))


def mutual_information(sigma: np.ndarray, p: Partition) -> float:
    aa = sigma[np.ix_(p.left, p.left)]
    bb = sigma[np.ix_(p.right, p.right)]
    return 0.5 * (logdet(aa) + logdet(bb) - logdet(sigma))


def score(sigma: np.ndarray, p: Partition, selector: str) -> float:
    mi = mutual_information(sigma, p)
    if selector == "raw":
        return mi
    if selector == "size":
        return mi / min(len(p.left), len(p.right))
    if selector == "entropy":
        normalizer = min(marginal_entropy(sigma, p.left), marginal_entropy(sigma, p.right))
        if normalizer <= 0:
            raise ArithmeticError("Non-positive differential-entropy normalizer")
        return mi / normalizer
    raise ValueError(selector)


def signature(n: int, p: Partition) -> str:
    half = n // 2
    module0, module1 = set(range(half)), set(range(half, n))
    left, right = set(p.left), set(p.right)
    small = min(len(left), len(right))
    if left in (module0, module1) or right in (module0, module1):
        return "module-boundary"
    if small == 1:
        singleton = tuple(sorted(left if len(left) == 1 else right))
        return f"singleton{singleton}"
    if len(left) == len(right):
        return f"balanced-cross {len(left)}|{len(right)}"
    return f"unbalanced-cross {len(left)}|{len(right)}"


def minima(n: int, b: float, selector: str, tol: float = 1e-10):
    sigma = covariance(n, b)
    scored = [(score(sigma, p, selector), p) for p in partitions(n)]
    best = min(v for v, _ in scored)
    winners = [(v, p) for v, p in scored if abs(v - best) <= tol * max(1.0, abs(best))]
    signatures = sorted({signature(n, p) for _, p in winners})
    return best, winners, signatures


def scan(n: int, selector: str, step: float):
    bs = np.round(np.arange(0.0, 1.4 + step / 2.0, step), 12)
    rows = []
    previous = None
    for b in bs:
        value, winners, signatures = minima(n, float(b), selector)
        state = tuple(signatures)
        if state != previous:
            rows.append((float(b), value, state, winners[0][1]))
            previous = state
    return rows


def raw_module_singleton_crossover(n: int) -> float:
    """Bisection root where the raw module cut and a singleton cut tie."""
    half = n // 2
    module = Partition(tuple(range(half)), tuple(range(half, n)))
    singleton = Partition((0,), tuple(range(1, n)))

    def difference(b: float) -> float:
        sigma = covariance(n, b)
        return score(sigma, module, "raw") - score(sigma, singleton, "raw")

    lo, hi = 0.0, 1.0
    if not (difference(lo) < 0.0 and difference(hi) > 0.0):
        raise ArithmeticError("Raw module/singleton crossover is not bracketed")
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if difference(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def format_partition(p: Partition) -> str:
    return f"{p.left}|{p.right}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--step", type=float, default=0.01, help="b-ramp resolution")
    args = parser.parse_args()
    if args.step <= 0:
        raise SystemExit("--step must be positive")

    print("Independent exhaustive Gaussian MIP verification")
    print(f"b ramp: 0.00..1.40; step={args.step:g}; a=g=1")
    for n in (6, 8):
        print(f"\nN={n} ({2 ** (n - 1) - 1} unordered bipartitions)")
        print(
            "  raw module/singleton equality: "
            f"b*={raw_module_singleton_crossover(n):.12f}"
        )
        for selector in ("raw", "size", "entropy"):
            print(f"  selector={selector}")
            for b, value, states, representative in scan(n, selector, args.step):
                state_text = "; ".join(states)
                print(
                    f"    from b={b:0.2f}: {state_text}; "
                    f"score={value:.12g}; representative={format_partition(representative)}"
                )

    print("\nSelected checkpoints")
    for n in (6, 8):
        for b in (0.0, 0.3, 0.4, 0.41, 0.42, 0.43, 0.5, 0.99, 1.0, 1.01, 1.4):
            fields = [f"N={n}", f"b={b:.2f}"]
            for selector in ("raw", "size", "entropy"):
                _, winners, states = minima(n, b, selector)
                fields.append(f"{selector}={'/'.join(states)} [{format_partition(winners[0][1])}]")
            print("; ".join(fields))


if __name__ == "__main__":
    main()
