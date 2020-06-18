import numpy as np
import turtle
import math

turtle.shape("circle")
turtle.resizemode("user")
turtle.shapesize(0.2,0.2,1)
turtle.speed(10)
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
    i=0
    while i<n and RUNNING:
        dist = 3.5 * (np.random.choice([-1,0,1]))
        print(dist)
        turtle.forward(dist)
        i+=1 
    return sum(np.random.choice([-1, 0, 1], n, p=p))

task1(10000,["move left", "no move", "move right"])