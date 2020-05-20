import numpy as np

def task1(n, p):
    """This function returns the displacement from initial point after n steps
    
    Args:
    - n: number of steps
    
    Returns:
    The displacement after n steps as an integer.
    """
    return sum(np.random.uniform(0, 1, n))
