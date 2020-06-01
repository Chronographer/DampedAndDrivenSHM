import matplotlib.pyplot as plt
import numpy as np
import shm_driven
import periodCounter
import animated_pendulum

initialTheta = 0.2
initialOmega = 0.0
initialAlpha = 0.0
initialTime = 0.0

maxTheta = np.pi - 0.01     # This is only used in periodCounter.py
thetaIncrement = 0.01  # This is only used in periodCounter.py

gravity = 9.8
pendulumLength = 9.8
mass = 1.0
dragCoefficient = 0.5
drivingForce = 1.2
drivingFrequency = 2/3

drivingPeriod = ((np.pi * 2) / drivingFrequency)

plotStartTime = 1000  # the time when the first point will be plotted on the graph. This variable has no effect for plotType 'periodVsAmplitude'.
timeStep = 0.01
maxTime = 1100

clamp = True
plotType = "phaseSpace"


if plotType == "energy":
    yAxisLabel = "Energy"
    xAxisLabel = "Time (seconds)"
elif plotType == "angle":
    yAxisLabel = "Angle (radians)"
    xAxisLabel = "Time (seconds)"
elif plotType == "velocity":
    yAxisLabel = "Velocity (m/s) (abs)"
    xAxisLabel = "Time (seconds)"
elif plotType == "acceleration":
    yAxisLabel = "Acceleration (m/s^2)"
    xAxisLabel = "Time (seconds)"
elif (plotType == "phaseSpace") or (plotType == "poincare"):
    yAxisLabel = "Velocity (m/s)"
    xAxisLabel = "Angle (rad)"
elif plotType == "periodVsAmplitude":
    yAxisLabel = "Period time (seconds)"
    xAxisLabel = "Initial angle (radians)"
elif plotType == "force":
    yAxisLabel = "Force (Newtons)"
    xAxisLabel = "Time (seconds)"
else:
    yAxisLabel = "y axis label was not defined!"
    xAxisLabel = "x axis label was not defined!"

shm_driven.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType)
#periodCounter.run(gravity, pendulumLength, initialTheta, maxTheta, thetaIncrement, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType)
#animated_pendulum.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType)

plt.legend(loc="best")
plt.grid(True)
plt.suptitle("Nonlinear harmonic motion: " + str(plotType))
plt.xlabel(xAxisLabel)
plt.ylabel(yAxisLabel)

plt.show()
