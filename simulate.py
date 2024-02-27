from simulation import SIMULATION
# import pybullet as p
# import pybullet_data
# import time
# import pyrosim.pyrosim as pyrosim
# import numpy
# import random
# import constants as c
#
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
#
# p.setGravity(0,0,c.G)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
#
# p.loadSDF("world.sdf")
#
# pyrosim.Prepare_To_Simulate(robotId)
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
# for i in range(0, c.ITERATIONS):
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#
#     pyrosim.Set_Motor_For_Joint(
# 	bodyIndex = robotId,
#         jointName = b'Torso_BackLeg',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = targetAnglesBL[i],
#         maxForce = 150
#     )
#     pyrosim.Set_Motor_For_Joint(
# 	bodyIndex = robotId,
#         jointName = b'Torso_FrontLeg',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = targetAnglesFL[i],
#         maxForce = 150
#     )
#
#     time.sleep(1/60)
#
# p.disconnect()
#
# numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
# numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)

simulation = SIMULATION()