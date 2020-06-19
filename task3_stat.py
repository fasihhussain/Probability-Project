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



def task3_stat(n):
    circle_r = 350
    # center of the circle (x, y)
    circle_x = 0
    circle_y = 0

    # random angle

    t1_x2 = 0 
    t1_y2 = 0

    face1 = 0

    i=0

    while i<n:

        direct1 = np.random.random_sample()*2*math.pi

        dist1 = 3.5 * np.random.random_sample()

        t1_x1, t1_y1 = t1_x2 + dist1*math.cos(direct1), t1_y2 + dist1*math.sin(direct1)

        if math.sqrt((t1_x2 - t1_x1)**2 + (t1_y2 - t1_y1)**2) == 0:
            continue

        if math.sqrt(t1_x1**2 + t1_y1**2) >= 350:
            t1_x1, t1_y1, face1 = Boundary_Handle(t1_x1, t1_x2, t1_y1, t1_y2, direct1, dist1, face1)
            t1_x2, t1_y2 = t1_x1, t1_y1
            continue
        
        i+=1

    return math.sqrt(t1_x2**2 + t1_y2**2)

lst= list()
for i in range(10000):
    lst.append (task3_stat(1000))


lst = sorted(lst)

fit = stats.norm.pdf(lst, np.mean(lst), np.std(lst))  #this is a fitting indeed

pl.plot(lst,fit,'-o')

pl.hist(lst,normed=True)      #use this to draw histogram of your data

pl.show()

ans="\n".join(lst)
output_file = open("task3.txt", "w")
output_file.write(ans)
output_file.close()