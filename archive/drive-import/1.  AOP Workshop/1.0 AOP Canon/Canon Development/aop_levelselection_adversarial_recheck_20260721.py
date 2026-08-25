#!/usr/bin/env python3
"""Independent adversarial checks of F1 and F4 for AOP canon v1.21 §13a."""

from __future__ import annotations

import itertools
import numpy as np


def covariance(n: int, b: float, a: float = 1.0) -> np.ndarray:
    half = n // 2
    w = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            w[i, j] = w[j, i] = a if ((i < half) == (j < half)) else b
    lap = np.diag(w.sum(axis=1)) - w
    return np.linalg.inv(np.eye(n) + lap)


def logdet(x: np.ndarray) -> float:
    sign, value = np.linalg.slogdet(x)
    assert sign > 0
    return float(value)


def mi(sigma: np.ndarray, left: tuple[int, ...]) -> float:
    n = len(sigma)
    right = tuple(i for i in range(n) if i not in left)
    aa = sigma[np.ix_(left, left)]
    bb = sigma[np.ix_(right, right)]
    return 0.5 * (logdet(aa) + logdet(bb) - logdet(sigma))


def phi(sigma: np.ndarray) -> tuple[float, tuple[tuple[int, ...], ...]]:
    n = len(sigma)
    cuts = []
    for r in range(1, n):
        for left in itertools.combinations(range(n), r):
            if 0 in left:
                cuts.append((mi(sigma, left), left))
    best = min(x[0] for x in cuts)
    return best, tuple(left for value, left in cuts if abs(value - best) < 1e-10)


def values(b: float) -> tuple[float, float]:
    whole_sigma = covariance(8, b)
    whole = phi(whole_sigma)[0]
    module_sigma = whole_sigma[np.ix_(range(4), range(4))]
    module = phi(module_sigma)[0]
    return module, whole


def bisect_difference(per_node: bool) -> float:
    def difference(b: float) -> float:
        module, whole = values(b)
        if per_node:
            module, whole = module / 4.0, whole / 8.0
        return whole - module
    lo, hi = 0.0, 1.4
    if difference(lo) * difference(hi) >= 0:
        raise ValueError((difference(lo), difference(hi)))
    for _ in range(100):
        mid = (lo + hi) / 2
        if difference(lo) * difference(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def derivative(f, x: float, h: float = 1e-6) -> tuple[float, float]:
    return (f(x) - f(x - h)) / h, (f(x + h) - f(x)) / h


def main() -> None:
    bstar = 0.330221124862
    print("F1 raw whole-system Phi_MIP")
    for b in (0.330, 0.3302, bstar, 0.34):
        p, cuts = phi(covariance(8, b))
        print(f"b={b:.12f} phi={p:.12f} winners={cuts}")
    dl, dr = derivative(lambda b: phi(covariance(8, b))[0], bstar)
    print(f"one-sided numerical slopes at b*: left={dl:.9f} right={dr:.9f} jump={dr-dl:.9f}")

    print("\nF4 module-vs-whole comparison")
    try:
        print(f"raw equality b={bisect_difference(False):.12f}")
    except ValueError as e:
        print(f"raw has no bracketed equality: {e}")
    try:
        print(f"per-node equality b={bisect_difference(True):.12f}")
    except ValueError as e:
        print(f"per-node has no bracketed equality: endpoint differences={e}")
    for b in (0.0, 0.1, 0.330221124862, 0.5, 1.0, 1.4, 10.0):
        module, whole = values(b)
        print(f"b={b:.12f} module={module:.12f} whole={whole:.12f} "
              f"winner_raw={'whole' if whole > module else 'module'} "
              f"module/N={module/4:.12f} whole/N={whole/8:.12f} "
              f"winner_per_node={'whole' if whole/8 > module/4 else 'module'}")


if __name__ == "__main__":
    main()
