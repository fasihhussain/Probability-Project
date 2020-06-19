from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as stats
import pylab as pl
import math


def Boundary_Handle(x1,x2,y1,y2, direct, dist,face):
    dx = x2 - x1
    dy = y2 - y1
    dr = math.sqrt(dx**2 + dy**2)
    D = x1*y2 - x2*y1
    if dr <= 0:
        return
    _x, x_= tuple(w/dr**2 for w in pm(D*dy,(-1 if dy < 0 else 1)*dx*(math.sqrt((350**2) * (dr**2) - D**2))))
    _y, y_= tuple(w/dr**2 for w in pm(-D*dx, abs(dy)*(math.sqrt((350**2) * (dr**2) - D**2))))
    x,y = close_to_circle(_x,x_,_y,y_, x2, y2)
    if (x,y) == (x2,y2):         
        dist = 3.5 * np.random.random_sample()
        q1,q2 = x2+dist*math.cos(face+(math.pi-direct)),y2+dist*math.sin(face+(math.pi-direct))
        return q1,q2,face+(math.pi-direct)
    vec_to = (x-x2,y-y2)
    angle = math.acos((vec_to[0]*x+vec_to[1]*y)/(math.sqrt(vec_to[0]**2+vec_to[1]**2)*math.sqrt(x**2+y**2)))
    x2,y2 = x, y
    dist = 3.5 * np.random.random_sample()
    if math.sqrt((x+dist*math.cos(math.pi-2*angle))**2 + (y+dist*math.sin(math.pi-2*angle))**2) == 350:
        x2,y2 = x2 + dist*math.cos(math.pi - direct), y2 + dist*math.cos(math.pi-direct)
    if math.sqrt((x+dist*math.cos(math.pi-2*angle))**2 + (y+dist*math.sin(math.pi-2*angle))**2) >= 350:
        return Boundary_Handle(turtle, x + dist*math.cos(math.pi-2*angle),x,y+dist*math.sin(math.pi-2*angle),y, direct, dist)
    else:
        x2,y2 = x2+dist*math.cos(face + math.pi-2*angle),y2+ dist*(face + math.pi-2*angle)
        face =face + math.pi-2*angle
        return x2, y2, face

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



def task8_stat():
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

    t1_x2 = r1 * math.cos(alpha1) + circle_x
    t1_y2 = r1 * math.sin(alpha1) + circle_y

    t2_x2 = r2 * math.cos(alpha2) + circle_x
    t2_y2 = r2 * math.sin(alpha2) + circle_y

    face1 = 0
    face2 = 0

    i=0

    while abs(math.sqrt((t1_x2 - t2_x2)**2 + (t1_y2 - t2_y2)**2)) > 3.5:

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
            t1_x1, t1_y1, face1 = Boundary_Handle(t1_x1, t1_x2, t1_y1, t1_y2, direct1, dist1, face1)
            t1_x2, t1_y2 = t1_x1, t1_y1
            continue
        if math.sqrt(t2_x1**2 + t2_y1**2) >= 350:
            t2_x1, t2_y1, face2 = Boundary_Handle(t2_x1, t2_x2, t2_y1, t2_y2, direct2, dist2, face2)
            t2_x2, t2_y2 = t2_x1, t2_y1
            continue

        if i%1000 == 0:
            print(i)
        i+=1

    return i

print(task8_stat())