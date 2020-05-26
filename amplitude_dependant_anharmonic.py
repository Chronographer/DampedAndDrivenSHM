import matplotlib.pyplot as plt
import numpy as np
import random

""" This program runs the driven and damped harmonic motion simulation for multiple initial values of theta """

yAxisList = []
xAxisList = []
thetaList = []
colorDotList = ['b.', 'g.', 'r.', 'c.', 'm.', 'y.', 'k.', 'b.', 'g.', 'r.', 'c.', 'm.', 'y.', 'k.']
colorList = ['b', 'g', 'r', 'c', 'm', 'y', 'b']
#tupleColorList = []


def run(gravity, pendulumLength, initialTheta, maxTheta, thetaIncrement, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType):
    currentOmega = initialOmega
    currentTime = initialTime
    thetaListPopulator = initialTheta
    naturalFrequency = np.sqrt(gravity / pendulumLength)

    while thetaListPopulator <= maxTheta:
        thetaList.append(thetaListPopulator)
        thetaListPopulator = thetaListPopulator + thetaIncrement
        """color = (random.randrange(0, 1), random.randrange(0, 1), random.randrange(0, 1))  # this would be used to make a unique color for any number of elements, but I cant quite get it to work and Im not sure its worth it.
        tupleColorList.append(color)"""
    print("thetaList has " + str(len(thetaList)) + " elements")
    for i in range(0, len(thetaList)):
        currentTheta = thetaList[i]
        currentTime = initialTime
        currentOmega = initialOmega
        xAxisList.clear()
        yAxisList.clear()
        print("current theta is: " + str(currentTheta))
        while currentTime <= maxTime:
            currentAlpha = (gravity * currentTheta) / pendulumLength
            currentOmega = currentOmega + (-naturalFrequency**2 * np.sin(currentTheta) - dragCoefficient * currentOmega + drivingForce * np.sin(drivingFrequency * currentTime)) * timeStep
            currentTheta = currentTheta + currentOmega * timeStep
            currentEnergy = 0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2
            currentTime = currentTime + timeStep

            if clamp is True:
                if currentTheta > np.pi:
                    currentTheta = currentTheta - 2 * np.pi
                elif currentTheta < - np.pi:
                    currentTheta = currentTheta + 2 * np.pi

            if currentTime > plotStartTime:
                handlePlotType(plotType, currentTime, currentEnergy, currentTheta, currentOmega, currentAlpha)
        plt.plot(xAxisList, yAxisList, colorDotList[i], ms=1.25, label="initial theta: " + str(round(thetaList[i], 3)))  # plots with points instead of a line
        #plt.plot(xAxisList, yAxisList, fmt='[.][tupleColorList[i]]', label="initial theta: " + str(round(thetaList[i], 3)))
        #plt.plot(xAxisList, yAxisList, label=plotType)


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
    else:
        exit("Error: '" + str(plotType) + "' is not a valid plot type!")
