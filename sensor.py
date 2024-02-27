import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName

        self.values = numpy.zeros(c.ITERATIONS)

    def Get_Value(self, t):
        currValue = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        self.values[t] = currValue
        if t+1 == c.ITERATIONS:
            print(self.values)
        return currValue