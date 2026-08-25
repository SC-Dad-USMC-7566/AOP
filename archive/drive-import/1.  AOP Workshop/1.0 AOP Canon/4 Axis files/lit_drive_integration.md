# Literature closure: the Drive → Integration (dynamic) edge

**Question.** AOP's coupling graph marks Drive→Integration FREE at equilibrium (parts may be
correlated at zero dissipation — a static fact) but leaves it OPEN dynamically: does sustained
dissipation/drive **build or maintain integration** (interdependence among parts, operationalized
as total correlation / multipartite mutual information) over time? Is the edge FORCED (a law), a
TENDENCY (holds under conditions), or genuinely OPEN?

**Markers:** ✓ read primary passage · ~ read abstract / named result · ? unread lead.

---

## VERDICT: TENDENCY-only (conditional), NOT a forced edge.

The literature does **not** license a law "drive builds integration." What it establishes is
narrower and cuts two ways:

1. **A necessity result (the strongest thing available):** *robust, size-extensive* correlation
   among many components **cannot** be sustained at equilibrium; it **requires** dissipation
   (far-from-equilibrium, time-dependent attractors). This makes dissipation **necessary** for a
   strong form of maintained integration — but necessity is not sufficiency, and it says drive is a
   *precondition*, not a *driver*.
2. **A cost/constraint result:** in stochastic thermodynamics, *maintaining* correlations against
   thermal erasure has a dissipative price (entropy production lower-bounds / trades against
   changes in mutual information). Again: integration that persists must be paid for by drive — but
   drive does not automatically *purchase* it. Dissipation can equally destroy correlation.

Neither body says sustained drive *tends to increase* integration in general. The England program,
which is the closest thing to such a claim, is a hedged proposal about **high-dissipation
structure**, not about interdependence, and is not proven. MaxEP, which would be the "law" version,
is explicitly **not a settled principle**. So AOP should state D→I(dynamic) as a **conditional
tendency / necessity relation**, grade it SYNTHESIS→FRONTIER, and **not lean on MaxEP or England
as if either were a law.**

---

## Body 1 — England, dissipative adaptation  ~ (Perspective + abstract of the PRX)

- **England, J. L. (2015). "Dissipative adaptation in driven self-assembly." *Nature
  Nanotechnology* 10, 919–923.** https://www.nature.com/articles/nnano.2015.250 — This is a
  **Perspective** (author's own framing: "I suggest… may at last be emerging"; "I propose that they
  imply a general thermodynamic mechanism"). It is **not a theorem paper.** The News & Views
  companion "Driven by theory" (nnano.2015.273) treats it as a program, not a settled result.
- **Perunov, Marsland & England (2016). "Statistical Physics of Adaptation." *Phys. Rev. X* 6,
  021036** (arXiv:1412.1875). https://link.aps.org/doi/10.1103/PhysRevX.6.021036 — Derives a
  generalized (finite-time, driven) free-energy / work-relation bookkeeping from
  Crooks/Jarzynski-type fluctuation relations, and argues that driven matter tends toward states
  that **reliably absorb and dissipate work** from the *specific* drive it experiences
  ("fine-tuning" to the drive).

**What is actually proven vs. suggested.** The *fluctuation-relation identity* it builds on is
rigorous. The *adaptation claim* — that systems self-organize toward high-work-absorbing
configurations — is a **suggested tendency**, demonstrated in illustrative small models, not a
general theorem. Crucially for AOP: **the England result is about dissipation/absorption, not about
integration.** It does **not** show drive builds *interdependence / total correlation among parts*.
Fine-tuning to a drive is not the same as parts becoming mutually dependent. Grade: **FRONTIER,
over-claimed by popularizers.** Do not cite as establishing D→I.

## Body 2 — Maximum Entropy Production (MaxEP)  ✓ (read Martyushev's status statement)

- **Martyushev, L. M. (2010). "The maximum entropy production principle: two basic questions."
  *Phil. Trans. R. Soc. B* 365, 1333.** https://pmc.ncbi.nlm.nih.gov/articles/PMC2871898/ — A
  *sympathetic* author states plainly: **"a principle like MEPP cannot be proved,"** and that
  attempted derivations rest on assumptions "less obvious than MEPP itself," with the bilinear
  flux–force / local-equilibrium form as a mandatory (near-equilibrium) condition.
- Martyushev & Seleznev (2006) *Phys. Rep.* 426, 1 (the standard review) and multiple critiques
  (e.g. Synthese 2023, "Is MEPP just a heuristic principle?") confirm: MaxEP is a **contested
  heuristic**, empirically useful in places, **not a settled law**, and not derivable in general.

**Status: NOT settled.** AOP must **not** invoke MaxEP as the mechanism that forces D→I. Even its
own advocates concede it is unprovable. Grade: **contested / not-settled.**

## Body 3 — Prigogine / Nicolis dissipative structures  ~ (Nobel lecture + reviews)

- **Nicolis & Prigogine, *Self-Organization in Nonequilibrium Systems* (1977);** Prigogine Nobel
  lecture (1977). https://www.nobelprize.org/uploads/2018/06/prigogine-lecture.pdf

**Settled:** Driven, far-from-equilibrium systems *can* spontaneously form ordered spatiotemporal
structure (Bénard convection, Belousov–Zhabotinsky). This is textbook and empirically robust — order
in driven systems is real. **Dated / restricted:** Prigogine's **minimum entropy production
theorem** is proven **only in the linear (near-equilibrium) regime** and does **not** extend far
from equilibrium; there is **no** accepted general extremal principle governing which structure
appears far from equilibrium. So Prigogine supports the *possibility* and *existence* of
drive-induced order, but supplies **no law** that drive increases integration, and its one clean
theorem is confined to the regime AOP cares least about. Grade: existence **SETTLED**; governing
principle **not settled**.

## Body 4 — Direct drive → correlation results  ~ (two primary abstracts read closely)

This is where the genuinely load-bearing, recent results live.

- **"Dissipation enables robust extensive scaling of multipartite correlations" (arXiv:2410.13375,
  2024/25).** https://arxiv.org/html/2410.13375 — **Proves** that multipartite mutual information
  I_M scales *extensively* and *robustly* with system size **only** when the system relaxes to
  **time-dependent attractors (limit cycles), which exist only far from equilibrium.** A single
  fixed point gives no extensive scaling; coexisting fixed points can but are **not robust** to
  perturbation; and **"robust extensive scaling of correlations cannot occur in thermal
  equilibrium."** The authors frame it as "the essential role of dissipation in the generation and
  **maintenance** of multipartite correlations." → **This is the cleanest support AOP has**, but it
  is a **necessity/conditional** statement (needs limit-cycle dynamics), not "drive monotonically
  builds integration."
- **"Irreversibility and correlations in coupled oscillators" (arXiv:1610.01172).**
  https://arxiv.org/pdf/1610.01172 — In the small-coupling limit, entropy-production rate is
  **proportional** to mutual information (I = Π_s/2κ_tot + O(G⁴)); the proportionality **breaks
  down** at strong coupling / large population imbalance. → Ties dissipation to correlation, but
  **conditional** and regime-limited.
- **Information-thermodynamics constraints** (Parrondo, Horowitz & Sagawa, *Nat. Phys.* 2015,
  "Thermodynamics of information"; Sagawa–Ueda fluctuation theorem with information exchange). ~ —
  Establish the **cost/trade-off** form: creating, maintaining, or consuming correlations enters the
  second law as a term bounding entropy production. These make integration **something drive must
  pay for**, not something drive automatically produces — dissipation can create *or* erase
  correlation.

Grade: **SYNTHESIS/FRONTIER.** A real, citable link exists — but every clean result is conditional
(limit cycles; small coupling; specific protocols).

---

## Recommendation for the AOP canon

State the Drive→Integration **dynamic** edge as a **conditional tendency backed by a necessity
result**, not a forced edge:

> "At equilibrium, integration is FREE (correlations at zero dissipation). Dynamically, sustained
> integration of the strong, robust, size-extensive kind is **not free**: it requires dissipation.
> Robust extensive multipartite correlation is impossible in equilibrium and requires
> far-from-equilibrium (time-dependent) dynamics [arXiv:2410.13375]; maintaining correlation against
> thermal erasure carries a dissipative cost in stochastic thermodynamics [Parrondo et al. 2015].
> Drive is therefore a **precondition** for maintained integration, but does **not force** it —
> dissipation can build or destroy correlation depending on dynamics. Claims that drive *maximizes*
> or *necessarily builds* integration (MaxEP; strong readings of dissipative adaptation) are **not
> settled** and are not relied on here."

**Do:** cite arXiv:2410.13375 (necessity of dissipation for robust extensive correlation) and the
information-thermodynamic cost bounds as the load-bearing support. **Do not:** cite MaxEP as a law;
do not cite England's dissipative adaptation as establishing integration (it is about dissipation,
is a Perspective, and is unproven). **Grade the edge SYNTHESIS→FRONTIER**, tendency/necessity — not
FORCED, not OPEN.

**Provenance honesty.** Primary passages read: Martyushev status statement (✓), and the abstracts/
result statements of England 2015, Perunov–Marsland–England 2016, arXiv:2410.13375, and
arXiv:1610.01172 (~). Full internal derivations of the two arXiv correlation papers were **not**
line-checked; before the canon leans on 2410.13375, its theorem statement and assumptions
(permutation-invariance, the exact "robust" definition) should be read in full (? → ✓ pending).
