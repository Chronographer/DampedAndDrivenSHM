# projectile (golf ball) with lift and drag
# June 26, 2007
# Chad Keefer
# convert to Vpython7
# Feb 2, 2020
# Antonio Cancio

"""The goals are to:
1) Realistically model the trajectory of a golf ball -- with a slice.

During flight, 3 forces act on a golf ball: gravity, lift, and drag. Gravity acts downward, drag acts opposite
the velocity, and the direction of the lift force varies with the direction of spin. In this model, lift due to
spin will act --nearly-- upward in the +y direction. There is a small deviation from vertical lift as might happen
if the golfer did not hit the ball squarely.  The force on the ball is therefore:


F = gravity + drag force + lift force       (<-- note that this is a *vector* equation --)


The force of gravity is:    F = mg          acting in the -y direction, where g is acceleration due to gravity

The drag force is:          F = 1/2pCAv^2   acting opposite the velocity vector, where p is the fluid density,
                                            C is the drag coefficient, A is the cross-sectional area, and v is
                                            the velocity of the ball.

The lift force is:          F = Kv          acting upward, and sideways in this case. K is called the Magnus coefficient.
                                            (From Am. J. Phys. (51)4, Ehrlichson)

Given the force equation, dividing by mass gives an equation of motion of the form:

a(v,t) = g + bv^2 + kv               where b = pCA/(2m) and k = K/m

This equation will be used to model the the trajectory of the golf ball."""

"""Note to teacher:
This is a really neat demo of the effects of spin on a projectile.
The introductory documentation has been somewhat altered to make it more clear what is going on and why.
Question: what parameters below would you want to vary in order to teach the physics of spin and drag?
"""

#IMPORT PACKAGES
from vpython import *
#from visual import *            # imports visual objects, math expressions, etc.
#from visual.graph import *      # imports graphs, etc.

# PHYSICAL CONSTANTS (in standard SI units (mks system) unless otherwise noted)
gravity = vector(0,-9.8,0)       # acceleration due to gravity

# GOLF BALL PROPERTIES
mass = 0.045                    # golf ball mass is approximately 45 g
surface_area = 0.001            # cross-sectional area of a golf ball (diameter is 1.68 in; circular area from pi*r^2)

# EXTERNAL CONDITIONS
fluid_density = 1.3             # density of air at sea level

# LAUNCH VARIABLES
theta = 23.                     # launch angle from the horizontal, in degrees. Default is 15 degrees to model a shot
# hit with a driver
speed = 70.                     # initial launch speed. Default value is 70 m/s, which is 157 mi/hr. Professional golfers
# obtain launch speeds near 180 mi/hr.

# LIFT AND DRAG PROPERTIES
drag_coefficient = 0.5          # drag coefficient of a smooth sphere
b = drag_coefficient*fluid_density*surface_area/(2*mass)
k = 0.247                       # lift coefficient on a golf ball. (See Am. J. Phys, 51(4), Ehrlichson, H.)

# GRAPHICS PROPERTIES
#scene properties
scene.width = 800
scene.height = 600

#graphic object properties
floor = box(pos=vector(150.,-1.5,0),length=320.,height=3.,width=50.,color=color.green)
tee = box(pos=vector(5.,-1.5,0.),length=20.,height=3.,width=40.,color=color.yellow)
green = cylinder(pos=vector(230,-1.5,0.),axis=vector(0,1.5,0),radius=20., \
                 color=color.yellow)
pin = cylinder(pos=vector(230,-1.5,0.),axis=vector(0,20,0),radius=1,color=color.red)
flag = box(pos=vector(235,16.0,0),length=10,height=5,width=0.1,color=color.white)

scene.center = vector(150.,0.,0)
#scene.forward = vector(2.0,0,-0.2)
scene.forward = vector(-2.0,0,-0.2)
scene.autoscale = 0

# GRAPHICS AND SUCH
#approximate length, height of trajectory
range_theory = speed**2*sin(2*theta)/mag(gravity)
ymax_theory = speed**2*(sin(theta))**2/(2*mag(gravity))

# ball properties
ball = sphere(pos=vector(0,0,0), radius=2,color=color.white)
ball.trail= curve(color=ball.color, radius=0.6)

# initial velocity and forces
theta = theta * pi/180.                                         # converts theta to radians
ball_velocity = vector(speed*cos(theta),speed*sin(theta),0)     # in m/s

# more initial conditions
t = 0.                                                          # starts the clock at 0
dt = 0.05
ymax = 0.

"""note to teacher:
Note that direction vector for lift must be normalized by dividing by its magnitude (or else k is off).
"""
# EULER LOOP #2
while ball.pos.y >= 0:

    # lift and drag accelerations
    drag_acceleration = -b*mag(ball_velocity)*ball_velocity         # acceleration due to drag, = Fdrag/m
    lift_acceleration = k*mag(ball_velocity)*vector(0.,1.,0.1)/mag(vector(0.,1.,0.1)) # acceleration due to lift, in +y direction

    # acceleration
    acceleration = gravity + drag_acceleration + lift_acceleration

    # velocity
    ball_velocity = ball_velocity + acceleration*dt

    # position
    ball.pos = ball.pos + ball_velocity*dt

    #ball trail graphic
    ball.trail.append(pos=ball.pos)

    # check ymax
    ymax = max(ymax, ball.pos.y)

    print(t, ball.pos.x, ball.pos.y, ball.pos.z)

    t = t + dt
    rate(10)

print("-------------------------------------------------")
print("                theta: ", theta*180/pi, " degrees")
print("         actual range: ", ball.pos.x, " m")
print("horizontal deflection: ", fabs(ball.pos.z), " m")
print("    actual max height: ", ymax, " m")
print("actual time of flight: ", t, " s")
print("-------------------------------------------------")


