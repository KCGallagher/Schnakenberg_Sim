"""Runs simulation of time and spatially dependant ODE model

Plots one concentration variable at subsequent timepoints and then converts 
these into a .gif, optionally deleting the image files afterwards"""


import glob
import os
from fipy import Grid2D, CellVariable, TransientTerm, DiffusionTerm, Viewer
from PIL import Image
from numpy import delete


D_A, D_B = 1.6, 160
alpha = 0.02
beta = 3
mu = 1
kappa = 1e-6
A_0, B_0 = 200, 75  # Shou;d be defined as floats

nx = 20
ny = nx
dx = 1.
dy = dx
L = dx * nx
m = Grid2D(dx=dx, dy=dy, nx=nx, ny=ny)

time_step = 0.002
step_num = 40
delete_images = True  # Boolean to delete images after running

v0 = CellVariable(name = "Concentration of A", mesh=m, hasOld=True, value=A_0)
v1 = CellVariable(name = "Concentration of B", mesh=m, hasOld=True, value=B_0)
plot_var = v0  # CHANGE THIS TO V0 OR V1 TO DETERMINE WHICH VARIABLE IS PLOTTED

eqn0 = TransientTerm(var=v0) == mu - alpha * v0 + kappa * v0**2 * v1 + DiffusionTerm(D_A, var=v0) 
eqn1 = TransientTerm(var=v1) == beta - kappa * v0**2 * v1 +  DiffusionTerm(D_B, var=v1)
eqn = eqn0 & eqn1

viewer = Viewer(vars=plot_var)
for step in range(step_num):
    v0.updateOld()
    v1.updateOld()
    eqn.solve(dt=time_step)
    viewer.plot(f"Images/Spatial_ODE/Mesh2D_{step}.png")


fp_in = "Images/Spatial_ODE/Mesh2D_*.png"
fp_out = "Images/Spatial_ODE/Mesh2D.gif"

img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)

if delete_images:
    for file in os.listdir('Images/Spatial_ODE/'):
        if file.endswith('.png'):
            try:
                os.remove('Images/Spatial_ODE/' + file) 
            except FileNotFoundError:
                print("Can't find file: " + str(file))
