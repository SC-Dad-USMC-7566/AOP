"""
AOP gate: does a pure divergence-free current move LIFETIME-persistence at fixed
stationary distribution pi and fixed dynamical activity t? (Driven ring.)
Verdict: GO. MFPT 12.35 -> 2.17 (5.7x) while occupancy is invariant by construction.
"""
import numpy as np
N=12
sites=np.arange(N)
pi=np.exp(3.0*np.cos(2*np.pi*sites/N)); pi/=pi.sum()   # well peaked at site 0
m=N//2                                                  # absorbing erased state
t=np.ones(N)                                            # fixed flat activity
def generator(J):
    Q=np.zeros((N,N))
    for i in range(N):
        ip=(i+1)%N
        Q[ip,i]+=(t[i]+J)/(2*pi[i]); Q[i,ip]+=(t[i]-J)/(2*pi[ip])
    for j in range(N): Q[j,j]=-(Q[:,j].sum()-Q[j,j])
    return Q
def mfpt(J,start=0):
    Q=generator(J); idx=[i for i in range(N) if i!=m]
    return np.linalg.solve(Q[np.ix_(idx,idx)],-np.ones(len(idx)))[idx.index(start)]
if __name__=="__main__":
    base=mfpt(0.0)
    print("J, current, MFPT(lifetime), ratio  [occupancy fixed by construction]")
    for J in [0.0,0.2,0.4,0.6,0.8,0.95]:
        print(f"  {J:.2f}  {J:.2f}  {mfpt(J):8.3f}  {mfpt(J)/base:.3f}x")
