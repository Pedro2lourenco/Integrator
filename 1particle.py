import numpy as np
from numpy import sin,cos,log,sqrt,square
import matplotlib.pyplot as plt

U = 20

a = 1

emax = 2*U*(1+a)

px = sqrt(2*emax)
py = 0
x = 0
y = 0

h=0.5


def K(PX,PY):
    return (PX*PX)+(PY*PY)

def V(X,Y):
    return U*(square(cos(X))+square(cos(Y))-2*a*cos(X)*cos(Y))

def H(K,V):
    return K+V

def evolveQ(X,Y,PX,PY,delta):
    X += PX*delta
    Y += PY*delta
    
    return (X,Y)

def evolveP(X,Y,PX,PY,delta):
    
    Fx = U*(2*cos(X)*sin(X)+2*a*cos(Y)*sin(X))
    Fy = U*(2*cos(Y)*sin(Y)+2*a*cos(Y)*sin(X))
    
    PX += Fx*delta
    PY += Fy*delta
    
    return (PX,PY)
    
    
s = 1/(4-4**(1/3))

delta1 = h*s

delta2 = 0.5*(h*s)

delta3 = 0.5*h*(1-(3*s))

delta4 = (1-(4*s))*h
    
def Suzuki4(X,Y,PX,PY):
    
    evolveQ(X,Y,PX,PY,delta2)
    evolveP(X,Y,PX,PY,delta1)
    evolveQ(X,Y,PX,PY,delta1)
    evolveP(X,Y,PX,PY,delta1)
    evolveQ(X,Y,PX,PY,delta3)
    evolveP(X,Y,PX,PY,delta4)
    evolveQ(X,Y,PX,PY,delta3)
    evolveP(X,Y,PX,PY,delta1)
    evolveQ(X,Y,PX,PY,delta1)
    evolveP(X,Y,PX,PY,delta1)
    evolveQ(X,Y,PX,PY,delta2)
    
    return(X,Y,PX,PY)

time = np.arange(0,1000,h)

for i in range(len(time)):
    
    x,y,px,py = Suzuki4(x,y,px,py)
    plt.scatter(x,y)
    
    plt.show()