import matplotlib.pyplot as plt
import numpy as np

yAxisList = []
xAxisList = []


def run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType):
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

        if periodTimer >= drivingFrequency:
            periodTimer = 0
            if plotType == "energy":  # this block allows the graph axis labels and legend labels to update automatically
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
    #plt.plot(xAxisList, yAxisList, 'b.', ms=1.25, label=plotType)
    plt.plot(xAxisList, yAxisList, label=plotType)


"""def separatrix(theta):
    w = """