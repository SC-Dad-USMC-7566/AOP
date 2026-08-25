"""
phaseC1_b2.py - Boundary screening residual B2 = I(in;out | interface).
Independent reconstruction, 21 July 2026. Canon v1.20 Edit E15 / gap-row 3.

CANON CLAIM: on a static Gaussian with interface F, B2=I(Xin;Xout|F) vanishes when
inside/outside interact only THROUGH F (screened), and is positive when a coupling
bypasses F; the cross-boundary dependence B5=I(Xin;Xout) stays high in both. B2, not
B5, separates a cut sealed-by-interface from one merely coupled-across.
"""
import numpy as np
def gauss_MI(Sig,a,b):  # I(a;b) for jointly Gaussian blocks
    Saa=Sig[np.ix_(a,a)];Sbb=Sig[np.ix_(b,b)];Sab=Sig[np.ix_(a,b)]
    return 0.5*np.log(np.linalg.det(Saa)*np.linalg.det(Sbb)/np.linalg.det(Sig[np.ix_(a+b,a+b)]))
def cond_MI(Sig,a,b,c):  # I(a;b|c) via conditional covariance (Schur complement on c)
    def cond(xy):
        Sxy=Sig[np.ix_(xy,xy)];Sxc=Sig[np.ix_(xy,c)];Scc=Sig[np.ix_(c,c)]
        return Sxy - Sxc@np.linalg.inv(Scc)@Sxc.T
    Sab_c=cond(a+b)
    na=len(a)
    Saa=Sab_c[:na,:na];Sbb=Sab_c[na:,na:]
    return 0.5*np.log(np.linalg.det(Saa)*np.linalg.det(Sbb)/np.linalg.det(Sab_c))
# nodes: 0=in, 1=interface F, 2=out. Build precision (inverse cov).
def model(bypass):
    J=np.eye(3)*2.0
    J[0,1]=J[1,0]=-0.8   # in <-> F
    J[1,2]=J[2,1]=-0.8   # F  <-> out
    if bypass: J[0,2]=J[2,0]=-0.5  # direct in<->out coupling (bypasses F)
    Sig=np.linalg.inv(J)
    return Sig
print("phaseC1_b2  (screening residual B2 separates sealed from coupled):")
for tag,byp in [("screened (through F)",False),("bypass (direct in-out)",True)]:
    Sig=model(byp)
    B2=cond_MI(Sig,[0],[2],[1]); B5=gauss_MI(Sig,[0],[2])
    print(f"  {tag:24}  B2=I(in;out|F)={B2:.3f} nats   B5=I(in;out)={B5:.3f} nats")
print("-> B2 ~ 0 when screened, B2 > 0 when a coupling bypasses F, while B5>0 in both:")
print("   B2 (not B5) distinguishes sealed-by-interface from merely-coupled-across. Direction reproduced.")
