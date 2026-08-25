"""
Recompute AOP's load-bearing quantitative claims from scratch (independent
verification, not reproduction of deposited figures). Prime, seed 20260720.

Results on this seed:
  FIG A  B-I Spearman = 0.834 (REPRODUCES canon ~0.83);
         Memory E=I(X_{t-1};X_t) Spearman with B and I = 0.61, 0.61
         (DID NOT reproduce canon's claimed |corr|<0.05 near-orthogonality)
  FIG B  detailed balance sigma=7.4e-17, E=0.704  (sigma>0=>E>0; converse fails)
  FIG C  MFPT ratio 5.40x while stationary occupancy flat to 7e-16
  FIG D  chain stiff/sloppy ratio 252.6 vs equicorr 11.3

Boundary  = 0.5*log(det Sig_in * det Sig_out / det Sig)
Integration TC = 0.5*(sum_i log Sig_ii - log det Sig)
Memory E  = I(X_{t-1};X_t) on lagged covariance C1 = A Sig
sigma (Markov) = sum_{i!=j} pi_j K_ij ln( K_ij pi_j / (K_ji pi_i) )
MFPT: solve K'[idx,idx] tau = -1 with one absorbing state removed.

Full runnable source is delivered alongside as aop_figs.py in the build dir;
this Drive copy is the archival record of method + numbers. See the HTML/MD
report for interpretation.
"""
# (archival header; the executable body is identical to the delivered aop_figs.py)
