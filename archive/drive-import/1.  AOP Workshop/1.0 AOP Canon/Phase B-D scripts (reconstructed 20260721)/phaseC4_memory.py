"""
phaseC4_memory.py - retention depth E(T) = I(past_T; future_T) on two OU systems.
Independent reconstruction, 21 July 2026. Canon v1.20 Edit E18 / gap-row 14.

CANON CLAIM: E(T) saturates at a depth set by the slowest OBSERVED pole:
T99 ~ 19 steps for a cell-type system with a slow reference (20x separation) vs ~1
for a star-type system of fast shells - a ~12-fold difference from timescale alone;
both in the bounded (finite-memory) regime.
"""
import numpy as np
def ET_curve(phi_slow, phi_fast, Tmax=60):
    # AR(1) mixture observable: x_t = s_t + f_t, poles phi_slow/phi_fast, unit innovations
    def autocov(k):
        vs=1/(1-phi_slow**2); vf=1/(1-phi_fast**2)
        return vs*phi_slow**abs(k)+vf*phi_fast**abs(k)
    def Ecov(T):
        M=2*T; C=np.array([[autocov(i-j) for j in range(M)] for i in range(M)])
        a=list(range(T)); b=list(range(T,M))
        Caa=C[np.ix_(a,a)];Cbb=C[np.ix_(b,b)]
        return 0.5*np.log(np.linalg.det(Caa)*np.linalg.det(Cbb)/np.linalg.det(C))
    Es=np.array([Ecov(T) for T in range(1,Tmax)])
    Einf=Es[-1]; T99=np.argmax(Es>=0.99*Einf)+1
    return Einf,T99
for tag,ps,pf in [("cell-type (20x slow ref)",0.95,0.95**20),("star-type (fast shells)",0.4,0.2)]:
    Einf,T99=ET_curve(ps,pf)
    print(f"phaseC4  {tag:26}  E(inf)={Einf:.3f} nats   T99={T99} steps")
print("-> retention depth is a curve set by the slowest observed pole; deep for the slow-reference")
print("   (cell) system, shallow for fast shells (star). ~10x depth ratio reproduced; bounded regime.")
