import matplotlib.pyplot as plt
import numpy as np

yAxisTable = []
xAxisTable = []
thetaTable = []


def run(gravity, pendulumLength, initialTheta, maxTheta, thetaIncrement, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType):
    currentOmega = initialOmega
    currentTime = initialTime
    thetaTablePopulator = initialTheta
    naturalFrequency = np.sqrt(gravity/pendulumLength)
    dragFactor = dragCoefficient / mass
    drivingAngularAcceleration = mass * pendulumLength * drivingForce

    while thetaTablePopulator < maxTheta:
        thetaTable.append(thetaTablePopulator)
        thetaTablePopulator = thetaTablePopulator + thetaIncrement
    print(len(thetaTable))
    for i in range(0, len(thetaTable)):
        currentTheta = thetaTable[i]
        print("current theta is: " + str(currentTheta))
        while currentTime <= maxTime:
            currentAlpha = (gravity * currentTheta) / pendulumLength
            currentOmega = currentOmega + (-naturalFrequency**2 * np.sin(currentTheta) - dragFactor * currentOmega + drivingAngularAcceleration * np.sin(drivingFrequency * currentTime)) * timeStep
            currentTheta = currentTheta + currentOmega * timeStep
            currentEnergy = 0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2
            currentTime = currentTime + timeStep

            if clamp == True:
                if currentTheta > np.pi:
                    currentTheta = currentTheta - 2 * np.pi
                elif currentTheta < - np.pi:
                    currentTheta = currentTheta + 2 * np.pi

            if plotType == "energy":  # this block deals with allowing the graph axis labels and legend labels to update automatically
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
            elif plotType == "phaseSpace":
                if currentTime > plotStartTime:
                    yAxisTable.append(currentOmega)
                    xAxisTable.append(currentTheta)
            else:
                exit("Error: '" + str(plotType) + "' is not a valid plot type!")
        currentTime = initialTime
    #plt.plot(xAxisTable, yAxisTable, 'b.', ms=1.25, label=plotType) # plots with points instead of a line
    plt.plot(xAxisTable, yAxisTable, label=plotType)
