from matplotlib import pyplot as plt
import numpy as np
import turtle
import math

turtle.shape("circle")
turtle.resizemode("user")
turtle.shapesize(0.2,0.2,1)
turtle.speed(0)
canvas = turtle.getcanvas()  # or, equivalently: turtle.getcanvas()
root = canvas.winfo_toplevel()

def on_close():
    global RUNNING
    RUNNING = False

RUNNING = True

def task1(n, p):
    """This function returns the displacement from initial point after n steps
    
    Args:
    - n: number of steps
    - p: probabilities as an array [move left, no move, move right]
    
    Returns:
    The displacement after n steps as an integer.
    """
    turtle.goto(0,0)
    i=0
    while i<n and RUNNING:
        dist = 3.5 * (np.random.choice([-1,0,1]))
        turtle.forward(dist)
        i+=1 
    return turtle.pos()[0]

lst = list()
val = 0
summation = 0
for i in range(10000):
    val = task1(10000, ["move left", "no move", "move right"])
    lst.append(val)
    summation += val

avg = summation/10000

print(avg)

x = np.arange(1,10000) 

plt.plot(x lst)


plt.plot(lst)

plt.show()