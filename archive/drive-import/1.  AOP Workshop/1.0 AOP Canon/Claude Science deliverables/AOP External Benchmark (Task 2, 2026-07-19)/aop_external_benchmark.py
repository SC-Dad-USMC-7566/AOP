#!/usr/bin/env python
"""
AOP External-Ground-Truth Benchmark — scoring (v1.1, deterministic re-run).

Scored strictly against the FROZEN preregistration v1.0 (unchanged — the pre-commitment
we are scored against). This script supersedes the v1.0 scorer; see CHANGES below.

CHANGES v1.0 -> v1.1 (per prime verification, 2026-07-19):
  1. DETERMINISM. FBA has non-unique optimal flux vectors, so the v1.0 rival
     "coupling strength" and the T4 Spearman moved run-to-run. Fix: the WT flux
     vector is now computed with parsimonious FBA (pfba). Separately, all growth /
     viability / strength values are rounded to a fixed tolerance TOL=1e-6 BEFORE
     any ranking or thresholding. This removes ~1e-15 LP tie-noise that was
     reshuffling the ~90 genuinely-zero-dV genes and jittering T1/T3 as well.
     Verified: every reported value is identical across TOL in [1e-9, 1e-3]
     (six orders of magnitude), confirming a clean gap between solver noise
     (~1e-15) and the smallest real signal (~3.6e-3).
  2. DE-CIRCULARIZATION. v1.0's 11 positives mixed 5 external-assay essentials
     with 6 model-labeled ones (absent from assay AND FBA-lethal), then scored
     the 6 with the same FBA -> circular, inflating T1. v1.1 reports the
     EXTERNAL-ONLY labels (5 assay positives) as the PRIMARY result, with the
     mixed-label version reported alongside (secondary, clearly marked).
  3. HONEST RE-REPORT. T4 is FALSIFIED (reproducible Spearman > 0.5 falsifier),
     not "partial". Verdict lines are emitted for both label sets.

Deterministic: LP + pfba + fixed tie tolerance; no random seed. cobra 0.31.1.
Reproduce: `python aop_external_benchmark.py`

Inputs (same dir):
  MODEL_e_coli_core.xml                         (MD5 2fd9c214652195707526448954b88696)
  EXT_KEY_price2018_fitness_Keio_BW25113.tsv    (MD5 936b99da2cbf37baa70a2b2e1b629c93)
Output:
  external_benchmark_results.json
"""
import os, json, csv, hashlib, statistics
os.environ.setdefault("HOME", os.path.join(os.getcwd(), ".fakehome"))
import numpy as np
import cobra
from cobra.io import read_sbml_model
from cobra.flux_analysis import single_gene_deletion, double_gene_deletion, pfba

HERE  = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, "MODEL_e_coli_core.xml")
KEY   = os.path.join(HERE, "EXT_KEY_price2018_fitness_Keio_BW25113.tsv")

TOL = 1e-6   # fixed tie tolerance: >> ~1e-15 LP noise, << ~3.6e-3 smallest real dV
def q(x):
    """Quantize to TOL so solver tie-noise cannot reshuffle ranks/thresholds."""
    return round(float(x) / TOL) * TOL

def md5(p):
    h = hashlib.md5()
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(65536), b''):
            h.update(c)
    return h.hexdigest()

def auroc(scores, labels):
    """AUROC via Mann-Whitney U; higher score => more likely positive. Ties averaged."""
    scores = np.asarray(scores, float); labels = np.asarray(labels, int)
    p = int((labels == 1).sum()); n = int((labels == 0).sum())
    if p == 0 or n == 0:
        return float('nan')
    _, inv, counts = np.unique(scores, return_inverse=True, return_counts=True)
    csum = np.cumsum(counts); starts = csum - counts
    ranks = ((starts + csum + 1) / 2.0)[inv]
    U = ranks[labels == 1].sum() - p * (p + 1) / 2.0
    return float(U / (p * n))

def spearman(x, y):
    def rank(a):
        a = np.asarray(a, float)
        _, inv, c = np.unique(a, return_inverse=True, return_counts=True)
        cs = np.cumsum(c); st = cs - c
        return ((st + cs + 1) / 2.0)[inv]
    return float(np.corrcoef(rank(x), rank(y))[0, 1])

def main():
    prov = {"model_md5": md5(MODEL), "key_md5": md5(KEY), "cobra": cobra.__version__,
            "flux_method": "pfba", "tie_tolerance": TOL}
    m = read_sbml_model(MODEL)
    wt = q(m.slim_optimize())
    THR = 0.01 * wt
    genes = [g.id for g in m.genes if g.id.startswith('b')]

    # ---- external key: mean glucose-minimal fitness per b-number ----
    with open(KEY) as f:
        r = csv.reader(f, delimiter='\t'); hdr = next(r)
        gcols = [i for i, h in enumerate(hdr) if 'D-Glucose (C)' in h]
        rows = list(r)
    ext = {}
    for row in rows:
        b = row[2].strip()
        vals = [float(row[i]) for i in gcols if i < len(row) and row[i] not in ('', 'NA')]
        if b.startswith('b') and vals:
            ext[b] = statistics.mean(vals)
    assayed = set(ext)

    # ---- AOP viability importance: single-gene deletion (quantized) ----
    sg = single_gene_deletion(m, gene_list=[m.genes.get_by_id(g) for g in genes], processes=1)
    dV = {}
    for _, rr in sg.iterrows():
        ids = list(rr['ids'])
        if len(ids) == 1:
            g = ids[0]; v = rr['growth']
            v = 0.0 if (v is None or (isinstance(v, float) and np.isnan(v))) else v
            dV[g] = q((wt - q(v)) / wt)
    fba_lethal = {g for g in genes if dV.get(g, 0) >= (1 - 0.01)}   # V_ko < 1% wt

    # ---- rival: coupling strength = sum |pfba WT flux| over a gene's reactions ----
    flux = pfba(m).fluxes
    strength = {g: q(sum(abs(flux[rxn.id]) for rxn in m.genes.get_by_id(g).reactions))
                for g in genes}

    # ---- labels ----
    # MIXED (v1.0 definition; secondary): assay positive OR (absent-from-assay AND FBA-lethal)
    label_mixed = {}; quarantine = []
    for g in genes:
        if g in assayed:
            label_mixed[g] = 1 if ext[g] < -2 else 0
        elif g in fba_lethal:
            label_mixed[g] = 1
        else:
            quarantine.append(g)
    scored_mixed = [g for g in genes if g in label_mixed]

    # EXTERNAL-ONLY (PRIMARY): only genes present in the assay; label by experiment alone
    scored_ext = [g for g in genes if g in assayed]
    label_ext = {g: (1 if ext[g] < -2 else 0) for g in scored_ext}

    def score_set(scored, label):
        y = [label[g] for g in scored]
        a = auroc([dV[g] for g in scored], y)
        rv = auroc([strength[g] for g in scored], y)
        return {"n": len(scored), "n_pos": int(sum(y)),
                "aop_auroc": round(a, 4), "rival_auroc": round(rv, 4),
                "margin": round(a - rv, 4)}

    S_ext = score_set(scored_ext, label_ext)          # primary
    S_mix = score_set(scored_mixed, label_mixed)       # secondary

    # T4 on the full scored (mixed) population — the strength vs viability relationship
    T4_spearman = spearman([strength[g] for g in scored_mixed],
                           [dV[g] for g in scored_mixed])

    # ---- T2: synthetic-lethal coalitions among individually-dispensable genes ----
    noness = [g for g in genes if dV.get(g, 0) < (1 - 0.01)]
    dd = double_gene_deletion(m, gene_list1=[m.genes.get_by_id(g) for g in noness], processes=1)
    sl_pairs = []
    for _, rr in dd.iterrows():
        ids = list(rr['ids'])
        if len(ids) != 2:
            continue
        v = rr['growth']; v = 0.0 if (v is None or (isinstance(v, float) and np.isnan(v))) else v
        dv12 = q((wt - q(v)) / wt)
        g1, g2 = sorted(ids)   # canonical within-pair order for reproducibility
        if dv12 >= 0.5 and dV.get(g1, 0) < 0.01 and dV.get(g2, 0) < 0.01:
            h = q(dv12 - dV.get(g1, 0) - dV.get(g2, 0))   # Mobius interaction
            sl_pairs.append({"g1": g1, "g2": g2,
                             "name1": m.genes.get_by_id(g1).name, "name2": m.genes.get_by_id(g2).name,
                             "dV_joint": round(dv12, 4), "dV_g1": round(dV.get(g1, 0), 4),
                             "dV_g2": round(dV.get(g2, 0), 4), "mobius_h": round(h, 4)})
    seen = set(); uniq = []
    # deterministic order: strongest interaction first, then by gene ids
    for p in sorted(sl_pairs, key=lambda x: (-x["mobius_h"], x["g1"], x["g2"])):
        k = (p["g1"], p["g2"])
        if k in seen:
            continue
        seen.add(k); uniq.append(p)
    sl_pairs = uniq

    out = {
        "provenance": prov,
        "wt_growth": round(wt, 6), "lethal_threshold": round(THR, 6),
        "n_core_genes": len(genes), "n_assayed": len(assayed & set(genes)),
        "n_quarantined": len(quarantine), "quarantined": sorted(quarantine),
        # PRIMARY (external-only) and SECONDARY (mixed) essentiality scoring
        "primary_external_only": S_ext,
        "secondary_mixed_labels": S_mix,
        # T-test values
        "T1_primary_aop_auroc": S_ext["aop_auroc"],
        "T1_secondary_mixed_aop_auroc": S_mix["aop_auroc"],
        "T3_primary_margin": S_ext["margin"],
        "T3_secondary_mixed_margin": S_mix["margin"],
        "T4_spearman_strength_vs_dV": round(T4_spearman, 4),
        "T2_n_synthetic_lethal_pairs": len(sl_pairs),
        "T2_synthetic_lethal_pairs": sl_pairs[:20],
        "fba_essential_genes": sorted(fba_lethal),
        "per_gene": {g: {"dV": round(dV.get(g, 0), 6), "strength": round(strength[g], 6),
                         "ext_fitness": (round(ext[g], 4) if g in ext else None),
                         "label_mixed": label_mixed.get(g),
                         "label_ext": label_ext.get(g)} for g in genes},
    }
    with open(os.path.join(HERE, "external_benchmark_results.json"), "w") as f:
        json.dump(out, f, indent=1, sort_keys=True)

    # ---- verdicts per FROZEN prereg criteria (pass >=0.75 / falsify <0.65 for T1;
    #      T3 margin >=0.10; T4 falsify if Spearman >0.5) ----
    def band_T1(a):
        return "PASS" if a >= 0.75 else ("FALSIFIED" if a < 0.65 else "PARTIAL")
    def band_T3(m_):
        return "PASS" if m_ >= 0.10 else "FAIL"
    print(f"WT growth {wt:.4f}")
    print(f"PRIMARY (external-only): n={S_ext['n']} pos={S_ext['n_pos']} "
          f"AOP={S_ext['aop_auroc']} rival={S_ext['rival_auroc']} margin={S_ext['margin']}")
    print(f"  T1 primary: {band_T1(S_ext['aop_auroc'])} (AUROC {S_ext['aop_auroc']})")
    print(f"  T3 primary: {band_T3(S_ext['margin'])} (margin {S_ext['margin']})")
    print(f"SECONDARY (mixed labels): n={S_mix['n']} pos={S_mix['n_pos']} "
          f"AOP={S_mix['aop_auroc']} rival={S_mix['rival_auroc']} margin={S_mix['margin']}")
    print(f"  T1 secondary: {band_T1(S_mix['aop_auroc'])} (AUROC {S_mix['aop_auroc']})")
    print(f"  T3 secondary: {band_T3(S_mix['margin'])} (margin {S_mix['margin']})")
    print(f"T2: {'PASS' if len(sl_pairs) >= 1 else 'FALSIFIED'} ({len(sl_pairs)} synthetic-lethal pairs)")
    print(f"T4: {'FALSIFIED' if T4_spearman > 0.5 else ('PASS' if T4_spearman <= 0.3 else 'PARTIAL')} "
          f"(Spearman {round(T4_spearman,4)})")
    return out

if __name__ == "__main__":
    main()
