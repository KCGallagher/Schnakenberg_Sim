import numpy as np
import scipy.integrate
import typing

h= 25*1e-3

m = 100  # number of rows
n = 100 # number of columns
shape = (m,n)
domain_size = (h*m,h*n) # = 1mm 
d_A = 1e-5/(2*h**2)
d_B = 1e-3/(2*h**2)

# Initialise
A_init = 200
B_init = 75

# Store all the parameters in a dictionary
params = {'mu': 1, 'beta': 3, 'alpha': .02, 'kappa': 1e-6, 
          'd_A': d_A, 'd_B': d_B}

A = A_init * np.ones(shape)
B = B_init * np.ones(shape)

print(A)