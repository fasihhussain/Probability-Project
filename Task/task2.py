import numpy as np
import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.shape("circle")
t1.resizemode("user")
t1.shapesize(0.2,0.2,1)
t1.speed(10)

t2.shape("circle")
t2.resizemode("user")
t2.shapesize(0.2,0.2,1)
t2.speed(0)
t2.color("red")

canvas = turtle.getcanvas()  # or, equivalently: turtle.getcanvas()
root = canvas.winfo_toplevel()

def on_close():
    global RUNNING
    RUNNING = False

RUNNING = True

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
    t2.penup()
    t2.goto(x,0)
    t2.pendown()
    i = 0
    while x1 != x2:
        r1 = np.random.choice([-1, 0, 1], p = p1)
        r2 = np.random.choice([-1, 0, 1], p = p2)
        x1 += r1
        x2 += r2
        t1.forward(r1)
        t2.forward(r2)
        i += 1
    return i

p = [0.33, 0.33, 0.34]
lst = list()

for i in range(10000):
    val = task2(100, p, p))
    lst.append(val)

