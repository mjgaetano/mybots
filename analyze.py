import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
targetAngles = numpy.load("data/targetAngles.npy")

#matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=4)
#matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg")
matplotlib.pyplot.plot(targetAngles, label="Target Angles")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()