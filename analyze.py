import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
targetAnglesBL = numpy.load("data/targetAnglesBL.npy")
targetAnglesFL = numpy.load("data/targetAnglesFL.npy")

#matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=4)
#matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg")
matplotlib.pyplot.plot(targetAnglesBL, label="Target Angles (Back Leg)", linewidth=4)
matplotlib.pyplot.plot(targetAnglesFL, label="Target Angles (Front Leg)")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()