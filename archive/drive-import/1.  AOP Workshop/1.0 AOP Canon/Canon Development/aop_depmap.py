"""
aop_depmap.py — dependence map for the non-energy triangle (B, I, M).
Prime, 20 July 2026 rev.2, seed 20260720. Reframe: correlation is a finding;
test dissociability + unique residual, not orthogonality.

RESULTS (seed 20260720, 4000 random stable VAR(1), n=6, in/out=3/3):

EXACT IDENTITY  I = B + TC_in + TC_out : max error 1.78e-15 (machine-exact).
  -> Boundary is the cross-cut slice of Integration; remainder = within-side TC.

PAIRWISE Spearman:  B-I 0.833 | B-M 0.612 | I-M 0.607
PARTIAL (control 3rd axis):  B-I|M 0.734 | B-M|I 0.242 | I-M|B 0.223
PARTIAL (control coupling strength):  B-M|coup -0.046 | I-M|coup -0.621
  -> B-I is direct/substrate; B/I-M is shared coupling strength (B-M vanishes).

UNIQUE variance (R^2 explained by other two -> unique residual):
  Memory  0.406 -> 0.59 unique   (MOST distinct axis)
  Boundary 0.712 -> 0.29 unique  (nested in Integration)
  Integration 0.709 -> 0.29 unique

DISSOCIATION CORNERS (B, I, E):
  sealed modules              0.000, 1.532, 0.000   (I without B)
  cross-cut only              1.010, 1.010, 0.000   (B = I, no internal)
  all-coupled memoryless      0.294, 0.728, 0.000   (coupling, no memory)
  pure memory                 0.000, 0.000, 4.982   (memory alone)

METHOD
  Boundary  B  = 0.5*(logdet Sig_in + logdet Sig_out - logdet Sig)
  Integration  = 0.5*(sum_i log Sig_ii - logdet Sig)   [= B + TC_in + TC_out]
  Memory  E    = I(X_{t-1};X_t) on lagged cov C1 = A Sig
  partial Spearman via rank-transform + partial-correlation formula
  unique variance via OLS of rank(target) on rank(others), report R^2
  corners: covariance constructed directly (A=0 -> E=0); pure memory A=0.9*I

Full runnable source delivered alongside as aop_depmap.py (build dir); this is
the archival record of method + numbers. See rev.2 HTML/MD report §5.
"""
