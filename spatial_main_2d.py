"""Runs simulation of time and spatially dependant ODE model"""

from fipy import Grid2D, CellVariable, TransientTerm, DiffusionTerm, Viewer

D_A, D_B = 1.6, 160
alpha = 0.02
beta = 3
mu = 1
kappa = 1e-6
A_0, B_0 = 200, 75

nx = 20
ny = nx
dx = 1.
dy = dx
L = dx * nx
m = Grid2D(dx=dx, dy=dy, nx=nx, ny=ny)

time_step = 0.002
step_num = 40

v0 = CellVariable(name = "Concentration of A", mesh=m, hasOld=True, value=A_0)
v1 = CellVariable(name = "Concentration of B", mesh=m, hasOld=True, value=B_0)
plot_var = v1  # CHANGE THIS TO V0 OR V1 TO DETERMINE WHICH VARIABLE IS PLOTTED

eqn0 = TransientTerm(var=v0) == mu - alpha * v0 + kappa * v0**2 * v1 + DiffusionTerm(D_A, var=v0) 
eqn1 = TransientTerm(var=v1) == beta - kappa * v0**2 * v1 +  DiffusionTerm(D_B, var=v1)
eqn = eqn0 & eqn1


viewer = Viewer(vars=plot_var)
for step in range(step_num):
    v0.updateOld()
    v1.updateOld()
    eqn.solve(dt=time_step)
    viewer.plot(f"Images/Spatial_ODE/Mesh2D_{step}.png")

