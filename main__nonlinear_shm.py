import matplotlib.pyplot as plt
import numpy as np
import shm_eulercromer
import shm_driven
import amplitude_dependant_anharmonic
import periodCounter

initialTheta = 0.2
initialOmega = 0.0
initialAlpha = 0.0
initialTime = 0.0

maxTheta = 0.31
thetaIncrement = 0.1
timeStep = 0.005
maxTime = 20.0
gravity = 9.8
pendulumLength = 1.0
mass = 1.0
dragCoefficient = 0.0
drivingForce = 0.0
drivingFrequency = 0.0
plotStartTime = 0  # the time when the first point will be plotted on the graph
clamp = True
plotType = "angle"


if plotType == "energy":
    yAxisLabel = "Energy"
    xAxisLabel = "Time (sec)"
elif plotType == "angle":
    yAxisLabel = "Angle (radians)"
    xAxisLabel = "Time (sec)"
elif plotType == "velocity":
    yAxisLabel = "Velocity (m/s) (abs)"
    xAxisLabel = "Time (sec)"
elif plotType == "acceleration":
    yAxisLabel = "Acceleration (m/s^2)"
    xAxisLabel = "Time (sec)"
elif plotType == "phaseSpace":
    yAxisLabel = "Velocity (m/s)"
    xAxisLabel = "Angle (rad)"

periodCounter.run(gravity, pendulumLength, initialTheta, maxTheta, thetaIncrement, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType)

plt.legend(loc="upper right")
plt.grid(True)
plt.suptitle("Driven harmonic motion")
plt.xlabel(xAxisLabel)
plt.ylabel(yAxisLabel)

plt.show()
