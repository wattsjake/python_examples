import numpy as np
import matplotlib.pyplot as plt

#the will return the count of points in the circle
def pts_circle(x,y,r):
    count = 0
    for i in range(points):
        if(x[i]**2+y[i]**2 <= r**2):
            count += 1
    return count

#set aspect ratio
plt.figure(figsize=(7,7)) #fig size same as before
ax = plt.gca() #you first need to get the axis handle
ax.set_aspect(1) #sets the height to width ratio to 1. 
#Use help(ax.set_aspect) for more options.

points = 500
mu = 0
sig = 0.2

#create the arrays for holding the points
ptx = np.zeros(points)
pty = np.zeros(points)

#create the random points for the simulation
# for i in range(points):
#     #x,y = np.random.uniform(-1,1,size=None),np.random.uniform(-1,1,size=None)
#     x,y = np.random.normal(mu,sig),np.random.normal(mu,sig) #not used for estimating pi
#     ptx[i] = x
#     pty[i] = y
  
ptx = np.random.uniform(-1,1,size=points)
pty = np.random.uniform(-1,1,size=points)

    
#create the circle data
theta = np.linspace(0, 2*np.pi, 1000)
r = np.sqrt(1)
x1 = r*np.cos(theta)
x2 = r*np.sin(theta)

#find how many points are in the circle
pts_cir = pts_circle(ptx, pty, r)





plt.scatter(ptx, pty,5,label='Points in Circle %.0f'%pts_cir)

plt.xlim(-1.05, 1.05);
plt.ylim(-1.05, 1.05);
plt.plot(x1,x2,'r')
plt.legend(loc='upper right')
#plt.box(False)
#plt.savefig('random_points.png')
plt.show()


pi = pts_cir*4/points

print('pi: %10f' %pi)


