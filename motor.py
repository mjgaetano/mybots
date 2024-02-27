import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c


class MOTOR:
    def __init__(self, jointName):
        print(jointName)
        self.jointName = jointName
        self.values = numpy.zeros(c.ITERATIONS)

        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        # self.frequency = c.frequency
        if self.jointName == b'Torso_BackLeg':
            self.frequency = c.frequency
        else:
            self.frequency = c.frequency/2
        self.offset = c.phaseOffset

        self.values = self.amplitude * numpy.sin(
            self.frequency * numpy.linspace(0, 2 * numpy.pi, c.ITERATIONS) + self.offset)

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.values[t],
            maxForce=150
        )

    def Save_Values(self):
        numpy.save(f"data/targetAngles{self.jointName}.npy", self.values)