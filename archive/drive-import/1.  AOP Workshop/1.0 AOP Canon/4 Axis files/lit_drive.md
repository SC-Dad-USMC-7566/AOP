# AOP Drive-axis literature closure — two open gaps

Date: 2026-07-20. Verification markers: ✓ = read primary passage this session · ~ = abstract/named only · ? = unread lead.
Grades: SETTLED (established peer-reviewed science) · SYNTHESIS (results exist, AOP must assemble) · FRONTIER (genuinely open).

---

## GAP 1 — SIGN of Drive's leverage on lifetime (MFPT to erasure)

**VERDICT: CLOSABLE-BY-CITATION — and it likely REFUTES AOP's current framing.**
The literature already contains a *universal* sign rule for exactly AOP's regime (divergence-free
current added at FIXED stationary distribution, small-noise limit). The rule is not
"geometry-dependent." It is one-sided: **measure-preserving circulation can only LOWER or leave
unchanged the MFPT — it can never raise it.** Anti-persistent or neutral; never pro-persistent.

### What is settled

1. **Exponent is fixed by the stationary measure.** For an irreversible diffusion the escape rate's
   exponential factor is governed by the Freidlin–Wentzell **quasipotential**, and near the attractor
   the quasipotential equals −ε ln ρ_s. Holding the stationary distribution ρ_s fixed therefore holds
   the barrier fixed; any lifetime change from added circulation is a **prefactor** effect.
   - Bouchet & Reygner, *Generalisation of the Eyring–Kramers Transition Rate Formula to Irreversible
     Diffusion Processes*, Annales Henri Poincaré 17, 3499 (2016); arXiv:1507.02104. **~** (read abstract
     this session; HAL/arXiv full text blocked). "the role of the potential is played by
     Freidlin–Wentzell's quasipotential"; the prefactor carries "a correction depending on the
     non-Gibbsianness of the system along the instanton." Grade: **SETTLED**.

2. **The prefactor monotonically favors escape — the decisive result.** For non-reversible diffusion
   with a Gibbs invariant measure e^{−U/ε} held fixed (drift b = −(∇U + ℓ), ℓ divergence-free,
   ∇U·ℓ = 0 — i.e. *precisely* "add a circulating current at fixed stationary distribution"):
   - Lee & Seo (Landim school), *Non-reversible Metastable Diffusions with Gibbs Invariant Measure I:
     Eyring–Kramers Formula*, Probab. Theory Relat. Fields (2021); arXiv:2008.08291. **✓** (read main
     theorem/lemma/corollary via arXiv PDF this session). Theorem 3.5: E[τ] = [1+o(1)] (ν₀/ω₀)·
     exp((H−h₀)/ε), with saddle prefactor ω^σ = μ^σ / (2π√(−det ℍ^σ)), where −μ^σ is the *unique
     negative eigenvalue of ℍ^σ + 𝕃^σ* (Hessian of U plus Jacobian of the non-reversible field ℓ at the
     saddle). **Lemma 3.4: μ^σ ≥ λ^σ** (the reversible eigenvalue), hence ω^σ ≥ ω_rev^σ, and
     **Corollary 3.9: E[τ] ≤ E_rev[τ] for all small enough ε.** Circulation raises the unstable
     eigenvalue at the saddle → faster escape → shorter lifetime, always. Grade: **SETTLED**.

3. **Independent confirmation, no sign reversals.** Le Peutrec / Landim / Seo lineage, *Exit Time and
   Principal Eigenvalue of Non-reversible Elliptic Diffusions*, Comm. Math. Phys. (2024),
   doi:10.1007/s00220-024-05032-4. **~** (read publisher summary). Same decomposition b = −(∇f + ℓ),
   ∇f·ℓ = 0; principal eigenvalue ≈ 1/MFPT; result is "universal in structure," no geometry-dependent
   sign reversals. Consistent with the acceleration-of-convergence literature (Lelièvre–Nier–Pavliotis;
   Hwang–Hwang–Sheu): measure-preserving antisymmetric drift never hurts. Grade: **SETTLED**.

4. **Why "quasipotential ≠ potential" (Maier–Stein) does NOT rescue geometry-dependence here.**
   Maier & Stein, *Escape problem for irreversible systems*, Phys. Rev. E 48, 931 (1993). **?** (named,
   not re-read this session). For non-gradient drift the quasipotential can differ from the naive
   potential and develop caustics — but that divergence is between the quasipotential and −ln(a *chosen*
   potential). When ρ_s itself is held fixed, the barrier is pinned to −ln ρ_s at the attractor and the
   Maier–Stein freedom is spent; only the prefactor moves, and (2) fixes its sign. Grade: SETTLED
   background.

### Reconciliation with AOP's finding (the important part)

- AOP's **ring → anti-persistent (~5.7× shorter MFPT)** is exactly the predicted universal behavior. ✓
- AOP's **star → pro-persistent (longer MFPT)** *contradicts* the settled small-noise result. Under the
  theorem's hypotheses, pro-persistence is impossible. So one of the following holds and must be
  identified before AOP publishes a "sign is geometry-dependent" claim:
  (a) the star result is a **finite-noise prefactor effect** outside the ε→0 asymptotic regime (the
      monotone μ^σ ≥ λ^σ ordering is an ε→0 statement);
  (b) the star **violates a hypothesis** — e.g. a star/tree graph has no cycles, so it cannot carry a
      genuinely divergence-free current at fixed stationary distribution without added edges; or its
      escape is over a degenerate/non-Kramers saddle where Theorem 3.5 does not apply;
  (c) artifact.

**Recommendation:** Cite Lee–Seo (arXiv:2008.08291) as the SETTLED sign rule and retire AOP's
"geometry → sign, no rule" framing for the fixed-measure small-noise regime — the rule exists and is
one-sided (anti-persistent/neutral only). Then treat the star's apparent pro-persistence as a claim to
be *reconciled*, not asserted: check regime (finite ε) and hypotheses (divergence-free? Kramers
saddle?). Any residual, genuinely finite-noise two-sidedness is **FRONTIER** — but the default (per the
charter) is that the "new" pro-persistent prediction is not real until it survives this check.

---

## GAP 2 — GENERALITY of the sector split (σ̇ antisymmetric; Memory/structure time-symmetric)

**VERDICT: CLOSABLE-BY-SYNTHESIS (the σ̇ half is essentially CLOSABLE-BY-CITATION).**
The general symmetric/antisymmetric (time-symmetric vs time-antisymmetric) decomposition is SETTLED for
general nonlinear, non-Gaussian dynamics — not model-specific. It already delivers half of AOP's claim
outright (σ̇ lives in the antisymmetric sector). AOP must supply one short argument for the other half
(that its specific Memory/structure functionals are time-symmetric observables).

### What is settled

1. **General generator/drift split + EP depends ONLY on the antisymmetric part** — for general
   nonlinear diffusions.
   - Da Costa, Barp, et al., *The entropy production of stationary diffusions*, J. Phys. A 56, 365001
     (2023); arXiv:2212.05125. **✓** (read propositions/theorem via PDF this session). Prop. 3.7:
     b = b_rev + b_irr with b_rev = D∇log ρ + ∇·D (detailed-balance, time-reversible) and
     ∇·(b_irr ρ) = 0 (divergence-free, time-irreversible). Prop. 3.12: generator L = A + S with A the
     antisymmetric and S the symmetric part. **Theorem 4.1: ep = ∫ b_irrᵀ D⁻¹ b_irr ρ dx** — a quadratic
     form of the irreversible part *only*; the reversible part contributes nothing. Explicitly holds for
     "non-elliptic, hypoelliptic and degenerate diffusions," nonlinear potentials — **no Gaussianity
     assumed.** Grade: **SETTLED**. This is the general upgrade of AOP's OU/finite-chain σ̇ result.

2. **Path-space version (jump + diffusion), the frenesy framework.**
   - Maes, *Frenesy: time-symmetric dynamical activity in nonequilibria*, Physics Reports 850, 1 (2020);
     arXiv:1904.10485. **~** (read abstract this session). The path-space action splits into a
     **time-antisymmetric** part = entropy flux (dissipation) and a **time-symmetric** part = frenesy /
     dynamical activity; realized for "Markov jump and diffusion processes." Establishes that dissipative
     (σ̇) and kinetic/structural quantities occupy the two distinct sectors. Grade: **SETTLED** (the
     decomposition; the taxonomy is a review-level consensus).
   - Schnakenberg, *Network theory of microscopic and macroscopic behavior of master equation systems*,
     Rev. Mod. Phys. 48, 571 (1976). **?** (named, standard). Cycle/current decomposition for finite
     Markov jump processes; EP is a sum over cycle affinities×currents (the circulation/antisymmetric
     part). Covers the discrete-state case general beyond AOP's finite-chain proof. Grade: **SETTLED**.

### What AOP still must assemble (the synthesis)

The literature settles: (i) the general two-sector split, and (ii) that σ̇ is a functional of the
antisymmetric/circulating sector only. It does **not**, off the shelf, prove that *AOP's particular
Memory/structure observables* — resolvability via the covariance, and the causal asymmetry
Ξ = Cμ⁺ − Cμ⁻ — live in the time-symmetric sector for arbitrary dynamics. That is a one-line addition
AOP owns: show these observables are **time-reversal-even functionals** (equal-time covariance and
symmetrized two-point correlations are manifestly time-symmetric; the Ξ construction must be checked to
be built from the time-symmetric part of the correlation structure). Once shown, "no forced
cross-sector coupling" follows generally from (1)+(2): σ̇ in the antisymmetric sector, Memory in the
symmetric sector, orthogonal by construction.

**Recommendation:** Cite Da Costa et al. (arXiv:2212.05125) + Maes frenesy (Physics Reports 850) +
Schnakenberg (RMP 48, 571) as the SETTLED general sector split, and downgrade AOP's status tag from
FRONTIER to SETTLED **for the σ̇ = antisymmetric-sector half**. Keep a SYNTHESIS tag on the full
no-cross-coupling claim until AOP writes the short lemma that its Memory functionals are time-symmetric.
Do not claim this is novel — it is the frenesy decomposition applied to AOP's observables.

---

### Sources (URLs consulted)
- Lee/Seo, arXiv:2008.08291 · https://arxiv.org/abs/2008.08291 (PDF read ✓)
- Bouchet & Reygner, AnHP 17:3499, arXiv:1507.02104 · https://arxiv.org/abs/1507.02104 (abstract ~)
- Exit Time & Principal Eigenvalue of Non-reversible Elliptic Diffusions, CMP 2024 ·
  https://link.springer.com/article/10.1007/s00220-024-05032-4 (summary ~)
- Da Costa et al., J.Phys.A 56:365001, arXiv:2212.05125 · https://arxiv.org/pdf/2212.05125 (PDF read ✓)
- Maes, Physics Reports 850, arXiv:1904.10485 · https://arxiv.org/abs/1904.10485 (abstract ~)
- Schnakenberg, RMP 48:571 (named ?); Maier & Stein, PRE 48:931 (named ?)
