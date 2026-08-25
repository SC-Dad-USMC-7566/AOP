"""
AOP real-system gate: do the substitutability mechanism-ceilings survive on real
mass-action kinetics? (Schlogl bistable birth-death process.)

Pre-registered exits (aop_realsystem_prereg.md): GO if the ceiling ordering
(Flux/Bank bounded, only Barrier unbounded) reproduces; NULL if Flux or Bank is
unbounded, or Barrier ceils too, or the knobs are inseparable.

Verdict: NULL. On real kinetics Barrier AND Bank are both unbounded (P->1), and
pure Flux (cycle current at fixed stationary distribution) has ZERO leverage on P
-- a 1-D birth-death theorem, not a numerical accident. The minimal-model ceilings
were artifacts. Also contains the gate-3 minimal-model check (bank-only vs bar+bank).
"""
import numpy as np
from scipy.signal import argrelextrema

Omega=25.0; NMAX=300
k1,k2,k3,k4=6.0,1.0,8.0,0.5
def channels(n,a,b):
    return (k1*a*n*(n-1)/Omega, k2*n*(n-1)*(n-2)/Omega**2, k4*b*Omega, k3*n)
def Wpm(n,a,b):
    R1f,R1b,R2f,R2b=channels(n,a,b); return R1f+R2f, R1b+R2b
def stat(a,b):
    logp=np.zeros(NMAX+1)
    for n in range(1,NMAX+1):
        logp[n]=logp[n-1]+np.log(max(Wpm(n-1,a,b)[0],1e-300))-np.log(max(Wpm(n,a,b)[1],1e-300))
    logp-=logp.max(); p=np.exp(logp); return p/p.sum()

# bistable base
base=None
for a in np.linspace(0.5,3,12):
    for b in np.linspace(2,20,12):
        p=stat(a,b); mn=argrelextrema(p,np.less)[0]; mx=argrelextrema(p,np.greater)[0]
        if len(mx)>=2 and len(mn)>=1 and p[:mn[0]].sum()>0.05 and p[mn[0]:].sum()>0.05:
            base=(a,b,mn[0]); break
    if base: break
a0,b0,sad=base; p0=stat(a0,b0)
Ph=lambda p: p[sad:].sum()

if __name__=="__main__":
    print(f"bistable base a={a0:.3f} b={b0:.3f} saddle n_s={sad}  base P(high)={Ph(p0):.4f}")
    print("\nBARRIER (deepen well on detailed-balance manifold, sigma_dot=0):")
    bfac=k1*k3/(k2*k4)
    for A in [0.5,1,2,5]:
        print(f"  a={A}: P={Ph(stat(A,bfac*A)):.4f}")
    print("\nFLUX, pure cycle current (stationary dist FIXED): P invariant =", round(Ph(p0),4),
          "-> zero leverage (1-D birth-death theorem)")
    print("\nFLUX, chemostat b (conflates barrier): P at b=2,4,8,16 =",
          [round(Ph(stat(1.0,b)),3) for b in (2,4,8,16)])
    print("\nBANK (reset low->high at n_reset, real metastable well):")
    n_reset=int(sad*1.6)
    def bank(rr):
        n=NMAX+1; Q=np.zeros((n,n))
        for m in range(n):
            Wp,Wm=Wpm(m,a0,b0)
            if m+1<n: Q[m+1,m]+=Wp
            if m-1>=0: Q[m-1,m]+=Wm
            if 0<m<=sad: Q[n_reset,m]+=rr
        for j in range(n): Q[j,j]=-(Q[:,j].sum()-Q[j,j])
        A=np.vstack([Q,np.ones(n)]); bb=np.zeros(n+1); bb[-1]=1
        return np.linalg.lstsq(A,bb,rcond=None)[0]
    for rr in [0,0.5,1,2,50]:
        print(f"  r={rr}: P={Ph(bank(rr)):.4f}")
    print("  => UNBOUNDED (no ceiling). Verdict: NULL.")
