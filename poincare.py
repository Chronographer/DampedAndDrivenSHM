import matplotlib.pyplot as plt
import numpy as np

yAxisList = []
xAxisList = []

"""
THIS SCRIPT IS DEPRECATED. It was originally made to produce a poincare plot, however this can now be accomplished by 
using driven_damped.py by setting plotType to 'poincare'.
"""


def run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, clamp, plotType):
    currentTheta = initialTheta
    currentOmega = initialOmega
    currentTime = initialTime
    periodTimer = 0

    naturalFrequency = np.sqrt(gravity / pendulumLength)

    while currentTime <= maxTime:
        currentAlpha = (gravity * currentTheta) / pendulumLength
        currentOmega = currentOmega + (-naturalFrequency**2 * np.sin(currentTheta) - dragCoefficient * currentOmega + drivingForce * np.sin(drivingFrequency * currentTime)) * timeStep
        currentTheta = currentTheta + currentOmega * timeStep
        currentEnergy = 0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2

        currentTime = currentTime + timeStep
        periodTimer = periodTimer + timeStep

        if clamp is True:
            if currentTheta > np.pi:
                currentTheta = currentTheta - 2 * np.pi
            elif currentTheta < - np.pi:
                currentTheta = currentTheta + 2 * np.pi

        if periodTimer >= ((np.pi * 2) / drivingFrequency):
            periodTimer = 0
            handlePlotType(plotType, currentTime, currentEnergy, currentTheta, currentOmega, currentAlpha)
    #plt.plot(xAxisList, yAxisList, 'b.', ms=1.25, label=plotType)
    plt.plot(xAxisList, yAxisList, label=plotType)


def handlePlotType(plotType, currentTime, currentEnergy, currentTheta, currentOmega, currentAlpha):  # this makes the graph axis labels and legend labels automatically change to reflect what is actually being plotted
    if plotType == "energy":
        yAxisList.append(currentEnergy)
        xAxisList.append(currentTime)
    elif plotType == "angle":
        yAxisList.append(currentTheta)
        xAxisList.append(currentTime)
    elif plotType == "velocity":
        yAxisList.append(np.abs(currentOmega))
        xAxisList.append(currentTime)
    elif plotType == "acceleration":
        yAxisList.append(currentAlpha)
        xAxisList.append(currentTime)
    elif plotType == "phaseSpace":
        yAxisList.append(currentOmega)
        xAxisList.append(currentTheta)
    elif plotType == "periodVsAmplitude":
        exit("Error: Plot type 'periodVsAmplitude' is not a valid plot type for script 'shm_driven' \nThis plot type is only applicable with script 'periodCounter.py' ")
    else:
        exit("Error: '" + str(plotType) + "' is not a valid plot type!")
