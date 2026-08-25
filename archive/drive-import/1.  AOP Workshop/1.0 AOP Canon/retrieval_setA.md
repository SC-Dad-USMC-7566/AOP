# Retrieval Record — Set A (four sources)

Prepared: 2026-07-25
Task: retrieve and deposit passages for human line-checking. No claims about AOP are made here.

---

## READ THIS FIRST — provenance caveat on all quoted material

Every "verbatim" passage below was extracted by the `WebFetch` tool, which fetches a page and
returns text produced by an **intermediary summarization model**. I did not transcribe these
strings character-by-character from a rendered PDF or HTML page myself. That means:

- Quotation marks below indicate *reported* verbatim text, not text I personally verified
  character-for-character against the source rendering.
- **Direct evidence of transcription drift in this very batch:** two separate fetches of the same
  PMC page (Source 4) returned the same sentence with a one-word difference — "keeping the
  conditional distribution ... **undisturbed**" vs. "... **undistributed**". "Undisturbed" is
  almost certainly correct and "undistributed" is a transcription error. This is a concrete
  demonstration that these strings can drift by a word.
- **Every quote below must be spot-checked against the source before it is used in the canon.**
  Treat this document as a retrieval map (what exists, where, and roughly what it says), not as a
  certified transcript.

Bibliographic *records* below are on firmer ground than the quoted prose — several were
cross-checked against two independent pages, as noted per source.

Prohibited tooling (bash/curl/python fetching) was not used. All retrieval was WebSearch/WebFetch.

---

## Source 1 — Francis & Wonham (1976), Automatica

### Bibliographic record (VERIFIED against the author's own publication list)

> "[J34] B.A. Francis, W.M. Wonham. The internal model principle of control theory.
> Automatica 12(5), 1976, pp. 457-465."

— entry J34 in `Wonham_Publications_20220531.pdf`, W.M. Wonham's own maintained publication list,
https://www.control.utoronto.ca/~wonham/Wonham_Publications_20220531.pdf

DOI: 10.1016/0005-1098(76)90006-6 (from the ScienceDirect and ACM DL landing URLs; the DOI string
was observed in URLs, and the metadata was not read off a retrieved publisher record).

The project's citation of Source 1 (authors, title, venue, volume, issue, pages, year) is
**correct as given**.

Adjacent works in the same list, which are frequently confused with this one:

> "[J32] B.A. Francis, W.M. Wonham. The internal model principle for linear multivariable
> regulators. Applied Mathematics and Optimization 2 (2), 1975, pp.170-194."
>
> "[J36] W.M. Wonham. Towards an abstract internal model principle. IEEE Trans. on Systems, Man
> and Cybernetics SMC-6 (11), 1976, pp. 735-740."
>
> "[T10] B.A. Francis. The Foundation of Linear Multivariable Regulation: The Internal Model
> Principle. Ph.D. Thesis, Dept. of Electl. Engrg., Univ. of Toronto, 1975."

### Retrieval status: **NOT RETRIEVED** (metadata only for the target paper)

The 1976 Automatica paper itself is paywalled and could not be reached:

| URL attempted | Result |
|---|---|
| https://www.sciencedirect.com/science/article/abs/pii/0005109876900066 | ROBOTS_DISALLOWED |
| https://dl.acm.org/doi/10.1016/0005-1098(76)90006-6 | HTTP 403 |
| https://www.semanticscholar.org/paper/...da7a60f2db454fda5a5c412f567edd798f506d80 | returned empty content |
| https://colab.ws/articles/10.1016%2F0005-1098(76)90006-6 | HTTP 403 |
| https://scholar.archive.org/search?... | archive.org rate-limit page |
| http://www.sontaglab.org/FTPDIR/imp-scl03.pdf (secondary source) | http→https redirect loop, unfetchable |
| https://www.math.rutgers.edu/~sontag/FTPDIR/imp-scl03.pdf (secondary source) | ROBOTS_DISALLOWED |

**I did not read the 1976 Automatica paper, its abstract, or any of its text.** Nothing below is
a quotation from it.

### Substitute evidence actually retrieved — two Wonham-authored open documents

These are **different documents from the target**. They are by the same author, on the same
principle, but they present the *abstract / general* version of the IMP developed later, in a
discrete-time set-and-function framework — **not** the 1976 linear time-invariant geometric result.
Do not attribute their wording to Francis & Wonham 1976.

**(1a) W. M. Wonham, "THE INTERNAL MODEL PRINCIPLE OF CONTROL THEORY", 2018.06.17**
URL reached: https://www.control.utoronto.ca/~wonham/W.M.Wonham_IMP_20180617.pdf
Status: FULL TEXT READ (via WebFetch; short-form note/paper)

The principle as two assertions:

> "Assertion 1. Error feedback + Perfect regulation ⇒ Internal Model"
>
> "Assertion 2. Structurally stable (or "robust") perfect regulation ⇒ Error feedback + Internal Model"

Theorem 1 as reported:

> "Assume that S satisfies internal stability, perfect regulation, error feedback, and exosystem
> detectability. Then 1) There exists a unique mapping αC : XC → XC determined by
> αC ◦ γ|K = γ ◦ α|K   2) αC ◦ γeE = γeE ◦ αeE   3) γeE is injective"

Reported gloss on conclusions 2 and 3: the controller dynamics are "a copy of the dynamics of E on
the global attractor", and this copy is "faithful, namely incorporates fully the exosystem dynamics".

Assumptions as reported:

> internal stability — "XeE is a global attractor, namely that, for every initial state xo in X,
> there is an integer N with αn(xo) ∈ XeE"
>
> error feedback — "the dynamics of C are autonomous as long as x ∈ K"
>
> exosystem detectability — "the controller is effectively coupled (via error feedback) to the exosystem"
>
> Rich Parameter Perturbation (used for Assertion 2) — "For each fixed xE, as µE varies through ME
> and µP varies through MP, R(µE)(xE) varies through XE"

Framework/scope:

> applies to a "very general class of systems", formulated in discrete time using "plain sets and
> functions" rather than a specifically linear or nonlinear framework

Stated limitation:

> "As stated here, the IMP crudely represents only a primitive 'intelligence'; issues of adaptation,
> learning, computing power, and 'real' problem-solving intelligence are open for investigation."

Note on citation practice inside this document: its reference to a 1976 paper is to
**[6] W. M. Wonham, "Towards an abstract internal model principle," IEEE Transactions on Systems,
Man, and Cybernetics, 6(11), pp. 735–740, 1976** — i.e. the SMC paper, *not* the Automatica paper.

**(1b) W. M. Wonham, "THE INTERNAL MODEL PRINCIPLE OF CONTROL THEORY: A QUICK INTRODUCTION", 2022.09.26**
URL reached: https://www.control.utoronto.ca/~wonham/IMP_20220926.pdf
Status: FULL TEXT READ (slide deck)

> "For a very general class of systems:
> 1. Error feedback + Perfect regulation ⇒ Internal Model
> 2. Structurally stable perfect regulation (i.e. regulation regardless of system perturbations)
> ⇒ Error feedback + Internal Model"   (slides 13, 40, 49)

On the controller embedding exosystem dynamics:

> "Statement 2 identifies these controller dynamics as a copy of the dynamics of 𝐄 on the global
> attractor (i.e. exosystem dynamics)."   (slide 31)
>
> "Internal model of exosystem in the controller is faithfully represented by
> (𝛾̃_E(X_E), α_C|𝛾̃_E(X_E))"   (slide 33)

Scope:

> "in general but rudimentary discrete-time framework, using just ordinary sets and functions"  (slide 14)
>
> "Assume that 𝐒 satisfies internal stability, regulation, feedback structure, and exosystem
> detectability."   (slide 30)

Citation on slide 52 is again to Wonham's own SMC 1976 paper, not the Automatica paper.

### What remains unchecked (Source 1)

**Everything asked for.** The actual 1976 Automatica text — its theorem statement, its linear
time-invariant hypotheses, its structural-stability formulation, and what it does and does not
license — was never retrieved; the two Wonham documents above are later, abstract restatements by
one co-author and are not substitutes for the 1976 theorem. Obtaining the Automatica PDF (library
access, ILL, or the Francis 1975 Toronto thesis) is required before any claim is attributed to
Francis & Wonham 1976.

---

## Source 2 — Bich, Mossio, Ruiz-Mirazo & Moreno, "Biological regulation: controlling the system from within"

### Bibliographic record

Bich, L., Mossio, M., Ruiz-Mirazo, K., & Moreno, A. — "Biological regulation: controlling the
system from within" — *Biology & Philosophy*.
DOI: **10.1007/s10539-015-9497-8**

Discrepancy to flag, not silently resolved: the copy retrieved carries a **2015** date (online-first)
and its header/filename read "…-2015-…"; the DOI suffix is likewise `-015-`. The project cites
**2016, vol. 31, pp. 237–265**, which is the print issue. Both are defensible; 2016;31:237–265 is
the print-of-record. The retrieved PDF did **not** display the journal volume or page range, so the
"31:237–265" part of the project's citation is **unconfirmed by retrieval** (it is consistent with
the Springer landing page URL but I did not read a page carrying those numbers).

### Retrieval status: **FULL TEXT READ** (author-hosted copy)

URL reached: https://leonardobich.wordpress.com/wp-content/uploads/2015/08/bich-mossio-ruiz-mirazo-moreno-2015-biological_regulation-controlling-the-system-from-within-biology-philosophy.pdf

**Important pagination warning:** this is the author's accepted-manuscript PDF. Page numbers
reported below (p. 2, p. 9, p. 15–18) are **manuscript pages**, not journal pages in the 237–265
range. Do not cite them as journal pagination.

### Passages bearing on the question

**Definition of a regulatory subsystem** (reported §5, manuscript p. 15–16):

> "Regulation requires that the self-maintaining organisation generates additional dedicated
> subsystems whose function is to handle perturbations."

> "a regulatory subsystem (R) needs to act freely from the constitutive regime (C) while at the
> same time being related to it."

> "the regulatory subsystem can work as operationally distinct from C, and can in principle act as
> a dedicated regulatory controller of C."   (p. 16)

> "it must (a) be produced by C and (b) be able to act on C."   (p. 16)

**The decoupling requirement — this is the passage asked for.** Reported as numbered condition (2)
in the authors' list of requirements (manuscript p. 17):

> "(2) To be regulatory, R must be dynamically decoupled from C, which it regulates. This means
> that R, even if it is a product of C, operates at a different dynamical scale and under different
> stoichiometric requirements than C."

Definitional gloss on what decoupling means (p. 16):

> "Dynamical decoupling means that the operations of the regulatory subsystem R are neither
> specified nor determined by the metabolism of the constitutive processes of C…"

Supporting characterizations:

> "the activity of R is 'stoichiometrically free' from that of C"

> "the triggering (activation) and operations of the regulatory subsystem (R) do not depend on the
> concentration (or variation in the concentration) of its main components."

**The full numbered list of requirements for regulation** (manuscript p. 17; note the reported text
uses a stray "‟" typographic artifact for primes, and the list was returned as a run-on — the exact
line breaks and any text elided at the ellipses are unverified):

> "(1) Regulatory mechanisms/subsystems R are endogenously synthesised: i.e., they are produced by
> the constitutive regime C of the living system; (2) To be regulatory, R must be dynamically
> decoupled from C, which it regulates… (3) The activation of R is triggered by specific
> changes/perturbations P in either internal or external conditions… (4) The functional role of R
> is to shift (either reversibly or irreversibly) between distinct constitutive/metabolic regimes
> C, C‟, C‟‟… (5) The new metabolic/constitutive regimes C‟ brought forth by R are capable of
> coping with the new conditions…"

**Regulation contrasted with self-maintenance / the constitutive regime:**

> "regulatory control cannot be regarded as a straightforward extension of the collective control
> that enables the dynamical stability of the constitutive regime."   (reported §3, p. 9)

> "Regulatory constraints are distinct from constitutive constraints because they do not directly
> participate in the network of mutually dependent constraints…"   (p. 18)

> "The network of internally produced and mutually dependent constraints realises the system as a
> far from equilibrium unity: the circular organisation underlying their continuous operational
> integration puts together the constitutive regime."   (p. 9)

> "…the action of a regulatory subsystem mediates the effects of a perturbation by modulating its
> own internal dynamics and, typically, by inducing a shift to a new regime, selected among a
> diverse set of available ones."   (p. 2)

### What remains unchecked (Source 2)

The journal volume/page range (31:237–265) was never seen on a retrieved page; conditions (2)–(5)
were returned with internal ellipses whose elided text I never read; and the page attributions and
exact wording come from the fetch tool rather than my own reading of the PDF, so both need
spot-checking against the published version.

---

## Source 3 — Aguilera & Di Paolo, "Integrated information in the thermodynamic limit"

### Bibliographic record — project's citation is **CORRECT**

Aguilera, M. & Di Paolo, E. A. (2019). "Integrated information in the thermodynamic limit."
*Neural Networks*, **114**, June 2019, pp. **136–146**. DOI: **10.1016/j.neunet.2019.03.001**

Title, venue, volume, pages and year all check out as the project has them. Cross-confirmed on two
independent pages: Aguilera's own site
(https://maguilera0.wordpress.com/2019/03/20/integrated-information-in-the-thermodynamic-limit/)
and the UPV/EHU ADDI repository record (https://addi.ehu.eus/handle/10810/32812). Publisher article
ID S0893608019300735 is consistent with both.

Nearby work not to confuse it with: Aguilera & Di Paolo, "Integrated Information and Autonomy in
the Thermodynamic Limit", arXiv:1805.00393 — a *different, earlier* preprint with a similar title.

### Retrieval status: **FULL TEXT READ — but of the arXiv preprint, not the published version**

URL reached: **https://arxiv.org/pdf/1806.07879v3** (arXiv:1806.07879)
Also reached, partially: https://ar5iv.labs.arxiv.org/html/1806.07879 (rendered only through §II;
its answers about later sections are unreliable and I have not relied on them).
The published-version PDF in the ADDI repository
(https://addi.ehu.es/bitstream/handle/10810/32812/1-s2.0-S0893608019300735-main.pdf) was
**ROBOTS_DISALLOWED on three attempts** and was never read.

Full section list confirmed present in the v3 PDF:

> I. INTRODUCTION / II. MODEL — A. Mean field kinetic Ising model — B. Integrated Information φ —
> C. Integrated information in the mean field model / III. RESULTS — A. Integrated information in a
> homogeneous kinetic Ising model — B. Integrated information for measuring agent-environment
> asymmetries — C. Adaptive integrated information facing environmental diversity / IV. DISCUSSION /
> V. CONCLUSION / Appendix A: IIT 3.0 / Appendix B: Simplified integrated information φ

### Passages bearing on the question asked (dynamical vs. static-Gaussian)

**Model class — a kinetic Ising model, i.e. a dynamical stochastic system:**

Abstract (quoted verbatim from Aguilera's own site, cross-checked against the arXiv abstract):

> "The capacity to integrate information is a prominent feature of biological, neural, and cognitive
> processes. Integrated Information Theory (IIT) provides mathematical tools for quantifying the
> level of integration in a system, but its computational cost generally precludes applications
> beyond relatively small models. In consequence, it is not yet well understood how integration
> scales up with the size of a system or with different temporal scales of activity, nor how a
> system maintains integration as it interacts with its environment. After revising some assumptions
> of the theory, we show for the first time how modified measures of information integration scale
> when a neural network becomes very large. Using kinetic Ising models and mean-field approximations,
> we show that information integration diverges in the thermodynamic limit at certain critical
> points. Moreover, by comparing different divergent tendencies of blocks that make up a system at
> these critical points, we can use information integration to delimit the boundary between an
> integrated unit and its environment. Finally, we present a model that adaptively maintains its
> integration despite changes in its environment by generating a critical surface where its
> integrity is preserved. We argue that the exploration of integrated information for these limit
> cases helps in addressing a variety of poorly understood questions about the organization of
> biological, neural, and cognitive systems"

§II Model, opening:

> "We start by describing a general model defining causal temporal interactions between variables."

> "We study a kinetic Ising model where N binary variables (Ising spins) s_i evolve in discrete
> time, with synchronous parallel dynamics."

Eq. (1) — the transition probability, an explicitly time-lagged conditional:

> "p(s_i(t)|s(t-1))=e^{βs_i(t)h_i(t)}/2cosh(βh_i(t))"

**The integrated-information construction — defined on a time-lagged conditional distribution,
Eq. (5):**

> "φ_M^{cut}(τ) = D(p(s(τ_0 + τ)|s(τ_0)), p^{cut}(s(τ_0 + τ)|s(τ_0)))"

i.e. a divergence between the actual conditional distribution over a time lag τ and the conditional
distribution under a *cut* (partitioned) system. The quantity is a function of the time lag τ.

**Minimum information partition:**

> "IIT computes integrated information as the value of φ^{cut} under the minimum information
> partition (MIP), which is the partition of mechanism with the least difference to the original
> partition"

From the Introduction:

> "φ captures the level of irreducibility of the system, understood in the sense that even the least
> disrupting bipartition of the system into two disconnected halves (this is called the minimum
> information partition, MIP) would imply a loss…"

**Gaussian / covariance:** the fetch of the v3 PDF reported that the words **"Gaussian" and
"covariance" do not appear anywhere in the document.** This is a *negative* finding produced by the
fetch tool's reading, not by my own string search over the file (I cannot run a local search, as
bash fetching is prohibited and the PDF was never downloaded). Treat it as strong but not
conclusive; it is consistent with the model being a binary-spin Ising system, for which Gaussian
covariance machinery would be out of place.

Barrett & Seth are cited, but per the fetch only in passing — "Barrett and Seth ([2011])" —
regarding alternative formulations that circumvent computational complexity; the fetch reported no
occurrence of the phrase "stochastic interaction". (Barrett & Seth 2011 is the usual home of the
*Gaussian* IIT-style measures, so where and how it is cited here is worth a human check.)

### What remains unchecked (Source 3)

I read the **arXiv v3 preprint, not the published Neural Networks article**, so any wording,
equation numbering, or section numbering may differ in the version of record; and the
"no Gaussian / no covariance" finding is the fetch tool's report rather than a search I ran myself.
Appendices A and B (where the full φ definition and the MIP optimization live) were listed but their
contents were not read.

---

## Source 4 — Kolchinsky & Wolpert, "Semantic information, autonomous agency and non-equilibrium statistical physics"

### Bibliographic record

Kolchinsky, A. & Wolpert, D. H. (2018). "Semantic information, autonomous agency and
non-equilibrium statistical physics." *Interface Focus* **8**(6): 20180041.
DOI: 10.1098/rsfs.2018.0041. PMCID: PMC6227811. PMID: 30443338.

Consistent with the project's citation. (Volume 8, article 20180041, 2018 — confirmed via the Royal
Society and PMC landing URLs; issue number 6 is inferred from the article's placement and was not
read off a retrieved masthead.)

### Retrieval status: **FULL TEXT REACHED (open access), TARGETED QUOTES EXTRACTED**

URL reached: **https://pmc.ncbi.nlm.nih.gov/articles/PMC6227811/**

Caveat specific to this source: a request for bulk verbatim reproduction of §5 was **declined by the
fetch tool on copyright grounds**. I therefore obtained only short, targeted quotes. The passages
below are consequently fragmentary — I do not have the connective prose, the full equation displays,
or the surrounding qualifications of §5.

### Passages bearing on the question asked (what is intervened upon)

**The core definition (§1.2):**

> semantic information is "the information that a physical system has about its environment that is
> causally necessary for the system to maintain its own existence over time"

**Syntactic vs. semantic (§1.1):**

> "syntactic information, which quantify various kinds of statistical correlation between two systems"
>
> semantic information refers to "those correlations which carry significance or 'meaning' for a
> given system"

**Viability function (§4):**

> "the viability function as the negative of the Shannon entropy of the marginal distribution of
> system 𝒮 at time τ"   (Equation 4.1)

An alternative based on KL divergence from the equilibrium distribution is discussed at Equation 4.2.

**The intervention — full scrambling (§5.1.1, Equation 5.2):**

> "we first consider an intervention that destroys all mutual information by transforming the actual
> initial distribution p_{X_0,Y_0} to the product initial distribution"

This maps the actual joint p(X₀,Y₀) to the product p(X₀)p(Y₀) — i.e. it destroys the
**system–environment correlation**.

**The intervention — partial scrambling via coarse-graining (§5.1.1, Equation 5.5):**

> "the intervened joint distribution at t=0 as q^φ_{X_0,Y_0} = p_{X_0|Y_0}^φ p_{Y_0}"

> "the intervened conditional distribution induced by φ … is taken to be the actual conditional
> probability of system states X_0 given coarse-grained environments φ(Y_0)"

> "Under the intervened distribution, X₀ is conditionally independent of Y₀ given φ(Y₀)"

Note the object being coarse-grained is **φ applied to environment states Y₀**, and the object being
modified is the **conditional p(X₀|Y₀) — the system–environment channel**.

**Explicit statement of what the interventions do and do not perturb (§5.2, "observed" semantic
information):** — *this is the most directly on-point passage retrieved*

> "we define a set of partial interventions in which we partially scramble the conditional
> distribution p_{X_{t+1}|X_t,Y_t}, while keeping the conditional distribution
> p_{Y_{t+1}|X_t,Y_t,X_{t+1}} undisturbed. This ensures that our interventions only perturb the
> information flow from the environment to the system, and not vice versa."

(As flagged at the top of this document: one fetch returned "undisturbed" here and another returned
"undistributed". "Undisturbed" is near-certainly the correct word. Verify before quoting.)

**Semantic information and semantic content (§5.1.1):**

> "we define the amount of stored semantic information as the mutual information in the optimal
> intervention"

> "the semantic content of system state x_0 as the conditional distribution p^*_{Y_0|X_0}"

**On the specific question of interventions internal to the system:**

The fetch tool, asked directly whether the paper anywhere discusses intervening on couplings/edges
internal to the system X, reported: the intervention acts **exclusively on the system–environment
channel**, specifically on p(X₀|Y₀), and the paper **does not** discuss intervening on internal
couplings within X.

This is a **negative/absence finding delivered by the fetch tool**, and absence claims are exactly
the kind a summarization model is worst at — it cannot reliably certify that something appears
nowhere in a long paper. The *positive* evidence retrieved does point the same way: every
intervention quoted operates on p(X₀|Y₀) or p(X_{t+1}|X_t,Y_t), i.e. on the environment→system
channel, and the §5.2 sentence explicitly frames the design goal as perturbing "the information
flow from the environment to the system, and not vice versa" — a system/environment directional
distinction, not a within-system one. But the absence claim itself is **not verified**.

### What remains unchecked (Source 4)

I never read §5 continuously — only short targeted quotes, with the connective prose, the full
equation displays (5.1–5.8), and any scope caveats unread; and the claim that the paper *nowhere*
licenses intervening on edges internal to the system is an unverified absence finding from the
fetch tool, not something I established by reading the paper end to end.

---

## Summary table

| # | Source | Status | URL actually reached |
|---|---|---|---|
| 1 | Francis & Wonham 1976, Automatica 12(5):457–465 | **NOT RETRIEVED** (bibliographic record verified only) | none for the paper; substitutes at control.utoronto.ca |
| 2 | Bich et al., Biological regulation | **FULL TEXT READ** (author manuscript; manuscript pagination) | leonardobich.wordpress.com PDF |
| 3 | Aguilera & Di Paolo 2019 | **FULL TEXT READ** (arXiv v3 preprint, not version of record) | arxiv.org/pdf/1806.07879v3 |
| 4 | Kolchinsky & Wolpert 2018 | **FULL TEXT REACHED; targeted quotes only** | pmc.ncbi.nlm.nih.gov/articles/PMC6227811/ |

Open items for a human with library access: (i) the Francis & Wonham 1976 Automatica PDF — nothing
about that theorem should be asserted until it is read; (ii) the published Neural Networks version
of Aguilera & Di Paolo, to confirm equation/section numbering; (iii) a continuous read of
Kolchinsky & Wolpert §5 to settle the internal-edge question positively rather than by reported
absence; (iv) journal pagination for Bich et al.
