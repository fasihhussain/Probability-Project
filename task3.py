import math
import numpy as np
import turtle

turtle.shape("circle")
turtle.resizemode("user")
turtle.shapesize(0.2,0.2,1)
# circle = turtle.Turtle()
canvas = turtle.getcanvas()  # or, equivalently: turtle.getcanvas()
root = canvas.winfo_toplevel()

def on_close():
    global RUNNING
    RUNNING = False

root.protocol("WM_DELETE_WINDOW", on_close)

RUNNING = True

turtle.penup()
turtle.goto(0,-350)
turtle.pendown()
turtle.circle(350)
turtle.penup()
turtle.goto(345,0)
turtle.pendown()
turtle.ht()
i = 0

def pm(x,y):
    return (x+y,x-y)

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

x2,y2 = 345,0
turtle.speed(10)
while RUNNING:
    
    i+=1
    # direct = np.random.random_sample()* 2 * math.pi
    direct = (np.random.random_sample()*4//1)*math.pi*0.5
    dist = 1.75 * (np.random.random_sample()//(1/3))
    x1,y1 = x2+dist*math.cos(direct),y2+dist*math.sin(direct)
    # print(direct*180/math.pi)
    dx = x2 - x1
    dy = y2 - y1
    dr = math.sqrt(dx**2 + dy**2)
    # print(math.sqrt(x1**2 + y1**2))
    if math.sqrt(x1**2 + y1**2) >= 350 and dr>0:
        print("Boundary")
        D = x1*y2 - x2*y1
        print(x1,x2,y1,y2)
        print("detr =",(350**2) * (dr**2) - D**2))
        print(dr,D,dist)
        _x, x_= tuple(w/dr**2 for w in pm(D*dy,(-1 if dy < 0 else 1)*dx*(math.sqrt((350**2) * (dr**2) - D**2))))
        _y, y_= tuple(w/dr**2 for w in pm(-D*dx, abs(dy)*(math.sqrt((350**2) * (dr**2) - D**2))))
        x,y = close_to_circle(_x,x_,_y,y_)
        if (x,y) == (x2,y2):         
            dist = 1.75 * (np.random.random_sample()//(1/3))
            turtle.right((math.pi-direct)*180/math.pi)
            turtle.forward(dist)
            continue
        vec_to = (x-x2,y-y2)
        angle = math.acos((vec_to[0]*x+vec_to[1]*y)/(math.sqrt(vec_to[0]**2+vec_to[1]**2)*math.sqrt(x**2+y**2)))
        print(angle)
        turtle.seth(direct*180/math.pi)
        turtle.setpos(x,y)
        print(x,y)
        dist = 1.75 * (np.random.random_sample()//(1/3))
        turtle.right((math.pi-2*angle)*180/math.pi)
        turtle.forward(dist)
        x2,y2 = turtle.position()
        continue
        
    turtle.seth(direct*180/math.pi)
    turtle.forward(dist)
    if i == 10000:
        break
    x2,y2 = x1,y1
    # print(i)

    

turtle.exitonclick()