"""Plot a reaction-diffusion system to generate Turing Patterns

This system described by a PDE called the FitzHugh–Nagumo equation.
It is evaluated here using finite difference methods taken from:
https://ipython-books.github.io/124-simulating-a-partial-differential
-equation-reaction-diffusion-systems-and-turing-patterns/
"""

import numpy as np
import matplotlib.pyplot as plt
from finite_difference import laplacian, show_patterns

a = 2.8e-4
b = 5e-3
tau = .1
k = -.005

size = 100  # size of the 2D grid
dx = 2. / size  # space step

T = 9.0  # total time
dt = .001  # time step
n = int(T / dt)  # number of iterations

U = np.random.rand(size, size)
V = np.random.rand(size, size)

fig, axes = plt.subplots(3, 3, figsize=(8, 8))
step_plot = n // 9
# Simulate the PDE with the finite difference method.
for i in range(n):
    # Compute the Laplacian of u and v.
    deltaU = laplacian(U, dx)
    deltaV = laplacian(V, dx)
    # Take the values of u and v inside the grid.
    Uc = U[1:-1, 1:-1]
    Vc = V[1:-1, 1:-1]
    # Update the variables.
    U[1:-1, 1:-1], V[1:-1, 1:-1] = \
        Uc + dt * (a * deltaU + Uc - Uc**3 - Vc + k),\
        Vc + dt * (b * deltaV + Uc - Vc) / tau
    # Neumann/zero flux conditions: derivatives at the edges
    # are null.
    for Z in (U, V):
        Z[0, :] = Z[1, :]
        Z[-1, :] = Z[-2, :]
        Z[:, 0] = Z[:, 1]
        Z[:, -1] = Z[:, -2]

    if i % step_plot == 0 and i < 9 * step_plot:
        ax = axes.flat[i // step_plot]
        show_patterns(U, ax=ax)
        ax.set_title(f'$t={i * dt:.2f}$')

plt.savefig("Images/Spatial_ODE/Turing_Evolution.png")
fig, ax = plt.subplots(1, 1, figsize=(8, 8))
show_patterns(U, ax=ax)
plt.savefig("Images/Spatial_ODE/Turing_Final_State.png")
