import pyrosim.pyrosim as pyrosim 

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5*height

for i in range(0, 10):
    pyrosim.Send_Cube(name="Box", pos=[x,y,z+i*height] , size=[length*(0.9**i),width*(0.9**i),height*(0.9**i)])
#pyrosim.Send_Cube(name="Box2", pos=[x+length,y,z+height] , size=[length,width,height])

pyrosim.End()