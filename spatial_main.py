"""Runs simulation of time and spatially dependant ODE model"""

from fipy import Grid1D, CellVariable, TransientTerm, DiffusionTerm, Viewer

D_1, D_2 = 1, 0.01
alpha = 1
beta = 1
mu = 1
kappa = 1
A_0, B_0 = 1.0, 1.0  # Should be floats

m = Grid1D(nx=100, Lx=1.)

v0 = CellVariable(mesh=m, hasOld=True, value=A_0)
v1 = CellVariable(mesh=m, hasOld=True, value=B_0)

eqn0 = TransientTerm(var=v0) == mu - alpha * v0 + kappa * v0**2 * v1 + DiffusionTerm(D_1, var=v0) 
eqn1 = TransientTerm(var=v1) == beta - kappa * v0**2 * v1 +  DiffusionTerm(D_2, var=v1)

eqn = eqn0 & eqn1

vi = Viewer((v0, v1))
from builtins import range
for t in range(10):
    v0.updateOld()
    v1.updateOld()
    eqn.solve(dt=1.e-3)
    vi.plot(f"Images/Spatial_ODE/coupledimage{t}.png")