import matplotlib.pyplot as plt
import numpy as np


def run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotType):
    currentTheta = initialTheta
    currentOmega = initialOmega
    currentTime = initialTime

    naturalFrequency = np.sqrt(gravity/pendulumLength)

    dragFactor = dragCoefficient / mass

    drivingAngularAcceleration = mass * pendulumLength * drivingForce

    plotTable = []
    timeTable = []

    while currentTime <= maxTime:
        currentAlpha = (gravity * currentTheta) / pendulumLength
        currentOmega = currentOmega + (-naturalFrequency**2 * np.sin(currentTheta) - dragFactor * currentOmega + drivingAngularAcceleration * np.sin(drivingFrequency)) * timeStep
        currentTheta = currentTheta + currentOmega * timeStep
        currentEnergy = 0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2
        currentTime = currentTime + timeStep

        """if currentTheta > np.pi:
            currentTheta = currentTheta - 2 * np.pi
            print("angle was clamped by -2*pi")
        elif currentTheta < - np.pi:
            currentTheta = currentTheta + 2 * np.pi
            print("angle was clamped by + 2*pi")"""

        timeTable.append(currentTime)
        if plotType == "energy":  # this block deals allows the graph axis labels and legend labels to update automatically
            plotTable.append(currentEnergy)
        elif plotType == "angle":
            plotTable.append(currentTheta)
        elif plotType == "velocity":
            plotTable.append(np.abs(currentOmega))
        elif plotType == "acceleration":
            plotTable.append(currentAlpha)
        else:
            exit("Error: '" + str(plotType) + "' is not a valid plot type!")

    plt.plot(timeTable, plotTable, label=plotType)
