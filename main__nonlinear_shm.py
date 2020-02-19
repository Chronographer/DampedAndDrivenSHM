import shm_eulercromer
import shm_driven
import matplotlib.pyplot as plt
import numpy as np


initialTheta = 0.2
initialOmega = 0.0
initialAlpha = 0.0
initialTime = 0.0

timeStep = 0.01
maxTime = 600.0
gravity = 9.8
pendulumLength = 1.0
mass = 1.0
dragCoefficient = 0.1
drivingForce = 4.73
drivingFrequency = np.sqrt(gravity/pendulumLength) - 0.23
plotStartTime = 400  # the time when the first point will be plotted on the graph
clamp = False
plotType = "phaseSpace"

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

shm_driven.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType)

plt.legend(loc="upper right")
plt.grid(True)
plt.suptitle("Driven harmonic motion")
plt.xlabel(xAxisLabel)
plt.ylabel(yAxisLabel)

plt.show()
