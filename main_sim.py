"""
Runs simulation of time dependant ODE model"""

import numpy as np
import matplotlib.pyplot as plt
from ode_simulator import solve_schnakenberg

if __name__ == '__main__':
    N_STEPS = int(1e3)
    STEP_SIZE = 0.005
    INITIAL_COND = [0,1]  # Starting value of [A, B]
    A_PROD, B_PROD = 1, 1  # Initial production rates

    t_steps = np.linspace(0, N_STEPS * STEP_SIZE, N_STEPS)

    t_values, state_values = solve_schnakenberg(t_max  = N_STEPS * STEP_SIZE,
                                                y_init = INITIAL_COND,
                                                rates = [A_PROD, B_PROD],
                                                t_eval = t_steps)

    plt.plot(t_values, state_values[0], label = 'A')
    plt.plot(t_values, state_values[1], label = 'B')
    plt.xlabel('Time (arbitrary units)')
    plt.ylabel('Concentration (arbitrary units)')
    plt.title('Schnakenberg System - Time Evolution')
    plt.legend()
    plt.savefig('Images/Schnakenberg_time_evolution.png')
    plt.show()