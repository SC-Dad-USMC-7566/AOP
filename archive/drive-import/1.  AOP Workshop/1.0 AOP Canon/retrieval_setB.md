# Retrieval Record — Set B

Retrieval date: 2026-07-25
Retriever: execution-seat agent, WebSearch + WebFetch only (no bash/curl/python fetching used)

---

## METHODOLOGICAL CAVEAT — READ BEFORE LINE-CHECKING

**The only web-retrieval tools available were `WebSearch` and `WebFetch`. `WebFetch` does not return raw page text to me; it fetches the page and runs a *small summarizing model* over it, returning that model's output.** Every "verbatim" passage below therefore passed through an intermediary model, and in some cases through OCR (archive.org DjVu text) as well.

Consequences a human reviewer must assume:

1. Quotes are **transcriptions reported by an intermediary**, not bytes I read directly. They should be treated as *high-confidence but not independently keystroke-verified*.
2. Mathematical notation is frequently mangled (`ǫ-machine` for ε-machine, `←−X` for the past-sequence arrow, subscripts flattened). Where I noticed corruption I flag it.
3. On several requests the intermediary **refused wholesale section transcription on copyright grounds** and returned only targeted sentence-level quotes. Full-section verbatim text was therefore not obtainable for the Spinney & Ford papers.
4. Any passage a claim actually leans on should be re-checked by a human against the PDF before publication.

Blocked routes (stated plainly): APS journal pages (`journals.aps.org`, `link.aps.org`) returned **HTTP 403**; NASA ADS returned **robots.txt disallowed**; `export.arxiv.org` returned **robots.txt disallowed**; arXiv `/abs/` pages returned **truncated content** (abstract body only, no metadata sidebar).

---

## SOURCE 1 — Spinney & Ford (2012), PRL

### Bibliographic record as actually found

- **Authors:** Richard E. Spinney; Ian J. Ford
- **Affiliations (from preprint):** Department of Physics and Astronomy, UCL, Gower Street, London WC1E 6BT, UK; London Centre for Nanotechnology, 17–19 Gordon Street, London WC1H 0AH, UK
- **Published title:** *Nonequilibrium Thermodynamics of Stochastic Systems with Odd and Even Variables*
- **Preprint title (differs by a hyphen):** *Non-equilibrium thermodynamics of stochastic systems with odd and even variables*
- **Venue:** Physical Review Letters **108**, 170603 (2012)
- **DOI:** 10.1103/PhysRevLett.108.170603
- **arXiv:** arXiv:1201.0904 [cond-mat.stat-mech]; v1 submitted Wed 4 Jan 2012 14:46:52 UTC, v2 Fri 10 Feb 2012 15:05:06 UTC
- **Related record found:** a *Publisher's Note* exists — "Publisher's Note: Nonequilibrium Thermodynamics of Stochastic Systems with Odd and Even Variables [Phys. Rev. Lett. 108, 170603 (2012)]", Phys. Rev. Lett. **108**, 199905, DOI 10.1103/PhysRevLett.108.199905. **I did not retrieve the Publisher's Note itself and do not know what it corrects.**

The proposed title/venue in the task brief **matches what I found**, apart from the preprint's hyphenation of "Non-equilibrium". No silent correction was made.

### Retrieval status

**FULL TEXT REACHED (ar5iv HTML rendering of the preprint) — PARTIAL VERBATIM EXTRACTION.**

URLs actually reached:
- `https://ar5iv.arxiv.org/html/1201.0904` (full-text HTML, reached; intermediary refused full-section transcription)
- `https://www.arxiv.org/abs/1201.0904v2` (metadata)
- `https://arxiv.org/pdf/1201.0904v2` (PDF, reached; sentence-level quotes returned)
- `https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.108.170603` — **NOT REACHED, HTTP 403.** The *published* version of record was never seen. All text below is from the **preprint**.

### Quoted passages

**Abstract (reported verbatim, ar5iv):**

> "The total entropy production of stochastic systems can be divided into three quantities. The first corresponds to the excess heat, whilst the second two comprise the house-keeping heat. We denote these two components the transient and generalised house-keeping heat and we obtain an integral fluctuation theorem for the latter, valid for all Markovian stochastic dynamics. A previously reported formalism is obtained when the stationary probability distribution is symmetric for all variables that are odd under time reversal which restricts consideration of directional variables such as velocity."

**Definition of the even/odd distinction (Introduction):**

> "Specifically, we consider the dynamics of a general set of variables x=(x¹,x²,…xⁿ) that behave differently under time reversal such that εx=(ε¹x¹,ε²x²,…εⁿxⁿ) where εⁱ=±1 for even and odd variables xⁱ respectively."

**Why odd variables matter (Introduction):**

> "Odd variables arise in the discussion of directional quantities and consequently such a consideration is essential when discussing velocities, from the most simple lattice Boltzmann model to considerations of full phase space."

**Statement of the generalisation being made (Introduction):**

> "We seek to take such a formalism and generalise its scope by the explicit inclusion of both even (e.g. spatial) and odd (e.g. momentum) variables that transform differently under time reversal."

**The prior two-component decomposition being generalised (Introduction):**

> "resulting in a formalism involving a division of the total entropy change into two distinct terms, the adiabatic and non-adiabatic entropy productions"

> "which map onto the house-keeping and excess heats, respectively, of Oono and Paniconi"

**The load-bearing restriction statement (Abstract, repeated in Conclusions):**

> "A previously reported formalism is obtained when the stationary probability distribution is symmetric for all variables that are odd under time reversal which restricts consideration of directional variables such as velocity."

### What remains unchecked

The published PRL text and the Publisher's Note (PRL 108, 199905) were never retrieved; all quotes are preprint text relayed by a summarizing intermediary, and no full section was transcribed continuously.

---

## SOURCE 2 — the second Spinney/Ford 2012 paper

### IMPORTANT DISCREPANCY — do not silently resolve this

The brief names **"Ford, I.J. & Spinney, R.E. (2012)"** and separately proposes the title *"Entropy production in full phase space for continuous stochastic dynamics" (Phys. Rev. E 85, 051113, 2012)*. **These are two different papers.** There are *two* 2012 Phys. Rev. E papers by this pair, with opposite author order:

**2A. Spinney, R.E. & Ford, I.J. — "Entropy production in full phase space for continuous stochastic dynamics"**
- Venue: Physical Review E **85**, 051113 (2012)
- DOI: 10.1103/PhysRevE.85.051113
- arXiv: arXiv:1203.0485
- Author order: **Spinney then Ford** (not "Ford & Spinney")
- PubMed record exists: PMID 23004709

**2B. Ford, I.J. & Spinney, R.E. — "Entropy production from stochastic dynamics in discrete full phase space"**
- Venue: Physical Review E **86**, 021127 (2012)
- DOI: 10.1103/PhysRevE.86.021127
- arXiv: arXiv:1204.4822; v1 21 Apr 2012, v2 20 Jul 2012
- Author order: **Ford then Spinney** — this is the paper that matches the brief's *author* string.

Both are documented below. A citation reading "Ford & Spinney (2012), *Entropy production in full phase space for continuous stochastic dynamics*, PRE 85, 051113" would be **a conflation of the two** and should be corrected by a human before use.

---

### 2A — Spinney & Ford, PRE 85, 051113 (arXiv:1203.0485)

**Retrieval status: FULL TEXT REACHED (ar5iv HTML + arXiv PDF) — PARTIAL VERBATIM EXTRACTION; renderings were truncated mid-document on more than one attempt.**

URLs actually reached:
- `https://ar5iv.arxiv.org/html/1203.0485` (reached; content truncated — the intermediary reported the document "ends abruptly" and could not locate a Conclusions section)
- `https://arxiv.org/pdf/1203.0485` (reached; the intermediary reported "the document does not have a 'Conclusions' section. It ends with Example II" — this is likely a truncation artifact of the fetch, **not** established fact about the paper)
- `https://arxiv.org/abs/1203.0485` (reached, truncated to abstract text only)
- `https://link.aps.org/doi/10.1103/PhysRevE.85.051113` — **NOT REACHED** (APS 403)

**Abstract (reported verbatim):**

> "The total entropy production and its three constituent components are described both as fluctuating trajectory-dependent quantities and as averaged contributions in the context of the continuous Markovian dynamics, described by stochastic differential equations with multiplicative noise, of systems with both odd and even coordinates with respect to time reversal, such as dynamics in full phase space. Two of these constituent quantities obey integral fluctuation theorems and are thus rigorously positive in the mean by Jensen's inequality. The third, however, is not and furthermore cannot be uniquely associated with irreversibility arising from relaxation, nor with the breakage of detailed balance brought about by non-equilibrium constraints."

**Time-reversal operation and even/odd definition (Section II):**

> "we consider the operation 𝜺x=(ε₁x₁,ε₂x₂,…εₙxₙ) where εᵢ=±1 for even and odd variables xᵢ respectively."

> "we consider the dynamics of a general set of variables x that may be odd or even under time reversal by considering the operation 𝜺x = (ε₁x₁, ε₂x₂, … εₙxₙ) where εᵢ = ±1 for even and odd variables xᵢ respectively."

**Splitting the deterministic dynamics by parity (Section II):**

> "Since we allow xᵢ to be either odd or even under time reversal we can divide the deterministic dynamics into reversible and irreversible components."

> "Aⁱʳ(x,t)=½(Aᵢ(x,t)+εᵢAᵢ(𝜺x))=εᵢAⁱʳ(𝜺x,t)"
> "Aʳᵉᵛ(x,t)=½(Aᵢ(x,t)−εᵢAᵢ(𝜺x))=−εᵢAʳᵉᵛ(𝜺x,t)"

*(Superscript labels as relayed; the reversible/irreversible superscripts appear possibly swapped in the intermediary's transcription — verify against the PDF before quoting.)*

**Three-component decomposition and the IFT asymmetry (Introduction / Section IV):**

> "Two of these constituent quantities obey integral fluctuation theorems and are thus rigorously positive in the mean by Jensen's inequality. The third, however, is not..."

> "Only two of the three components of entropy production satisfy an integral fluctuation theorem (IFT), making them rigorously positive in the mean, properties shared by the sum of all three; the third, however, does not satisfy an IFT, and in the mean can take either sign."

**Identification of the components with heats (Section IV):**

> "we associate ΔS₁ with the excess heat ΔQₑₓ=(ΔS₁−ΔSₛᵧₛ)k_BT_env, ΔS₂ with a so called 'generalised house-keeping heat' ΔQ_hk,G=ΔS₂k_BT_env and ΔS₃ with the 'transient house-keeping heat', ΔQ_hk,T=ΔS₃k_BT_env"

**The odd-variable condition — the passage most directly on point:**

> "a third component of entropy production could be conceived, arising from the non-equilibrium constraint, but associated with relaxation towards the stationary state. It only arises when odd dynamical variables play a role in the dynamics, and even then only in specific cases."

> "The additional complexity of ΔS₃ arises because Eq. (68) can only differ from Eq. (54) when the stationary state is out of equilibrium, such that p^st(x) ≠ p^st(εx)." *(Section IV; equation numbers as relayed)*

> "Such a formalism asserts that the two origins of entropy production may often be more closely related, with such a circumstance arising under the inclusion of odd variables and when the stationary distribution is asymmetric in any of those odd variables."

> "Finally we point out that, being in the stationary state, d⟨ΔS₃⟩/dt = 0, but since it is a non-equilibrium stationary state that is asymmetric in the odd velocity variable we have ΔS₃ ≠ 0 in detail." *(Section V, Example I)*

**On configuration-space / restricted-coordinate reductions:**

> "In such coordinates Dᵢ(x) is assumed constant and taken to zero. The remaining terms then clearly diverge unless we demand Aⁱʳ(x)=0 since in these instances, for the reverse path to be a solution to the forward dynamics the motion must be purely reversible."

> "the correct representation of the entropy production requires the more exact relation between the evaluation points"

**Honest note on the specific question asked.** The brief asks for "any statement that results derived for even-variable (configuration-space) dynamics do not carry over unchanged to odd-variable systems." **I did not retrieve a single sentence in 2A stating that in those words.** What I did retrieve is the *converse* framing, which carries the same content: the earlier two-component (adiabatic / non-adiabatic) formalism is the **special case** recovered when the stationary distribution is symmetric in all odd variables; the extra component ΔS₃ appears precisely when it is not, and ΔS₃ **does not obey an IFT and can be negative in the mean**. The cleanest single sentence for this is the PRL abstract (Source 1) plus PRE 85's "It only arises when odd dynamical variables play a role in the dynamics."

**What remains unchecked:** the Conclusions/final section of PRE 85, 051113 was never successfully rendered by any route; the published version of record was never seen; equation numbering and the reversible/irreversible superscript assignment above are unverified.

---

### 2B — Ford & Spinney, PRE 86, 021127 (arXiv:1204.4822)

**Retrieval status: ABSTRACT + INTRODUCTION REACHED (arXiv abs page and ar5iv); full text not systematically read.**

URLs actually reached:
- `https://arxiv.org/abs/1204.4822`
- `https://ar5iv.arxiv.org/html/1204.4822`
- An open UCL Discovery PDF was identified but **not fetched**: `https://discovery-pp.ucl.ac.uk/id/eprint/1376005/7/Ford_discrete_full_phase_space.pdf`
- `https://journals.aps.org/pre/abstract/10.1103/PhysRevE.86.021127` — **NOT REACHED** (APS 403)

**Caveat:** my first fetch of the arXiv abs page returned a **paraphrase** of the abstract, not the abstract. The quotes below come from the second (ar5iv) fetch, which returned sentence-level quotations. Treat as reported-verbatim.

**Abstract (quoted sentences):**

> "The stochastic entropy generated during the evolution of a system interacting with an environment may be separated into three components, but only two of these have a non-negative mean."

> "The third component of entropy production is associated with the relaxation of the system probability distribution towards a stationary state and with nonequilibrium constraints within the dynamics that break detailed balance."

> "It exists when at least some of the coordinates of the system phase space change sign under time reversal, and when the stationary state is asymmetric in these coordinates."

**Introduction — the even/odd asymmetry stated operationally:**

> "When the system state is described in a full phase space of spatial and velocity variables, or indeed any set that includes variables that change sign under time reversal, the reversed path clearly corresponds to a set of points in phase space that retraces the sequence of spatial positions, but with velocity coordinates that are inverted."

**On model-dependence (paraphrase relayed by the intermediary, NOT a quote):** the abstract was reported to state that entropy production in stochastic thermodynamics depends on the level of model detail, and to characterise it as a measure of the failure of Loschmidt's expectation of dynamical reversibility. **This sentence is a paraphrase and must not be quoted as the authors' words.**

**What remains unchecked:** everything past the Introduction of 2B, and the published version of record.

---

## SOURCE 3 — Crutchfield, Ellison & Mahoney (2009)

### Bibliographic record as actually found

- **Authors:** James P. Crutchfield; Christopher J. Ellison; John R. Mahoney
- **Affiliations (preprint header):** Complexity Sciences Center and Physics Department, University of California at Davis; Santa Fe Institute
- **Title:** *Time's Barbed Arrow: Irreversibility, Crypticity, and Stored Information*
- **Venue:** Physical Review Letters **103**, 094101 (2009)
- **DOI:** 10.1103/PhysRevLett.103.094101 *(confirmed only via the resolvable APS link `link.aps.org/doi/10.1103/PhysRevLett.103.094101` appearing in search results; the APS page itself was not reachable)*
- **arXiv:** arXiv:0902.1209 [cond-mat.stat-mech]
- **Also circulated as:** Santa Fe Institute Working Paper 09-02-002; the UC Davis PDF carries "Dated: February 7, 2009" and a placeholder "arxiv.org:09XX.XXXX [physics.gen-ph]" in its header

Title/venue/year in the brief **match what I found**.

### Retrieval status

**FULL TEXT READ (author-hosted PDF + OCR plain text), via intermediary summarization.**

URLs actually reached:
- `https://csc.ucdavis.edu/~cmg/papers/tba.pdf` — author-hosted full PDF, **reached and queried four times**
- `https://archive.org/stream/arxiv-0902.1209/0902.1209_djvu.txt` — OCR plain text of the arXiv version, **reached and queried twice**
- `https://arxiv.org/abs/0902.1209` — reached, abstract text only, metadata fields truncated
- `https://ui.adsabs.harvard.edu/abs/2009PhRvL.103i4101C/abstract` — **NOT REACHED** (robots.txt)
- `https://www.semanticscholar.org/paper/01562546...` — **NOT REACHED** (empty content returned)

**Notation warning:** the source renderings corrupt ε (as `ǫ`), the past/future arrow-overbar notation (as `←−X` / `−→X`), and subscripts. I have preserved the corruption where it appeared rather than silently normalising it.

### Quoted passages

**Abstract (opening sentence — the only part I could confirm verbatim; the fetched renderings returned this sentence alone and I could not confirm whether the published abstract continues):**

> "We show why the amount of information communicated between the past and future — the excess entropy — is not in general the amount of information stored in the present — the statistical complexity."

**Opening sentence of the paper:**

> "Constructing a theory can be viewed as our attempt to extract from measurements a system's hidden organization. This suggests a parallel with decryption..."

---

#### (a) That C_μ is a property of a declared process / measurement channel

**The process is defined as a communication channel over measurement outcomes:**

> "A process Pr(←−X, −→X) is a communication channel with a fixed input distribution Pr(←−X): It transmits information from the past ←−X = . . . X−3X−2X−1 to the future −→X = X0X1X2 . . ."

> "Xt is the discrete random variable for the measurement outcome at time t"

**Causal states are defined by an equivalence relation over pasts of that process:**

> "ǫ(←−x ) = {←−x′ : Pr(−→X|←−x ) = Pr(−→X|←−x′)}"

> "the previous mapping from pasts to causal states is denoted ǫ+ and it gave, what we will call, the predictive causal states S+."

> "Causal states have the Markovian property that they render the past and future statistically independent; they shield the future from the past"

**The ε-machine and C_μ built from those causal states:**

> "The resulting model, consisting of the causal states and transitions, is called the process's ǫ-machine."

> "Out of all optimally predictive models, the ǫ-machine captures the minimal amount of information that a process must store in order to communicate all of the excess entropy from the past to the future. This is the statistical complexity: Cµ ≡ H[S]"

> "C_μ ≡ H[S] ≤ H[R_b]" *(comparison against alternative predictive models R; relayed with possible notation loss)*

**Modelling is explicitly framed as decrypting what is present in the observations:**

> "building a model corresponds directly to decrypting the hidden state information in measurements"

> "the information used to build a model is only that available in the observed process"

**HONEST LIMITATION on point (a).** The paper's framing throughout is that E, C_μ, and χ are functionals of a *process* — a distribution over measurement-outcome sequences, defined as a communication channel — and of the ε-machine built from that process's causal states. That much is directly quoted above. **However, I found no sentence in this paper that explicitly contrasts C_μ with "a physical object's material complexity", or that explicitly warns against reading C_μ as a property of an object.** Anyone asserting that this paper *states* such a disclaimer would be overreading it. What the paper supports directly is the weaker, purely definitional point: C_μ is defined on Pr(←−X, −→X), i.e. on the declared process.

---

#### (b) E, C_μ, and the crypticity gap

**Excess entropy defined:**

> "At a minimum, a good predictor needs to capture all of the information I shared between past and future: E = I[←−X;−→X]—the process's excess entropy"

**Theorem 1:**

> "Theorem 1. Excess entropy is the mutual information between the predictive and retrodictive causal states: E = I[S+; S−]."

*(One OCR pass returned this garbled as "E = I[X; X̄; S⁻; S⁺]" — the clean PDF rendering "E = I[S+; S−]" is the one to trust, but a human should confirm.)*

**Crypticity defined:**

> "A process's crypticity is χ ≡ H[S+|S−] + H[S−|S+]. This is the distance between a process's forward and reverse ǫ-machines"

> "A process's crypticity is d(M+,M−) = H[S+|S−] + H[S−|S+]. This is the distance between a process's forward and reverse e-machines and expresses most explicitly the difference between prediction and modeling."

**Corollary 1 — the gap relation:**

> "Corollary 1. M±'s statistical complexity is: C±µ = E + χ."

**The directional forms:**

> "the predictive statistical complexity is given by C+ = E + H[S+|S−]"

> "the retrodictive statistical complexity by C− = E + H[S−|S+]"

> "E = C+ + C− − C±"

> "Only when E = C± does the bidirectional machine prove efficient: C+ < C± and C− < C±"

**What the gap means:**

> "Referring to d as crypticity derives from this result: It is the amount of internal state information (C±µ) not directly present in the observed sequence (E). That is, a process hides χ bits of information."

> "When a process's crypticity is high, χ ≈ C±µ, then little of it's structural information is directly present in observations."

> "Moreover, there are truly cryptic processes (E ≈ 0) that are highly structured (C±µ ≫ 0)."

> "Practically, these results elucidate the difference between observed (mutual) information (E) and a process's stored information (Cµ)."

**Closing statement:**

> "Analyzing a process only in terms of mutual information... one concludes that a process is more random than it is"

> "When this happens, one concludes that a process is more random than it is and that it has little structure, when neither is true."

**HONEST LIMITATION on the inequality E ≤ C_μ.** I searched this paper's full text (both the author PDF and the OCR text) for an explicit inequality "E ≤ C_μ" / "C_μ ≥ E" and **did not find one stated as such.** What the paper states is the *equality* C±µ = E + χ (Corollary 1), together with C+ = E + H[S+|S−] and C− = E + H[S−|S+]. Since conditional entropies are non-negative, E ≤ C_μ follows immediately — but as an **inference**, not as a quoted sentence from this paper. The inequality E ≤ C_μ is conventionally attributed to earlier computational-mechanics work (Crutchfield & Feldman 2003, *Chaos* 13, 25 — **not retrieved or verified here**). A claim citing *Time's Barbed Arrow* for "E ≤ C_μ" should either cite it for the equality C_μ = E + χ, or cite the earlier source.

### What remains unchecked

The published PRL version was never seen (APS 403), the full published abstract beyond its first sentence was not confirmed, the DOI was confirmed only from a search-result link and not from the APS record itself, and all quotes carry OCR/intermediary risk on the mathematical notation.

---

## SOURCE 4 — Joyce (1994), foreword to *Origins of Life: The Central Concepts*

### PRIMARY SOURCE: **NOT RETRIEVED.**

This is stated flatly and without hedging. **I did not read Joyce's 1994 foreword. No quotation below is primary verification.**

What I established about retrievability:

- A scanned copy of the book **does exist** on the Internet Archive: `https://archive.org/details/originsoflifecen0000unse` — "Origins of life: the central concepts", D. W. Deamer and Gail R. Fleischaker, Jones and Bartlett Publishers, Boston, 1994, ISBN 0867201819, xvi + 431 pp.
- **Its access status is restricted.** The item is flagged "Access-restricted item", in the "print-disabled" / "inlibrary" collections. **No open full-text view and no "Search inside" facility was offered** on the page as fetched. The foreword text was therefore not reachable.
- No Google Books preview, publisher excerpt, PDF, or other route to the foreword text surfaced in any search.
- Bookseller listings (Biblio, AbeBooks, Eureka Books) confirm the print edition exists but carry no text.

**Conclusion: the primary text is not retrievable by the tools available here.** It would require a physical copy or an in-library/print-disabled loan.

### (a) The wording as quoted in secondary sources — NOTE THE VARIANTS

Two distinct wordings circulate, and they are **not identical**:

- **"a self-sustaining chemical system capable of Darwinian evolution"** — the dominant form (Stanford Encyclopedia of Philosophy)
- **"a self-sustained chemical system capable of Darwinian evolution"** — used by Mix (2026), an article specifically about this definition's provenance
- **"Life is a self-sustaining chemical system capable of Darwinian evolution"** — with a leading "Life is", in *QRB Discovery* (Chen & Nowak-type origins piece, PMC10392681)

Which of these matches the 1994 page is **unresolved** and cannot be resolved without the primary.

### (b) Secondary sources that quote or cite it, with attribution

**1. Stanford Encyclopedia of Philosophy, "Life"** — reached at `https://plato.stanford.edu/entries/life/`
Quotation in the entry:
> "Consider NASA's operational definition of life as 'a self-sustaining chemical system capable of Darwinian evolution' (Joyce 1994)."

Its bibliography entry, as reported:
> Joyce, Gerard F., 1994, forward, in D. W. Deamer, G. R. Fleischaker (eds.), *Origins of Life: the Central Concepts*, Boston: Jones & Bartlett, pp. xi–xii.

*(The SEP entry's own word "forward" for "foreword" is reproduced as reported; this may be an SEP typo or an intermediary transcription slip.)*

**2. Ruiz-Mirazo, Peretó & Moreno (2004), "A Universal Definition of Life: Autonomy and Open-Ended Evolution", *Origins of Life and Evolution of the Biosphere* 34: 323** — reached at `https://link.springer.com/article/10.1023/B:ORIG.0000016440.53346.dc`
Reference entry as reported:
> "Joyce, G. F.: 1994, 'Foreword', in D. W. Deamer and G. R. Fleischaker (eds), *Origins of Life: The Central Concepts*, Jones and Bartlett, Boston, pp. xi–xii."

*(Only the reference list was reachable; the article body containing any quotation of the wording was behind the paywall. **The definition's wording was not seen in this source.**)*

**3. *The Quest for a Universal Theory of Life* (Cambridge University Press), reference list** — reached at `https://www.cambridge.org/core/books/abs/quest-for-a-universal-theory-of-life/references/18DEC1B341E5B2AB13C14C030D33BEC5`
Reference entry as reported:
> "Joyce, G. F., Foreword, in Origins of Life: The Central Concepts, pp. xi–xii, Deamer, D. W. and Fleischaker, G. R., eds., Jones & Bartlett, Boston, MA, 1994."

**4. Mix, Lucas J. (2026), "The Origin, Extension, and Future of the 'NASA Definition' of Life", *Astrobiology* 26(1): 66–74, DOI 10.1177/15311074251412317** — reached at `https://journals.sagepub.com/doi/10.1177/15311074251412317`

This is the most directly relevant secondary source, being a dedicated provenance study. Points reported from it:
- It gives the definition as **"a self-sustained chemical system capable of Darwinian evolution."**
- It describes Joyce's contribution as **"a four-sentence introduction in a book foreword"** to *Origins of life: the central concepts* (Deamer & Fleischaker, eds., Jones and Bartlett, Boston).
- **It attributes the definition's authorship not to Joyce but to a NASA body:** the definition was **"a product of the Exobiology Discipline Working Group"**.
- It notes **"the only subsequent defense can be found in an online interview of Joyce"**.
- **Its reference entry for Joyce 1994 carries no page numbers.**

**Caveat:** I reached the SAGE landing page; whether the intermediary saw the full article text or only abstract/preview material is not established. **Mix's exact sentences should be re-verified by a human**, especially the "Exobiology Discipline Working Group" attribution, which materially changes how the definition should be cited.

**5. *QRB Discovery* origins article (PMC10392681)** — reached at `https://pmc.ncbi.nlm.nih.gov/articles/PMC10392681/`
Reported quotation:
> "Life is a self-sustaining chemical system *capable of Darwinian evolution*" (Joyce *et al.*, 1994)

**Flag: this source's attribution is defective.** It cites "Joyce, G., Deamer, D.W., and Fleischaker, G. 1994" as co-authors of the source. Joyce wrote the foreword; Deamer and Fleischaker were the volume's *editors*. This is a mis-citation and should not be propagated.

### (c) Explicit statement

**The primary source — Joyce's 1994 foreword, pp. xi–xii of *Origins of Life: The Central Concepts* — was NOT retrieved and NOT read.** The wording above is known to me only through secondary quotation. The page attribution "pp. xi–xii" is corroborated by three independent secondary reference lists (SEP; Ruiz-Mirazo et al. 2004; the Cambridge volume) but is **not** confirmed against the book. The exact wording on the page — in particular "self-sustaining" vs "self-sustained", and whether the sentence begins "Life is" — is **unverified**. Per Mix (2026), the wording may not be Joyce's own but the Exobiology Discipline Working Group's, with Joyce as the reporter; **this too is secondary and unverified.**

### What remains unchecked

Everything about the primary: the exact wording, the page, whether Joyce presents the definition as his own or as a NASA working group's, and the surrounding four sentences Mix refers to.

---

## Summary table

| # | Source | Status | Primary route reached |
|---|--------|--------|----------------------|
| 1 | Spinney & Ford, PRL 108, 170603 (2012) | Preprint full text reached; partial verbatim; published VoR not seen | ar5iv/arXiv 1201.0904 |
| 2A | Spinney & Ford, PRE 85, 051113 (2012) | Preprint reached but renderings truncated; Conclusions never obtained | arXiv 1203.0485 |
| 2B | Ford & Spinney, PRE 86, 021127 (2012) | Abstract + Introduction only | arXiv 1204.4822 |
| 3 | Crutchfield, Ellison & Mahoney, PRL 103, 094101 (2009) | Full text read (author PDF + OCR); published VoR not seen | csc.ucdavis.edu/~cmg/papers/tba.pdf |
| 4 | Joyce (1994), foreword | **NOT RETRIEVED** — secondary documentation only | n/a; book is access-restricted on IA |

## Open items a human should close

1. **Resolve the Source 2 author-order conflation** — decide whether the intended citation is Spinney & Ford PRE 85, 051113 or Ford & Spinney PRE 86, 021127. They are different papers.
2. **Do not cite *Time's Barbed Arrow* for an explicit "E ≤ C_μ"** — it states C±µ = E + χ; the inequality is an inference from χ ≥ 0.
3. **Do not attribute to *Time's Barbed Arrow* an explicit warning against reading C_μ as material/object complexity** — that warning is not in the retrieved text; only the definitional "process as communication channel over measurement outcomes" framing is.
4. **Retrieve the Conclusions of PRE 85, 051113** by another route before relying on any claim about how it frames the even→odd non-transferability.
5. **Retrieve Joyce (1994) pp. xi–xii physically**, and check Mix (2026) directly on the Exobiology Discipline Working Group attribution.
6. **Check the PRL Publisher's Note** (PRL 108, 199905) to see what it corrects in Source 1.
