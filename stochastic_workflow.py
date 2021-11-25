import sim
import numpy as np
import matplotlib.pyplot as plt

# Set gridsize parameters ###

h = 25*1e-3  #mm

m = 2  # number of rows
n = 100 # number of columns
domain_size = (h*m,h*n) # = 1mm

### Set the rate parameters  ###

# Birth rate for species A
k2 = 64000
# Birth rate for species B
k4 = 192000
# Death rate for species A
k3 = .02
# Reaction rate for "2A + B -> 3A"
k1 = 2.44*1e-16

# Initialise
A_init = 200
B_init = 75

# Store all the parameters in a dictionary
params = {'mu': k2*h**3, 'beta': k4*h**3, 'alpha': k3, 'kappa': k1/h**6,
          'd_A': 1e-5/(2*h**2), 'd_B': 1e-3/(2*h**2)}

tau = .2 # time interval
N_t = 1_00_000  # number of units of time

X_A, X_B = sim.initialize_picture(m, n, A_init, B_init)

# Loop through time
for t in np.arange(N_t-1):
    if t % 100_000 == 0:
        print(t)
    X_A, X_B = sim.calculate_picture(tau, X_A, X_B, **params)

fig, ax1 = plt.subplots()
ax1.plot(X_A[0, :], label = 'A')
ax2 = ax1.twinx()
ax2.plot(X_B[0,:], label = 'B', linestyle = 'dashed', color = 'r')
plt.show()
#plt.imshow(X_A)
#plt.show()
plt.imshow(X_B)
plt.show()