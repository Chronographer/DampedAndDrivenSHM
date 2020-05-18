import matplotlib.pyplot as plt
import numpy as np

#  TO DO: Make different values of theta plot separately, preferably with different colors or something.

yAxisList = []
xAxisList = []
thetaList = []
singlePeriodTimeList = []
averagePeriodList = []


def run(gravity, pendulumLength, initialTheta, maxTheta, thetaIncrement, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType):
    currentOmega = initialOmega
    currentTime = initialTime
    thetaListPopulator = initialTheta
    naturalFrequency = np.sqrt(gravity / pendulumLength)
    dragFactor = dragCoefficient / mass
    drivingAngularAcceleration = mass * pendulumLength * drivingForce
    currentPeriodStartTime = 0
    totalPeriodTime = 0.0

    while thetaListPopulator <= maxTheta:
        thetaList.append(thetaListPopulator)
        thetaListPopulator = thetaListPopulator + thetaIncrement
    for i in range(0, len(thetaList)):
        currentTheta = thetaList[i]
        currentOmega = initialOmega
        currentTime = initialTime
        currentPeriodStartTime = currentTime

        while currentTime <= maxTime:
            currentAlpha = (gravity * currentTheta) / pendulumLength
            lastOmega = currentOmega
            currentOmega = currentOmega + (-naturalFrequency**2 * np.sin(currentTheta) - dragFactor * currentOmega + drivingAngularAcceleration * np.sin(drivingFrequency * currentTime)) * timeStep
            currentTheta = currentTheta + currentOmega * timeStep
            currentEnergy = 0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2
            currentTime = currentTime + timeStep

            if (lastOmega > 0 > currentOmega) or (lastOmega < 0 < currentOmega):
                currentPeriodTime = currentTime - currentPeriodStartTime
                singlePeriodTimeList.append(currentPeriodTime)
                currentPeriodStartTime = currentTime

            if clamp is True:
                if currentTheta > np.pi:
                    currentTheta = currentTheta - 2 * np.pi
                elif currentTheta < - np.pi:
                    currentTheta = currentTheta + 2 * np.pi

            if currentTime >= plotStartTime:
                handlePlotType(plotType, currentTime, currentEnergy, currentTheta, currentOmega, currentAlpha)

        for index in range(0, len(singlePeriodTimeList)):
            totalPeriodTime = totalPeriodTime + singlePeriodTimeList[i]
        averagePeriodTime = totalPeriodTime / len(singlePeriodTimeList)
        singlePeriodTimeList.clear()
        print("average period for initial theta of " + str(thetaList[i]) + " was: " + str(averagePeriodTime) + " seconds")
        averagePeriodList.append(averagePeriodTime)

    if plotType == "periodVsAmplitude":
        xAxisList = thetaList
        yAxisList = averagePeriodList

    #plt.plot(xAxisList, yAxisList, 'b.', ms=1.25, label=plotType)  # plots with points instead of a line
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
    elif plotType == "periodVsAmplitude":  # do nothing here, as this can only be plotted once for each initial theta, not once each time step.
        placeHolderValue = 0
    else:
        exit("Error: '" + str(plotType) + "' is not a valid plot type!")
