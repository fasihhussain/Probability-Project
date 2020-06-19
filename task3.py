import math
import numpy as np
import turtle

def move(dist,angle=None,turn=None):
    if turn != None:
        turtle.seth(turn+turtle.heading())
    else:
        turtle.seth(angle)
    turtle.forward(dist)

def pm(x,y):
    return (x+y,x-y)

def Boundary_Handle(x1,x2,y1,y2):
    # Change in Position
    dx = x2 - x1
    dy = y2 - y1
    dr = math.sqrt(dx**2 + dy**2)
    D = x1*y2 - x2*y1
    # Check if position has changed
    if dr<=0:
        return
    print("x1:",x1,"x2:",x2,"y1:",y1,"y2:",y2,"\ndx:",dx,"\ndy:",dy,"\nD:",D)
    _x, x_= tuple(w/dr**2 for w in pm(D*dy,(-1 if dy < 0 else 1)*dx*(math.sqrt((350**2) * (dr**2) - D**2))))
    _y, y_= tuple(w/dr**2 for w in pm(-D*dx, abs(dy)*(math.sqrt((350**2) * (dr**2) - D**2))))
    x,y = close_to_circle(_x,x_,_y,y_)
    if (x,y) == (x2,y2):         
        dist = 1.75 * (np.random.random_sample()//(1/3))
        move(dist,turn=(math.pi-direct)*180/math.pi)
    vec_to = (x-x2,y-y2)
    angle = math.acos((vec_to[0]*x+vec_to[1]*y)/(math.sqrt(vec_to[0]**2+vec_to[1]**2)*math.sqrt(x**2+y**2)))
    turtle.seth(direct*180/math.pi)
    turtle.setpos(x,y)
    dist = 1.75 * (np.random.random_sample()//(1/3))
    if math.sqrt((x+dist*math.cos(math.pi-2*angle))**2 + (y+dist*math.sin(math.pi-2*angle))**2) >= 350:
        Boundary_Handle(x+dist*math.cos(math.pi-2*angle),x,y+dist*math.sin(math.pi-2*angle),y)
    else:
        move(dist,turn=(math.pi-2*angle)*180/math.pi)
        x2,y2 = turtle.position()

def close_to_circle(t1,t2,s1,s2):
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

turtle.shape("circle")
turtle.resizemode("user")
turtle.shapesize(0.2,0.2,1)
canvas = turtle.getcanvas()  # or, equivalently: turtle.getcanvas()
root = canvas.winfo_toplevel()

def on_close():
    global RUNNING
    RUNNING = False

root.protocol("WM_DELETE_WINDOW", on_close)

RUNNING = True

turtle.speed(0)
turtle.penup()
turtle.goto(0,-350)
turtle.pendown()
turtle.circle(350)
turtle.penup()
turtle.goto(345,0)
turtle.pendown()
i = 0


x2,y2 = 345,0
while RUNNING:
    
    i+=1

    direct = (np.random.random_sample()*4//1)*math.pi*0.5
    dist = 1.75 * (np.random.random_sample()//(1/3))
    x1,y1 = x2+dist*math.cos(direct),y2+dist*math.sin(direct)
    
    if math.sqrt((x2-x1)**2 + (y2-y1)**2)==0:
        continue
    if math.sqrt(x1**2 + y1**2) >= 350:
        Boundary_Handle(x1,x2,y1,y2)
        x2,y2 = turtle.position()
        continue
        
    turtle.seth(direct*180/math.pi)
    turtle.forward(dist)
    if i == 1000:
        break
    x2,y2 = x1,y1
    
