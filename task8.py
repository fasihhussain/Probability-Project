import numpy as np
import math
import random
import turtle

def move(turtle,dist,angle=None,turn=None):
    if turn != None:
        turtle.seth(turn+turtle.heading())
    else:
        turtle.seth(angle)
    turtle.forward(dist)

def pm(x,y):
    return (x+y,x-y)

def Boundary_Handle(turtle,x1,x2,y1,y2, direct, dist):
    dx = x2 - x1
    dy = y2 - y1
    dr = math.sqrt(dx**2 + dy**2)
    D = x1*y2 - x2*y1
    if dr == 0:
        return x2,y2,face
    # print("Boundary")
    # print("x1,x2,y1,y2",x1,x2,y1,y2)
    # print("detr =",(350**2) * (dr**2) - D**2)
    # print("dr, D", dr,D)
    _x, x_= tuple(w/dr**2 for w in pm(D*dy,(-1 if dy < 0 else 1)*dx*(math.sqrt((350**2) * (dr**2) - D**2))))
    _y, y_= tuple(w/dr**2 for w in pm(-D*dx, abs(dy)*(math.sqrt((350**2) * (dr**2) - D**2))))
    x,y = close_to_circle(_x,x_,_y,y_, x2, y2)
    if (x,y) == (x2,y2):         
        dist = 3.5 * np.random.random_sample()
        # print(dist,direct)
        print("Point on Circle")
        move(turtle, dist,turn=(math.pi-direct)*180/math.pi)
        return
    vec_to = (x-x2,y-y2)
    angle = math.acos((vec_to[0]*x+vec_to[1]*y)/(math.sqrt(vec_to[0]**2+vec_to[1]**2)*math.sqrt(x**2+y**2)))
    # print(angle)
    turtle.seth(direct*180/math.pi)
    turtle.setpos(x,y)
    # print(x,y)
    dist = 3.5 * np.random.random_sample()
    if math.sqrt((x+dist*math.cos(math.pi-2*angle))**2 + (y+dist*math.sin(math.pi-2*angle))**2) == 350:
        move(turtle, dist,turn=(math.pi-direct)*180/math.pi)
        print("Point on circle 2")
    elif math.sqrt((x+dist*math.cos(math.pi-2*angle))**2 + (y+dist*math.sin(math.pi-2*angle))**2) > 350:
        print("Point outside circle")
        Boundary_Handle(turtle, x + dist*math.cos(math.pi-2*angle),x,y+dist*math.sin(math.pi-2*angle),y, direct, dist)
    else:
        move(turtle, dist,turn=(math.pi-2*angle)*180/math.pi)
        x2,y2 = turtle.position()

    # print(turtle.position(),math.sqrt(x2**2+y2**2))

def close_to_circle(t1, t2, s1, s2, x2, y2):
    dis1 = math.sqrt((t1-x2)**2+(s1-y2)**2)
    dis2 = math.sqrt((t1-x2)**2+(s2-y2)**2)
    dis3 = math.sqrt((t2-x2)**2+(s1-y2)**2)
    dis4 = math.sqrt((t2-x2)**2+(s2-y2)**2)
    mini = min(dis1,dis2,dis3,dis4)
    if mini == dis1:
        return t1,s1
    elif mini == dis2:
        return t1,s2
    elif mini == dis3:
        return t2,s1
    elif mini == dis4:
        return t2,s2

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.shape("circle")
t1.resizemode("user")
t1.shapesize(0.2,0.2,1)
t1.speed(0)
t1.color('black')

t2.shape("circle")
t2.resizemode("user")
t2.shapesize(0.2,0.2,1)
t2.speed(0)
t2.color('red')

canvas = turtle.getcanvas()  # or, equivalently: turtle.getcanvas()
root = canvas.winfo_toplevel()

def on_close():
    global RUNNING
    RUNNING = False

root.protocol("WM_DELETE_WINDOW", on_close)

RUNNING = True

t1.penup()
t1.sety(-350)
t1.pendown()
t1.circle(350)
t1.penup()

# radius of the circle
circle_r = 350
# center of the circle (x, y)
circle_x = 0
circle_y = 0

# random angle
alpha1 = 2 * math.pi * np.random.random_sample()
alpha2 = 2 * math.pi * np.random.random_sample()
# random radius
r1 = circle_r * math.sqrt(np.random.random_sample())
r2 = circle_r * math.sqrt(np.random.random_sample())
# calculating coordinates
t1.goto(r1 * math.cos(alpha1) + circle_x, r1 * math.sin(alpha1) + circle_y)

t2.penup()

t2.goto(r1 * math.cos(alpha2) + circle_x, r2 * math.sin(alpha2) + circle_y)

t1.pendown()
t2.pendown()

i = 0

t1_x2 = r1 * math.cos(alpha1) + circle_x
t1_y2 = r1 * math.sin(alpha1) + circle_y

t2_x2 = r2 * math.cos(alpha2) + circle_x
t2_y2 = r2 * math.sin(alpha2) + circle_y

while RUNNING:
    
    i+=1

    direct1 = np.random.random_sample()*2*math.pi
    direct2 = np.random.random_sample()*2*math.pi

    dist1 = 3.5 * np.random.random_sample()
    dist2 = 3.5 * np.random.random_sample()

    t1_x1, t1_y1 = t1_x2 + dist1*math.cos(direct1), t1_y2 + dist1*math.sin(direct1)
    t2_x1, t2_y1 = t2_x2 + dist2*math.cos(direct2), t2_y2 + dist2*math.sin(direct2)

    if math.sqrt((t1_x2 - t1_x1)**2 + (t1_y2 - t1_y1)**2) == 0:
        continue
    if math.sqrt((t2_x2 - t2_x1)**2 + (t2_y2 - t2_y1)**2) == 0:
        continue

    if math.sqrt(t1_x1**2 + t1_y1**2) >= 350:
        Boundary_Handle(t1, t1_x1, t1_x2, t1_y1, t1_y2, direct1, dist1)
        t1_x2, t1_y2 = t1.position()
        continue
    if math.sqrt(t2_x1**2 + t2_y1**2) >= 350:
        Boundary_Handle(t2, t2_x1, t2_x2, t2_y1, t2_y2, direct2, dist2)
        t2_x2, t2_y2 = t2.position()
        continue

    move(t1, dist1, angle = direct1*180/math.pi)
    move(t2, dist2, angle = direct2*180/math.pi)
    print(math.sqrt((t1_x1 - t2_x1)**2 + (t1_y1 - t2_y1)**2))
    if i == 10000 or math.sqrt((t1_x1 - t2_x1)**2 + (t1_y1 - t2_y1)**2) <= 3.5:
        break

    t1_x2, t1_y2 = t1_x1, t1_y1
    t2_x2, t2_y2 = t2_x1, t2_y1
    
# print(t1.position())

# turtle.exitonclick()
