import matplotlib.pyplot as plt
import numpy as np
import shm_eulercromer
import shm_driven
import amplitude_dependant_anharmonic
import periodCounter
import shm_poincare
import animated_pendulum

initialTheta = 0.2
initialOmega = 0.0
initialAlpha = 0.0
initialTime = 0.0

maxTheta = np.pi  # This is only used in amplitude_dependant_anharmonic.py and periodCounter.py
thetaIncrement = 0.1  # This is only used in amplitude_dependant_anharmonic.py and periodCounter.py

timeStep = 0.04
maxTime = 60
gravity = 9.8
pendulumLength = 9.8
mass = 1.0
dragCoefficient = 0.5
drivingForce = 1.2
drivingFrequency = 2/3


plotStartTime = 0  # the time when the first point will be plotted on the graph
clamp = False
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
elif plotType == "periodVsAmplitude":
    yAxisLabel = "Period time (seconds)"
    xAxisLabel = "Initial angle (radians)"
else:
    yAxisLabel = "y axis label was not defined!"
    xAxisLabel = "x axis label was not defined!"

shm_driven.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType)
#amplitude_dependant_anharmonic.run(gravity, pendulumLength, initialTheta, maxTheta, thetaIncrement, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType)
#periodCounter.run(gravity, pendulumLength, initialTheta, maxTheta, thetaIncrement, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType)
#shm_poincare.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType)
#animated_pendulum.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType)

plt.legend(loc="best")
plt.grid(True)
plt.suptitle("Nonlinear harmonic motion: " + str(plotType))
plt.xlabel(xAxisLabel)
plt.ylabel(yAxisLabel)

plt.show()
