import numpy as np

def task1(n, p):
    """This function returns the displacement from initial point after n steps
    
    Args:
    - n: number of steps
    - p: probabilities as an array [move left, no move, move right]
    
    Returns:
    The displacement after n steps as an integer.
    """
    return sum(np.random.choice([-1, 0, 1], n, p=p))
