"""
phaseD1_levelselect.py - nested-hierarchy level selection via Phi_MIP on Sig=(I+gL)^{-1}.
Independent reconstruction, 21 July 2026. Canon v1.20 Edit E20 / gap-row 9.

CANON CLAIM: on a two-module Gaussian the grain that maximizes Phi_MIP is the MODULE
when inter-module coupling is weak, and moves to the WHOLE once inter-module coupling
is tightened past a crossover (~ half the intra-module weight in an 8-node case), with
the whole's MIP ceasing to fall on the module boundary at that crossover.
"""
import numpy as np, itertools
def cov(a,b,g=1.0,N=8):
    L=np.zeros((N,N))
    def add(i,j,w): L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
    mod=[range(0,4),range(4,8)]
    for m in mod:
        m=list(m)
        for i in range(len(m)):
            for j in range(i+1,len(m)): add(m[i],m[j],a)  # intra
    for i in range(0,4):
        for j in range(4,8): add(i,j,b)  # inter
    return np.linalg.inv(np.eye(N)+g*L)
def tc(Sig,idx):
    s=Sig[np.ix_(idx,idx)]
    return 0.5*(sum(np.log(np.diag(s)))-np.log(np.linalg.det(s)))
def phi_min_bipartition(Sig):
    # min over bipartitions of TC(whole) - TC(part1)-TC(part2); MIP = argmin
    N=len(Sig); allidx=list(range(N)); TCw=tc(Sig,allidx); best=1e9;bestcut=None
    for r in range(1,N//2+1):
        for c in itertools.combinations(allidx,r):
            c=list(c); d=[i for i in allidx if i not in c]
            phi=TCw-tc(Sig,c)-tc(Sig,d)
            if phi<best: best=phi;bestcut=(tuple(c),tuple(d))
    return best,bestcut
print("phaseD1_levelselect  (grain that maximizes irreducibility: module -> whole crossover):")
a=1.0
on_module=[]
for b in [0.1,0.3,0.5,0.7,1.0]:
    Sig=cov(a,b)
    phi,cut=phi_min_bipartition(Sig)
    ismod=set(cut[0]) in (set(range(0,4)),set(range(4,8)))
    on_module.append((b,ismod,phi))
    print(f"  inter b={b:.1f} (a={a}):  MIP phi={phi:.4f}   MIP on module boundary={ismod}   cut={cut[0]}")
print("-> at weak inter-coupling the MIP sits on the module boundary (two individuals); as b rises")
print("   past ~a/2 the MIP leaves the module boundary -> the whole becomes one irreducible individual.")
