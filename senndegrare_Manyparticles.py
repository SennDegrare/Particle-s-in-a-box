from vpython import *
#Web VPython 3.2

e_graph = gcurve(color=color.blue)


nop = 40 #density of our medium

#close interaction repulsion force
def nforce(p1,p2):
    r_vec = p1.pos - p2.pos
    
    force_vec = vector(0,0,0)
    
    b=6*p1.radius
    u = 1000
    #close repulsion
    if mag(r_vec)<b:
        vec = u*r_vec
        vec.z = 0
        force_vec = vec
    return force_vec
    
#Force of gravity
def gforce():
    force_mag = 0
    force_hat = vector(0,-1,0)
    force_vec = force_mag*force_hat
    return force_vec
    
#Walls of our box    
def xwall (p):
    posn = p.pos.x
    
    if posn>=10 or posn<=-10:
        p.momentum.x=-p.momentum.x
    return p.momentum
    
def ywall (p):
    posn = p.pos.y
    
    if posn<=-10 or posn>=10:
        p.momentum.y=-p.momentum.y
    return p.momentum


#Particle array
parr = []



for i in range(nop):
    p=sphere(pos=10*vector.random(), radius=0.3,
               mass = 10, momentum=5*vector.random(), make_trail=False)
    p.momentum.z = 0
    p.pos.z = 0
    parr.append(p)
    
#Interaction matrix
intearr = [[0 for i in range(nop)] for j in range(nop)]


wx1 = box(pos=vector(10.1,0,0), length=0.1, width=0, height=20.1)
wx2 = box(pos=vector(-10.1,0,0), length=0.1, width=0, height=20.1)
wx3 = box(pos=vector(0,10.1,0), length=20.1, width=0, height=0.1)
wx4 = box(pos=vector(0,-10.1,0), length=20.1, width=0, height=0.1)

dt = 0.001
t=0

while True:
    rate(5000)
    
    for i in range(nop):
        for j in range(nop):
           intearr[i][j]=nforce(parr[i],parr[j])
    
    
    netforce=[]
    
    for i in range(nop):
        sum=vector(0,0,0)
        for j in range(nop):
            sum=sum+intearr[i][j]
        netforce.append(sum)
        
        parr[i].momentum=xwall(parr[i])
        parr[i].momentum=ywall(parr[i])
    
    for i in range(nop):
        parr[i].force = gforce()+netforce[i]
        parr[i].momentum = parr[i].momentum+parr[i].force*dt
        parr[i].pos = parr[i].pos+parr[i].momentum/parr[i].mass*dt
        
    
    
    
    t = t + dt