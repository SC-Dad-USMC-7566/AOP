#!/usr/bin/env python3
"""Independent numerical checks for the adversarial review of AOP §13a.

Reimplemented from the work-order model specification.  This script does not
import or execute any deposited AOP/Prime/Aster implementation.
"""

from itertools import combinations

import numpy as np
from scipy.optimize import brentq


def covariance(n: int, b: float, a: float = 1.0, g: float = 1.0) -> np.ndarray:
    half = n // 2
    weights = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(i + 1, n):
            same_module = (i < half) == (j < half)
            weights[i, j] = weights[j, i] = a if same_module else b
    laplacian = np.diag(weights.sum(axis=1)) - weights
    return np.linalg.inv(np.eye(n) + g * laplacian)


def unordered_bipartitions(n: int):
    """Enumerate each nontrivial bipartition once by requiring node 0 in A."""
    nodes = tuple(range(n))
    for size in range(1, n):
        for part in combinations(nodes[1:], size - 1):
            a = (0,) + part
            if len(a) == n:
                continue
            b = tuple(i for i in nodes if i not in a)
            yield a, b


def gaussian_mi(sigma: np.ndarray, a, b) -> float:
    aa = sigma[np.ix_(a, a)]
    bb = sigma[np.ix_(b, b)]
    return 0.5 * (
        np.linalg.slogdet(aa)[1]
        + np.linalg.slogdet(bb)[1]
        - np.linalg.slogdet(sigma)[1]
    )


def raw_mip(sigma: np.ndarray):
    scored = [
        (gaussian_mi(sigma, a, b), a, b)
        for a, b in unordered_bipartitions(len(sigma))
    ]
    best = min(x[0] for x in scored)
    ties = [(a, b) for score, a, b in scored if abs(score - best) <= 1e-10]
    return best, ties


def whole_phi(b: float) -> float:
    return raw_mip(covariance(8, b))[0]


def module_phi(b: float) -> float:
    sigma = covariance(8, b)
    return raw_mip(sigma[:4, :4])[0]


def module_phi_conditional(b: float) -> float:
    sigma = covariance(8, b)
    aa = sigma[:4, :4]
    ae = sigma[:4, 4:]
    ee = sigma[4:, 4:]
    conditional = aa - ae @ np.linalg.solve(ee, ae.T)
    return raw_mip(conditional)[0]


def module_phi_induced() -> float:
    # For n=4, setting a=b=1 makes all six edges equal: the induced K4 module.
    return raw_mip(covariance(4, 1.0))[0]


def two_supernode_phi(b: float) -> float:
    sigma = covariance(8, b)
    w = np.zeros((2, 8))
    w[0, :4] = 0.25
    w[1, 4:] = 0.25
    macro_sigma = w @ sigma @ w.T
    return raw_mip(macro_sigma)[0]


def derivative(f, x: float, h: float, side: str) -> float:
    if side == "left":
        return (f(x) - f(x - h)) / h
    return (f(x + h) - f(x)) / h


def main() -> None:
    raw_relabel = 0.330221124862
    print("F1 values")
    for b in (0.3300, 0.3302, raw_relabel, 0.3400):
        print(f"b={b:.12f} whole_phi={whole_phi(b):.12f}")
    for h in (1e-4, 1e-5, 1e-6, 1e-7):
        left = derivative(whole_phi, raw_relabel, h, "left")
        right = derivative(whole_phi, raw_relabel, h, "right")
        print(f"h={h:.0e} left={left:.9f} right={right:.9f} jump={right-left:.9f}")

    root = brentq(lambda x: module_phi(x) - whole_phi(x), 0.25, 0.35,
                  xtol=1e-14, rtol=1e-14)
    print("\nF4 raw module-whole equality")
    print(f"root={root:.12f}")
    for b in (0.0, root, raw_relabel, 0.5, 1.0, 1.4, 10.0):
        m = module_phi(b)
        w = whole_phi(b)
        print(
            f"b={b:.12f} module={m:.12f} whole={w:.12f} "
            f"module/4={m/4:.12f} whole/8={w/8:.12f}"
        )

    print("\nEnvironmental-treatment sensitivity")
    isolated = module_phi_induced()
    print(f"induced/isolated module phi={isolated:.12f}")
    for label, f in (("marginal", module_phi), ("conditional", module_phi_conditional)):
        roots = []
        grid = np.linspace(0.0, 10.0, 2001)
        values = [f(x) - whole_phi(x) for x in grid]
        for lo, hi, vlo, vhi in zip(grid[:-1], grid[1:], values[:-1], values[1:]):
            if vlo == 0.0:
                roots.append(lo)
            elif vlo * vhi < 0:
                roots.append(brentq(lambda x: f(x) - whole_phi(x), lo, hi))
        print(f"{label} roots={roots}")
        for b in (0.0, 0.3, raw_relabel, 1.0, 1.4):
            print(f"  b={b:.6f} module={f(b):.12f} whole={whole_phi(b):.12f}")

    induced_roots = []
    grid = np.linspace(0.0, 10.0, 2001)
    vals = [isolated - whole_phi(x) for x in grid]
    for lo, hi, vlo, vhi in zip(grid[:-1], grid[1:], vals[:-1], vals[1:]):
        if vlo * vhi < 0:
            induced_roots.append(brentq(lambda x: isolated - whole_phi(x), lo, hi))
    print(f"induced/isolated roots={induced_roots}")

    print("\nLiteral two-supernode coarse grain (module averages)")
    for b in (0.0, 0.1, 0.3, raw_relabel, 0.5, 1.0, 1.4):
        macro = two_supernode_phi(b)
        micro = whole_phi(b)
        print(
            f"b={b:.12f} macro2={macro:.12f} micro8={micro:.12f} "
            f"macro-minus-micro={macro-micro:.12f}"
        )


if __name__ == "__main__":
    main()
