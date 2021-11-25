import sim
import numpy as np
import matplotlib.pyplot as plt

#### Set gridsize parameters ###

h= 2.5*1e-3

m = 40  # number of rows
n = 40 # number of columns
domain_size = (h*m,h*n) # = 1mm 

### Set the rate parameters  ###

# Birth rate for species A
k2 = 15625
# Birth rate for species B
k4 = 46875
# Death rate for species A
k3 = .02
# Reaction rate for "2A + B -> 3A" 
k1 = 2.5*1e-5

# Diffusion parameters for species A and B
d_A = 1e-5/(2*h**2)
d_B = 1e-3/(2*h**2)

# Initialise
A_init = 200
B_init = 75

# Store all the parameters in a dictionary
params = {'mu': k2*h**3, 'beta': k4*h**3, 'alpha': k3, 'kappa': k1*h**6, 
          'd_A': d_A, 'd_B': d_B}

tau = 0.002 # time interval
N_t = 1_00_000  # number of units of time

X_A, X_B = sim.initialize_movie(N_t, m, n, A_init, B_init)

# Loop through time
for t in np.arange(N_t-1):
    if t % 100_000 == 0:
        print(t)
    sim.calculate_movie(tau, X_A, X_B, t, **params)