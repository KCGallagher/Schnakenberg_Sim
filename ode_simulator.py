""" Solves time dependant ODE model without spatial variation
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

N_STEPS = int(1e3)
STEP_SIZE = 0.01
INITIAL_COND = [0,1]  # Starting value of [A, B]
A_PROD, B_PROD = 1, 1  # Initial production rates


t_span = np.linspace(0, N_STEPS * STEP_SIZE, N_STEPS)
# t_eval = t_span[1: -2]
# print(t_span)
# print(t_eval)

def ode_schnakenberg(t, y):
    """Derivatives to be called into solve_ivp
    
    This returns an array of derivatives y' = [A', B'], for a given
    state [A, B] at a time t. This is based on the classical 
    Schnakenberg system.

    Params:
    t [float] - the time at which the derivative is evaluated
    y [array] - the current state of the system, in the form [A, B]
    """

    return [y[0]**2 * y[1] - y[0] + A_PROD, -y[0]**2 * y[1] + B_PROD ]

solution = solve_ivp(ode_schnakenberg, 
                     t_span = (0, N_STEPS * STEP_SIZE), 
                     t_eval = t_span,
                     y0 = INITIAL_COND,
                     method = 'RK45',
                     dense_output=True)

plt.plot(solution.t, solution.y[0], label = 'A')
plt.plot(solution.t, solution.y[1], label = 'B')
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Concentration (arbitrary units)')
plt.title('Schnakenberg System - Time Evolution')
plt.legend()
plt.show()

print(solution.t)
print(len(solution.y[0]))