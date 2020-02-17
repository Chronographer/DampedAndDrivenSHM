import shm_eulercromer
import shm_driven
import numpy as np
import matplotlib.pyplot as plt


initialTheta = 0.2
initialOmega = 0.0
initialAlpha = 0.0
initialTime = 0.0

timeStep = 0.01
maxTime = 20.0
gravity = 9.8
pendulumLength = 1.0
mass = 1.0
dragCoefficient = 1.0
drivingForce = 0.0
drivingFrequency = 0.0
plotType = "velocity vs angle"

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
elif plotType == "velocity vs angle":
    yAxisLabel = "Velocity (m/s)"
    xAxisLabel = "Angle (rad)"

shm_driven.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotType)

#shm_driven.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, "angle")
#shm_driven.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, "velocity")
#shm_driven.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, "acceleration")
#shm_driven.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, "energy")

plt.legend(loc="upper right")
plt.grid(True)
plt.suptitle("Driven harmonic motion")
plt.xlabel(xAxisLabel)
plt.ylabel(yAxisLabel)
plt.show()
