import matplotlib.pyplot as plt
import numpy as np


def run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, plotType):
    currentTheta = initialTheta
    currentOmega = initialOmega
    currentTime = initialTime

    naturalFrequency = np.sqrt(gravity/pendulumLength)

    dragFactor = dragCoefficient / mass

    drivingAngularAcceleration = mass * pendulumLength * drivingForce

    yAxisTable = []
    xAxisTable = []

    while currentTime <= maxTime:
        currentAlpha = (gravity * currentTheta) / pendulumLength
        currentOmega = currentOmega + (-naturalFrequency**2 * np.sin(currentTheta) - dragFactor * currentOmega + drivingAngularAcceleration * np.sin(drivingFrequency * currentTime)) * timeStep
        currentTheta = currentTheta + currentOmega * timeStep
        currentEnergy = 0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2
        currentTime = currentTime + timeStep

        """if currentTheta > np.pi:
            currentTheta = currentTheta - 2 * np.pi
            print("angle was clamped by -2*pi")
        elif currentTheta < - np.pi:
            currentTheta = currentTheta + 2 * np.pi
            print("angle was clamped by + 2*pi")"""

        if plotType == "energy":  # this block deals allows the graph axis labels and legend labels to update automatically
            if currentTime > plotStartTime:
                yAxisTable.append(currentEnergy)
                xAxisTable.append(currentTime)
        elif plotType == "angle":
            if currentTime > plotStartTime:
                yAxisTable.append(currentTheta)
                xAxisTable.append(currentTime)
        elif plotType == "velocity":
            if currentTime > plotStartTime:
                yAxisTable.append(np.abs(currentOmega))
                xAxisTable.append(currentTime)
        elif plotType == "acceleration":
            if currentTime > plotStartTime:
                yAxisTable.append(currentAlpha)
                xAxisTable.append(currentTime)
        elif plotType == "velocity vs angle":
            if currentTime > plotStartTime:
                yAxisTable.append(currentOmega)
                xAxisTable.append(currentTheta)
        else:
            exit("Error: '" + str(plotType) + "' is not a valid plot type!")

    plt.plot(xAxisTable, yAxisTable, label=plotType)
