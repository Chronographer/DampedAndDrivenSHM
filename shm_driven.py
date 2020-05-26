import matplotlib.pyplot as plt
import numpy as np

""" Models simple harmonic motion with the addition of a drag force and a driving force. """

yAxisList = []
xAxisList = []
periodTimer = 0.0


def run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType):
    global periodTimer
    currentTheta = initialTheta
    currentOmega = initialOmega
    currentTime = initialTime
    #currentEnergy = 0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2

    naturalFrequency = np.sqrt(gravity / pendulumLength)

    while currentTime <= maxTime:
        currentAlpha = (gravity * currentTheta) / pendulumLength
        currentOmega = currentOmega + (-naturalFrequency**2 * np.sin(currentTheta) - dragCoefficient * currentOmega + drivingForce * np.sin(drivingFrequency * currentTime)) * timeStep
        currentTheta = currentTheta + currentOmega * timeStep
        #currentEnergy = ((0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2) + currentEnergy) / 2
        currentEnergy = 0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2
        currentTime = currentTime + timeStep
        periodTimer = periodTimer + timeStep

        if clamp is True:
            if currentTheta > np.pi:
                currentTheta = currentTheta - 2 * np.pi
            elif currentTheta < - np.pi:
                currentTheta = currentTheta + 2 * np.pi

        if currentTime > plotStartTime:
            handlePlotType(plotType, currentTime, currentEnergy, currentTheta, currentOmega, currentAlpha, drivingFrequency)

    #plt.plot(xAxisList, yAxisList, 'b.', ms=1.25, label="initial theta: " + str(np.round(initialTheta, 2)) + "\n" + "drive force: " + str(drivingForce) + "\n" + "drive frequency: " + str(np.round(drivingFrequency, 2)) + "\n" + "time step: " + str(timeStep))
    #plt.plot(xAxisList, yAxisList, 'b.', ms=1.25, label="drive force: " + str(drivingForce))
    #plt.plot(xAxisList, yAxisList, label="initial theta: " + str(np.round(initialTheta, 2)) + "\n" + "drive force: " + str(drivingForce) + "\n" + "drive frequency: " + str(np.round(drivingFrequency, 2)) + "\n" + "time step: " + str(timeStep))
    plt.plot(xAxisList, yAxisList, label="drive force: " + str(drivingForce))


def handlePlotType(plotType, currentTime, currentEnergy, currentTheta, currentOmega, currentAlpha, drivingFrequency):  # this makes the graph axis labels and legend labels automatically change to reflect what is actually being plotted
    global periodTimer
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
    elif plotType == "poincare":
        if periodTimer >= drivingFrequency:
            periodTimer = 0
            yAxisList.append(currentOmega)
            xAxisList.append(currentTheta)
    elif plotType == "periodVsAmplitude":
        exit("Error: Plot type 'periodVsAmplitude' is not a valid plot type for script 'shm_driven' \nThis plot type is only applicable with script 'periodCounter.py' ")
    else:
        exit("Error: '" + str(plotType) + "' is not a valid plot type!")


"""def separatrix(theta):
    w = """