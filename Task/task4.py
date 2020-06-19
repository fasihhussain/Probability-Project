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

def task4(n, p):
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
        dist = np.random.uniform(-1, 1)
        turtle.forward(dist)
        i+=1

    return turtle.pos()[0]

lst = list()
val = 0

for i in range(10000):
    val = task4(100, [1/3,1/3,1/3])
    lst.append(val)

lst = sorted(lst)

fit = stats.norm.pdf(lst, np.mean(lst), np.std(lst))  #this is a fitting indeed

pl.plot(lst,fit,'-o')

pl.hist(lst,normed=True)      #use this to draw histogram of your data

pl.show()