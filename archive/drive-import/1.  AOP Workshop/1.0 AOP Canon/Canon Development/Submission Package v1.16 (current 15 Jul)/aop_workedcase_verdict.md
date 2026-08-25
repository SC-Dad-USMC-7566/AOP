# AOP Gate — Do the Per-Mechanism Ceilings Predict the Worked Cases? VERDICT

**Frozen exit: NULL** (pre-registration `aop_workedcase_prereg.md`, v1) — **by dependency.** The
gate's entire prediction rested on the per-mechanism ceilings being real. The real-system gate
(`aop_realsystem_verdict.md`, run in the same session) showed that **two of the three ceilings
are artifacts** of the minimal model: pure flux has no leverage on persistence at all, and Bank
is unbounded on a real bistable system. NULL criterion 2 fires directly: *"a pure-Bank
configuration reaches arbitrary persistence on the model (no ceiling), so the spore argument is
moot and the ceiling structure makes no worked-case prediction."*

## What was tested and what happened

The gate proposed to predict the worked-case durability ranking (crystal > spore > flame) from
the ceiling ordering, with a sharp sub-claim: the spore's near-immortality must be **Barrier**-
borne (a physical wall), because a pure-Bank persister would be ceiling-limited and could not be
near-immortal.

- **On the minimal model, where the gate was pre-registered, the internal logic held:** bank-only
  caps at P=0.705; adding a barrier lifts it to 0.79. So *within the toy*, the spore-needs-a-wall
  argument is self-consistent.
- **But the premise is false on real kinetics.** Once Bank reset re-injects into a genuine
  metastable well (the real-system gate), it drives P → 1 without bound. There is no Bank ceiling
  to forbid a pure-Bank persister from being near-immortal. The load-bearing prediction — "the
  spore's durability *must* come from Barrier, not Bank" — therefore **has no support.** A spore
  could, as far as this structure can say, be durable through stored-structure recovery alone.

## The honest reading

The worked-case prediction was **downstream of a result that did not survive**, so it collapses
with it. The spore's biology is not in question — spores plainly have both a coat (a wall) and
deep dormancy (a bank); the point is only that the *ceiling structure* cannot be used to argue
one is doing the persistence work rather than the other. The framework's four-axis profiles of
the worked cases (crystal Barrier-dominated, flame Flux-dominated, spore Memory-rich) are
untouched — this gate never tested those; it tested a would-be *quantitative consequence* of the
ceilings, and that consequence is void.

## Verdict: NULL (by dependency)

No worked-case prediction is licensed by the ceiling structure. The gate is recorded as a NULL to
keep the ledger honest: a prediction was pre-registered, its premise failed an independent test,
and the prediction is withdrawn rather than quietly dropped. Nothing here changes the canon's
worked cases or the four-axis structure.

## Reproduce

Minimal-model check in `aop_realsystem_gate.py` (bank-only 0.705 vs barrier+bank 0.79); the
real-system refutation is the Schlögl bank sweep in the same script (P → 0.998).
