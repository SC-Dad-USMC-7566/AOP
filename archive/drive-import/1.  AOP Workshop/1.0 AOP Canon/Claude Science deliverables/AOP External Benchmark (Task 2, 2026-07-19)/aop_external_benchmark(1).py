#!/usr/bin/env python
"""
AOP External-Ground-Truth Benchmark — scoring (frozen per preregistration v1.0).

Self-contained: reads the frozen SBML model and the frozen external key from the
same directory. Deterministic (LP; no random seed needed). Reproduces all four
preregistered tests T1-T4. Prime can re-run: `python aop_external_benchmark.py`.

Inputs (same dir):
  MODEL_e_coli_core.xml                         (MD5 2fd9c214652195707526448954b88696)
  EXT_KEY_price2018_fitness_Keio_BW25113.tsv    (MD5 936b99da2cbf37baa70a2b2e1b629c93)
Outputs:
  external_benchmark_results.json
"""
import os, sys, json, csv, hashlib, statistics
os.environ.setdefault("HOME", os.path.join(os.getcwd(), ".fakehome"))
import numpy as np
import cobra
from cobra.io import read_sbml_model
from cobra.flux_analysis import single_gene_deletion, double_gene_deletion

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, "MODEL_e_coli_core.xml")
KEY   = os.path.join(HERE, "EXT_KEY_price2018_fitness_Keio_BW25113.tsv")

def md5(p):
    h=hashlib.md5()
    with open(p,'rb') as f:
        for c in iter(lambda:f.read(65536),b''): h.update(c)
    return h.hexdigest()

def auroc(scores, labels):
    """AUROC via Mann-Whitney U; higher score => more likely positive label."""
    scores=np.asarray(scores,float); labels=np.asarray(labels,int)
    pos=scores[labels==1]; neg=scores[labels==0]
    if len(pos)==0 or len(neg)==0: return float('nan')
    order=np.argsort(scores); ranks=np.empty(len(scores)); ranks[order]=np.arange(1,len(scores)+1)
    # average ties
    _,inv,counts=np.unique(scores,return_inverse=True,return_counts=True)
    csum=np.cumsum(counts); starts=csum-counts
    avg=(starts+csum+1)/2.0
    ranks=avg[inv]
    rp=ranks[labels==1].sum()
    U=rp-len(pos)*(len(pos)+1)/2.0
    return U/(len(pos)*len(neg))

def spearman(x,y):
    x=np.asarray(x,float); y=np.asarray(y,float)
    def rank(a):
        o=np.argsort(a); r=np.empty(len(a)); r[o]=np.arange(1,len(a)+1)
        _,inv,c=np.unique(a,return_inverse=True,return_counts=True)
        cs=np.cumsum(c); st=cs-c; r=((st+cs+1)/2.0)[inv]; return r
    rx,ry=rank(x),rank(y)
    return float(np.corrcoef(rx,ry)[0,1])

def main():
    prov={"model_md5":md5(MODEL),"key_md5":md5(KEY),"cobra":cobra.__version__}
    m=read_sbml_model(MODEL)
    wt=m.optimize().objective_value
    THR=0.01*wt
    genes=[g.id for g in m.genes if g.id.startswith('b')]

    # ---- external key: mean glucose-minimal fitness per b-number ----
    with open(KEY) as f:
        r=csv.reader(f,delimiter='\t'); hdr=next(r)
        gcols=[i for i,h in enumerate(hdr) if 'D-Glucose (C)' in h]
        ext={}
        rows=list(r)
    for row in rows:
        b=row[2].strip()
        vals=[float(row[i]) for i in gcols if i<len(row) and row[i] not in ('','NA')]
        if b.startswith('b') and vals: ext[b]=statistics.mean(vals)
    assayed=set(ext)

    # ---- AOP viability importance: single-gene deletion ----
    sg=single_gene_deletion(m, gene_list=[m.genes.get_by_id(g) for g in genes])
    dV={}
    for _,rr in sg.iterrows():
        ids=list(rr['ids'])
        if len(ids)==1:
            g=ids[0]; v=rr['growth']
            v=0.0 if (v is None or (isinstance(v,float) and np.isnan(v))) else v
            dV[g]=(wt-v)/wt
    fba_lethal={g for g in genes if dV.get(g,0)>=(1-0.01)}  # V_ko < 1% wt

    # ---- rival: coupling strength = sum |WT flux| over a gene's reactions ----
    sol=m.optimize(); flux=sol.fluxes
    strength={}
    for g in genes:
        gene=m.genes.get_by_id(g)
        strength[g]=float(sum(abs(flux[rxn.id]) for rxn in gene.reactions))

    # ---- external binary label (per prereg) ----
    label={}; quarantine=[]
    for g in genes:
        if g in assayed:
            label[g]=1 if ext[g] < -2 else 0
        else:  # absent from assay
            if g in fba_lethal: label[g]=1
            else: quarantine.append(g)
    scored=[g for g in genes if g in label]

    y=[label[g] for g in scored]
    aop_scores=[dV[g] for g in scored]            # higher dV = more important
    riv_scores=[strength[g] for g in scored]

    T1_auroc=auroc(aop_scores,y)
    T3_auroc_rival=auroc(riv_scores,y)
    T4_spearman=spearman([strength[g] for g in scored],[dV[g] for g in scored])

    # ---- T2: synthetic-lethal coalitions among individually-dispensable genes ----
    noness=[g for g in genes if dV.get(g,0)<(1-0.01)]  # single-KO viable
    dd=double_gene_deletion(m, gene_list1=[m.genes.get_by_id(g) for g in noness])
    sl_pairs=[]
    for _,rr in dd.iterrows():
        ids=list(rr['ids'])
        if len(ids)!=2: continue
        v=rr['growth']; v=0.0 if (v is None or (isinstance(v,float) and np.isnan(v))) else v
        dv12=(wt-v)/wt
        g1,g2=ids
        if dv12>=0.5 and dV.get(g1,0)<0.01 and dV.get(g2,0)<0.01:
            h=dv12-dV.get(g1,0)-dV.get(g2,0)   # Mobius interaction
            sl_pairs.append({"g1":g1,"g2":g2,"name1":m.genes.get_by_id(g1).name,
                             "name2":m.genes.get_by_id(g2).name,"dV_joint":round(dv12,4),
                             "dV_g1":round(dV.get(g1,0),4),"dV_g2":round(dV.get(g2,0),4),
                             "mobius_h":round(h,4)})
    # dedupe (a,b)==(b,a)
    seen=set(); uniq=[]
    for p in sorted(sl_pairs,key=lambda x:-x["mobius_h"]):
        k=frozenset([p["g1"],p["g2"]])
        if k in seen: continue
        seen.add(k); uniq.append(p)
    sl_pairs=uniq

    out={
     "provenance":prov,
     "wt_growth":round(wt,6),"lethal_threshold":round(THR,6),
     "n_core_genes":len(genes),"n_assayed":len(assayed&set(genes)),
     "n_scored":len(scored),"n_positive":int(sum(y)),"n_quarantined":len(quarantine),
     "quarantined":sorted(quarantine),
     "T1_AOP_auroc":round(T1_auroc,4),
     "T3_rival_auroc":round(T3_auroc_rival,4),
     "T3_aop_minus_rival":round(T1_auroc-T3_auroc_rival,4),
     "T4_spearman_strength_vs_dV":round(T4_spearman,4),
     "T2_n_synthetic_lethal_pairs":len(sl_pairs),
     "T2_synthetic_lethal_pairs":sl_pairs[:20],
     "fba_essential_genes":sorted(fba_lethal),
     "per_gene":{g:{"dV":round(dV.get(g,0),4),"strength":round(strength[g],4),
                    "ext_fitness":(round(ext[g],4) if g in ext else None),
                    "label":label.get(g)} for g in genes},
    }
    with open(os.path.join(HERE,"external_benchmark_results.json"),"w") as f:
        json.dump(out,f,indent=1)
    # verdicts
    def verdict(name,cond_pass,cond_fals,val):
        return f"{name}: {'PASS' if cond_pass else ('FALSIFIED' if cond_fals else 'PARTIAL')}  (value={val})"
    print(f"WT growth {wt:.4f} | scored {len(scored)} genes, {sum(y)} positive, {len(quarantine)} quarantined")
    print(verdict("T1 AOP recovers essentiality (AUROC>=.75)", T1_auroc>=0.75, T1_auroc<0.65, round(T1_auroc,4)))
    print(verdict("T2 synthetic-lethal coalition exists", len(sl_pairs)>=1, len(sl_pairs)==0, len(sl_pairs)))
    print(verdict("T3 AOP beats rival by>=.10", (T1_auroc-T3_auroc_rival)>=0.10, T3_auroc_rival>=T1_auroc, round(T1_auroc-T3_auroc_rival,4)))
    print(verdict("T4 strength_|_viability (Spearman<=.3)", T4_spearman<=0.3, T4_spearman>0.5, round(T4_spearman,4)))
    print("rival AUROC:",round(T3_auroc_rival,4))
    return out

if __name__=="__main__":
    main()
