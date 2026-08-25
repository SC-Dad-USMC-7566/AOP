# Did AOP pass or fail the external benchmark? — plain-language summary

**Short answer: it passed the two competence tests and its headline claim came out partly qualified. A genuinely mixed, honest result — not a rigged win.**

## What we did

The earlier benchmark (§11b) was a toy the framework built itself, so it couldn't really fail. This one uses a real system — *E. coli* central metabolism — and an answer key from an experiment nobody on this project ran: a genome-wide measurement (Price et al., *Nature* 2018) of which genes the bacterium actually needs to grow on sugar. We wrote down our predictions and pass/fail lines **first**, froze them on Drive, and only then scored the model. Biology, not us, set the right answers.

## What we asked, and what happened

1. **Can AOP tell essential genes from dispensable ones?** — *Yes.* Reading each gene's importance as "how much does growth drop if you remove it," AOP ranked the truly essential genes near the top (AUROC 0.85). Pass.

2. **Can AOP find hidden teamwork that a simple method misses?** — *Yes.* It found 13 gene *pairs* where each gene is useless to delete on its own (removing one does nothing) but removing both is lethal. These are real biological backup systems — duplicate enzymes like the two aconitases, two transketolases, two cytochrome oxidases — that the cell keeps as spares. A method that only looks at genes one at a time is blind to all of them. AOP's "coalition" layer sees them. Pass.

3. **Does AOP beat the simple rival?** — *Barely.* We scored a one-number rival ("how much chemical traffic flows through this gene"). AOP won, but by a hair — and the rival was a decent classifier here (much better than on the toy). So: a narrow win, honestly reported.

4. **Does AOP's flashiest claim hold up?** — *Only partly, and this is the real finding.* On the toy model, "how strong a gene looks" and "how much the system needs it" were engineered to point in opposite directions. On real metabolism they line up more than they diverge (correlation +0.48, where the toy was near zero). Real high-traffic genes often *are* the important ones. So the dramatic "strength points away from importance" headline is a feature of the toy, not a law of nature. AOP's careful machinery still adds something real — it catches the backup-team structure a single number can't — but the clean orthogonality story is qualified by contact with data.

## Why the mixed result is the point

A benchmark that can only pass tells you nothing. This one could have failed — and on its most quotable claim, it partly did. What survived is the substance: AOP recovers real essentiality and real redundancy that a single-axis reading misses, on a system whose answers came from an independent experiment. What got corrected is the overreach: the toy model's clean "strength anti-ranks viability" dissociation is a toy artifact, not a general truth. That correction is worth more to the project than another rigged pass.

## For the manuscript

The right posture: *the four-target, coalition-aware, viability-anchored method recovers structure a single axis misses on a real system with an external answer key — while explicitly not claiming the clean toy-model orthogonality holds in general.* Favorable, externally validated, honestly bounded — a Perspective result, not an adjudication.

## Files (all on Drive, Task-2 folder)

Design spec · frozen preregistration · external answer key + provenance · frozen model · self-contained scoring code · results JSON · results write-up · this summary · figure.
