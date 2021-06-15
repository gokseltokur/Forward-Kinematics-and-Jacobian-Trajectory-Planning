# Göksel Tokur
import numpy as np
from vpython import *

def rotation_y(input_vector, angle):
    x = input_vector.x * cos(angle) + input_vector.z * sin(angle)
    y = input_vector.y
    z = input_vector.x * (-sin(angle)) + input_vector.z * cos(angle)
    return vector(x, y, z)

a1 = 1
a2 = 1
a3 = 1

T1 = 0
T2 = 0
T3 = 0

T1 = -(T1/180.0)*np.pi
T2 = (T2/180.0)*np.pi
T3 = -(T3/180.0)*np.pi


R0_1 = [[np.cos(T1), 0, np.sin(T1)], [np.sin(T1), 0, -np.cos(T1)], [0, 1, 0]]
R1_2 = [[np.cos(T2), np.sin(T2), 0], [np.sin(T2), -np.cos(T2), 0], [0, 0, -1]]
R2_3 = [[np.cos(T3), -np.sin(T3), 0], [np.sin(T3), np.cos(T3), 0], [0, 0, 1]]

R0_2 = np.dot(R0_1, R1_2)
R0_3 = np.dot(R0_2, R2_3)

d0_1 = [[0], [0], [a1]]
d1_2 = [[a2*np.cos(T2)], [a2*np.sin(T2)], [0]]
d2_3 = [[a3*np.cos(T3)], [a3*np.sin(T3)], [0]]

H0_1 = np.concatenate((R0_1, d0_1), 1)
H0_1 = np.concatenate((H0_1, [[0,0,0,1]]), 0)

H1_2 = np.concatenate((R1_2, d1_2), 1)
H1_2 = np.concatenate((H1_2, [[0,0,0,1]]), 0)

H2_3 = np.concatenate((R2_3, d2_3), 1)
H2_3 = np.concatenate((H2_3, [[0,0,0,1]]), 0)


H0_2 = np.dot(H0_1, H1_2) 
H0_3 = np.dot(H0_2, H2_3) # Position of end effector


joint1_pos = vector((H0_1[:,3])[0], (H0_1[:,3])[2], (H0_1[:,3])[1])
joint2_pos = vector((H0_2[:,3])[0], (H0_2[:,3])[2], (H0_2[:,3])[1])
end_effector_pos = vector((H0_3[:,3])[0], (H0_3[:,3])[2], (H0_3[:,3])[1])

print('###########################################################')
print('Theta1: ', T1)
print('Theta2: ', T2)
print('Theta3: ', T3)
print('H0_1: \n', H0_1)
print('H0_2: \n', H0_2)
print('H0_3: \n', H0_3)
print('Joint 2 Position: ', joint1_pos)
print('Joint 3 Position: ', joint2_pos)
print('End Effector Position', end_effector_pos)
print('###########################################################')

joint0 = cylinder(pos=vector(0,0,0), axis=vector(0,0.4,0), radius=0.1, color=color.red)
link00 = curve(pos=[joint0.pos, vector(0,a1,0)])
joint1_axis = rotation_y(vector(0,0,-0.4), -T1)
joint1 = cylinder(pos=joint1_pos, axis=joint1_axis, radius=0.1, color=color.yellow)
link10 = curve(pos=[joint1.pos, joint2_pos])
joint2_axis = rotation_y(vector(0,0,-0.4), -T1)
joint2 = cylinder(pos=joint2_pos, axis=joint2_axis, radius=0.1, color=color.blue)
link20 = curve(pos=[joint2.pos, end_effector_pos])

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
    t2 = (t2/180.0)*np.pi
    t3 = -(t3/180.0)*np.pi


    R0_1 = [[np.cos(t1), 0, np.sin(t1)], [np.sin(t1), 0, -np.cos(t1)], [0, 1, 0]]
    R1_2 = [[np.cos(t2), np.sin(t2), 0], [np.sin(t2), -np.cos(t2), 0], [0, 0, -1]]
    R2_3 = [[np.cos(t3), -np.sin(t3), 0], [np.sin(t3), np.cos(t3), 0], [0, 0, 1]]

    R0_2 = np.dot(R0_1, R1_2)
    R0_3 = np.dot(R0_2, R2_3)

    d0_1 = [[0], [0], [a1]]
    d1_2 = [[a2*np.cos(t2)], [a2*np.sin(t2)], [0]]
    d2_3 = [[a3*np.cos(t3)], [a3*np.sin(t3)], [0]]

    H0_1 = np.concatenate((R0_1, d0_1), 1)
    H0_1 = np.concatenate((H0_1, [[0,0,0,1]]), 0)

    H1_2 = np.concatenate((R1_2, d1_2), 1)
    H1_2 = np.concatenate((H1_2, [[0,0,0,1]]), 0)

    H2_3 = np.concatenate((R2_3, d2_3), 1)
    H2_3 = np.concatenate((H2_3, [[0,0,0,1]]), 0)


    H0_2 = np.dot(H0_1, H1_2) 
    H0_3 = np.dot(H0_2, H2_3) # Position of end effector

    joint1_pos = vector((H0_1[:,3])[0], (H0_1[:,3])[2], (H0_1[:,3])[1])
    joint2_pos = vector((H0_2[:,3])[0], (H0_2[:,3])[2], (H0_2[:,3])[1])
    end_effector_pos = vector((H0_3[:,3])[0], (H0_3[:,3])[2], (H0_3[:,3])[1])

    #joint0 = cylinder(pos=vector(0,0,0), axis=vector(0,0.4,0), radius=0.1)
    link00.modify(0, joint0.pos) #(pos=[joint0.pos, vector(0,a1,0)])
    link00.modify(1, vector(0,a1,0))

    joint1_axis = rotation_y(vector(0,0,-0.4), -t1)
    #joint1 = cylinder(pos=joint1_pos, axis=joint1_axis, radius=0.1)
    joint1.pos = joint1_pos
    joint1.axis = joint1_axis

    #link10 = curve(pos=[joint1.pos, joint2_pos])
    link10.modify(0, joint1.pos)
    link10.modify(1, joint2_pos)

    #link11 = curve(pos=[vector(joint1.pos.x, joint1.pos.y, joint1.pos.z-0.4), vector(joint2_pos.x, joint2_pos.y, joint2_pos.z-0.4)])

    joint2_axis = rotation_y(vector(0,0,-0.4), -t1)
    #joint2 = cylinder(pos=joint2_pos, axis=joint2_axis, radius=0.1)
    joint2.pos = joint2_pos
    joint2.axis = joint2_axis


    #link20 = curve(pos=[joint2.pos, end_effector_pos])
    link20.modify(0, joint2.pos)
    link20.modify(1, end_effector_pos)

    print('###########################################################')
    print('Theta1: ', T1)
    print('Theta2: ', T2)
    print('Theta3: ', T3)
    print('H0_1: \n', H0_1)
    print('H0_2: \n', H0_2)
    print('H0_3: \n', H0_3)
    print('Joint 2 Position: ', joint1_pos)
    print('Joint 3 Position: ', joint2_pos)
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
    t2 = (t2/180.0)*np.pi
    t3 = -(t3/180.0)*np.pi


    R0_1 = [[np.cos(t1), 0, np.sin(t1)], [np.sin(t1), 0, -np.cos(t1)], [0, 1, 0]]
    R1_2 = [[np.cos(t2), np.sin(t2), 0], [np.sin(t2), -np.cos(t2), 0], [0, 0, -1]]
    R2_3 = [[np.cos(t3), -np.sin(t3), 0], [np.sin(t3), np.cos(t3), 0], [0, 0, 1]]

    R0_2 = np.dot(R0_1, R1_2)
    R0_3 = np.dot(R0_2, R2_3)

    d0_1 = [[0], [0], [a1]]
    d1_2 = [[a2*np.cos(t2)], [a2*np.sin(t2)], [0]]
    d2_3 = [[a3*np.cos(t3)], [a3*np.sin(t3)], [0]]

    H0_1 = np.concatenate((R0_1, d0_1), 1)
    H0_1 = np.concatenate((H0_1, [[0,0,0,1]]), 0)

    H1_2 = np.concatenate((R1_2, d1_2), 1)
    H1_2 = np.concatenate((H1_2, [[0,0,0,1]]), 0)

    H2_3 = np.concatenate((R2_3, d2_3), 1)
    H2_3 = np.concatenate((H2_3, [[0,0,0,1]]), 0)


    H0_2 = np.dot(H0_1, H1_2) 
    H0_3 = np.dot(H0_2, H2_3) # Position of end effector

    joint1_pos = vector((H0_1[:,3])[0], (H0_1[:,3])[2], (H0_1[:,3])[1])
    joint2_pos = vector((H0_2[:,3])[0], (H0_2[:,3])[2], (H0_2[:,3])[1])
    end_effector_pos = vector((H0_3[:,3])[0], (H0_3[:,3])[2], (H0_3[:,3])[1])

    #joint0 = cylinder(pos=vector(0,0,0), axis=vector(0,0.4,0), radius=0.1)
    link00.modify(0, joint0.pos) #(pos=[joint0.pos, vector(0,a1,0)])
    link00.modify(1, vector(0,a1,0))

    joint1_axis = rotation_y(vector(0,0,-0.4), -t1)
    #joint1 = cylinder(pos=joint1_pos, axis=joint1_axis, radius=0.1)
    joint1.pos = joint1_pos
    joint1.axis = joint1_axis

    #link10 = curve(pos=[joint1.pos, joint2_pos])
    link10.modify(0, joint1.pos)
    link10.modify(1, joint2_pos)

    #link11 = curve(pos=[vector(joint1.pos.x, joint1.pos.y, joint1.pos.z-0.4), vector(joint2_pos.x, joint2_pos.y, joint2_pos.z-0.4)])

    joint2_axis = rotation_y(vector(0,0,-0.4), -t1)
    #joint2 = cylinder(pos=joint2_pos, axis=joint2_axis, radius=0.1)
    joint2.pos = joint2_pos
    joint2.axis = joint2_axis


    #link20 = curve(pos=[joint2.pos, end_effector_pos])
    link20.modify(0, joint2.pos)
    link20.modify(1, end_effector_pos)

    print('###########################################################')
    print('Theta1: ', T1)
    print('Theta2: ', T2)
    print('Theta3: ', T3)
    print('H0_1: \n', H0_1)
    print('H0_2: \n', H0_2)
    print('H0_3: \n', H0_3)
    print('Joint 2 Position: ', joint1_pos)
    print('Joint 3 Position: ', joint2_pos)
    print('End Effector Position', end_effector_pos)
    print('###########################################################')

scene.append_to_caption('\n\nJoint 2 - Theta 2\n')   
winput( bind=theta2 )



def theta3(s):
    print(s.text, s.number)
    global T1
    global T2
    global T3
    t1 = T1
    t2 = T2
    t3 = s.number
    T3 = t3

    t1 = -(t1/180.0)*np.pi
    t2 = (t2/180.0)*np.pi
    t3 = -(t3/180.0)*np.pi


    R0_1 = [[np.cos(t1), 0, np.sin(t1)], [np.sin(t1), 0, -np.cos(t1)], [0, 1, 0]]
    R1_2 = [[np.cos(t2), np.sin(t2), 0], [np.sin(t2), -np.cos(t2), 0], [0, 0, -1]]
    R2_3 = [[np.cos(t3), -np.sin(t3), 0], [np.sin(t3), np.cos(t3), 0], [0, 0, 1]]

    R0_2 = np.dot(R0_1, R1_2)
    R0_3 = np.dot(R0_2, R2_3)

    d0_1 = [[0], [0], [a1]]
    d1_2 = [[a2*np.cos(t2)], [a2*np.sin(t2)], [0]]
    d2_3 = [[a3*np.cos(t3)], [a3*np.sin(t3)], [0]]

    H0_1 = np.concatenate((R0_1, d0_1), 1)
    H0_1 = np.concatenate((H0_1, [[0,0,0,1]]), 0)

    H1_2 = np.concatenate((R1_2, d1_2), 1)
    H1_2 = np.concatenate((H1_2, [[0,0,0,1]]), 0)

    H2_3 = np.concatenate((R2_3, d2_3), 1)
    H2_3 = np.concatenate((H2_3, [[0,0,0,1]]), 0)


    H0_2 = np.dot(H0_1, H1_2) 
    H0_3 = np.dot(H0_2, H2_3) # Position of end effector

    joint1_pos = vector((H0_1[:,3])[0], (H0_1[:,3])[2], (H0_1[:,3])[1])
    joint2_pos = vector((H0_2[:,3])[0], (H0_2[:,3])[2], (H0_2[:,3])[1])
    end_effector_pos = vector((H0_3[:,3])[0], (H0_3[:,3])[2], (H0_3[:,3])[1])

    #joint0 = cylinder(pos=vector(0,0,0), axis=vector(0,0.4,0), radius=0.1)
    link00.modify(0, joint0.pos) #(pos=[joint0.pos, vector(0,a1,0)])
    link00.modify(1, vector(0,a1,0))

    joint1_axis = rotation_y(vector(0,0,-0.4), -t1)
    #joint1 = cylinder(pos=joint1_pos, axis=joint1_axis, radius=0.1)
    joint1.pos = joint1_pos
    joint1.axis = joint1_axis

    #link10 = curve(pos=[joint1.pos, joint2_pos])
    link10.modify(0, joint1.pos)
    link10.modify(1, joint2_pos)

    #link11 = curve(pos=[vector(joint1.pos.x, joint1.pos.y, joint1.pos.z-0.4), vector(joint2_pos.x, joint2_pos.y, joint2_pos.z-0.4)])

    joint2_axis = rotation_y(vector(0,0,-0.4), -t1)
    #joint2 = cylinder(pos=joint2_pos, axis=joint2_axis, radius=0.1)
    joint2.pos = joint2_pos
    joint2.axis = joint2_axis


    #link20 = curve(pos=[joint2.pos, end_effector_pos])
    link20.modify(0, joint2.pos)
    link20.modify(1, end_effector_pos)

    print('###########################################################')
    print('Theta1: ', T1)
    print('Theta2: ', T2)
    print('Theta3: ', T3)
    print('H0_1: \n', H0_1)
    print('H0_2: \n', H0_2)
    print('H0_3: \n', H0_3)
    print('Joint 2 Position: ', joint1_pos)
    print('Joint 3 Position: ', joint2_pos)
    print('End Effector Position', end_effector_pos)
    print('###########################################################')

scene.append_to_caption('\n\nJoint 3 - Theta 3\n')   
winput( bind=theta3 )

scene.append_to_caption('\n\nWrite angles and hit enter to manipulate joints.\n')