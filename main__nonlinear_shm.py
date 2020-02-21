import shm_eulercromer
import shm_driven
import matplotlib.pyplot as plt


initialTheta = 0.2
initialOmega = 0.0
initialAlpha = 0.0
initialTime = 0.0

timeStep = 0.1
maxTime = 400.0
gravity = 9.8
pendulumLength = 1.0
mass = 1.0
dragCoefficient = 1.0
drivingForce = 10.7
drivingFrequency = 0.54
plotStartTime = 0  # the time when the first point will be plotted on the graph
plotType = "velocity"

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

shm_driven.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, plotType)
#shm_driven.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, 0.0, 0.0, plotStartTime, plotType)

#shm_driven.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, "angle")
#shm_driven.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, "velocity")
#shm_driven.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, "acceleration")
#shm_driven.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, "energy")

plt.legend(loc="upper right")
plt.grid(True)
plt.suptitle("Driven harmonic motion")
plt.xlabel(xAxisLabel)
plt.ylabel(yAxisLabel)
#plt.axis(xmin=-80, xmax=24, ymin=-12, ymax=12)  # This is used for the animated version.
plt.show()
