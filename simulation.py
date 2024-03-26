from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import constants as c


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.G)

        self.world = WORLD()
        self.robot = ROBOT()

        # pyrosim.Prepare_To_Simulate(self.robot.robotId)

    def __del__(self):
        p.disconnect()

    def Run(self):
        for i in range(0, c.ITERATIONS):
            p.stepSimulation()

            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            time.sleep(c.SLEEP_TIME)

    def Get_Fitness(self):
        self.robot.Get_Fitness()