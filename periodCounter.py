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

            if plotType == "energy":  # this block deals with allowing the graph axis labels and legend labels to update automatically
                if currentTime > plotStartTime:
                    yAxisList.append(currentEnergy)
                    xAxisList.append(currentTime)
            elif plotType == "angle":
                if currentTime > plotStartTime:
                    yAxisList.append(currentTheta)
                    xAxisList.append(currentTime)
            elif plotType == "velocity":
                if currentTime > plotStartTime:
                    yAxisList.append(np.abs(currentOmega))
                    xAxisList.append(currentTime)
            elif plotType == "acceleration":
                if currentTime > plotStartTime:
                    yAxisList.append(currentAlpha)
                    xAxisList.append(currentTime)
            elif plotType == "phaseSpace":
                if currentTime > plotStartTime:
                    yAxisList.append(currentOmega)
                    xAxisList.append(currentTheta)
            else:
                exit("Error: '" + str(plotType) + "' is not a valid plot type!")
        currentTime = initialTime
        currentPeriodStartTime = currentTime
    plt.plot(xAxisList, yAxisList, 'b.', ms=1.25, label=plotType)  # plots with points instead of a line
    #plt.plot(xAxisList, yAxisList, label=plotType)

    for i in range(0, len(singlePeriodTimeList)):
        print("period " + str(i) + " was " + str(singlePeriodTimeList[i]) + " seconds.")
        totalPeriodTime = totalPeriodTime + singlePeriodTimeList[i]
    averagePeriodTime = totalPeriodTime / len(singlePeriodTimeList)
    singlePeriodTimeList.clear()
    print("\n")
    print("average period is: " + str(averagePeriodTime))
    averagePeriodList.append(averagePeriodTime)


