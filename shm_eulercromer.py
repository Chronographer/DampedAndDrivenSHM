import matplotlib.pyplot as plt


def run(gravity, pendulumLength, initialTheta, initialOmega, initialTime, timeStep, maxTime, mass, plotType):
    currentTheta = initialTheta
    currentOmega = initialOmega
    currentTime = initialTime

    initialEnergy = 0.5 * mass * pendulumLength**2 * (currentOmega**2 + (gravity / pendulumLength) * currentTheta**2)
    currentEnergy = initialEnergy

    plotTable = []
    timeTable = []

    while currentTime <= maxTime:
        currentAlpha = (gravity * currentTheta) / pendulumLength
        currentOmega = currentOmega - currentAlpha * timeStep
        currentTheta = currentTheta + currentOmega * timeStep
        currentEnergy = currentEnergy + 0.5 * (mass * pendulumLength * (currentOmega ** 2 + (gravity / pendulumLength) * currentTheta ** 2)) * timeStep ** 2  # this is currently incorrect.
        currentTime = currentTime + timeStep

        timeTable.append(currentTime)
        if plotType == "energy":
            plotTable.append(currentEnergy)
        elif plotType == "angle":
            plotTable.append(currentTheta)
        elif plotType == "velocity":
            plotTable.append(currentOmega)
        elif plotType == "acceleration":
            plotTable.append(currentAlpha)
        else:
            exit("Error: '" + str(plotType) + "' is not a valid plot type!")

    plt.plot(timeTable, plotTable, label=plotType)
