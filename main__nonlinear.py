import matplotlib.pyplot as plt
import numpy as np
import driven_damped
import periodCounter
import animated_pendulum

initialTheta = 0.2
initialOmega = 0.0
initialAlpha = 0.0
initialTime = 0.0

maxTheta = np.pi - 0.01  # This is only used in periodCounter.py
thetaIncrement = 0.01    # This is only used in periodCounter.py

gravity = 9.8
pendulumLength = 9.8  # 3.5
mass = 1.0
dragCoefficient = 0.5  # 0.73
drivingForce = 1.2  # 3.2
drivingFrequency = 2/3  # 4/7
phaseShift = np.pi/3  # Only used with plot type 'poincare'. Determines the amount to phase shift the period of plotting points. For example, when set to 0, points will be plotted every drive period. When set to pi/2, points will be plotted ever (drive period + pi/2) seconds.

drivingPeriod = ((np.pi * 2) / drivingFrequency)

plotStartTime = 1000 * drivingPeriod   # the time when the first point will be plotted on the graph. This variable has no effect for plotType 'periodVsAmplitude'.
timeStep = 0.01 * drivingPeriod
maxTime = 2000 * drivingPeriod

"""print("drive period: " + str(drivingPeriod))
print("start time: " + str(plotStartTime))
print("max time: " + str(maxTime))
print("timeStep: " + str(timeStep))
print("total number of steps: " + str(maxTime / timeStep))"""

clamp = True
plotType = "poincare"


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

#shm_driven.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, phaseShift, plotStartTime, clamp, plotType)
#periodCounter.run(gravity, pendulumLength, initialTheta, maxTheta, thetaIncrement, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType)
animated_pendulum.run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency)

plt.legend(loc="best")
plt.grid(True)
#plt.ylim(-1.934, 0.711)  # uncommenting these will force the plot to be scaled to a reasonable degree. Useful when trying to make a non phase-shifted poincare plot of simple harmonic motion.
#plt.xlim(-3.4, 3.4)
plt.suptitle("Nonlinear harmonic motion: " + str(plotType))
plt.xlabel(xAxisLabel)
plt.ylabel(yAxisLabel)

plt.show()
