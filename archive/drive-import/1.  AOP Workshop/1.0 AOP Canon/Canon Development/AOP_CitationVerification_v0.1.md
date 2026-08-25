# AOP_CitationVerification_v0.1

**Order:** `TASK_CS_AOP_CitationVerification_20260726`
**Seat:** Claude Science (checker; did not raise these flags and built none of them)
**Date:** 27 July 2026
**Status:** Returned for Ben's sign-off. Verdicts only — no canon edit, no change set.

---

## 0. Eligibility, and the one conflict to record

I verified canon v1.26 in the previous round (order `TASK_CS_AOP_v126_Verification_20260725`,
verdict PASS-WITH-DEFECTS). That round was a **change-set faithfulness** audit: it asked whether
the 85 changed regions matched what the change set authorized. It did not read a single reference
against a primary source, and the references section was byte-identical across the v1.25→v1.26
fold. **No verification claim in this report inherits from that one**, and nothing in that round
committed me to any position on the citations below.

I did not raise the flags. They came from the Drive→Memory re-proof seat
(`AOP_DriveMemory_Reproof_v0.1.md`, Drive id `1DeeSdzz408LC6PO0M3ra8jSbebknKXTR`, §7). I read that
§7 to learn what was alleged, then went to the primaries. **Four of the fourteen flags turn out to
be aimed at papers the canon does not cite**, and one of those four names a defect that is
nevertheless really present — on a different reference. That asymmetry is the most useful thing in
this report and it is set out in §6.

---

## 1. Integrity

| Item | Value |
|---|---|
| Canon file | `AOP_CANON_MASTER_v1.26.md` |
| Drive id | `1MN7rhZExgNSv3mv2h92GqSjUzHSzgpWn` |
| Bytes | 254,046 |
| md5 (recomputed) | `54ceb3772e29f25c6e139b703d550d59` |
| md5 (per order §2) | `54ceb3772e29f25c6e139b703d550d59` — **match** |
| Access | read-only; no write attempted |
| Lines | 850 (`wc -l` / `splitlines`); 851 under `str.split('\n')` |

The AOP folder was swept for a later master: highest version present is v1.26. A candidate
`AOP_Canon_ChangeSet_v1_26_to_v1_27.md` exists in Canon Development (id
`1q20FnSaSEr2oFEukfcoFYnoZf06Ag9Kg`, modified 27 Jul 15:10) and its §4 states **"No reference
altered, added, or removed … References section is byte-identical"** and that the re-proof's
citation flags are "under separate verification and were not folded." That is this order. The
pending fold does, however, introduce one new citation *use*, and it has a defect — §6.4.

### What "read the passage" meant here

Fourteen primary sources were retrieved as full PDFs and text-extracted; every quote below was
matched programmatically against the extracted bytes before being written into this table (no
quote in this report was typed from memory or from an abstract). Retrieval route per source is in
the Retrieval column. Two items are `NOT-CHECKABLE` and are listed separately in §4 with the
access that would close them. **No content anywhere below is inferred from an abstract.**

---

## 2. Tier A — the flagged set

Quotes are ≤15 words and are verbatim from the retrieved primary. Ligature/hyphenation artefacts
of PDF extraction are silently repaired inside quoted strings; nothing else is altered.

---

### A1. Kawai, Parrondo & Van den Broeck, *Phys. Rev. Lett.* **98**, 080602 (2007)

| Field | Content |
|---|---|
| **Canon claim** | **None.** The canon never cites this paper. Grep of all 850 lines: no `080602`, no `Kawai R, Parrondo`, no 2007 Kawai entry. The only occurrence of "Kawai" in the canon is as third author of reference **[1]** (L630, the 2009 *New J. Phys.* review). |
| **Primary says** | Abstract: <q>D(ρ‖ρe) is the relative entropy of ρ versus ρe</q>, where ρ, ρe are <q>the phase space density of the system measured at the same intermediate but otherwise arbitrary point in time</q>. Hamiltonian, equilibrium→equilibrium, ⟨W_diss⟩ = kT·D. |
| **Retrieval** | Full text, arXiv:cond-mat/0701397 (4 pp.); bibliographic record confirmed at Crossref (title *Dissipation: The Phase-Space Perspective*, PRL 98, issue 8, 2007). |
| **Verdict** | `SUPPORTED` — as a characterisation of the 2007 paper, the flag's description is exactly right: single-time phase-space densities, not a path measure, not a rate. |
| **Flag assessment** | `FLAG-INCORRECT` **as applied to the canon** — the conditional never fires, because the canon does not cite this paper for anything. **But see §6.1: the identical defect is present in the canon, on reference [1].** The re-proof's own §7 parenthesis noticed the canon cites the 2009 review and judged it "a closer fit"; that judgement is the part that does not survive checking. |

---

### A2. Lebowitz & Spohn, *J. Stat. Phys.* **95**, 333 (1999)

| Field | Content |
|---|---|
| **Canon claim** | **None.** Zero occurrences of "Lebowitz", "Spohn", or "95, 333" in the canon. |
| **Primary says** | The terminological claim holds: in the full retrieved text, **0 occurrences** of "relative entropy", "Kullback", "Leibler", or "divergence" (24 of "entropy", 30 of "action functional"). But the *object* is there under another name — Eq. (2.21) and the sentence after it: <q>the action functional equals − log(dP R [0,t] /dP[0,t])</q>, with <q>dP R/dP denoting the Radon-Nikodym derivative</q>, P and P^R the forward and time-reversed **path measures** of the stationary process. |
| **Retrieval** | Full text, arXiv:cond-mat/9811220 (30 pp.); Crossref confirms Lebowitz & Spohn, *J. Stat. Phys.* 95, 333–365 (1999). **Preprint, not the version of record** — see §4.2. |
| **Verdict** | `SUPPORTED` on the narrow terminological reading; the paper does establish the forward/reverse path-measure log-density, just never names it a relative entropy. |
| **Flag assessment** | `FLAG-OVERSTATED`. "Never uses 'relative entropy' or 'Kullback–Leibler'" is true and I established it properly (exhaustive search of the whole text, not a spot check). "Do not cite for the KL formulation" over-reaches: the paper contains the Radon–Nikodym path-measure statement that *is* the KL integrand. The honest instruction is narrower — cite it for the action functional as −log(dP^R/dP), not for the words "relative entropy". Moot for the canon either way. |

---

### A3. Parrondo, Van den Broeck & Kawai, *New J. Phys.* **11**, 073008 (2009) — canon's **[1]**

| Field | Content |
|---|---|
| **Canon claim** | Three load-bearing uses. §2 L61: <q>entropy production equals the relative entropy (Kullback–Leibler divergence) between the forward and time-reversed **trajectory distributions** [1]</q>. §4 L125: <q>the process must be stationary, the regime in which σ = D(forward ∥ reverse) is the clean object used here</q>. §4 L123 / Table 3 L444: the D→M edge is <q>a scoped corollary of the trajectory-irreversibility identity we already invoke for Drive [1]</q>. σ is used throughout as a **rate** ("entropy production rate", L77/L123; Figure DM plots σ in <q>nats per step</q>, L181). |
| **Primary says** | Abstract: an exact relationship <q>quantified by the relative entropy between forward and backward **states**</q>. §2, Eq. (3): D(ρ‖ρ̃) = ∫dΓ ρ(Γ,t) ln[ρ(Γ,t)/ρ̃(Γ̃,t)] — ρ is <q>the probability density in phase space to observe the system to be in a micro-state Γ</q> at <q>an intermediate time t</q>. Setting is Liouville/Hamiltonian with a control protocol λ(t) over [0,τ]; the quantity delivered is a total ΔS for the process, and §5 gives the coarse-graining inequality ΔS = kD(ρ‖ρ̃) ≥ kD(p‖p̃). Full text contains **0 occurrences of "path measure"**, "per unit time", "master equation", or "entropy production rate". §3.3 reaches a NESS only as a limit of *n* initially decoupled canonical systems brought into thermal contact — still a single-time phase-space D. |
| **Retrieval** | Full text, arXiv:0904.1573 (15 pp.); Crossref record confirms venue, volume, DOI. |
| **Verdict** | `MISSTATED`. Reference [1] is a single-time phase-space-density identity for a protocol-driven transition, not a trajectory-distribution identity and not a rate. The canon's L61 wording ("trajectory distributions") and L125's σ-as-rate reading both go past what [1] establishes. **This is exactly the defect the flag attributed to the 2007 PRL — it is on the 2009 review instead, and the canon does rely on it.** |
| **Flag assessment** | `FLAG-OVERSTATED` in the direction that matters: the flag asked me to "check adequacy" and the re-proof's parenthesis pre-judged the 2009 review as "a closer fit than the 2007 PRL". It is closer, and it is still inadequate for what the canon claims. |
| **Materiality** | High. This reference supports the canon's **only** `forced × theorem/corollary` row (Tier B, §3′). The mathematics is not in question — the fix is the citation, per A4. |

---

### A4. Maes & Netočný, *J. Stat. Phys.* **110**, 269 (2003), Prop. 4.2, Eqs. 4.4–4.6

| Field | Content |
|---|---|
| **Canon claim** | **None.** Not currently cited. Proposed by the re-proof as the sharper primary to substitute for [1]. |
| **Primary says** | Prop. 4.1, Eq. (4.3)–(4.4) define R^t_μ̂ ≡ ln dP^μ̂/dP^{μ̂_t πΘ} — an explicit Radon–Nikodym derivative of a **path-space measure** against its time-reversal. Prop. 4.2, Eq. (4.5)–(4.6): E[e^{−R}] = 1 and <q>its expectation equals the (Gibbs-) entropy production</q>. **The rate is elsewhere:** §6, Eq. (6.11), when μ̃ is stationary for the Markov chain, gives <q>the mean entropy production rate</q> Σ μ̃(M)q(M,M′)ln[q(M,M′)/q(πM′,πM)] — with the time-reversal involution π explicit, which is precisely the canon's slot **R**. |
| **Retrieval** | Full text, arXiv:cond-mat/0202501 (39 pp.); Crossref confirms Maes & Netočný, *J. Stat. Phys.* 110, 269–310 (2003), DOI 10.1023/A:1021026930129. |
| **Verdict** | `SUPPORTED`, **with a locator correction.** Prop. 4.2 / Eqs. 4.4–4.6 is the path-measure log-density object as claimed, and its expectation is an entropy production — but a *difference over an interval*, not a rate. The canon needs a rate. The rate statement is **Eq. (6.11)**, and it is better than the canon needs: stationary, discrete-state Markov, involution-explicit. |
| **Flag assessment** | `FLAG-CONFIRMED`. The substitution is the right move. Cite **Prop. 4.2 / Eqs. (4.4)–(4.6)** for the path-measure identity and **Eq. (6.11)** for the stationary rate; citing 4.2 alone for σ-as-rate would reproduce the [1] defect in a new place. |

---

### A5. Spinney & Ford — parity framing (order §3: highest Tier A priority)

| Field | Content |
|---|---|
| **Canon claim** | §4 L125, the sentence the citation is actually attached to: <q>the decomposition of entropy production for stochastic dynamics with odd as well as even variables carries a component beyond the familiar two, and the two-component treatment is recovered as the special case in which the stationary distribution *is* symmetric in the odd variables</q> [Spinney & Ford 2012; Ford & Spinney 2012]. The convention language sits in a **separate, uncited** sentence: <q>that claim is convention-dependent</q>, and the framing that R must be *declared* is made on the canon's own authority as declaration-tuple design (L90, L592, L594). |
| **Primary says** | PRL 108 abstract, verbatim: <q>A previously reported formalism is obtained when the stationary probability distribution is symmetric for all variables that are odd under time reversal</q>, and the total <q>can be divided into three quantities</q>. PRE 85: the third component <q>only arises when odd dynamical variables play a role in the dynamics</q>. PRE 86 abstract: it <q>exists when at least some of the coordinates … change sign under time reversal, and when the stationary state is asymmetric in these coordinates</q>. The flag's own quote is confirmed present: <q>The correct path, x*, to consider is the time reversed trajectory proper</q> (PRL 108, p. 1–2). |
| **Retrieval** | Full text of all three: arXiv:1201.0904 (PRL 108, both v1 and v2 pulled and diffed), arXiv:1203.0485 (PRE 85), arXiv:1204.4822 (PRE 86). |
| **Verdict** | `SUPPORTED`. The canon's §4 sentence is a near-verbatim restatement of the PRL abstract, in both halves (three components; two-component form recovered under odd-variable symmetry of the stationary distribution). |
| **Flag assessment** | `FLAG-INCORRECT`. The flag's premise — "a canon sentence presenting parity as a convention on their authority" — does not obtain. The canon does not attribute the convention framing to Spinney & Ford; it attributes the *decomposition* to them, which is what they prove, and it makes the declare-R point separately and unsourced. Both things the flag says S&F argue (that the sign flip is correct, not free) are true of the papers and are **not contradicted** by anything the canon says on their authority. **The scope condition being folded in v1.27 is not exposed by this flag.** |
| **Residual nit** | L444 (Table 3) sets the citation immediately after <q>until R is declared for that case</q>, so the bracket sits adjacent to declare-R phrasing. The cited proposition (silence on odd-variable systems) is supported; only the adjacency is loose. Optional tightening, not a defect. |

---

### A6. Author-order and title pairing; the Publisher's Note

| Field | Content |
|---|---|
| **Canon claim** | L672: Spinney RE, Ford IJ — PRE **85**, 051113. L674: Ford IJ, Spinney RE — PRE **86**, 021127, plus the canon's own note that <q>these are two distinct papers with opposite author order</q> and that pairing "Ford & Spinney" with the PRE 85 title <q>is a conflation</q>. L674 also records the PRL 108, 170603 paper and states the Publisher's Note at PRL 108, 199905 <q>has **not** been retrieved and whose content is unknown</q>. |
| **Primary says** | Crossref, all four: PRE 85, 051113 = **Spinney, Ford** (*Entropy production in full phase space for continuous stochastic dynamics*); PRE 86, 021127 = **Ford, Spinney** (*…in discrete full phase space*); PRL 108, 170603 = **Spinney, Ford** (*Nonequilibrium Thermodynamics of Stochastic Systems with Odd and Even Variables*); PRL 108, 199905 = <q>Publisher's Note: Nonequilibrium Thermodynamics of Stochastic Systems with Odd and Even Variables</q>, Spinney & Ford, issue 19, 2012 — **it exists**. Author orders and title–venue pairings in the canon are correct in every case. |
| **Retrieval** | Crossref records (4/4) + full text of all three research papers via arXiv. **Publisher's Note content: not retrieved.** |
| **Verdict** | `SUPPORTED` on pairing and author order. Publisher's Note **existence** `SUPPORTED`; its **content** `NOT-CHECKABLE` (§4.1). |
| **Flag assessment** | `FLAG-CONFIRMED` on existence — and the canon already carries the conflation warning and already describes the Note's content as unknown, which is the accurate posture. Nothing to correct. |
| **Do not over-read** | arXiv v1 of 1201.0904 carries a different title (*"…An integral Fluctuation Theorem for a generalised house-keeping heat"*) from v2/published. That is suggestive of what the Note addresses and is **not evidence of it.** I did not retrieve the Note and make no claim about its content. |

---

### A7. Seifert, *Rep. Prog. Phys.* **75**, 126001 (2012), Secs. 4.1 and 4.5.2

| Field | Content |
|---|---|
| **Canon claim** | **None.** This review is not in the canon. (The canon's two Seifert entries are Barato–Seifert TUR 2015 at L636 and Speck–Seifert 2005 at L805.) Proposed by the re-proof as support for the not-forced framing. |
| **Primary says** | Sec. 4.1, verbatim: <q>Three choices for the conjugate dynamics and the associated mapping have been considered so far</q> — enumerated as reversed, dual, dual-reversed. Sec. 4.5.2, verbatim: <q>one could also keep the flow unchanged for the conjugate dynamics</q>, <q>which would lead to another class of FTs</q>. |
| **Retrieval** | Full text, arXiv:1205.4176 (105 pp.); Crossref confirms venue/volume/page/DOI. |
| **Verdict** | `SUPPORTED` for the not-forced framing, **with a scope caveat**: Sec. 4.5.2's freedom is over the reversal of an **external flow field** u(r), not over the parity of a velocity coordinate. It is a good analogue of the canon's point, not a literal statement about odd variables. Sec. 4.1's three-choices enumeration is the stronger and more on-point support. |
| **Flag assessment** | On the substitution: `FLAG-CONFIRMED` (with the caveat above). On the UNVERIFIED sub-flag: **`FLAG-CONFIRMED`.** I searched the entire 105-page text for an explicit statement that velocity or momentum flips sign under time reversal and found none. Sec. 2.6.1 introduces underdamped motion with v ≡ ẋ and never states its parity; Sec. 4.5.1 says the FTs hold <q>with the obvious modification that initial (and daggered) distributions now depend on x and v</q> — leaving the parity implicit; Sec. 4.5.3 on magnetic fields does not discuss reversing B, as the flag said. The only explicit parity statements in the review concern **functionals** (work and heat odd under reversed dynamics, Sec. 4.2.1), not coordinates. |
| **Consequence** | If the canon ever wants an explicit *coordinate*-parity statement, Seifert 2012 is the wrong source. Spinney & Ford PRL 108 supplies it directly (εx with ε_i = ±1 for even/odd variables) and is already in the canon. |

---

### A8. Crutchfield & Feldman 2003 and Bialek–Nemenman–Tishby 2001 for "E = 0 iff i.i.d."

| Field | Content |
|---|---|
| **Canon claim** | §4 L123: <q>E = 0 holds if and only if past and future are independent, i.e. the process is i.i.d.</q> — **carrying no citation at all.** The bracket in that sentence's vicinity, [13], attaches to the *definition* of E (Crutchfield, Ellison & Mahoney 2009). C&F 2003 is cited in the canon at exactly two places (L194, L456) and for exactly one thing: that <q>E is defined only for a stationary process</q>. BNT 2001 is cited once (L198) for the bounded/logarithmic/power-law regimes. **Neither is cited for the iff.** |
| **Primary says** | C&F: forward direction only, and by example — Sec. VI A, on two coins, <q>for both processes the excess entropy E and the transient information T are zero</q>; the classification section, <q>We have E = 0 and T = 0. Independent, identically distributed (IID) processes are examples of this class.</q> The one genuine iff in the paper is about a different object — App. A, <q>the inequality is saturated if and only if the process is independent identically distributed</q>, said of H(L) ≥ L·h_μ(L), not of E = 0. BNT: Eq. (18) gives I_pred for the Markov case with no proof. |
| **Retrieval** | C&F full text, arXiv:cond-mat/0102181 (35 pp.). BNT full text, arXiv:physics/0007070 (53 pp.). Both Crossref-confirmed. |
| **Verdict** | On the sources: `SUPPORTED` — the flag characterises both correctly; neither states the iff, and C&F gives only the forward direction. On the canon: the iff is **unsourced**, which is a different and slightly worse defect than misattribution — a reader cannot tell it is the framework's own step. |
| **Flag assessment** | `FLAG-INCORRECT` on attribution (the canon does not cite these sources for the iff), `FLAG-CONFIRMED` on the substance (the converse must be presented as derived). |
| **Already in hand** | The pending v1.27 Edit 3 replaces the eliding "i.e." with an explicit derivation via shift-invariance and induction on the split point. That is the right repair and it lands on the right line (L123). No further correction needed beyond ensuring the derived step is *labelled* as the framework's own. |

---

### A9. E = I(X₀;X₁) for a stationary Markov chain — "folklore"

| Field | Content |
|---|---|
| **Canon claim** | **None.** No occurrence in the canon of `I(X₀;X₁)`, `I(X_0`, or "stationary Markov chain". The claim is a lemma internal to the re-proof memo, not a canon claim. |
| **Primary says** | C&F **Prop. 11**: <q>For an order-R Markovian process, the excess entropy is given by E = H(R) − Rh_μ</q> — which at R = 1 is I(X₀;X₁). Its proof, verbatim: <q>This result will be proved in Sec. VI C, when we consider an example Markovian process.</q> — i.e. by worked example, plus a pointer to three references. BNT Eq. (18) states the Markov reduction without proof. |
| **Retrieval** | Full text (both). |
| **Verdict** | `SUPPORTED` — the flag's characterisation of both sources is exact. |
| **Flag assessment** | `FLAG-CONFIRMED`, and **not-applicable to the canon.** If a future fold imports this identity it must arrive with a derivation; today there is nothing in the canon to correct. |

---

### A10. Equation numbering: C&F Prop. 8

| Field | Content |
|---|---|
| **Canon claim** | The canon cites C&F by **section**, never by equation: L726 credits <q>whose Section II.B fixes the measurement stream as a stationary stochastic process</q>. No `Eq. (54)` or `Eq. (55)` anywhere in the canon. |
| **Primary says** | In the retrieved arXiv version (cond-mat/0102181v1, the **only** version on arXiv), Prop. 8 is **Eq. (53)**: E = lim_{L→∞} I[S₀S₁···S_{2L−1}; S_{2L}S_{2L+1}S_{2L−1}]. Eq. (54) is Prop. 9 (h_μ(L) convergence); Eq. (56) is Prop. 10 (periodic); Eq. (57) is Prop. 11. I enumerated every Proposition→Equation pairing in the file to confirm this is not a local mis-parse. |
| **Retrieval** | arXiv full text. **Published (AIP) version not retrieved** — see §4.3. |
| **Verdict** | `WRONG-LOCATOR` **against the flag**: the arXiv number is 53, not 55. The published number is `NOT-CHECKABLE`. |
| **Flag assessment** | `FLAG-INCORRECT` on the arXiv half, which is the half I could check. The flag's stated discrepancy ("(54) published / (55) arXiv") does not match the arXiv document. Moot for the canon, which cites no equation number — **but see §6.4, because the pending v1.27 text starts citing Prop. 8 and gets something else about it wrong.** |
| **Source typo, recorded** | The second block in the printed Eq. (53) ends `S2L−1`, duplicating the first block's last index; it should run to a higher index. A typo in the source, not in the canon or the flag. |

---

### A11. Esposito & Van den Broeck, PRE **82**, 011143 (2010), Eq. (33); author order in 011144

| Field | Content |
|---|---|
| **Canon claim** | **None.** No `011143`, `011144`, `090601`, `S_na`, "non-adiabatic" or "nonadiabatic" anywhere in the canon. Used only inside the re-proof's §4 to close off a bad repair. |
| **Primary says** | Eq. (33) of Paper I, verbatim: `Ṡ_na(t) = ½ Σ_{m,m′} J_{m,m′}(t) N_{m,m′}(t) ≥ 0` , with the second line `= − Σ_m ṗ_m(t) ln[p_m(t)/p^st_m(λ_t)]`. Exactly the form the re-proof relies on: at a genuine NESS ṗ_m = 0, so it vanishes identically. Crossref: 011143 = **Esposito, Van den Broeck**, *Three faces of the second law. I. Master equation formulation*; 011144 = **Van den Broeck, Esposito**, *…II. Fokker-Planck formulation*. |
| **Retrieval** | Full text of Paper I (arXiv:1005.1683) and Paper II (arXiv:1005.1686); both Crossref-confirmed. |
| **Verdict** | `SUPPORTED` — equation number, content, and both author orders confirmed. |
| **Flag assessment** | `FLAG-CONFIRMED` on the reversed author order (real, and a genuine trap), **not-applicable to the canon.** The re-proof's use of Eq. (33) is faithful. |

---

### A12. Esposito & Van den Broeck, *Phys. Rev. Lett.* **104**, 090601 (2010) — the ⟨ΔS_na⟩ = 0 sentence

| Field | Content |
|---|---|
| **Canon claim** | **None** (not cited). |
| **Primary says** | The sentence in question, in context: <q>During such a so-called adiabatic process, the probability distribution will assume at all times the instantaneous steady state form</q> p^st_m(λ_t), and <q>this implies ⟨ΔS_na⟩ = 0</q>. The premise is an explicit timescale separation — relaxation fast relative to the driving schedule — and the conclusion is an **ensemble average**. The very next sentence: when that separation does not exist, ⟨ΔS_na⟩ ≠ 0. |
| **Retrieval** | Full text, arXiv:0911.2666 (4 pp.); Crossref confirms *Three Detailed Fluctuation Theorems*, PRL 104, 2010. |
| **Verdict** | `SUPPORTED` — the flag is right on both counts (slow-driving/adiabatic premise; ensemble average). |
| **Flag assessment** | `FLAG-CONFIRMED`, not-applicable to the canon. The genuine-NESS claim should rest on Paper I Eq. (33), where ṗ_m = 0 does the work directly — as the re-proof in fact did. |

---

### A13. Hatano & Sasa, *Phys. Rev. Lett.* **86**, 3463 (2001)

| Field | Content |
|---|---|
| **Canon claim** | Cited at L131 and L803, but **not** for a vanishing-at-constant-driving claim: L131 uses it (with Oono–Paniconi and Speck–Seifert) for the housekeeping term σ_hk verified against a Schnakenberg cycle decomposition; L803 describes it as the <q>housekeeping/excess decomposition of dissipation for driven Langevin systems</q>. |
| **Primary says** | The full text contains **0 occurrences of the word "constant"**; the only nearby framing is <q>for the case of time-independent α, Eq. (30) reduces to the relation referred to as the fluctuation theorem</q> — a different statement. Eq. (11) is `⟨exp[−∫₀^τ dt α̇ ∂φ(x;α)/∂α]⟩ = 1`; the α̇ factor is what makes the integrand vanish at constant driving. So the property follows from Eq. (11) rather than being asserted in prose. |
| **Retrieval** | Full text, arXiv:cond-mat/0010405 (4 pp.). |
| **Verdict** | `SUPPORTED` — flag's characterisation exact. The canon's own use of the paper is faithful (housekeeping/excess split is Eqs. (15)–(19), which the paper does state in prose). |
| **Flag assessment** | `FLAG-CONFIRMED` on the source; **the canon does not make the flagged claim**, so nothing to correct there. |
| **Bonus, discharged** | The canon's L803 residual <q>⚠ confirm DOI before final</q> is now closed: DOI `10.1103/PhysRevLett.86.3463`, pp. 3463–3466, issue 16, 2001, Crossref-verified. |

---

### A14. Schnakenberg, *Rev. Mod. Phys.* **48**, 571 (1976), Sec. VII, Eq. (7.6)

| Field | Content |
|---|---|
| **Canon claim** | **The canon does rely on it** — the order asked me to determine this, and the answer is yes, in three places. §4 L127: the σ̇ sector-split result <q>is the general instance of the time-antisymmetric (entropy-flux) versus time-symmetric (frenesy / dynamical activity) split of the path-space action for Markov jump and diffusion processes</q> [Maes 2020; **Schnakenberg 1976**]. Table 3 L468 repeats it. L822 records the consequence: <q>The sector-split σ̇-half is upgraded FRONTIER→SETTLED-general [Da Costa et al. 2023; Maes 2020; Schnakenberg 1976]</q>. The reference entry L787 describes it as <q>cycle/affinity decomposition; entropy production is a sum over cycle affinities × currents</q> and carries <q>⚠ read decomposition statement in full text before final</q>. |
| **Primary says** | **Not retrieved.** Closed access; no OA copy exists (Semantic Scholar: `CLOSED`, no openAccessPdf; Unpaywall: no OA location; no PMC; no Crossref TDM link). Publisher pages returned HTTP 403 after the domain was allowlisted. Bibliographic record confirmed at Crossref: Schnakenberg J., *Network theory of microscopic and macroscopic behavior of master equation systems*, Rev. Mod. Phys. 48(4), 571–585 (1976). |
| **Retrieval** | `NOT RETRIEVED` — routes tried in §4.4. |
| **Verdict** | `NOT-CHECKABLE` on the flag's two specific counts (continuous-time flux×affinity form vs. discrete-time chain expression; arbitrary time-dependent p(t) vs. stationary states only). I will not confirm them, and per the order's standing rule I do not guess from the abstract. |
| **Flag assessment** | `NOT-CHECKABLE`. The flag may well be right; I cannot say so. |
| **Separate finding that *is* checkable** | See **§6.2**: independent of the flag's two counts, the canon's L127/L468 attribution to Schnakenberg 1976 is anachronistic. A 1976 master-equation network paper cannot be the source of "the time-antisymmetric versus time-symmetric split of the path-space action" — that framing is Maes's. This is establishable from the canon's own claim plus Maes 2020 (retrieved), without opening Schnakenberg. |

---

## 3. Tier B — the settled core

Per order §2, every reference supporting a claim graded `forced × theorem/corollary` in v1.26.
Confirmed to be **exactly one row**: canon §12′ Table 3′ L573, *D→M memory floor, direction
σ>0 ⇒ E>0*, graded `forced (four scope conditions, incl. time-reversal parity)` × `theorem/corollary`.
L588 and L844 both state that after v1.26 <q>the hard floor is **one row**, not two</q>, the
causal-boundary row having left with the deleted physics block. The count is right.

Its supporting references, each read at the primary:

| Reference | Canon claim | Primary says | Retrieval | Verdict |
|---|---|---|---|---|
| **[1]** Parrondo, Van den Broeck & Kawai 2009 | σ = KL between forward and reverse **trajectory distributions**, as a **rate** (L61, L125) | relative entropy between forward and backward **states** — single-time phase-space densities; total ΔS, not a rate | Full text, arXiv:0904.1573 | **`MISSTATED`** — see A3. The canon's strongest-graded row rests on it. |
| **[13]** Crutchfield, Ellison & Mahoney 2009 | E = I(past; future) (L123); the crypticity decomposition Cμ = E + χ, χ ≥ 0 (L125); Ξ = Cμ⁺ − Cμ⁻ as the <q>forward/reverse statistical-complexity asymmetry</q> (L125) | Thm 1: <q>Excess entropy is the mutual information between the predictive and retrodictive causal states</q>; <q>the predictive statistical complexity is given by C⁺μ = E + H[S⁺\|S⁻]</q>; Cor. 1: C^±μ = E + d(M⁺,M⁻) with <q>A process's crypticity is d(M+, M−) ≡ H[S +\|S−] + H[S −\|S+]</q>; <q>It is helpful to use causal irreversibility to measure this asymmetry: Ξ ≡ C⁺μ − C⁻μ</q> | Full text, arXiv:0902.1209 | `SUPPORTED`. One looseness: the canon writes an unsubscripted "Cμ = E + χ". In the source the gap is H[S⁺\|S⁻] for the predictive Cμ⁺ and the full crypticity d for the bidirectional C^±μ. Worth a subscript; not a defect. |
| **C&F 2003** | <q>E is defined only for a stationary process</q> (L194, L456); Sec. II.B fixes the stream as stationary (L726) | Sec. II.B: <q>The measurement streams we shall consider will be stationary stochastic processes.</q> | Full text, arXiv:cond-mat/0102181 | `SUPPORTED`. Exactly what the canon uses it for. |
| **Spinney & Ford 2012 / Ford & Spinney 2012** | the fourth (parity) scope condition on the theorem, L125/L444/L842 | see A5 — near-verbatim restatement of the PRL abstract | Full text ×3 | `SUPPORTED` |

**Tier B verdict: the row's grade is not supported by its citation.** The `forced × theorem/corollary`
grade is a claim about a *cited law*; the law as cited (reference [1]) is an equilibrium-to-equilibrium
single-time identity, not the stationary trajectory-level rate the theorem needs. The mathematics is
unaffected and the correction is bibliographic — Maes & Netočný Eq. (6.11) is the statement the row
actually stands on. Until that substitution is folded, the canon's single strongest-graded row cites
a source that does not say what the row asserts.

---

## 4. `NOT-CHECKABLE`, and what would close each

**4.1 Publisher's Note, PRL 108, 199905 (2012) — content.** Existence confirmed at Crossref (title
and authors verified). Content not retrieved. Routes tried: `journals.aps.org` abstract and PDF
(HTTP 403 after the domain was allowlisted); `link.aps.org` (blocked, and the HTTPS-only fetcher
rejects the http:// URL Semantic Scholar returns); Unpaywall (no valid OA PDF); PMC (no PMCID);
Crossref TDM (no links). **Closes with:** institutional APS access, or a PDF placed in the folder.
The canon's current posture — "not retrieved, content unknown" — is accurate and needs no change.

**4.2 Lebowitz & Spohn — version of record.** I read arXiv:cond-mat/9811220, not *J. Stat. Phys.*
95, 333–365. The negative existence claim in A2 is established **for the preprint**; a published
version could in principle differ. **Closes with:** Springer access. Low priority — the canon does
not cite this paper.

**4.3 Crutchfield & Feldman — published equation numbering.** `pubs.aip.org` returned 403 after
allowlisting; `csc.ucdavis.edu` blocked; Unpaywall/Crossref-TDM report no OA location for the
published version (arXiv is the only OA copy, status GREEN). **Closes with:** AIP access.
Consequence-free for the canon, which cites by section.

**4.4 Schnakenberg 1976 — Sec. VII, Eq. (7.6).** The material one. Routes tried: `journals.aps.org`
abstract and PDF (403 after allowlisting), Unpaywall (no OA location), Semantic Scholar
(`CLOSED`, empty openAccessPdf), PMC (no PMCID), Crossref TDM (no links), DOI resolution (landing
page only). **Closes with:** institutional APS access to Rev. Mod. Phys., or a scan placed in the
folder. **This blocks the canon's L787 residual** — the entry's own <q>⚠ read decomposition
statement in full text before final</q> stands, undischarged. It does **not** block §6.2, which is
establishable without the paper.

---

## 5. Tier C

Out of scope per order §2 and left untouched. The canon's reference list (§References, L628–L820)
contains **71 bibliographic entries**. Nine were examined under Tier A/B: reference [1] (L630),
[13] (L654), Spinney & Ford PRE 85 (L672), Ford & Spinney PRE 86 + PRL 108 + Publisher's Note
(L674), Crutchfield & Feldman (L686), Maes 2020 (L785, read as co-cited source for the same claim
as Schnakenberg), Schnakenberg (L787), Hatano & Sasa (L803), Bialek–Nemenman–Tishby (L815).
**Tier C therefore stands at 62 entries, unexamined.**

Two Tier-C-adjacent residuals were discharged incidentally, both by Crossref record, and are
reported so they are not re-done: **Hatano–Sasa 2001** DOI (§A13) and **Bialek–Nemenman–Tishby
2001** DOI `10.1162/089976601753195969`, *Neural Comput.* 13(11), 2409–2463 — L815's
<q>⚠ confirm DOI before final</q> is closed. BNT's canon use at L198 (bounded / logarithmic /
power-law regimes of predictive information) was also checked against the primary while I had it
open and is `SUPPORTED`: <q>Ipred(T) can remain finite, grow logarithmically, or grow as a
fractional power law</q>.

---

## 6. Findings not in the flag list

The order asked for independent checking, so these are reported whether or not anyone flagged them.
§6.1 and §6.2 are the two that matter.

**6.1 The σ-as-path-measure defect is real, and it is on reference [1].** The flag list spent items
1–4 on this cluster and aimed the MISSTATED verdict at a paper the canon does not cite (2007 PRL),
while treating the paper the canon *does* cite (2009 NJP review, reference [1]) as "a closer fit."
It is closer and it is still wrong for the job: single-time phase-space densities, protocol-driven
equilibrium→equilibrium, total ΔS not a rate; zero occurrences of "path measure" or "entropy
production rate" in the full text. The canon asserts trajectory distributions (L61) and uses σ as a
rate in nats per step (L181). **This sits under the canon's only `forced × theorem/corollary` row.**
The flag's structure — chasing the wrong paper for the right defect — is exactly the failure mode
the order warned about in the opposite direction.

**6.2 Schnakenberg 1976 is cited for a result that postdates it by decades.** Canon L127 and L468
cite [Maes 2020; Schnakenberg 1976] jointly for "the time-antisymmetric (entropy-flux) versus
time-symmetric (frenesy / dynamical activity) split of the path-space action," and L822 leans on
that pair to upgrade the sector-split half FRONTIER→SETTLED-general. Maes 2020 supports it exactly
— <q>Frenesy is the time-symmetric part of the path-space action with respect to a reference
process</q>, for Markov jump and diffusion processes. Schnakenberg 1976 is a master-equation network
paper about cycle/affinity decomposition; "frenesy," "dynamical activity," and the path-space action
split are Maes's framework, roughly forty years later. Corroborating detail: in Maes 2020's own text
Schnakenberg appears **only once, in the bibliography** (ref. [21]) — Maes does not use it in-text
for the split. The canon's own reference entry (L787) describes Schnakenberg correctly as a
cycle/affinity decomposition, which is *not* the claim L127/L468 attach to it — so the canon is
internally inconsistent about what this reference says. **This is checkable without retrieving
Schnakenberg**, and it is independent of the flag's two NOT-CHECKABLE counts. Recommended fix: carry
the path-space-action split on Maes 2020 (and Da Costa et al. 2023) alone, and cite Schnakenberg
only for cycle/affinity decomposition, which is what L787 and L131 already use it for.

**6.3 The "E = 0 iff i.i.d." step is unsourced, not misattributed.** Recorded in A8; noted here
because the flag's framing ("the canon must present the converse as derived, not cited") implies the
canon currently cites it. It does not cite anything. The pending v1.27 Edit 3 fixes the proof; the
labelling should make clear the step is the framework's own.

**6.4 A defect in the pending v1.27 text, flagged before it lands.** Change set Edit 2 inserts, as
the new fifth scope condition, the verbatim text: *"the past–future split is contiguous, with the
present assigned to the past: E = I(X_{≤0} ; X_{≥1}), following Crutchfield & Feldman (2003),
Prop. 8."* In C&F's own proof of Prop. 8 (App. A 7) the split runs the other way: `H[→S^L | ←S^L] =
H[S₀, S₁, …, S_{L−1} | S_{−L}, …, S_{−1}]` — the past is S_{−L}…S_{−1} and the **present S₀ belongs
to the future**, i.e. E = I(X_{≤−1}; X_{≥0}). Both are contiguous splits, so the theorem and the
counterexample argument are untouched; but "with the present assigned to the past … following
Crutchfield & Feldman, Prop. 8" attributes to C&F the opposite indexing convention from the one they
use. Cheapest fix: keep the canon's own convention and drop "following", or say "contiguous split;
C&F Prop. 8 uses the mirror-image index assignment, which is the same object under relabelling."
This is a builder's fold, not mine to make.

**6.5 One optional tightening (A5 residual).** L444's citation bracket sits adjacent to
"until R is declared for that case." Supported as to the cited proposition; loose as to adjacency.

---

## 7. Corrections list, ready for a future fold

Ordered by consequence. None of these is applied here; a builder folds them.

| # | Location | Correction | Basis | Consequence |
|---|---|---|---|---|
| **C-1** | §2 L61; §4 L125; and reference **[1]** at L630 | Stop citing [1] for the trajectory-level, rate-valued identity. Substitute **Maes & Netočný 2003**: Prop. 4.2 / Eqs. (4.4)–(4.6) for the path-measure log-density, **Eq. (6.11)** for the stationary mean entropy production rate. Retain [1], if wanted, for the coarse-graining inequality (its §5) — which is what L456 already uses it for and which it does support. | A3, A4, §6.1 | **High.** Repairs the citation under the canon's only `forced × theorem/corollary` row. Mathematics unchanged; grade unchanged. |
| **C-2** | §4 L127; §12 L468; changelog L822 | Remove Schnakenberg 1976 from the bracket supporting the path-space-action time-antisymmetric/time-symmetric split. Carry that on Maes 2020 + Da Costa et al. 2023. Keep Schnakenberg for cycle/affinity decomposition (L131, L787). | A14, §6.2 | **High.** Fixes an anachronistic attribution and an internal inconsistency with L787. Does not weaken the SETTLED-general upgrade, which Maes and Da Costa carry. |
| **C-3** | Pending v1.27 change set, Edit 2 | Correct or drop "following Crutchfield & Feldman (2003), Prop. 8" as support for assigning the present to the past. | §6.4 | Medium — catches it before it enters canon. |
| **C-4** | §4 L123 (as folded by v1.27 Edit 3) | Ensure the derived converse is labelled as the framework's own step, not left to read as imported. | A8, §6.3 | Low; presentational. |
| **C-5** | Reference L803 | Discharge the DOI residual: `10.1103/PhysRevLett.86.3463`, pp. 3463–3466. | A13 | Housekeeping. |
| **C-6** | Reference L815 | Discharge the DOI residual: `10.1162/089976601753195969`, *Neural Comput.* 13(11), 2409–2463. | §5 | Housekeeping. |
| **C-7** | §4 L125 | Subscript the crypticity gap: Cμ⁺ = E + H[S⁺\|S⁻] (predictive) or C^±μ = E + d(M⁺,M⁻) (bidirectional), rather than an unsubscripted "Cμ = E + χ". | Tier B, [13] row | Low; precision. |
| **C-8** | Reference L787 | Leave the ⚠ in place. It is **not** discharged — Schnakenberg's full text remains unretrieved (§4.4). | A14 | Do-not-touch note. |
| **C-9** | §12 Table 3 L444 | Optional: move the [Spinney & Ford; Ford & Spinney] bracket off the "until R is declared" clause and onto the silence-on-odd-variables clause. | §6.5 | Cosmetic. |

**No correction is required for:** the Spinney & Ford parity framing (A5 — flag incorrect), the
author-order and title pairings (A6 — canon already correct, including its own conflation warning),
the Publisher's Note posture (A6 — "content unknown" is the accurate statement), Hatano–Sasa's
canon use (A13), or C&F's canon use (A8, Tier B — cited for stationarity, which it states).

---

## 8. Summary

- **14 Tier A flags:** **7** `FLAG-CONFIRMED` (A4, A6, A7, A9, A11, A12, A13), **2** `FLAG-OVERSTATED`
  (A2, A3), **4** `FLAG-INCORRECT` (A1, A5, A8-on-attribution, A10), **1** `NOT-CHECKABLE` (A14).
  Of the seven confirmed, four (A9, A11, A12, A13) are confirmed *about their sources* but
  not-applicable to the canon, which does not make the flagged claims; and A6 is confirmed on the
  Publisher's Note's **existence** only, its content being `NOT-CHECKABLE` (§4.1).
- **Four flags target papers the canon does not cite** (A1 Kawai 2007, A4 Maes as-yet-uncited,
  A7 Seifert RPP, A11/A12 Esposito–Van den Broeck). A9 targets a claim the canon does not make.
- **The highest-priority Tier A item (A5, the parity framing) does not survive.** The canon does not
  present parity as a convention on Spinney & Ford's authority; it cites them for the decomposition
  they prove. The v1.27 scope condition is not exposed by this flag.
- **Two material defects found, neither of them a flag as written:** reference [1] is misstated under
  the canon's only strongest-graded row (§6.1), and Schnakenberg 1976 is cited anachronistically for
  a path-space-action result (§6.2).
- **Tier B is one row, correctly counted, and its citation does not support its grade.** Fix is
  bibliographic (C-1); no mathematics moves and no grade changes.
- **Tier C: 62 entries left unexamined**, as instructed.
- **Nothing was self-graded.** This report is a set of verdicts for Ben; the fold is a builder's, and
  the check on this report is someone else's.

---
*End of AOP_CitationVerification_v0.1.*
