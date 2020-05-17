import matplotlib.pyplot as plt
import numpy as np

""" Models simple harmonic motion with the addition of a drag force and a driving force. """

yAxisList = []
xAxisList = []


def run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType):
    currentTheta = initialTheta
    currentOmega = initialOmega
    currentTime = initialTime
    #currentEnergy = 0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2

    naturalFrequency = np.sqrt(gravity / pendulumLength)
    dragFactor = dragCoefficient / mass
    drivingAngularAcceleration = mass * pendulumLength * drivingForce

    while currentTime <= maxTime:
        currentAlpha = (gravity * currentTheta) / pendulumLength
        currentOmega = currentOmega + (-naturalFrequency**2 * np.sin(currentTheta) - dragFactor * currentOmega + drivingAngularAcceleration * np.sin(drivingFrequency * currentTime)) * timeStep
        currentTheta = currentTheta + currentOmega * timeStep
        #currentEnergy = ((0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2) + currentEnergy) / 2
        currentEnergy = 0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2
        currentTime = currentTime + timeStep

        if clamp is True:
            if currentTheta > np.pi:
                currentTheta = currentTheta - 2 * np.pi
            elif currentTheta < - np.pi:
                currentTheta = currentTheta + 2 * np.pi

        if currentTime > plotStartTime:
            handlePlotType(plotType, currentTime, currentEnergy, currentTheta, currentOmega, currentAlpha)

    plt.plot(xAxisList, yAxisList, 'b.', ms=1.25, label=plotType)
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

"""def separatrix(theta):
    w = """