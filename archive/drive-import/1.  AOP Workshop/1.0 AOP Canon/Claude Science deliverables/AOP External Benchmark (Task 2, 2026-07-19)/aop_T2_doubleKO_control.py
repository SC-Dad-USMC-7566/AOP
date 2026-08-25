#!/usr/bin/env python
"""
T2 specificity control — plain double-KO FBA synthetic-lethal screen (NO AOP layer).

Frozen per REV_AOP_T2_Control_Preregistration_v1_0.md (deposited before this run).
Answers: does an ordinary double-knockout FBA SL screen recover the same 13 pairs
AOP's coalition layer flags? If yes, T2 is standard SL detection, not AOP-specific.

Deterministic: pFBA-consistent settings + quantize growth to TOL=1e-6 before thresholding
(same as the v1.1 benchmark Fix 1). No Mobius, no viability functional — raw FBA growth only.

Input (same dir): MODEL_e_coli_core.xml (MD5 2fd9c214652195707526448954b88696)
Output: T2_control_results.json
"""
import os, json, hashlib
os.environ.setdefault("HOME", os.path.join(os.getcwd(), ".fakehome"))
import numpy as np
import cobra
from cobra.io import read_sbml_model
from cobra.flux_analysis import single_gene_deletion, double_gene_deletion

HERE   = os.path.dirname(os.path.abspath(__file__))
MODEL  = os.path.join(HERE, "MODEL_e_coli_core.xml")
AOPJSON = os.path.join(HERE, "external_benchmark_results.json")  # frozen v1.1 results
TOL = 1e-6
def q(x): return round(float(x) / TOL) * TOL
def md5(p):
    h = hashlib.md5()
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(65536), b''): h.update(c)
    return h.hexdigest()

# The 13 AOP coalition pairs — loaded from the frozen v1.1 results JSON (no hand-transcription)
with open(AOPJSON) as _f:
    AOP_PAIRS = [(p["g1"], p["g2"]) for p in json.load(_f)["T2_synthetic_lethal_pairs"]]

def main():
    m = read_sbml_model(MODEL)
    wt = q(m.slim_optimize())
    genes = [g.id for g in m.genes if g.id.startswith('b')]
    name = {g: m.genes.get_by_id(g).name for g in genes}

    # ---- single-KO growth (to find individually-viable genes) ----
    sg = single_gene_deletion(m, gene_list=[m.genes.get_by_id(g) for g in genes], processes=1)
    g1_growth = {}
    for _, rr in sg.iterrows():
        ids = list(rr['ids'])
        if len(ids) == 1:
            v = rr['growth']; v = 0.0 if (v is None or (isinstance(v, float) and np.isnan(v))) else v
            g1_growth[ids[0]] = q(v)
    viable = [g for g in genes if g1_growth[g] > 0.99 * wt]      # individually viable (single KO)

    # ---- plain double-KO screen over all viable-gene pairs (NO AOP layer) ----
    dd = double_gene_deletion(m, gene_list1=[m.genes.get_by_id(g) for g in viable], processes=1)
    joint = {}
    for _, rr in dd.iterrows():
        ids = list(rr['ids'])
        if len(ids) == 2:
            v = rr['growth']; v = 0.0 if (v is None or (isinstance(v, float) and np.isnan(v))) else v
            joint[frozenset(ids)] = q(v)

    def pairkey(g1, g2): return frozenset([g1, g2])
    def emit(k, jgrowth):
        g1, g2 = sorted(k)
        drop = q((wt - jgrowth) / wt)
        return {"g1": g1, "g2": g2, "name1": name[g1], "name2": name[g2],
                "joint_growth": round(jgrowth, 6), "joint_drop": round(drop, 4)}

    # SCREEN A — matched threshold: both single viable, double drop >= 0.5 (same as AOP T2 op-def)
    screenA = []
    for k, jg in joint.items():
        g1, g2 = tuple(k)
        drop = q((wt - jg) / wt)
        if drop >= 0.5 and g1_growth[g1] > 0.99*wt and g1_growth[g2] > 0.99*wt:
            screenA.append(emit(k, jg))
    screenA.sort(key=lambda x: (-x["joint_drop"], x["g1"], x["g2"]))

    # SCREEN B — strict SL: each single viable (>tau), double lethal (<=tau), tau=0.01*wt
    tau = 0.01 * wt
    screenB = []
    for k, jg in joint.items():
        g1, g2 = tuple(k)
        if jg <= tau and g1_growth[g1] > tau and g1_growth[g2] > tau:
            screenB.append(emit(k, jg))
    screenB.sort(key=lambda x: (-x["joint_drop"], x["g1"], x["g2"]))

    aop_set = {frozenset(p) for p in AOP_PAIRS}
    A_set = {pairkey(p["g1"], p["g2"]) for p in screenA}
    B_set = {pairkey(p["g1"], p["g2"]) for p in screenB}

    def setnames(s):
        return sorted(f"{name[sorted(k)[0]]}/{name[sorted(k)[1]]}" for k in s)

    # ---- ranking check (C): AOP Mobius-h order vs plain joint-drop order over the 13 ----
    # AOP h for these pairs == joint_drop (both singles ~0), so compute plain joint_drop for the 13
    aop13_drop = {}
    for k in aop_set:
        aop13_drop[k] = joint.get(k)  # may be None if a pair member wasn't in 'viable'
    ranked = sorted([(k, q((wt - jg)/wt)) for k, jg in aop13_drop.items() if jg is not None],
                    key=lambda x: (-x[1], sorted(x[0])))   # deterministic tie-break by gene id
    ranking = [{"pair": f"{name[sorted(k)[0]]}/{name[sorted(k)[1]]}", "joint_drop": round(d, 4)} for k, d in ranked]

    out = {
        "provenance": {"model_md5": md5(MODEL), "cobra": cobra.__version__, "tie_tolerance": TOL,
                       "wt_growth": round(wt, 6)},
        "n_viable_genes": len(viable),
        "screenA_matched_threshold_ge0.5": {"n": len(screenA), "pairs": screenA},
        "screenB_strict_tau0.01": {"n": len(screenB), "pairs": screenB, "tau": round(tau, 6)},
        "aop_13_pairs": setnames(aop_set),
        # overlap
        "A_recovers_of_13": len(aop_set & A_set),
        "A_missed_of_13": setnames(aop_set - A_set),
        "A_extra_not_in_aop": setnames(A_set - aop_set),
        "B_recovers_of_13": len(aop_set & B_set),
        "B_missed_of_13": setnames(aop_set - B_set),
        "B_extra_not_in_aop": setnames(B_set - aop_set),
        "ranking_check_C": ranking,
        "aop_subset_of_A": aop_set <= A_set,
    }
    with open(os.path.join(HERE, "T2_control_results.json"), "w") as f:
        json.dump(out, f, indent=1, sort_keys=True)

    print(f"WT {wt:.4f} | viable genes {len(viable)}")
    print(f"Screen A (matched >=0.5): {len(screenA)} pairs | recovers {out['A_recovers_of_13']}/13 | "
          f"AOP subset of A: {out['aop_subset_of_A']} | A-extra: {len(out['A_extra_not_in_aop'])}")
    print(f"Screen B (strict tau):    {len(screenB)} pairs | recovers {out['B_recovers_of_13']}/13 | "
          f"B-missed: {out['B_missed_of_13']}")
    return out

if __name__ == "__main__":
    main()
