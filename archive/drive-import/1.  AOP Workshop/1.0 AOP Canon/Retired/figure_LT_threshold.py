"""Figure LT-T — the living-threshold discriminator is architectural, not a
timescale-separation magnitude (AOP v1.15, Section 11a).

Deposited reproduction. Two claims, both computed here:
 (A) Sweeping the slow/fast timescale ratio of a decoupled-reference (cell-type)
     regulator, the model-edge weight (viability drop when the reference->regulated
     edge is scrambled) stays high, load-bearing, and flat across the star-cell
     window (~0.79 at 2x to ~0.72 at 20x): no threshold knee. Separation is not
     the discriminator.
 (B) At matched conditions, what separates star from cell is structural: the cell
     holds its set-point in a separate, separately-interventable reference node
     (architecture = 1); the star carries its target in the fast constitutive
     drift (architecture = 0). Both are load-bearing; only the cell is decoupled.

Model: linear OU, dx = -B (x - x*) dt + sqrt(SIG2) dW, stationary covariance from
the continuous Lyapunov equation. Viability V = 1/(1+MSE of the regulated node
about its target mu). Edge scramble = zero the reference->regulated coupling.
"""
import numpy as np
from scipy.linalg import solve_continuous_lyapunov

SIG2 = 0.05
MU, A, BETA = 2.0, 1.0, 0.5   # target; regulated-node rate; reference back-coupling

def _stat(B, b):
    m = np.linalg.solve(B, b)
    S = solve_continuous_lyapunov(B, SIG2 * np.eye(B.shape[0]))
    return m, S

def _V(m, S, reg):
    mse = np.mean([(m[i] - MU) ** 2 + S[i, i] for i in reg])
    return 1.0 / (1.0 + mse)

def cell_weight(sep):
    """Decoupled-reference regulator at slow/fast ratio `sep`; return model-edge weight."""
    eps = A / sep
    B = np.array([[eps + BETA, -BETA], [-A, A]]); b = np.array([eps * MU, 0.0])
    m, S = _stat(B, b); v0 = _V(m, S, [1])
    Bs = B.copy(); Bs[1, 0] = 0.0                     # scramble reference -> regulated edge
    ms, Ss = _stat(Bs, b)
    return (v0 - _V(ms, Ss, [1])) / v0

def star_weight():
    """Model-free self-restoring node: target in its own drift; scramble = remove target."""
    B = np.array([[A]]); b = np.array([A * MU])
    m, S = _stat(B, b); v0 = _V(m, S, [0])
    ms, Ss = _stat(B, np.array([0.0]))
    return (v0 - _V(ms, Ss, [0])) / v0

if __name__ == "__main__":
    seps = np.geomspace(1.0, 100.0, 60)
    w = np.array([cell_weight(s) for s in seps])
    i2, i20 = np.argmin(abs(seps - 2)), np.argmin(abs(seps - 20))
    print(f"(A) cell-type sweep: weight[2x]={w[i2]:.3f}  weight[20x]={w[i20]:.3f}  "
          f"weight[100x]={w[-1]:.3f}  monotone={bool(np.all(np.diff(w) <= 1e-9))}  "
          f"stays_positive={bool(w.min() > 0)}")
    print(f"(B) architecture: star weight={star_weight():.3f} (arch=0), "
          f"cell weight@20x={w[i20]:.3f} (arch=1)")
