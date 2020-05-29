import matplotlib.pyplot as plt
import numpy as np

"""
This script runs the driven and damped oscillator code (additionally computing the length of the period) once for each value of the initialTheta stored in thetaList. thetaList is populated at runtime by adding values 
from 0 to maxTheta in increments of thetaIncrement. Although all of the plot types work with this script (except for 'poincare'), it is primarily intended to be run with the plot type 'periodVsAmplitude' which will
plot one data point for each element in thetaList. All other plot types will behave the same as they would normally, but will plot the Entire list of data points for a given initialTheta for EACH element in 
thetaList, producing a plot so full of points that no useful information can be gathered from it except possibly for a relatively small range of initial thetas. 
"""

yAxisList = []
xAxisList = []
thetaList = []
singlePeriodTimeList = []
averagePeriodList = []


def run(gravity, pendulumLength, initialTheta, maxTheta, thetaIncrement, initialOmega, initialTime, timeStep, maxTime, mass, dragCoefficient, drivingForce, drivingFrequency, plotStartTime, clamp, plotType):
    global xAxisList, yAxisList
    currentOmega = initialOmega
    currentTime = initialTime
    thetaListPopulator = initialTheta
    naturalFrequency = np.sqrt(gravity / pendulumLength)
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
            currentOmega = currentOmega + (-naturalFrequency**2 * np.sin(currentTheta) - dragCoefficient * currentOmega + drivingForce * np.sin(drivingFrequency * currentTime)) * timeStep
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
        if len(singlePeriodTimeList) > 0:
            for index in range(0, len(singlePeriodTimeList)):
                totalPeriodTime = totalPeriodTime + singlePeriodTimeList[index]
            averagePeriodTime = totalPeriodTime / len(singlePeriodTimeList)
        else:
            print("\nWARNING: Pendulum with an initial angle of " + str(thetaList[i]) + " radians did not complete a full period of oscillation in " + str(maxTime) + " seconds!\n  The period time for this initial angle is not correct! Try increasing 'maxTime' or decreasing 'maxTheta' in main_nonlinear_shm.py to fix this.")
        singlePeriodTimeList.clear()
        totalPeriodTime = 0
        print("average period for initial theta of " + str(thetaList[i]) + " was: " + str(averagePeriodTime) + " seconds")
        averagePeriodList.append(averagePeriodTime)

    if plotType == "periodVsAmplitude":
        xAxisList = thetaList
        yAxisList = averagePeriodList

    #plt.plot(xAxisList, yAxisList, 'b.', ms=1.25, label=plotType)  # plots with points instead of a line
    plt.plot(xAxisList, yAxisList, label="time step: " + str(timeStep) + "\n" + "drive force: " + str(drivingForce) + "\n" + "drive frequency: " + str(round(drivingFrequency, 2)))


def handlePlotType(plotType, currentTime, currentEnergy, currentTheta, currentOmega, currentAlpha):  # this makes the graph axis labels and legend labels automatically change to reflect what is actually being plotted
    global xAxisList, yAxisList
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
        placeHolderValue = 0  # This variable does nothing, it is only here because I need to have some piece of code in the indent or it apparently does not count as an indent and throws a syntax error.
    elif plotType == "poincare":
        exit("Error: Plot type 'poincare' is not a valid plot type for script 'periodCounter.py' \nThis plot type is only applicable with script 'shm_driven.py'")
    else:
        exit("Error: '" + str(plotType) + "' is not a valid plot type!")
