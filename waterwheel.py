#Malkus chaotic waterwheel



import numpy as np
import matplotlib.pyplot as plt

M = 10

theta = 0
#gravity (m/s)
g = 9.8
#wheel radius (m)
r = 2
#leakage rate (vol/s)
K = 2
#rotational damping rate (?)
v = 5
#moment of inertia of wheel
I = M*pow(r,2)
#number of steps 
N = 50
#angular velocity
omega = 4

q1 = 10


#Prandtl number
sigma = v/(K*I)
#Rayleigh number

def rayleigh(q1,v):
    return (np.pi*g*r*q1)/(pow(K,2)*v)

def checkRayleigh(a):
    if a > 1:
        c =  'Positive: Steady rotation.'
    if a == 0:
        c = 'Zero: No rotation'
    if a < 1:
        c = 'Negative: No fixed point'

R = rayleigh(q1,v)

print(checkRayleigh(R))

#b (nameless)
b = 1

def xp(x,y):
    return sigma*(y-x)

def yp(x,y,z):
    return R*x-y-x*z

def zp(x,y,z):
    return x*y - b*z


# def fxn(x,y,z):
#     a = xp(x,y)
#     b = yp(x,y,z)
#     c = zp(x,y,z)
#     return np.array([x,y,z])

def fxn(x):
    return xp(x)


#RK4 my beloved

h = 1/N
x = 10
y = 3
z = 2
u = np.array([x,y,z])
uhold = []
xhold = []
yhold = []
zhold = []

i = 0

while i <= N:

    k1 = h*xp(x,y)
    l1 = h*yp(x,y,z)
    g1 = h*zp(x,y,z)


    k2 = h*xp(x+(1/2)*k1,y+(1/2)*l1)
    l2 = h*yp(x+(1/2)*k1,y+(1/2)*l1,z+(1/2)*g1)
    g2 = h*zp(x+(1/2)*k1,y+(1/2)*l1,z+(1/2)*g1)
    
    k3 = h*xp(x+(1/2)*k2,y+(1/2)*l2)
    l3 = h*yp(x+(1/2)*k2,y+(1/2)*l2,z+(1/2)*g2)
    g3 = h*zp(x+(1/2)*k2,y+(1/2)*l2,z+(1/2)*g2)
    
    k4 = h*xp(x+k3,y+l3)
    l4 = h*yp(x+k3,y+l3,z+g3)
    g4 = h*zp(x+k3,y+l3,z+g3)

    xn = x + (1/6)*(k1+ 2*k2+2*k3+k4)
    yn = y + (1/6)*(l1+ 2*l2+2*l3+l4)
    zn = z + (1/6)*(g1+ 2*g2+2*g3+g4)

    xhold.append(xn)
    yhold.append(yn)
    zhold.append(zn)

    

    x = xn
    y = yn
    z = zn

    i+=h


fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot3D(xhold,yhold,zhold)
ax.set_xlabel('Time')
ax.set_ylabel('Position')
ax.set_title('Malkus waterwheel')
plt.show()

