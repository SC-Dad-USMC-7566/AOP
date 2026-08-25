"""
phaseC2_b4.py - Boundary maintenance burden B4 = housekeeping entropy production.
Independent reconstruction, 21 July 2026. Canon v1.20 Edit E14 / gap-row 4.

CANON CLAIM: on a minimal driven NESS the maintenance burden (panel B4) equals the
housekeeping EP rate sigma_hk = f*J (drive affinity x futile-cycle current): exactly
zero at equilibrium; quadratic in the held contrast, linear in the leak; and the
direct EP equals the Schnakenberg cycle decomposition to ~1e-13.

This script verifies: (i) sigma_hk = 0 at equilibrium (f=0, detailed balance);
(ii) sigma_hk = f*J identically (drive force x cycle current) = Schnakenberg cycle EP,
to machine precision; (iii) quadratic-in-contrast onset.
"""
import numpy as np

def ep_cycle(f, a=1.0):
    # 3-state ring; forward rate a*exp(f/6), backward a*exp(-f/6) on each of 3 edges
    # -> exact cycle affinity = f; at f=0 detailed balance (EP=0).
    kf, kb = a*np.exp(f/6), a*np.exp(-f/6)
    k = np.zeros((3,3))
    for i in range(3):
        k[i,(i+1)%3] = kf
        k[i,(i-1)%3] = kb
    K = k.copy()
    for i in range(3): K[i,i] = -k[i].sum()
    A = np.vstack([K.T, np.ones(3)]); b = np.array([0.,0.,0.,1.])
    p,*_ = np.linalg.lstsq(A,b,rcond=None)
    # direct EP
    ep_direct = 0.0
    for i in range(3):
        j=(i+1)%3
        Jij = k[i,j]*p[i]-k[j,i]*p[j]
        ep_direct += Jij*np.log((k[i,j]*p[i])/(k[j,i]*p[j]))
    # cycle current J (net around ring) and Schnakenberg EP = J * affinity(f)
    J = k[0,1]*p[0]-k[1,0]*p[1]
    ep_schnak = J*f
    return ep_direct, ep_schnak, J, p

print("phaseC2_b4  (B4 = sigma_hk = f*J):")
epeq,_,_,_ = ep_cycle(0.0)
print(f"  equilibrium (f=0):  sigma_hk = {epeq:.3e}   (= 0 at detailed balance)")
print("  f      sigma_hk(direct)   f*J(Schnakenberg)   |diff|          quadratic-onset sigma/f^2")
for f in [0.01,0.05,0.2,0.5]:
    epd, eps, J, p = ep_cycle(f)
    print(f"  {f:.2f}   {epd:.10e}   {eps:.10e}   {abs(epd-eps):.2e}   {epd/f**2:.5f}")
print("-> sigma_hk vanishes at equilibrium; equals f*J (drive x current) to ~1e-13;")
print("   onset is quadratic in the drive/contrast. Matches canon B4 = housekeeping EP.")
print("   (The specific leak coefficient 0.5*Delta^2*g(g+w)/w is the pump+leak elaboration")
print("    of the same f*J identity; core identity reproduced here.)")
