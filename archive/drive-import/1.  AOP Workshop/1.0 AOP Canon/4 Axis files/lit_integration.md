# AOP F2 Seam — Literature Closure Report

**Task:** Does the literature already supply the machinery AOP calls its principal open problem
(the "F2 seam") — (i) nested level-selection and (ii) non-stationary / critical Φ_MIP — so AOP can
cite rather than invent?

**AOP scope being extended:** Φ_MIP = integrated information across the Minimum Information
Partition (Aguilera & Di Paolo), scoped to STATIC GAUSSIAN systems at a FIXED partition.

**Markers:** ✓ read primary · ~ abstract/named · ? unread lead
**Grades:** SETTLED (established science) · SYNTHESIS (this-framework reorganization) · FRONTIER (open)

---

## SUB-QUESTION 1 — NESTED LEVEL-SELECTION

**VERDICT: CLOSABLE-BY-SYNTHESIS.**
The *principle* is closable-by-citation; porting it to AOP's static-Gaussian Φ_MIP and reconciling
it with AOP's own refusal-to-individuate is a small synthesis, not new physics.

### The rule the literature already supplies
The published, principled criterion for "which level is the individual" is:
**select the spatiotemporal grain that MAXIMIZES integrated (or effective) information.**
This is not a lead — it is a settled construction inside IIT, stated explicitly.

### Verified key results

**Hoel, Albantakis, Marshall & Tononi (2016), "Can the macro beat the micro? Integrated
information across spatiotemporal scales," *Neuroscience of Consciousness* 2016(1):niw012.** ✓ read primary (OUP full text)
- Computes Φ at many spatial AND temporal grains and selects the maximum.
- Quoted criterion: *"the set of elements with Φ^Max is called the 'complex'... a physical system
  that specifies a maximally irreducible cause–effect structure"*; *"the spatiotemporal maximum of
  integrated information fixes the spatiotemporal scale"* — the ΦMax grain is the privileged level
  at which the system exists as a whole "from its own intrinsic perspective."
- **This is a full, explicit level-selection RULE.** Grade: **SETTLED** (within IIT).
- **Caveat for AOP:** systems are DISCRETE binary first/second-order Markov elements, NOT Gaussian.

**Marshall, Grasso, Mayner, Zaeemzadeh et al. (2026), "Intrinsic units: identifying a system's
causal grain," *Neuroscience of Consciousness* 2026(1):niag013 (IIT 4.0).** ✓ read primary
- Modern IIT machinery that identifies the grain (the "intrinsic units") at which a system's
  integrated information φ_s is maximal and maximally irreducible: a complex is *"a maximum of
  intrinsic, specific, unitary cause-effect power."*
- Presented as *the* method by which IIT fixes a system's level. Grade: **SETTLED→FRONTIER** (very recent).
- **Caveat:** discrete binary-state units only; authors explicitly reject multi-state units.

**Hoel, Albantakis & Tononi (2013), "Quantifying causal emergence shows that macro can beat
micro," *PNAS* 110(49):19790–19795.** ~ named / reproduced via the 2016 paper (PMC full text
captcha-blocked; not read directly)
- Origin of the effective-information macro-beats-micro result; the EI-maximizing coarse-graining
  is the causally optimal scale. Grade: **SETTLED** (highly cited). Verify passage directly before quoting.

**Zhao/Zhang et al., "An Exact Theory of Causal Emergence for Linear Stochastic Iteration
Systems," *npj Complexity* (2025) / arXiv:2405.09207.** ✓ read primary (PMC PMC11354030)
- **This is the Gaussian-scope match and the analytic bridge AOP needs.**
- Provides a CLOSED-FORM effective-information functional J(A,Σ) for **linear systems with Gaussian
  noise** (determinants of covariance matrices); the optimal coarse-graining and maximal causal
  emergence are *"primarily determined by the principal eigenvalues and eigenvectors of the
  dynamic system's parameter matrix."*
- Analytic, not estimated — aligns with Ben's "build on analytic results" rule. Grade: **SYNTHESIS/FRONTIER**.

**Krakauer, Bertschinger, Olbrich, Flack & Ay (2020), "The information theory of individuality,"
*Theory in Biosciences* 139:209–223 (arXiv:1412.2447).** ✓ read primary (arXiv full text)
- Defines individuality via autonomy **A\* = I(S_{n+1}; S_n)** (system-past predicts system-future),
  with the system/environment partition chosen to maximize autonomy / non-trivial closure.
- Crucially: individuality is **graded and continuous** (*"we do not assume that individuality is
  binary but allow it to be continuous"*) and **explicitly nested** (*"individuals can contain
  individuals... organelles nested within cells"*). **They deliberately REFUSE to pick one
  privileged level:** *"a productive research program... should allow a-priori for the possibility
  of multiple degrees of individuality at all levels."* Grade: **SETTLED**.
- **This is the direct tension AOP must resolve** (see below): IIT selects ONE level (ΦMax);
  Krakauer keeps all qualifying levels, graded.

### Recommendation for AOP (sub-question 1)
1. **Adopt the maximize-integration criterion as the level-selection ordering**, citing
   Hoel-Albantakis-Marshall-Tononi 2016 and Marshall et al. 2026 [SETTLED within IIT]: over a nested
   hierarchy, order levels by Φ_MIP and treat the grain that maximizes Φ_MIP as most one-irreducible-whole.
2. **Port it to AOP's static-Gaussian scope analytically** using the closed-form Gaussian
   effective-information / eigenvalue construction of Zhang et al. 2025 [SYNTHESIS] — this is the
   piece that makes the port a synthesis rather than new physics, and it keeps AOP's computed
   claims closed-form.
3. **Frame the output as GRADED, not a unique winner** (Krakauer et al. 2020 [SETTLED]). This is not
   optional polish: AOP's canon already *refuses to individuate*, so adopting IIT's single-ΦMax
   "ontologically privileged level" verbatim would contradict AOP's own refusal. Use Φ_MIP-max as a
   syntactic *ordering* over levels and let the semantic (viability) layer read out which level(s)
   matter — consistent with Krakauer's graded/nested stance.
4. **Flag the residual gap honestly:** every existing maximize-Φ level-selector (Hoel 2016, Marshall
   2026) is built on DISCRETE binary systems; the Gaussian cross-scale maximization is demonstrated
   only for linear-dynamical (not static) Gaussian systems (Zhang 2025). The static-Gaussian nested
   Φ_MIP maximization is therefore a bridge AOP writes, backed by these anchors — SYNTHESIS with a
   clearly labeled derivation, not a bare citation.

---

## SUB-QUESTION 2 — NON-STATIONARY / CRITICAL Φ_MIP

**VERDICT: SPLIT.**
- **AT criticality:** CLOSABLE-BY-CITATION.
- **Non-stationary / time-varying / developmental Φ_MIP:** NEEDS-NEW-WORK.

### Verified key result (the criticality half)

**Aguilera & Di Paolo (2019), "Integrated information in the thermodynamic limit," *Neural
Networks* 114:136–146 (arXiv:1805.00393v3).** ✓ read primary (arXiv v3 full text)
- **Measure:** an *effects-only* integrated information φ (simplified IIT φ), on a **kinetic Ising
  model** with **mean-field** (infinite-range) coupling.
- **MIP:** the bipartition of least difference to the whole; for their homogeneous system this
  reduces to isolating single nodes — *"finding which region R affects less future states when one
  node of the region is isolated."*
- **Stationarity:** results are computed *"starting from a state in the stationary solution,"* i.e.
  they **assume stationarity for the computed values**, while noting IIT in principle *"does not
  require the existence of stationary conditions."*
- **Central proven result:** integrated information **DIVERGES at the critical point in the
  thermodynamic limit.** Quoted: *"the value of integrated information φ^MN(τ→∞) diverges when
  J→1+"*; per-unit φ^MN/N *"would tend to 0 at any position but in the critical point."* Analytic
  near J=1: φ^MN(τ→∞) = ½·|√3(2J−3) / (2√(J³(J−1)))|. Implication they draw: a system holding
  integration-per-unit as it grows *"may need to be poised near a critical point."*
- Grade: **SETTLED** (analytic, peer-reviewed). **Caveat:** this is the DISCRETE kinetic-Ising φ,
  adjacent to but not identical with AOP's static-Gaussian Φ_MIP; cite as "Φ diverges at criticality
  in the thermodynamic limit," not as a Gaussian result.

Companion (Gaussian criticality): **Aguilera (2019), "Scaling Behaviour and Critical Phase
Transitions in Integrated Information Theory," *Entropy* 21(12):1198.** ? unread lead — likely the
Gaussian-scoped companion; verify before relying on it for the Gaussian critical claim.

### The gap (the non-stationary half)
- Aguilera & Di Paolo vary only the *time horizon* τ (τ = 1,2,4,8,16,∞) — **still measured from the
  stationary solution.** They do **NOT** treat φ across genuinely evolving/developing dynamics, and
  do **NOT** address nested level selection. ✓ verified in primary text.
- No primary source located that defines Φ_MIP for a genuinely **non-stationary / time-varying /
  developmental** system at AOP's Gaussian scope. IIT asserts stationarity is not required in
  principle, but no worked construction exists.

### Recommendation for AOP (sub-question 2)
- **Critical Φ_MIP:** close by citation — Aguilera & Di Paolo 2019 [SETTLED] establishes the
  divergence of integrated information at criticality in the thermodynamic limit; use it directly,
  labeling it as the kinetic-Ising result and (pending verification) the Entropy-2019 companion for
  the Gaussian statement.
- **Non-stationary / developmental Φ_MIP:** **genuinely NEEDS-NEW-WORK.** The reason is specific and
  defensible: every existing computation — including the divergence result — is anchored to a
  *stationary* solution, and the only time-dependence studied is the horizon τ from that stationary
  state. Defining the MIP itself when the covariance is time-varying (the partition can move as the
  system develops) is unaddressed. This is a legitimate AOP open problem, not a citation gap.

---

## One-line seam summary
The **level-selection** half of the F2 seam is essentially already solved in the literature
("pick the grain that maximizes integrated information"; Hoel 2016, Marshall 2026, Zhang 2025 for
the Gaussian/analytic version) and only needs AOP to port + regrade it, taking Krakauer's graded
stance to stay consistent with its own refusal-to-individuate. The **non-stationary Φ_MIP** half is
the real remaining novelty: criticality is cited (Aguilera & Di Paolo 2019), but time-varying /
developmental Φ_MIP is genuinely NEEDS-NEW-WORK.

## Sources
- Hoel, Albantakis, Marshall & Tononi 2016, *Neurosci. Consciousness* — https://academic.oup.com/nc/article/2016/1/niw012/2757132
- Marshall et al. 2026, "Intrinsic units," *Neurosci. Consciousness* — https://academic.oup.com/nc/article/2026/1/niag013/8654505
- Hoel, Albantakis & Tononi 2013, *PNAS* — https://www.pnas.org/doi/10.1073/pnas.1314922110
- Zhang et al. 2025, causal emergence for linear stochastic systems — https://pmc.ncbi.nlm.nih.gov/articles/PMC11354030/ ; npj Complexity https://www.nature.com/articles/s44260-025-00028-0
- Krakauer, Bertschinger, Olbrich, Flack & Ay 2020, "Information theory of individuality" — https://arxiv.org/abs/1412.2447
- Aguilera & Di Paolo 2019, "Integrated information in the thermodynamic limit," *Neural Networks* — https://arxiv.org/abs/1805.00393 ; https://www.sciencedirect.com/science/article/pii/S0893608019300735
- Aguilera 2019, "Scaling Behaviour and Critical Phase Transitions in IIT," *Entropy* — https://www.mdpi.com/1099-4300/21/12/1198 (unverified lead)
