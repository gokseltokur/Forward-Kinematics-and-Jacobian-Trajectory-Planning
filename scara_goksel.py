from vpython import *
import math
import numpy as np

scene.width = scene.height = 600
scene.range = 1.8
CURRENT_JOINT1 = 0

def rotation_y(input_vector, angle):
    x = input_vector.x * cos(angle) + input_vector.z * sin(angle)
    y = input_vector.y
    z = input_vector.x * (-sin(angle)) + input_vector.z * cos(angle)
    return vector(x, y, z)

def joint1_rotation(s):
    global CURRENT_JOINT1
    degree_to_radian = radians(s.value)
    degree_to_radian = degree_to_radian - CURRENT_JOINT1
    wt.text = '{:1.0f}'.format(s.value)
    #joint1.axis = rotation_y(joint1.axis, degree_to_radian)
    link11.axis = rotation_y(link11.axis, degree_to_radian)
    link12.axis = rotation_y(link12.axis, degree_to_radian)
    joint2.pos = rotation_y(joint2.pos, degree_to_radian)
    link21.axis = rotation_y(link21.pos, degree_to_radian)
    link22.axis = rotation_y(link22.pos, degree_to_radian)
    CURRENT_JOINT1 = radians(s.value)

def joint2_rotation(s):
    global CURRENT_JOINT1
    degree_to_radian = radians(s.value)
    degree_to_radian = degree_to_radian - CURRENT_JOINT1
    wt.text = '{:1.0f}'.format(s.value)
    joint1.axis = rotation_y(joint1.axis, degree_to_radian)
    link11.axis = rotation_y(link11.axis, degree_to_radian)
    link12.axis = rotation_y(link12.axis, degree_to_radian)
    CURRENT_JOINT1 = radians(s.value)

joint1 = cylinder(pos=vector(0,0,0), axis=vector(0,0.4,0), radius=0.1)
link11 = cylinder(pos=vector(joint1.pos.x, joint1.pos.y+0.4, joint1.pos.z), axis=vector(0,0.4,0), radius=0.01)
link12 = cylinder(pos=vector(link11.pos.x, link11.pos.y+0.4, link11.pos.z), axis=vector(0.4,0,0), radius=0.01)


joint2 = cylinder(pos=vector(0.4, joint1.pos.y+0.4+0.2, 0), axis=vector(0,0.4,0), radius=0.1)
link21 = cylinder(pos=vector(joint2.pos.x, joint2.pos.y+0.4, joint2.pos.z), axis=vector(0,0.4,0), radius=0.01)
link22 = cylinder(pos=vector(link21.pos.x, link21.pos.y+0.4, link21.pos.z), axis=vector(0.4,0,0), radius=0.01)


scene.append_to_caption('\nJoint 1\n\n')
slider1 = slider(min=0, max=360, value=0, length=360, bind=joint1_rotation, right=15)
wt = wtext(text='{:1.0f}'.format(slider1.value))


scene.append_to_caption('\nJoint 2\n\n')
slider2 = slider(min=0, max=360, value=0, length=360, bind=joint2_rotation, right=15)
wt = wtext(text='{:1.0f}'.format(slider2.value))