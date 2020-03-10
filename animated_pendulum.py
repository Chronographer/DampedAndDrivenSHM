"""Make a VPython simple pendulum with pedestal and stand.

Moving system is ball attached to (potentially massive) bar.
"""
from vpython import *

def makependulum(pendulumLength, radius_sphere):
    """make a single rigid pendulum using VPython objects.

    INPUT
    length_bar -- length of pendulum bar
    radius_sphere -- radius of spherical bob at end
    OUTPUT
    pendulum -- visual pendulum object with
      Fixed:
      -- base -- box forming floor of device
      -- pedestal -- box acting as "stand" from which pendulum rotates
      -- axle -- axle on which pendulum rotates
      Moving:
      -- bar -- pendulum bar
      -- sphere -- spherical bob with "mass" of pendulum
    """
    # dimensions of structures
    bard = 0.015             # thickness of bar
    length_display = pendulumLength + radius_sphere
    # show bar a bit longer than physical,
    #    to overlap axle

    hpedestal = 1.3 * pendulumLength    # height of pedestal
    wpedestal = 0.1               # width of pedestal
    tbase = 0.05                  # thickness of base
    offset = 4.*radius_sphere     # from center of pedestal to center of bar
    wbase = 4.*offset             # width of base
    top = vector(0,0,0)           # top of bar

    xbar = (length_display-radius_sphere) / 2.0
    xball = pendulumLength + radius_sphere / 2.0
    #colors
    pedestalcolor = vector(0.4,0.4,0.5)

    #sets scene center, and physical dimensions to useful values.
    scene.center = top-vector(0, pendulumLength / 2, 0)
    scene.height = scene.width = 400

    #construct fixed apparatus
    pedestal = box(pos=top-vector(0,hpedestal/2.,offset),
                   height=1.1*hpedestal, length=wpedestal, width=wpedestal,
                   color=pedestalcolor )
    base = box(pos=top-vector(0,hpedestal+tbase/2.,offset),
               height=tbase, length=wbase, width=wbase,
               color=pedestalcolor )
    axle = cylinder(pos=top-vector(0,0,offset), axis=vector(0,0,offset),
                    radius=radius_sphere/4., color=color.yellow)

    #construct moving portion as a COMPOUND, originally sticks out along x-axis
    bar = box(pos=vector(xbar,0,0),
              size=vector(length_display,bard,bard), color=color.red)
    ball = sphere(pos=vector(xball,0,0),
                  radius=radius_sphere, color=color.green)
    pendulum = compound([bar,ball])

    #point the frame in -y direction (which will define theta=0).
    pendulum.axis = vector(0,-1,0)
    pendulum.pos = vector(0,-0.5*length_display,0)
    print( pendulum )

    return pendulum

#simple debug thing to do if run this code as main program:
if __name__ == "__main__":
    from vpython import scene, rotate, pi
    import vpython
    import numpy as np
    #scene.title = "Simple Pendulum"
    Lbar = 0.5         # physical length of bar
    Rsphere = 0.05     # radius of sphere
    pendulum = makependulum(Lbar,Rsphere)

    gravity = 9.8
    mass = 1.0
    dragCoefficient = 1.0
    currentTime = 0
    maxTime = 400
    pendulumLength = 1.0
    timeStep = 0.005
    drivingForce = 10.2
    drivingFrequency = 0.54
    currentTheta = 90
    currentOmega = 0.0
    naturalFrequency = np.sqrt(gravity/pendulumLength)
    dragFactor = dragCoefficient / mass
    drivingAngularAcceleration = mass * pendulumLength * drivingForce
    lastTheta = 0
    pendulum.rotate(origin=vector(0,0,0), angle=currentTheta, axis=vector(0,0,1))
    vpython.sleep(1)


while currentTime <= maxTime:
    currentAlpha = (gravity * currentTheta) / pendulumLength
    currentOmega = currentOmega + (-naturalFrequency**2 * np.sin(currentTheta) - dragFactor * currentOmega + drivingAngularAcceleration * np.sin(drivingFrequency * currentTime)) * timeStep
    lastTheta = currentTheta
    currentTheta = currentTheta + currentOmega * timeStep
    currentEnergy = 0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2
    currentTime = currentTime + timeStep
    rate(60)
    pendulum.rotate(origin=vector(0,0,0), angle=currentTheta-lastTheta, axis=vector(0,0,1))
