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

lst=[]
for x in range(10000):
    lst.append(str(task1(1000, [3/6, 2/6, 1/6])))
ans="\n".join(lst)
output_file = open("D:\\Test\\l_result_unequal2.txt", "w")
output_file.write(ans)
output_file.close()