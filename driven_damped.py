import matplotlib.pyplot as plt
import numpy as np

""" Models simple harmonic motion with the addition of a drag force and a driving force. """

yAxisList = []
xAxisList = []
periodTimer = 0.0  # stores the current elapsed time in the current drive period. Used for plotType 'poincare'.


def run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, phaseShift, plotStartTime, clamp, plotType):
    global periodTimer
    currentTheta = initialTheta
    currentOmega = initialOmega
    currentTime = initialTime

    totalSteps = maxTime / timeStep
    inverseTotalSteps = 1 / totalSteps  # These two variables are only used to compute the current progress of the computation. The inverse values are used because it is faster to multiply numbers than it is to divide them, so in theory computing the inverse once here and using that value is faster than dividing by the original value many times. In other words, this is intended to reduce any performance impacts that enabling the progress report has on the total speed of the program.
    inverseTimeStep = 1 / timeStep
    lastProgress = 0
    showProgress = True  # Set this to True to display the percentage of the current computation in 1% intervals in the console/terminal. Set it to False to disable this feature.

    naturalFrequency = np.sqrt(gravity / pendulumLength)
    drivingPeriod = np.pi * 2 / drivingFrequency

    while currentTime <= maxTime:
        currentAlpha = (gravity * currentTheta) / pendulumLength
        currentOmega = currentOmega + (-naturalFrequency**2 * np.sin(currentTheta) - dragCoefficient * currentOmega + drivingForce * np.sin(drivingFrequency * currentTime)) * timeStep
        currentTheta = currentTheta + currentOmega * timeStep
        currentForce = - (gravity / pendulumLength) * np.sin(currentTheta)
        #currentEnergy = 0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * currentTheta**2  # original energy formula: not valid for large angles
        currentEnergy = 0.5 * mass * pendulumLength**2 * currentOmega**2 + 0.5 * mass * gravity * pendulumLength * (1 - np.cos(currentTheta))  # correct energy formula (I think)
        currentTime = currentTime + timeStep
        periodTimer = periodTimer + timeStep

        if showProgress is True:  # This displays what percentage of the current computation has been completed.
            currentSteps = currentTime * inverseTimeStep
            progress = currentSteps * inverseTotalSteps
            if progress - lastProgress > 0.01:
                print(str(round((progress * 100), 1)) + "% complete")
                lastProgress = progress

        if clamp is True:
            if currentTheta > np.pi:
                currentTheta = currentTheta - 2 * np.pi
            elif currentTheta < - np.pi:
                currentTheta = currentTheta + 2 * np.pi

        if currentTime > plotStartTime:
            handlePlotType(plotType, currentTime, currentEnergy, currentTheta, currentOmega, currentAlpha, currentForce, drivingPeriod, phaseShift)

    plt.plot(xAxisList, yAxisList, 'b.', ms=1.25, label="initial theta: " + str(np.round(initialTheta, 2)) + "\ndrive force: " + str(round(drivingForce, 2)) + "\ndrive frequency: " + str(np.round(drivingFrequency, 2)) + "\ndrag coefficient: " + str(dragCoefficient) + "\ntime step: " + str(timeStep))
    #plt.plot(xAxisList, yAxisList, 'b.', ms=1.25, label="drive force: " + str(drivingForce))
    #plt.plot(xAxisList, yAxisList, label="initial theta: " + str(np.round(initialTheta, 2)) + "\n" + "drive force: " + str(drivingForce) + "\n" + "drive frequency: " + str(np.round(drivingFrequency, 2)) + "\n" + "time step: " + str(timeStep))
    #plt.plot(xAxisList, yAxisList, label="drive force: " + str(drivingForce))

    if showProgress is True:
        print("100.0% complete")


def handlePlotType(plotType, currentTime, currentEnergy, currentTheta, currentOmega, currentAlpha, currentForce, drivingPeriod, phaseShift):  # this makes the graph axis labels and legend labels automatically change to reflect what is actually being plotted
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
    elif plotType == "force":
        yAxisList.append(currentForce)
        xAxisList.append(currentTime)
    elif plotType == "poincare":
        if periodTimer >= drivingPeriod + phaseShift:
            periodTimer = 0
            yAxisList.append(currentOmega)
            xAxisList.append(currentTheta)
    elif plotType == "periodVsAmplitude":
        exit("Error: Plot type 'periodVsAmplitude' is not a valid plot type for script 'shm_driven' \nThis plot type is only applicable with script 'periodCounter.py'")
    else:
        exit("Error: '" + str(plotType) + "' is not a valid plot type!")
