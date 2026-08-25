"""
AOP budget gate: is persistence a conserved "budget" priced in a common currency?

Pre-registered exits (aop_budget_prereg.md): GO if the exchange-rate loop closes
NON-VACUOUSLY and sigma_dot is (near-)constant on an iso-P surface (<=10% spread);
NULL if the loop closes only vacuously (forced by P being a scalar) or sigma_dot
varies with mechanism-mix at fixed P.

Verdict: NULL. Loop product = -1 identically (vacuous: true for any scalar P).
sigma_dot on iso-P=0.50 ranges 0.000 (barrier) to 1.313 (flux) = 157% of mean.
No mechanism-independent price -> no budget.

Reuses the substitutability model (aop_substitutability_gate.py).
"""
import numpy as np
from scipy.optimize import brentq

N=6; KAPPA=1.0; G0=0.6; BASIN=set([3,4,5,6]); RESET_TO=4

def build_Q(b=0.0,f=0.0,r=0.0):
    n=N+1; Q=np.zeros((n,n))
    def add(j,i,rate): Q[i,j]+=rate
    for i in range(1,n): add(i,i-1,KAPPA)
    g=G0*np.exp(b)
    for i in range(0,n-1): add(i,i+1,g)
    if f>0:
        for i in range(0,n-1): add(i,i+1,f)
        add(n-1,0,f)
    if r>0: add(0,RESET_TO,r)
    for j in range(n): Q[j,j]=-(Q[:,j].sum()-Q[j,j])
    return Q
def stat(Q):
    n=Q.shape[0]; A=np.vstack([Q,np.ones(n)]); b=np.zeros(n+1); b[-1]=1
    p,*_=np.linalg.lstsq(A,b,rcond=None); return p
def P(b,f,r): return sum(stat(build_Q(b,f,r))[i] for i in BASIN)
def sd(b,f,r):
    p=stat(build_Q(b,f,r)); Q=build_Q(b,f,r); s=0.0; n=Q.shape[0]
    for i in range(n):
        for j in range(n):
            if i==j: continue
            Jf=Q[i,j]*p[j]; Jb=Q[j,i]*p[i]
            if Jf>1e-15 and Jb>1e-15: s+=(Jf-Jb)*np.log(Jf/Jb)
            elif Jf>1e-15 and Jb<=1e-15: s+=Jf*30
    return 0.5*s

if __name__=="__main__":
    eps=1e-4
    def loop(b,f,r):
        Pb=(P(b+eps,f,r)-P(b-eps,f,r))/(2*eps)
        Pf=(P(b,f+eps,r)-P(b,f-eps,r))/(2*eps)
        Pr=(P(b,f,r+eps)-P(b,f,r-eps))/(2*eps)
        return (-Pb/Pf)*(-Pf/Pr)*(-Pr/Pb)
    f0=brentq(lambda f:P(0.15,f,0.10)-0.50,0,50)
    f1=brentq(lambda f:P(0.10,f,0.05)-0.50,0,50)
    print("TEST A loop product (two generic points):",
          round(loop(0.15,f0,0.10),6), round(loop(0.10,f1,0.05),6),
          "-> VACUOUS (forced by scalar P)")
    print("\nTEST B sigma_dot on iso-P=0.50:")
    pts=[("barrier",brentq(lambda b:P(b,0,0)-0.50,0,5),0,0),
         ("flux",0,brentq(lambda f:P(0,f,0)-0.50,0,50),0),
         ("bank",0,0,brentq(lambda r:P(0,0,r)-0.50,0,50))]
    vals=[]
    for nm,b,f,r in pts:
        v=sd(b,f,r); vals.append(v); print(f"  {nm:8} sigma_dot={v:.4f}")
    vals=np.array(vals)
    print(f"  spread/mean = {(vals.max()-vals.min())/vals.mean()*100:.0f}%  => NULL (no common price)")
