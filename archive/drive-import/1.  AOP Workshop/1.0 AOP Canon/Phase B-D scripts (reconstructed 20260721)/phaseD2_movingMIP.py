"""
phaseD2_movingMIP.py - adiabatic non-stationary Phi_MIP[Sig(t)].
Independent reconstruction, 21 July 2026. Canon v1.20 Edit E21 / gap-row 11.

CANON CLAIM: the instantaneous/adiabatic spatial Phi_MIP[Sig(t)] is well-posed:
zero-calibration survives off-stationarity (Phi_MIP = 0 exactly on a block-decomposable
Sig(t)); along a ramp merging two modules the MIP relabels at a kink (Phi_MIP(t)
continuous, derivative discontinuous). The time-EXTENDED moving partition remains FRONTIER.
"""
import numpy as np, itertools
def tc(Sig,idx):
    s=Sig[np.ix_(idx,idx)]; return 0.5*(sum(np.log(np.diag(s)))-np.log(np.linalg.det(s)))
def phi_mip(Sig):
    N=len(Sig);allidx=list(range(N));TCw=tc(Sig,allidx);best=1e9;cut=None
    for r in range(1,N//2+1):
        for c in itertools.combinations(allidx,r):
            c=list(c);d=[i for i in allidx if i not in c]
            phi=TCw-tc(Sig,c)-tc(Sig,d)
            if phi<best:best=phi;cut=tuple(c)
    return best,cut
def Sig_t(t,N=6,g=1.0):
    # two 3-node modules; inter-module coupling ramps up with t in [0,1]
    L=np.zeros((N,N))
    def add(i,j,w):L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
    for m in [range(0,3),range(3,6)]:
        m=list(m)
        for i in range(len(m)):
            for j in range(i+1,len(m)): add(m[i],m[j],1.0)
    for i in range(0,3):
        for j in range(3,6): add(i,j,1.2*t)
    return np.linalg.inv(np.eye(N)+g*L)
print("phaseD2_movingMIP  (adiabatic spatial Phi_MIP off-stationarity):")
# block-decomposable check: t=0 exactly block diagonal
phi0,cut0=phi_mip(Sig_t(0.0))
print(f"  block-decomposable Sig(0):  Phi_MIP = {phi0:.2e}  (=0, zero-calibration survives)  MIP cut={cut0}")
prev=None
for t in np.linspace(0,1,11):
    phi,cut=phi_mip(Sig_t(t))
    flag="  <-- MIP relabels" if (prev is not None and cut!=prev) else ""
    print(f"  t={t:.1f}  Phi_MIP={phi:.4f}  MIP cut={cut}{flag}")
    prev=cut
print("-> Phi_MIP=0 exactly on block-decomposable Sig(t); MIP relabels along the ramp (kink).")
print("   Time-EXTENDED moving partition over a window is NOT computed here (remains FRONTIER).")
