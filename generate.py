import pyrosim.pyrosim as pyrosim 

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5*height

for i in range(-2, 3):
  for j in range(-2, 3):
    for k in range(0, 10):
      pyrosim.Send_Cube(name="Box", pos=[x+(i*length),y+(j*width),z+k*height] , size=[length*(0.9**k),width*(0.9**k),height*(0.9**k)])

pyrosim.End()