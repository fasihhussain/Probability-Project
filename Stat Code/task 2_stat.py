  
import numpy as np

def task2(x, p1, p2):
    """This function returns the time/steps after which subjects meet
    
    Args:
    - x: initial distance between subject 1 and 2
    - p1: probabilities of subject 1 as an array [move left, no move, move right]
    - p2: probabilities of subject 2 as an array [move left, no move, move right]
    
    Returns:
    The time/steps after which subjects meet as an integer.
    """
    x1 = 0
    x2 = abs(x)
    i = 0
    while x1 != x2:
        x1 += np.random.choice([-1, 0, 1], p = p1)
        x2 += np.random.choice([-1, 0, 1], p = p2)
        i += 1
    return i

p = [1/3, 1/3, 1/3]
for x in range(18,19):
    n=0
    for i in range(50):
        n+=task2(x, p, p)
        # print(i)
    print(x,":",n/50)