# Göksel Tokur
import numpy as np
from vpython import *

a1 = 1
a2 = 1
a3 = 1
a4 = 1
a5 = 0.5

T1 = 0
T2 = 0
T3 = 0

T1 = -(T1/180.0)*np.pi
T2 = -(T2/180.0)*np.pi
T3 = -(T3/180.0)*np.pi

R0_1 = [[np.cos(T1), -np.sin(T1), 0], [np.sin(T1), np.cos(T1), 0], [0, 0, 1]]
R1_2 = [[np.cos(T2), -np.sin(T2), 0], [np.sin(T2), np.cos(T2), 0], [0, 0, 1]]
R2_3 = [[np.cos(T3), -np.sin(T3), 0], [np.sin(T3), np.cos(T3), 0], [0, 0, 1]]

R0_2 = np.dot(R0_1, R1_2)

d0_1 = [[a2*np.cos(T1)], [a2*np.sin(T1)], [a1]]
d1_2 = [[a4*np.cos(T2)], [a4*np.sin(T2)], [a3]]
d2_3 = [[0], [0], [a5]]

H0_1 = np.concatenate((R0_1, d0_1), 1)
H0_1 = np.concatenate((H0_1, [[0,0,0,1]]), 0)

H1_2 = np.concatenate((R1_2, d1_2), 1)
H1_2 = np.concatenate((H1_2, [[0,0,0,1]]), 0)

H2_3 = np.concatenate((R2_3, d2_3), 1)
H2_3 = np.concatenate((H2_3, [[0,0,0,1]]), 0)

# Position of end effector
H0_2=np.dot(H0_1, H1_2)
H0_3=np.dot(H0_2, H2_3)

joint2_pos = vector((H0_1[:,3])[0], (H0_1[:,3])[2], (H0_1[:,3])[1])
joint3_pos = vector((H0_2[:,3])[0], (H0_2[:,3])[2], (H0_2[:,3])[1])
end_effector_pos = vector((H0_3[:,3])[0], (H0_3[:,3])[2], (H0_3[:,3])[1])

print('###########################################################')
print('Theta1: ', T1)
print('Theta2: ', T2)
print('H0_1: \n', H0_1)
print('H0_2: \n', H0_2)
print('H0_3: \n', H0_3)
print('Joint 2 Position: ', joint2_pos)
print('Joint 3 Position: ', joint3_pos)
print('End Effector Position', end_effector_pos)
print('###########################################################')


joint1 = cylinder(pos=vector(0,0,0), axis=vector(0,0.4,0), radius=0.1, color=color.red)
link11 = curve(pos=[joint1.pos, vector(0,a1,0)])
link12 = curve(pos=[vector(0,a1,0), joint2_pos])
joint2 = cylinder(pos=joint2_pos, axis=vector(0,0.4,0), radius=0.1, color=color.blue)
#print(joint2_pos)
link21 = curve(pos=[joint2.pos, vector(joint2.pos.x, joint2.pos.y+a3, joint2.pos.z)])
link22 = curve(pos=[vector(joint2.pos.x, joint2.pos.y+a3, joint2.pos.z), joint3_pos])
joint3 = box(pos=joint3_pos, length=0.2, height=0.2, width=0.2, color=color.yellow)
link31 = curve(pos=[joint3_pos, vector(joint3.pos.x, joint3.pos.y-a5, joint3.pos.z)])


def theta1(s):
    print(s.text, s.number)
    global T1
    global T2
    global T3
    t1 = s.number
    T1 = t1
    t2 = T2
    t3 = T3

    t1 = -(t1/180.0)*np.pi
    t2 = -(t2/180.0)*np.pi
    t3 = -(t3/180.0)*np.pi

    R0_1 = [[np.cos(t1), -np.sin(t1), 0], [np.sin(t1), np.cos(t1), 0], [0, 0, 1]]
    R1_2 = [[np.cos(t2), -np.sin(t2), 0], [np.sin(t2), np.cos(t2), 0], [0, 0, 1]]
    R2_3 = [[np.cos(t3), -np.sin(t3), 0], [np.sin(t3), np.cos(t3), 0], [0, 0, 1]]

    R0_2 = np.dot(R0_1, R1_2)

    d0_1 = [[a2*np.cos(t1)], [a2*np.sin(t1)], [a1]]
    d1_2 = [[a4*np.cos(t2)], [a4*np.sin(t2)], [a3]]
    d2_3 = [[0], [0], [a5]]

    H0_1 = np.concatenate((R0_1, d0_1), 1)
    H0_1 = np.concatenate((H0_1, [[0,0,0,1]]), 0)

    H1_2 = np.concatenate((R1_2, d1_2), 1)
    H1_2 = np.concatenate((H1_2, [[0,0,0,1]]), 0)

    H2_3 = np.concatenate((R2_3, d2_3), 1)
    H2_3 = np.concatenate((H2_3, [[0,0,0,1]]), 0)

    # Position of end effector
    H0_2=np.dot(H0_1, H1_2)
    H0_3=np.dot(H0_2, H2_3)

    joint2_pos = vector((H0_1[:,3])[0], (H0_1[:,3])[2], (H0_1[:,3])[1])
    joint3_pos = vector((H0_2[:,3])[0], (H0_2[:,3])[2], (H0_2[:,3])[1])
    end_effector_pos = vector((H0_3[:,3])[0], (H0_3[:,3])[2], (H0_3[:,3])[1])

    link11.modify(0, pos=joint1.pos)
    link11.modify(1, pos=vector(0,a1,0))
    link12.modify(0, pos=vector(0,a1,0))
    link12.modify(1, pos=joint2_pos)
    joint2.pos = joint2_pos
    link21.modify(0, pos=joint2.pos)
    link21.modify(1, pos=vector(joint2.pos.x, joint2.pos.y+a3, joint2.pos.z))
    link22.modify(0, pos=vector(joint2.pos.x, joint2.pos.y+a3, joint2.pos.z))
    link22.modify(1, pos=joint3_pos)
    #joint3 = box(pos=joint3_pos, length=0.2, height=0.2, width=0.2)
    joint3.pos = joint3_pos
    #link31 = curve(pos=[joint3_pos, vector(joint3.pos.x, joint3.pos.y-a5, joint3.pos.z)])
    link31.modify(0, pos=joint3_pos)
    link31.modify(1, pos=vector(joint3.pos.x, joint3.pos.y-a5, joint3.pos.z))

    print('###########################################################')
    print('Theta1: ', T1)
    print('Theta2: ', T2)
    print('H0_1: \n', H0_1)
    print('H0_2: \n', H0_2)
    print('H0_3: \n', H0_3)
    print('Joint 2 Position: ', joint2_pos)
    print('Joint 3 Position: ', joint3_pos)
    print('End Effector Position', end_effector_pos)
    print('###########################################################')

scene.append_to_caption('\n\nJoint 1 - Theta 1\n')   
winput( bind=theta1 )

def theta2(s):
    print(s.text, s.number)
    global T1
    global T2
    global T3
    t1 = T1
    t2 = s.number
    T2 = t2
    t3 = T3


    t1 = -(t1/180.0)*np.pi
    t2 = -(t2/180.0)*np.pi
    t3 = -(t3/180.0)*np.pi

    R0_1 = [[np.cos(t1), -np.sin(t1), 0], [np.sin(t1), np.cos(t1), 0], [0, 0, 1]]
    R1_2 = [[np.cos(t2), -np.sin(t2), 0], [np.sin(t2), np.cos(t2), 0], [0, 0, 1]]
    R2_3 = [[np.cos(t3), -np.sin(t3), 0], [np.sin(t3), np.cos(t3), 0], [0, 0, 1]]

    R0_2 = np.dot(R0_1, R1_2)

    d0_1 = [[a2*np.cos(t1)], [a2*np.sin(t1)], [a1]]
    d1_2 = [[a4*np.cos(t2)], [a4*np.sin(t2)], [a3]]
    d2_3 = [[0], [0], [a5]]

    H0_1 = np.concatenate((R0_1, d0_1), 1)
    H0_1 = np.concatenate((H0_1, [[0,0,0,1]]), 0)

    H1_2 = np.concatenate((R1_2, d1_2), 1)
    H1_2 = np.concatenate((H1_2, [[0,0,0,1]]), 0)

    H2_3 = np.concatenate((R2_3, d2_3), 1)
    H2_3 = np.concatenate((H2_3, [[0,0,0,1]]), 0)

    # Position of end effector
    H0_2=np.dot(H0_1, H1_2)
    H0_3=np.dot(H0_2, H2_3)

    joint2_pos = vector((H0_1[:,3])[0], (H0_1[:,3])[2], (H0_1[:,3])[1])
    joint3_pos = vector((H0_2[:,3])[0], (H0_2[:,3])[2], (H0_2[:,3])[1])
    end_effector_pos = vector((H0_3[:,3])[0], (H0_3[:,3])[2], (H0_3[:,3])[1])

    link11.modify(0, pos=joint1.pos)
    link11.modify(1, pos=vector(0,a1,0))
    link12.modify(0, pos=vector(0,a1,0))
    link12.modify(1, pos=joint2_pos)
    joint2.pos = joint2_pos
    link21.modify(0, pos=joint2.pos)
    link21.modify(1, pos=vector(joint2.pos.x, joint2.pos.y+a3, joint2.pos.z))
    link22.modify(0, pos=vector(joint2.pos.x, joint2.pos.y+a3, joint2.pos.z))
    link22.modify(1, pos=joint3_pos)
    #joint3 = box(pos=joint3_pos, length=0.2, height=0.2, width=0.2)
    joint3.pos = joint3_pos
    #link31 = curve(pos=[joint3_pos, vector(joint3.pos.x, joint3.pos.y-a5, joint3.pos.z)])
    link31.modify(0, pos=joint3_pos)
    link31.modify(1, pos=vector(joint3.pos.x, joint3.pos.y-a5, joint3.pos.z))

    print('###########################################################')
    print('Theta1: ', T1)
    print('Theta2: ', T2)
    print('H0_1: \n', H0_1)
    print('H0_2: \n', H0_2)
    print('H0_3: \n', H0_3)
    print('Joint 2 Position: ', joint2_pos)
    print('Joint 3 Position: ', joint3_pos)
    print('End Effector Position', end_effector_pos)
    print('###########################################################')

scene.append_to_caption('\n\nJoint 2 - Theta 2\n')   
winput( bind=theta2 )

scene.append_to_caption('\n\nWrite angles and hit enter to manipulate joints.\n')   