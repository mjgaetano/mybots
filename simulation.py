from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import constants as c


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.G)

        self.world = WORLD()
        self.robot = ROBOT()

        pyrosim.Prepare_To_Simulate(self.robot.robotId)

    def Run(self):
        for i in range(0, c.ITERATIONS):
            p.stepSimulation()
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            #
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=self.robot.robotId,
            #     jointName=b'Torso_BackLeg',
            #     controlMode=p.POSITION_CONTROL,
            #     targetPosition=targetAnglesBL[i],
            #     maxForce=150
            # )
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=robotId,
            #     jointName=b'Torso_FrontLeg',
            #     controlMode=p.POSITION_CONTROL,
            #     targetPosition=targetAnglesFL[i],
            #     maxForce=150
            # )
            #
            time.sleep(1 / 60)
            print(i)
