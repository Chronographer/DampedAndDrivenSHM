import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation


def data_gen(t=0):
    currentOmega = 0.0
    currentTheta = 0.2
    while t <= 400:
        gravity = 9.8
        pendulumLength = 1.0
        timeStep = 0.1
        dragFactor = 1.0
        drivingAngularAcceleration = 10.73
        currentTime = t
        drivingFrequency = 0.54
        naturalFrequency = np.sqrt(gravity/pendulumLength)
        currentOmega = currentOmega + (-naturalFrequency**2 * np.sin(currentTheta) - dragFactor * currentOmega + drivingAngularAcceleration * np.sin(drivingFrequency * currentTime)) * timeStep
        currentTheta = currentTheta + currentOmega * timeStep
        t = t + timeStep

        yield currentTheta, currentOmega
        #print(t)


def init():
    line.set_data(xdata, ydata)
    return line,


fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.grid()
xdata, ydata = [], []
ax.set_xlim(left=-80, right=24)
ax.set_ylim(top=12, bottom=-12)


def run(data):
    t, y = data
    xdata.append(t)
    ydata.append(y)
    line.set_data(xdata, ydata)

    return line


print("before ani =")
ani = matplotlib.animation.FuncAnimation(fig, run, data_gen, interval=1, repeat=False)
print("before plt.show")
plt.show()
print("after plt.show()")
#ani.save("your_argument_is_invalid.mp4")
print("after ani.save()")

