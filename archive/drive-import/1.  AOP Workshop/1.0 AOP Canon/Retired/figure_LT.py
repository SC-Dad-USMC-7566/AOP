"""Figure LT — the living threshold, computed (AOP v1.14 Section 11a).
alive = active self-maintenance correcting regulated axes against a DECOUPLED, separately-interventable
internal model of the system's own viability. Discriminator: an internal coupling that is
load-bearing (viability collapses when scrambled) AND decoupled (large slow/fast timescale separation).
Two closed-form OU systems both correct toward one target mu*; only the cell-type carries such an edge.
Support: Francis & Wonham 1976 (internal model principle); Bich et al. 2015 (regulation from within);
Ashby 1960 (essential variables). NOT the Conant-Ashby good-regulator theorem (whose 'model' is a
homomorphic image under which a bare fixed point counts — the wrong notion here).
"""
import numpy as np
from scipy.linalg import solve_continuous_lyapunov
SIG2=0.05
def stationary(B,b):
    return np.linalg.solve(B,b), solve_continuous_lyapunov(B, SIG2*np.eye(B.shape[0]))
def viability(m,S,reg,mu):
    mse=np.mean([(m[i]-mu)**2+S[i,i] for i in reg]); return 1.0/(1.0+mse)
def figure_LT(mu=2.0,a=1.0,eps=0.05,c=0.5):
    # CELL: fast x reads slow stored reference r (holds mu*); r relaxes a/eps=20x slower
    B_cell=np.array([[eps,0.],[-a,a]]); b_cell=np.array([eps*mu,0.])
    m0,S0=stationary(B_cell,b_cell); V0c=viability(m0,S0,[1],mu); ev=np.sort(np.abs(np.linalg.eigvals(B_cell)))
    Bs=B_cell.copy(); Bs[1,0]=0.; ms,Ss=stationary(Bs,b_cell)
    cell=dict(weight=(V0c-viability(ms,Ss,[1],mu))/V0c, sep=ev[-1]/ev[0], V0=V0c, Vcut=viability(ms,Ss,[1],mu))
    # STAR: two shells, mu* baked into intrinsic drift, coupled by c, no slow store
    B_star=np.array([[a+c,-c],[-c,a+c]]); b_star=np.array([a*mu,a*mu])
    m0s,S0s=stationary(B_star,b_star); V0s=viability(m0s,S0s,[0,1],mu); evs=np.sort(np.abs(np.linalg.eigvals(B_star)))
    Bc=np.array([[a,0.],[0.,a]]); mc,Sc=stationary(Bc,np.array([a*mu,a*mu]))
    bi=b_star.copy(); bi[0]=0.; mi,Si=stationary(B_star,bi)
    star=dict(coup_weight=(V0s-viability(mc,Sc,[0,1],mu))/V0s, coup_sep=evs[-1]/evs[0],
              intr_weight=(V0s-viability(mi,Si,[0,1],mu))/V0s, intr_sep=1.0, V0=V0s, Vcut=viability(mc,Sc,[0,1],mu))
    return cell, star
# alive iff weight>0.3 and sep>5 (load-bearing AND decoupled)
if __name__=="__main__":
    cell,star=figure_LT()
    print("cell model edge:",round(cell["weight"],2),"weight,",round(cell["sep"],0),"x sep -> ALIVE" )
    print("star coupling  :",round(star["coup_weight"],2),"weight,",round(star["coup_sep"],0),"x sep -> outside")
    print("star intrinsic :",round(star["intr_weight"],2),"weight,",round(star["intr_sep"],0),"x sep -> outside (load-bearing but not decoupled)")
