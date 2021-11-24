import numpy as np

def birth(tau, M, c):
    """
    Get the change in number of molecules to each cell of matrix M 
    by birth,
    the propensity in each cell is 
    c
    """
    
    # Get the propensity 
    P = c

    # Get the change (positive cause of birth)
    Z = np.random.poisson(lam=tau*P, size=M.shape)
    
    return Z


def die(tau, M, c):
    """
    Get the change in number of molecules to each cell of matrix M 
    by death,
    the propensity in cell i is
    c * M_i
    """

    # Get the propensity
    P = c * M

    # Get the change (negative cause of death)
    Z = -1 * np.random.poisson(lam=tau*P)
    
    return Z


def react(tau, M_A, M_B, c):
    """
    Get the change in number of molecules to each cell of matrices
    M_A and M_B, respectively
    by the reaction of species A and B according to the equation:
    2A + B -> 3A
    where the propensity in cell i is
    c * M_A_i * (M_A_i - 1) * M_B_i
    """
    

    # Get the propensity
    P = c * M_A * (M_A - 1) * M_B

    # Get the change
    Z = np.random.poisson(lam=tau*P)
    
    # The change is plus one for A and minus one for B
    Z_A = 1 * Z
    Z_B = -1 * Z
    
    return Z_A, Z_B


def diffuse(tau, M, d):
    """
    Get the change in number of molecules to each cell of matrix M 
    by diffusion in each of four directions,
    the propensity in cell i is
    d * M_i
    """
    
    # Get the matrix of propensity functions (for each cell)
    P  = d * M
    
    # Get the amount diffused in each of four directions
    Ds = np.random.poisson(lam=tau*P, size=(4,) + M.shape)
    
    # Zero matrix (for calculating difference vector)
    Z = np.zeros(shape=M.shape)
    
    ### 1. Take from top of matrix and give to bottom of matrix 
    # Make D equal to all of first of Ds except bottom row
    D = Ds[0]  # grab first direction (down)
    D = D[:-1,:]  # get top (index all except bottom row)
    Z[:-1,:] -= D  # subtract from top
    Z[1:,:] += D  # add to bottom

    ### 2. Take from bottom of matrix and give to top of matrix  
    # Make D equal to all of second of Ds except top row
    D = Ds[1]  # grab second direction (up)
    D = D[1:,:]  # grab bottom (index all except top row)
    Z[1:,:] -= D  # subtract from bottom
    Z[:-1,:] += D  # add to top

    ### 3. Take from left of matrix and give to right of matrix
    D = Ds[2]  # grab third direction (right)
    D = D[:,:-1]  # grab left
    Z[:,:-1] -= D  # subtract from left
    Z[:,1:] += D  # add to right

    ### 4. Take from right of matrix and give to left of matrix
    D = Ds[3]  # grab fourth direction (left)
    D = D[:,1:]  # grab right
    Z[:,1:] -= D  # subtract from right
    Z[:,:-1] += D  # add to left
    
    return Z


def calculate(tau, X_A, X_B, t, mu, beta, alpha, kappa, d_A, d_B):
    """
    Calculate the number of molecules in each cell of the A and B grids
    for time t+1.
    """
    
    # Birth
    Z_A_birth = birth(tau, M=X_A[t], c=mu)
    Z_B_birth = birth(tau, M=X_B[t], c=beta)


    # Die
    Z_A_death = die(tau, M=X_A[t], c=alpha)


    # React
    Z_A_react, Z_B_react = react(tau, X_A[t], X_B[t], c=kappa)


    # Diffuse
    Z_A_diffusion = diffuse(tau, M=X_A[t], d=d_A)
    Z_B_diffusion = diffuse(tau, M=X_B[t], d=d_B)
    
    
    # Calculate next grid
    X_A[t+1] = X_A[t] + Z_A_birth + Z_A_death + Z_A_react + Z_A_diffusion
    X_B[t+1] = X_B[t] + Z_B_birth + Z_B_react + Z_B_diffusion
