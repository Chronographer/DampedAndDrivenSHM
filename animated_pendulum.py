"""Make a VPython simple pendulum with pedestal and stand.
Moving system is ball attached to (potentially massive) bar.

This is a modified version of a piece of example code provided by Dr. Cancio in the PHYS336 Computational Physics course
at Ball State University during the spring 2020 semester.
"""
from vpython import *


def makePendulum(pendulumLength, radius_sphere):
    """make a single rigid pendulum using VPython objects.

    INPUT
    length_bar -- length of pendulum bar
    radius_sphere -- radius of spherical bob at end
    OUTPUT
    pendulum -- visual pendulum object with
      Static:
      -- base -- box forming floor of device
      -- pedestal -- box acting as "stand" from which pendulum rotates
      -- axle -- axle on which pendulum rotates
      Moving:
      -- bar -- pendulum bar
      -- sphere -- spherical bob with "mass" of pendulum
    """
    # dimensions of structures
    barDiameter = 0.015
    length_display = pendulumLength + radius_sphere  # The length of the pendulum shown in the animation (slightly longer than actual length used in calculations so it overlaps the axel)
    pedestalHeight = 1.3 * pendulumLength
    pedestalWidth = 0.1
    baseThickness = 0.05
    offset = 4.0 * radius_sphere  # from center of pedestal to center of bar
    baseWidth = 4.0 * offset
    barTop = vector(0, 0, 0)

    xBar = (length_display - radius_sphere) / 2.0  # The initial x position of the bar
    xBall = pendulumLength + radius_sphere / 2.0   # The initial x position of the ball
    pedestalColor = vector(0.4, 0.4, 0.5)

    scene.center = barTop - vector(0, pendulumLength / 2, 0)
    scene.height = scene.width = 400

    # construct fixed apparatus
    pedestal = box(pos=barTop-vector(0, pedestalHeight/2.0, offset), height=1.1*pedestalHeight, length=pedestalWidth, width=pedestalWidth, color=pedestalColor)
    base = box(pos=barTop-vector(0, pedestalHeight+baseThickness/2.0, offset), height=baseThickness, length=baseWidth, width=baseWidth, color=pedestalColor)
    axle = cylinder(pos=barTop-vector(0, 0, offset), axis=vector(0, 0, offset), radius=radius_sphere/4.0, color=color.yellow)

    # construct moving portion as a COMPOUND, originally sticks out along x-axis
    bar = box(pos=vector(xBar, 0, 0), size=vector(length_display, barDiameter, barDiameter), color=color.red)
    ball = sphere(pos=vector(xBall, 0, 0), radius=radius_sphere, color=color.green)
    pendulum = compound([bar, ball])

    # point the frame in -y direction (which will define theta=0).
    pendulum.axis = vector(0, -1, 0)
    pendulum.pos = vector(0, -0.5*length_display, 0)
    print(pendulum)

    return pendulum


def run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, dragCoefficient, drivingForce, drivingFrequency):
    import vpython
    import numpy as np
    scene.title = "Complex Pendulum"
    barLength = 0.5
    sphereRadius = 0.05
    pendulum = makePendulum(barLength, sphereRadius)

    currentTime = initialTime
    currentTheta = initialTheta
    currentOmega = initialOmega
    naturalFrequency = np.sqrt(gravity / pendulumLength)
    pendulum.rotate(origin=vector(0, 0, 0), angle=currentTheta, axis=vector(0, 0, 1))
    vpython.sleep(1)

    while currentTime <= maxTime:
        currentOmega = currentOmega + (-naturalFrequency**2 * np.sin(currentTheta) - dragCoefficient * currentOmega + drivingForce * np.sin(drivingFrequency * currentTime)) * timeStep
        lastTheta = currentTheta
        currentTheta = currentTheta + currentOmega * timeStep
        currentTime = currentTime + timeStep
        rate(60)
        pendulum.rotate(origin=vector(0, 0, 0), angle=currentTheta-lastTheta, axis=vector(0, 0, 1))
