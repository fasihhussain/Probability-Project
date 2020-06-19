import numpy as np

def task4(n):
    """This function returns the displacement from initial point after n steps
    
    Args:
    - n: number of steps
    - p: probabilities as an array [move left, no move, move right]
    
    Returns:
    The displacement after n steps as an integer.
    """
    return sum(np.random.uniform(-1, 1, n))

lst=[]
for x in range(10000):
    lst.append(str(task4(1000)))
ans="\n".join(lst)
output_file = open("C:\\Users\\Fasih Hussain\\Documents\GitHub\\Probability-Project\\Results\\task4.txt", "w")
output_file.write(ans)
output_file.close()