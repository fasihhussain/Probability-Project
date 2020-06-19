import numpy as np
import math


def Boundary_Handle(x1,x2,y1,y2, direct, dist,face):
    dx = x2 - x1
    dy = y2 - y1
    dr = math.sqrt(dx**2 + dy**2)
    D = x1*y2 - x2*y1
    if dr == 0:
        return x2,y2,face
    if math.sqrt(x2**2+y2**2) > 350:
        x2,y2 = x2+dist*math.cos(math.pi - face),y2+ dist*(math.pi - face)
        face = math.pi-face
        return x2, y2, face
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
        return Boundary_Handle( x + dist*math.cos(math.pi-2*angle),x,y+dist*math.sin(math.pi-2*angle),y, direct, dist,face)
    else:
        x2,y2 = x2+dist*math.cos(face + math.pi-2*angle),y2+ dist*(face + math.pi-2*angle)
        face =face + math.pi-2*angle
        return x2, y2
    
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

def initialize():
    x=101
    y=101
    while x**2+y**2>10000:
        x=np.random.uniform(-100, 100)
        y=np.random.uniform(-100, 100)
    return x,y

def task8():
    x1, y1=initialize()
    x2, y2=initialize()
    i=0
    while ((x1-x2)**2+(y1-y2)**2)>1:
        dir1=np.random.uniform(0, 2*np.pi)
        dir2=np.random.uniform(0, 2*np.pi)
        d1=np.random.uniform(0, 1)
        d2=np.random.uniform(0, 1)
        x1 += (d1*np.cos(dir1))
        x2 += (d2*np.cos(dir2))
        y1 += (d1*np.sin(dir1))
        y2 += (d2*np.sin(dir2))
        i+=1
        if (x1**2+y1**2)>10000:
            x1=x1-d1*np.cos(dir1)
            y1=y1-d1*np.sin(dir1)
            # x1, y1 = Boundary_Handle(x1, y1, x_, y_, dir1, d1, np.atan((y1-y_)/(x1-x_)))
            # print("Out of bound 1")
        if (x2**2+y2**2)>10000:
            x2=x2-d2*np.cos(dir2)
            y2=y2-d2*np.sin(dir2)
            # x2, y2 = Boundary_Handle(x2, y2, x_, y_, dir2, d2, np.atan((y2-y_)/(x2-x_)))
            # print("Out of bound 2")
    return i

lst=[]
for x in range(200):
    print(x)
    lst.append(str(task8()))
ans="\n".join(lst)
print(ans)
output_file = open("C:\\Users\\Fasih Hussain\\Documents\GitHub\\Probability-Project\\Results\\task8.txt", "w")
output_file.write(ans)
output_file.close()