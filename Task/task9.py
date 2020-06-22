import numpy as np
import math
import random
import turtle

canvas = turtle.getcanvas()  # or, equivalently: turtle.getcanvas()
root = canvas.winfo_toplevel()

def on_close():
    global RUNNING
    RUNNING = False

root.protocol("WM_DELETE_WINDOW", on_close)

RUNNING = True

sop = False
first_node = True
nodes = True
i = 0
lst = []
healthy = []
immune = []
while nodes:

    lst.insert(0, turtle.Turtle())
    healthy.insert(0, lst[0])
    lst[0].shape('circle')
    lst[0].resizemode("user")
    lst[0].shapesize(0.2,0.2,1)
    lst[0].speed(0)
    lst[0].color('black')
    lst[0].penup()

    if first_node:
        lst[0].goto(0, -350)
        lst[0].circle(350)
        lst[0].goto(0, 0)
        lst[0].pendown()
        first_node = False

    else:
        rand_node = np.random.random_integers(0, len(lst)-1)
        x, y = lst[rand_node].pos()[0], lst[rand_node].pos()[1]
        lst[0].goto(x, y)
        lst[0].seth(np.random.uniform(0, 360))
        if sop:
            lst[0].forward(50*3.5)
        else:
            lst[0].forward(5*3.5)

        lst[0].pendown()

    if i == 10:
        nodes = False

    i += 1

sick = []
rand_node = np.random.random_integers(0, len(lst)-1)
lst[rand_node].color('red')
sick.append((lst[rand_node], 0))
healthy.pop(rand_node)


while RUNNING:
    
    i+=1

    for node in lst:
        direct = np.random.random_sample()*2*math.pi
        dist = 3.5 * np.random.random_sample()
        
        node.seth((direct*180)/math.pi)
        node.penup()
        node.forward(dist)
        node.pendown()

        if node in healthy and node not in immune:
            x,y = node.pos()[0], node.pos()[1]

            for s, t in sick:
                s_x, s_y = s.pos()[0], s.pos()[1]
                if abs(math.sqrt((x - s_x)**2 + (y - s_y)**2)) <= 3.5:
                    node.color('red')
                    sick.append((node, 0))
                    healthy.remove(node)
                    break

    for s, t in sick:

        i = sick.index((s,t))

        if t >= 10:

            mortality = np.random.random_integers(1, 100)

            if mortality == 1 or mortality == 2:
                s.hideturtle()
                lst.remove(s)
                sick.pop(i)

            else:
                s.color('blue')
                sick.pop(i)
                immune.append(s)

        else:
            sick[i] = (s, t+1)

    if i == 1000:
        break
    
    
