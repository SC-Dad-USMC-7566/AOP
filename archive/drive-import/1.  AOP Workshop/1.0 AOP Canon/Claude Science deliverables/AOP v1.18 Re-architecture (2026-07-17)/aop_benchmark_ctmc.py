"""
AOP Benchmark — Leaky Autocatalytic Compartment (exactly-solvable CTMC)
=======================================================================
Companion to OAI Remediation Phase 4. Closed-form (no Monte-Carlo):
finite-horizon survival via matrix exponential of the transient subgenerator,
full coalition table over 2^7 mechanism subsets, Mobius interaction terms,
Shapley values, minimal failure cut-sets, viability-preserving sets.

State (n, r, z):
  n in 0..N  copy number of core autocatalytic species; n=0 = extinction (absorbing)
  r in {0,1} fuel-driven regulator (leak suppression); creates entropy production
  z in {0,1} downstream readout tracking r; feeds nothing back (inert spectator)

Mechanisms (intervenable couplings), gates chosen so the controls are clean:
  A, B   redundant birth pair   -> OR gate on autocatalytic birth (either sufficient)
  S1, S2 synergy birth pair     -> AND gate on a second birth term (both needed)
  R      leak-suppression       -> death rate *= (1 - rho) when r=1
  C      weak constitutive influx
  Z      r->z tracking coupling  (raises MI(z;r); zero viability effect)
"""
import numpy as np
from scipy.linalg import expm
from itertools import combinations, chain
from math import factorial

PB = dict(N=8, k_auto=0.72, kS=0.34, kC=0.055, delta=0.38, delta0=0.03,
          rho=0.55, f=0.9, w=0.7, lam=1.4, lam0=0.05)
MECHS = ['A','B','C','R','S1','S2','Z']

def gen(mech, p=PB):
    P={**PB,**(p or {})}; N=P['N']
    A=mech.get('A',1);B=mech.get('B',1);C=mech.get('C',1);R=mech.get('R',1)
    S1=mech.get('S1',1);S2=mech.get('S2',1);Z=mech.get('Z',1)
    states=[(n,r,z) for n in range(N+1) for r in (0,1) for z in (0,1)]
    ix={s:i for i,s in enumerate(states)}; M=len(states); Q=np.zeros((M,M))
    auto=lambda n:n*(1-n/N)
    for (n,r,z) in states:
        i=ix[(n,r,z)]
        if n==0: continue
        if n<N:
            or_gate=1.0 if (A or B) else 0.0
            and_gate=1.0 if (S1 and S2) else 0.0
            birth=P['k_auto']*or_gate*auto(n)+P['kS']*and_gate*auto(n)+P['kC']*C
            if birth>0: Q[i,ix[(n+1,r,z)]]+=birth
        supp=(1-P['rho']*R) if r==1 else 1.0
        death=(P['delta']*supp+P['delta0'])*n
        if death>0: Q[i,ix[(n-1,r,z)]]+=death
        if r==0: Q[i,ix[(n,1,z)]]+=P['f']
        else:    Q[i,ix[(n,0,z)]]+=P['w']
        rate_to1=(P['lam']*Z if r==1 else 0.0)+P['lam0']
        rate_to0=(P['lam']*Z if r==0 else 0.0)+P['lam0']
        if z==0: Q[i,ix[(n,r,1)]]+=rate_to1
        else:    Q[i,ix[(n,r,0)]]+=rate_to0
    for i in range(M): Q[i,i]=-Q[i].sum()
    ab=np.array([s[0]==0 for s in states])
    return Q,states,ab

def surv(mech,tau,start=None,p=PB):
    Q,st,ab=gen(mech,p)
    if start is None: start=((p or PB)['N'],0,0)
    tr=np.where(~ab)[0]; T=Q[np.ix_(tr,tr)]
    trs=[st[i] for i in tr]; pos={s:i for i,s in enumerate(trs)}
    v=np.zeros(len(tr)); v[pos[start]]=1.0
    return float((v@expm(T*tau)).sum())

def coalition_table(tau=15):
    base=surv({},tau)
    coal={S: base-surv({m:0 for m in S},tau) for k in range(len(MECHS)+1) for S in combinations(MECHS,k)}
    return base, coal

def mobius(coal):
    ps=lambda S: chain.from_iterable(combinations(S,r) for r in range(len(S)+1))
    h={}
    for k in range(len(MECHS)+1):
        for S in combinations(MECHS,k):
            h[S]=coal[S]-sum(h[T] for T in ps(S) if set(T)<set(S))
    return h

def shapley(coal,m):
    n=len(MECHS); phi=0.0; others=[x for x in MECHS if x!=m]
    for k in range(len(others)+1):
        for T in combinations(others,k):
            S=set(T); wt=factorial(k)*factorial(n-k-1)/factorial(n)
            phi+=wt*(coal[tuple(sorted(S|{m}))]-coal[tuple(sorted(S))])
    return phi

if __name__=='__main__':
    base,coal=coalition_table(15); h=mobius(coal)
    print('baseline V(15)=%.4f'%base)
    for m in MECHS: print(' dV(%s)=%+.4f  shapley=%+.4f'%(m,coal[(m,)],shapley(coal,m)))
    print('h(A,B)=%+.4f  h(S1,S2)=%+.4f'%(h[('A','B')],h[('S1','S2')]))
