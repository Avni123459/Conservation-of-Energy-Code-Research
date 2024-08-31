import math
from matplotlib import pyplot as plt 

# User Input for Initial Velocity, Angle that object is projected at and the Mass of object
u=int(input('Enter the initial velocity: '))
angle=(int(input('Enter the angle of projection: ')))
mass=int(input('Enter the mass of the object: '))

# Value of Gravity constant
g=9.81

# Calcute Initial Velocity in the vertical and horizontal vector
horizontal_velocity=u*math.cos(math.radians(angle))
vertical_initial_velocity=u*math.sin(math.radians(angle))

# Calculate time using v=u+at equation 
t=int(2*vertical_initial_velocity)/(g)
height =(vertical_initial_velocity*t)-(0.5*g*(t*t))
print('Height: ', height)



import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from numpy import *

plt.xlabel('Time (s)')
plt.ylabel('Energy (J)')
plt.title('Projectile Motion Conservation of Energy')
x=linspace(0,t,5000)
y=((0.5*mass*g*g)*x**2)-((mass*g*(vertical_initial_velocity))*x)+(0.5*mass*u*u)
y1=(-1*(0.5*mass*g*g)*x**2)+((mass*g*(vertical_initial_velocity))*x)
initial=0.5*mass*u*u
plt.axhline(y=initial, xmin=0.048, color='green', label='Total Energy')
plt.plot(x,y, label='KE')
plt.plot(x,y1, label='GPE')
plt.legend()
fig, ax=plt.subplots()
ax.set_ylim(0)
plt.show()

