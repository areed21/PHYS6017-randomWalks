"""
Animating random walks in 3D
Inspired by code from https://matplotlib.org/3.1.1/gallery/animation/random_walk.html

To view animation in IDLE use "%matplotlib qt" in console9
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from math import pi,sin,cos,sqrt

nsteps =  100         #number of steps each particle takes
nwalks =  50          #number of particles going for a walk

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

def randwalk(length):
    """
    Generates a random walk for a particle taking a 
    number of steps (=length) of random length defined by phi, theta. 
    Returns the position of the particle (x,y,z) at each step.
    """
    x = y = z = 0              #start at origin
    X = [0]                    #record origin as 1st point
    Y = [0]
    Z = [0]
    for i in range(length):
        phi = 2*pi*np.random.uniform(0,1)       #generating a random azimuthal angle
        ctheta = 2*np.random.uniform(0,1)-1.0
        stheta = sqrt(1.0-ctheta*ctheta)
        x = x+(stheta*cos(phi))
        y = y+(stheta*sin(phi))
        z = z+ctheta
        X.append(x)
        Y.append(y)  
        Z.append(z)
    linedata = np.array([X,Y,Z])
    return linedata

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def refresh_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines


#attaching 3D axis to the figure
fig = plt.figure(figsize = (10,10))
ax = p3.Axes3D(fig)

#fifty lines of random 3-D lines
data = [randwalk(nsteps) for index in range(nwalks)]

#creating fifty line objects
#NOTE: Can't pass empty arrays into 3d version of plot()
lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

#setting the axes properties
limit = int(abs(np.amax(data)))+1        #setting the axes limit depending on the data    

ax.set_xlim3d([-limit, limit])
ax.set_xlabel('x axis')

ax.set_ylim3d([-limit, limit])
ax.set_ylabel('y axis')

ax.set_zlim3d([-limit, limit])
ax.set_zlabel('z axis')

ax.set_title('3D random walk of {} particles taking {} steps'.format(nwalks,nsteps))

#creating the animation object
anim = animation.FuncAnimation(fig, refresh_lines, nsteps, fargs=(data, lines),
                                   interval=nwalks, repeat=False, blit=False)

#rotating the graph through 180degrees
for angle in range(0, 180):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)

plt.show()

#saving animation as .mp4 file
"""  
dpi = 100
Writer = animation.FFMpegWriter()

anim.save('random-walk-animation.mp4', writer=Writer, dpi=dpi)
"""


