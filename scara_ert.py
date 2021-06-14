from vpython import *
import math
import numpy as np

scene.width = scene.height = 600
scene.range = 1.8

joint = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0.3, 0), radius=0.1)
link = cylinder(pos=vector(joint.pos.x, joint.pos.y + 0.3, joint.pos.z), axis=vector(0, .3, 0), radius=0.01)
link1 = cylinder(pos=vector(link.pos.x, link.pos.y + 0.3, link.pos.z), axis=vector(0.6, 0, 0), radius=0.01)

last_rad = 0


def setTheta(s):
    rad = radians(s.value)
    global last_rad
    rad = rad - last_rad
    wt.text = '{:1.0f}'.format(s.value)
    joint.axis = Ry(joint.axis, rad)
    link.axis = Ry(link.axis, rad)
    link1.axis = Ry(link1.axis, rad)
    joint2.pos = Ry(joint2.pos, rad)
    link2.pos = Ry(link2.pos, rad)
    link21.pos = Ry(link21.pos, rad)
    link21.axis = Ry(link21.axis, rad)
    link22.pos = Ry(link22.pos, rad)
    m_box.axis = Ry(m_box.axis, rad)
    m_box.pos = Ry(m_box.pos, rad)
    link3.pos = Ry(link3.pos, rad)
    last_rad = radians(s.value)


scene.append_to_caption('\nTheta 0 \n\n')
theta = slider(min=0, max=360, value=0, length=360, bind=setTheta, right=15)
wt = wtext(text='{:1.0f}'.format(theta.value))
scene.append_to_caption(' degrees\n')


joint2 = cylinder(pos=vector(link1.pos.x + 0.6, link1.pos.y - 0.15,
                             link1.pos.z), axis=vector(0, 0.3, 0), radius=0.1, color=color.cyan)
link2 = cylinder(pos=vector(joint2.pos.x, joint2.pos.y + 0.3,
                            joint2.pos.z), axis=vector(0, .3, 0), radius=0.01, color=color.cyan)
link21 = cylinder(pos=vector(link2.pos.x, link2.pos.y + 0.3,
                             link2.pos.z), axis=vector(0.6, 0, 0), radius=0.01, color=color.cyan)
link22 = cylinder(pos=vector(link21.pos.x + 0.6, link21.pos.y - 0.1,
                             link21.pos.z), axis=vector(0, 0.1, 0), radius=0.01, color=color.cyan)

last_rad1 = 0


def setTheta1(s):
    rad = radians(s.value)
    global last_rad1
    rad = rad - last_rad1
    wt1.text = '{:1.0f}'.format(s.value)
    joint2.axis = Ry(joint2.axis, rad)
    link2.axis = Ry(link2.axis, rad)
    link21.axis = Ry(link21.axis, rad)

    # Translate as the object rotates on origin (0, 0, 0)
    vec = Ry(vector(link22.pos.x - link2.pos.x,
                    link22.pos.y, link22.pos.z - link2.pos.z), rad)
    # Then translate back where it suppose to be
    link22.pos = vector(vec.x + link2.pos.x,
                        vec.y, vec.z + link2.pos.z)

    # Translate as the object rotates on origin (0, 0, 0)
    vec1 = Ry(vector(m_box.pos.x - link2.pos.x,
                     m_box.pos.y, m_box.pos.z - link2.pos.z), rad)
    # Then translate back where it suppose to be
    m_box.pos = vector(vec1.x + link2.pos.x,
                       vec1.y, vec1.z + link2.pos.z)
    m_box.axis = Ry(m_box.axis, rad)

    # Translate as the object rotates on origin (0, 0, 0)
    vec2 = Ry(vector(link3.pos.x - link2.pos.x,
                     link3.pos.y, link3.pos.z - link2.pos.z), rad)
    # Then translate back where it suppose to be
    link3.pos = vector(vec2.x + link2.pos.x,
                       vec2.y, vec2.z + link2.pos.z)

    last_rad1 = radians(s.value)
    # trail.append(link1.pos+link1.axis)


scene.append_to_caption('\nTheta 1 \n\n')
theta1 = slider(min=0, max=360, value=0, length=360, bind=setTheta1, right=15)
wt1 = wtext(text='{:1.0f}'.format(theta1.value))
scene.append_to_caption(' degrees\n')

m_box = box(pos=vector(link22.pos.x, link22.pos.y - 0.1,
                       link22.pos.z), length=.2, height=.2, width=.2, color=color.green)

link3 = cylinder(pos=vector(m_box.pos.x, m_box.pos.y - .2, m_box.pos.z),
                 axis=vector(0, 0.1, 0), radius=0.01, color=color.green)

scene.append_to_caption('\nAlpha \n\n')
theta1 = slider(min=0, max=100, value=10, length=360, bind=setTheta1, right=15)
wt2 = wtext(text='{:1.0f}'.format(theta1.value))
scene.append_to_caption(' degrees\n')


def Rx(v, angle):
    new_y = cos(angle) * v.y - sin(angle) * v.z
    new_z = sin(angle) * v.y + cos(angle) * v.z
    return vector(v.x, new_y, new_z)


def Ry(v, angle):
    new_x = cos(angle) * v.x + sin(angle) * v.z
    new_z = -sin(angle) * v.x + cos(angle) * v.z
    return vector(new_x, v.y, new_z)


def Rz(v, angle):
    new_x = cos(angle) * v.y - sin(angle) * v.z
    new_y = sin(angle) * v.y + cos(angle) * v.z
    return vector(new_x, new_y, v.z)
