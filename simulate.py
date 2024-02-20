import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random

ITERATIONS = 1000

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-98)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(ITERATIONS)
frontLegSensorValues = numpy.zeros(ITERATIONS)

targetAngles = numpy.sin(numpy.linspace(0, 2*numpy.pi, ITERATIONS))
numpy.save("data/targetAngles.npy", targetAngles)
exit()

for i in range(0, ITERATIONS):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    tgtPos = (random.random() * numpy.pi) - (numpy.pi / 2)
    pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = tgtPos,
        maxForce = 150
    )
    tgtPos = (random.random() * numpy.pi) - (numpy.pi / 2)
    pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = tgtPos,
        maxForce = 150
    )

    time.sleep(1/60)

p.disconnect()

numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)