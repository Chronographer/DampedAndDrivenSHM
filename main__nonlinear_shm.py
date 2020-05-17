import matplotlib.pyplot as plt
import numpy as np
import shm_eulercromer
import shm_driven
import amplitude_dependant_anharmonic
import periodCounter
import shm_poincare
import animated_pendulum

initialTheta = np.pi / 2
initialOmega = 0.0
initialAlpha = 0.0
initialTime = 0.0

timeStep = 0.01
maxTime = 300
gravity = 9.8
pendulumLength = 1.0
mass = 1.0
dragCoefficient = 1.0
drivingForce = 0
drivingFrequency = 0.53
maxTheta = 1.0  # This is only used in amplitude_dependant_anharmonic.py and periodCounter.py
thetaIncrement = 0.1  # This is only used in amplitude_dependant_anharmonic.py and periodCounter.py

plotStartTime = 0  # the time when the first point will be plotted on the graph
clamp = True
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

#periodCounter.run(gravity, pendulumLength, initialTheta, maxTheta, thetaIncrement, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType)
#shm_driven.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType)
#amplitude_dependant_anharmonic.run(gravity, pendulumLength, initialTheta, maxTheta, thetaIncrement, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType)
#shm_poincare.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType)
animated_pendulum.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType)

plt.legend(loc="upper right")
plt.grid(True)
plt.suptitle("Driven harmonic motion: " + str(plotType))
plt.xlabel(xAxisLabel)
plt.ylabel(yAxisLabel)

plt.show()
