
from vpython import *
import math
import numpy as np

scene.width = scene.height = 600
scene.range = 1.8

joint1 = cylinder(pos=vector(0,0,0), axis=vector(0,0.4,0), radius=0.1)
link11 = cylinder(pos=vector(joint1.pos.x, joint1.pos.y+0.4, joint1.pos.z), axis=vector(0,0.4,0), radius=0.01)
link12 = cylinder(pos=vector(link11.pos.x, link11.pos.y+0.4, link11.pos.z), axis=vector(0.4,0,0), radius=0.01)

#joint2 = cylinder(pos=vector(0.4, joint1.pos.y+0.3+0.2, 0), axis=vector(0,0.3,0), radius=0.1)
#link21 = cylinder(pos=vector(joint2.pos.x, joint2.pos.y+0.3, joint2.pos.z), axis=vector(0,0.4,0), radius=0.01)
#link22 = cylinder(pos=vector(joint2.pos.x, joint2.pos.y+0.3+0.4, joint2.pos.z), axis=vector(0.4,0,0), radius=0.01)

current_radian = 0
def set_angles(s):
    degree_to_radian = radians(s.value)
    global current_radian
    degree_to_radian = degree_to_radian - current_radian
    wt1.text = '{:1.0f}'.format(s.value)
    joint1.axis = rotation_y(joint1.axis, degree_to_radian)
    link11.axis = rotation_y(link11.axis, degree_to_radian)
    link12.axis = rotation_y(link12.axis, degree_to_radian)
    current_radian = radians(s.value)
    #joint1.rotate(angle=sl1.value, axis=vector(0,1,0))

current_radian = 0
def joint1_rotation(s):
    degree_to_radian = radians(s.value)
    global current_radian
    degree_to_radian = degree_to_radian - current_radian
    wt.text = '{:1.0f}'.format(s.value)
    joint1.axis = rotation_y(joint1.axis, degree_to_radian)
    link11.axis = rotation_y(link11.axis, degree_to_radian)
    link12.axis = rotation_y(link12.axis, degree_to_radian)
    current_radian = radians(s.value)

scene.append_to_caption('\nTheta 0 \n\n') 
sl1 = slider(min=0, max=360, value=0, length=500, bind=set_angles, right=15)
wt1 = wtext(text='{:1.0f}'.format(sl1.value))


def rotation_y(input_vector, angle):
    x = input_vector.x * cos(angle) + input_vector.z * sin(angle)
    y = input_vector.y
    z = input_vector.x * (-sin(angle)) + input_vector.z * cos(angle)
    return vector(x, y, z)

#sl2 = slider(min=0, max=360, value=0, length=500, bind=set_angles, right=15)
#wt2 = wtext(text='{:1.2f}'.format(sl2.value))


#joint2 = cylinder(pos=vector(0,0,0), axis=vector(0,1,0), radius=1)
#joint3 = cylinder(pos=vector(0,0,0), axis=vector(0,1,0), radius=1)