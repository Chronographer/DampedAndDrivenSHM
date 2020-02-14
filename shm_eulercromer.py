import matplotlib.pyplot as plt
import numpy as np


def run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, plotType):
    currentTheta = initialTheta
    currentOmega = initialOmega
    currentTime = initialTime

    plotTable = []
    timeTable = []

    while currentTime <= maxTime:
        currentAlpha = (gravity * currentTheta) / pendulumLength
        currentOmega = currentOmega - currentAlpha * timeStep
        currentTheta = currentTheta + currentOmega * timeStep
        currentEnergy = 0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2
        currentTime = currentTime + timeStep

        if currentTheta > np.pi:
            currentTheta = currentTheta - 2 * np.pi
        elif currentTheta < - np.pi:
            currentTheta = currentTheta + 2 * np.pi

        timeTable.append(currentTime)
        if plotType == "energy":  # this block deals allows the graph axis labels and legend labels to update automatically
            plotTable.append(currentEnergy)
        elif plotType == "angle":
            plotTable.append(currentTheta)
        elif plotType == "velocity":
            plotTable.append(currentOmega)
        elif plotType == "acceleration":
            plotTable.append(currentAlpha)
        else:
            exit("Error: '" + str(plotType) + "' is not a valid plot type!")

    plt.plot(timeTable, plotTable, label=plotType)
