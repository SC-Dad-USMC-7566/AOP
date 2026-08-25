"""
AOP substitutability gate: are Barrier, Flux, and Bank fungible at fixed persistence?

Pre-registered exits (aop_substitutability_prereg.md): GO if all three mechanisms
reach P*=0.80 alone AND a continuous iso-P surface connects the corners with finite
exchange rates AND the three are distinct axes; NULL if any corner is unreachable.

Verdict: NULL at P*=0.80 (flux and bank have hard ceilings below the target).
Post-hoc: a genuine iso-P=0.50 substitution surface exists below the lowest ceiling.

Self-contained: (N+1)-state CTMC, kick rate KAPPA toward the erased state 0,
basin = states >= N/2. Three knobs: Barrier b (equilibrium climb bias, sigma_dot=0),
Flux f (driven ring current, sigma_dot>0), Bank r (reset 0->basin).
"""
import numpy as np
from scipy.optimize import brentq

N=6; KAPPA=1.0; G0=0.6; BASIN=set([3,4,5,6]); RESET_TO=4

def build_Q(b=0.0, f=0.0, r=0.0):
    n=N+1; Q=np.zeros((n,n))
    def add(j,i,rate): Q[i,j]+=rate      # transition j -> i
    for i in range(1,n): add(i,i-1,KAPPA)               # kick down
    g=G0*np.exp(b)
    for i in range(0,n-1): add(i,i+1,g)                 # barrier climb (DB)
    if f>0:
        for i in range(0,n-1): add(i,i+1,f)             # flux push up
        add(n-1,0,f)                                    # flux closure N->0 (breaks DB)
    if r>0: add(0,RESET_TO,r)                           # bank reset
    for j in range(n): Q[j,j]=-(Q[:,j].sum()-Q[j,j])
    return Q

def stat(Q):
    n=Q.shape[0]; A=np.vstack([Q,np.ones(n)]); b=np.zeros(n+1); b[-1]=1
    p,*_=np.linalg.lstsq(A,b,rcond=None); return p

def persistence(Q): return sum(stat(Q)[i] for i in BASIN)

def sigma_dot(Q):
    p=stat(Q); s=0.0; n=Q.shape[0]
    for i in range(n):
        for j in range(n):
            if i==j: continue
            Jf=Q[i,j]*p[j]; Jb=Q[j,i]*p[i]
            if Jf>1e-15 and Jb>1e-15: s+=(Jf-Jb)*np.log(Jf/Jb)
            elif Jf>1e-15 and Jb<=1e-15: s+=Jf*30
    return 0.5*s

if __name__=="__main__":
    print("Ceilings (knob alone -> infinity):")
    print(f"  barrier: {persistence(build_Q(b=8)):.4f}")
    print(f"  flux:    {persistence(build_Q(f=1024)):.4f}  (= 4/7 = {4/7:.4f})")
    print(f"  bank:    {persistence(build_Q(r=1024)):.4f}")
    print(f"Barrier reaches P*=0.80 at b={brentq(lambda b:persistence(build_Q(b=b))-0.80,0,5):.3f}")
    print("=> NULL at P*=0.80: flux and bank cannot reach it.")
    print("\nPost-hoc iso-P=0.50 barrier<->flux surface (r=0):")
    for b in np.linspace(0,0.428,7):
        Pb=persistence(build_Q(b=b))
        f=0.0 if Pb>=0.50 else brentq(lambda f:persistence(build_Q(b=b,f=f))-0.50,0,200)
        print(f"  b={b:.3f}  f={f:.3f}  sigma_dot={sigma_dot(build_Q(b=b,f=f)):.3f}")
