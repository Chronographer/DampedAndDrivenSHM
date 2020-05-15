import matplotlib.pyplot as plt
import numpy as np


def run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, plotType):
    currentTheta = initialTheta
    currentOmega = initialOmega
    currentTime = initialTime

    plotList = []
    timeList = []

    while currentTime <= maxTime:
        currentAlpha = (gravity * currentTheta) / pendulumLength
        currentOmega = currentOmega - currentAlpha * timeStep
        currentTheta = currentTheta + currentOmega * timeStep
        currentEnergy = 0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2
        currentTime = currentTime + timeStep

        if currentTheta > np.pi:
            currentTheta = currentTheta - 2 * np.pi
            print("angle was clamped by -2*pi")
        elif currentTheta < - np.pi:
            currentTheta = currentTheta + 2 * np.pi
            print("angle was clamped by + 2*pi")

        timeList.append(currentTime)
        if plotType == "energy":  # this block allows the graph axis labels and legend labels to update automatically
            plotList.append(currentEnergy)
        elif plotType == "angle":
            plotList.append(currentTheta)
        elif plotType == "velocity":
            plotList.append(currentOmega)
        elif plotType == "acceleration":
            plotList.append(currentAlpha)
        else:
            exit("Error: '" + str(plotType) + "' is not a valid plot type!")

    plt.plot(timeList, plotList, label=plotType)
