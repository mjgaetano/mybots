from simulation import SIMULATION
# import pybullet as p
# import pybullet_data
# import time
# import pyrosim.pyrosim as pyrosim
# import numpy
# import random
# import constants as c
#
# backLegSensorValues = numpy.zeros(c.ITERATIONS)
# frontLegSensorValues = numpy.zeros(c.ITERATIONS)
#
# targetAnglesFL = c.amplitudeFL * numpy.sin(c.frequencyFL * numpy.linspace(0, 2*numpy.pi, c.ITERATIONS) + c.phaseOffsetFL)
# targetAnglesBL = c.amplitudeBL * numpy.sin(c.frequencyBL * numpy.linspace(0, 2*numpy.pi, c.ITERATIONS) + c.phaseOffsetBL)
# # numpy.save("data/targetAnglesFL.npy", targetAnglesFL)
# # numpy.save("data/targetAnglesBL.npy", targetAnglesBL)
# # exit()
#
#
# p.disconnect()
#
# numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
# numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)

simulation = SIMULATION()
simulation.Run()