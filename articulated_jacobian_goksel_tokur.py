# Göksel Tokur
import numpy as np
from vpython import *
import time

a1 = 1
a2 = 1
a3 = 1

T1 = 0
T2 = 60
T3 = -90

T1 = -(T1/180.0)*np.pi
T2 = (T2/180.0)*np.pi
T3 = -(T3/180.0)*np.pi

t = 0
v = 2*np.pi/100
R = 1


trail = curve(color=color.cyan, radius= .01)


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





def rotation_y(input_vector, angle):
    x = input_vector.x * cos(angle) + input_vector.z * sin(angle)
    y = input_vector.y
    z = input_vector.x * (-sin(angle)) + input_vector.z * cos(angle)
    return vector(x, y, z)


joint0 = cylinder(pos=vector(0,0,0), axis=vector(0,0.4,0), radius=0.1, color=color.red)
link00 = curve(pos=[joint0.pos, vector(0,a1,0)])
joint1_axis = rotation_y(vector(0,0,-0.4), -T1)
joint1 = cylinder(pos=joint1_pos, axis=joint1_axis, radius=0.1, color=color.yellow)
link10 = curve(pos=[joint1.pos, joint2_pos])
joint2_axis = rotation_y(vector(0,0,-0.4), -T1)
joint2 = cylinder(pos=joint2_pos, axis=joint2_axis, radius=0.1, color=color.blue)
link20 = curve(pos=[joint2.pos, end_effector_pos])

axisx = curve(pos=[vector(0,0,0), vector(5,0,0)], color=color.orange)
axisy = curve(pos=[vector(0,0,0), vector(0,5,0)], color=color.green)
axisz = curve(pos=[vector(0,0,0), vector(0,0,5)], color=color.blue)

def draw_line():
    global T1
    global T2
    global T3
    global t
    global v
    global R


        
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


    #joint1_pos = vector((H0_1[:,3])[0], (H0_1[:,3])[2], (H0_1[:,3])[1])
    #joint2_pos = vector((H0_2[:,3])[0], (H0_2[:,3])[2], (H0_2[:,3])[1])
    #end_effector_pos = vector((H0_3[:,3])[0], (H0_3[:,3])[2], (H0_3[:,3])[1])

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


    print('### JACOBIAN ###')
    I = [[1,0,0],[0,1,0],[0,0,1]]
    m0_0_1 = [[0],[0],[1]]
    JR_0_1 = H0_1[:3,:3]
    JD_0_1 = H0_1[0:3,3]
    JR_0_2 = H0_2[:3,:3]
    JD_0_2 = H0_2[0:3,3]
    JR_0_3 = H0_3[:3,:3]
    JD_0_3 = H0_3[0:3,3]
    print(JD_0_1, JD_0_2, JD_0_3)

    # Joint1
    J_joint1_up = np.cross(np.dot(I, m0_0_1), JD_0_3, axis=0)
    J_joint1_down = np.dot(I, m0_0_1)
    J_joint1 = np.concatenate((J_joint1_up, J_joint1_down), axis=0)
    print(J_joint1)

    # Joint2
    J_joint2_up = np.cross(np.dot(JR_0_1, m0_0_1), (JD_0_3-JD_0_1), axis=0)
    J_joint2_down = np.dot(JR_0_1, m0_0_1)
    J_joint2 = np.concatenate((J_joint2_up, J_joint2_down), axis=0)
    print(J_joint2)

    # Joint3
    J_joint3_up = np.cross(np.dot(JR_0_2, m0_0_1), (JD_0_3-JD_0_2), axis=0)
    J_joint3_down = np.dot(JR_0_2, m0_0_1)
    J_joint3 = np.concatenate((J_joint3_up, J_joint3_down), axis=0)
    print(J_joint3)

    J = np.concatenate((J_joint1, J_joint2, J_joint3), axis=1)
    print(J)

    while True:
        rate(10)

        #point_on_line = [1, 0, 0]

        dot_matrix = [[-R*v*np.sin((v)*100)], [R*v*np.cos((v)*100)], [0]]

        #dot_matrix = [[-v/sqrt(2)], [-v/sqrt(2)], [0]]
        #print(np.delete(J[:3,:3], 1, 0))
        #print(J[:3,:3])
        #print(np.linalg.pinv(J[:3,:3]))
        theta_dot_matrix = np.dot(np.linalg.inv(J[:3,:3]), dot_matrix)
        print(theta_dot_matrix)

        print(theta_dot_matrix[0][0]*t, theta_dot_matrix[1][0]*t, theta_dot_matrix[2][0]*t)

        print(T1, T2, T3)
        T1 -= (theta_dot_matrix[0][0])*t
        T2 += (theta_dot_matrix[1][0])*t
        T3 -= (theta_dot_matrix[2][0])*t


        # T1 -= ((theta_dot_matrix[0][0]/180.0)*np.pi)*t
        # T2 += ((theta_dot_matrix[1][0]/180.0)*np.pi)*t
        # T3 -= ((theta_dot_matrix[2][0]/180.0)*np.pi)*t
        print(T1, T2, T3)

        theta1()
        theta2()
        theta3()

        t = t + 0.01
        if t == 1:
            t = 0


def theta1():
    #print("$$$$" + str(s))
    
    global T1
    global T2
    global T3
    print(T3)
    t1 = T1
    #T1 = t1
    t2 = T2
    t3 = T3
    print(t3)

    # t1 = -(t1/180.0)*np.pi
    # t2 = (t2/180.0)*np.pi
    # t3 = -(t3/180.0)*np.pi


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

    trail.append(end_effector_pos)

    # print('###########################################################')
    # print('Theta1: ', T1)
    # print('Theta2: ', T2)
    # print('Theta3: ', T3)
    # print('H0_1: \n', H0_1)
    # print('H0_2: \n', H0_2)
    # print('H0_3: \n', H0_3)
    # print('Joint 2 Position: ', joint1_pos)
    # print('Joint 3 Position: ', joint2_pos)
    # print('End Effector Position', end_effector_pos)
    # print('###########################################################')

#scene.append_to_caption('\n\nJoint 1 - Theta 1\n')   
#winput( bind=theta1 )


def theta2():
    #print("$$$$" + str(s))
    global T1
    global T2
    global T3
    t1 = T1
    t2 = T2
    #T2 = t2
    t3 = T3
    print(t3)

    # t1 = -(t1/180.0)*np.pi
    # t2 = (t2/180.0)*np.pi
    # t3 = -(t3/180.0)*np.pi


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

    # print('###########################################################')
    # print('Theta1: ', T1)
    # print('Theta2: ', T2)
    # print('Theta3: ', T3)
    # print('H0_1: \n', H0_1)
    # print('H0_2: \n', H0_2)
    # print('H0_3: \n', H0_3)
    # print('Joint 2 Position: ', joint1_pos)
    # print('Joint 3 Position: ', joint2_pos)
    # print('End Effector Position', end_effector_pos)
    # print('###########################################################')

#scene.append_to_caption('\n\nJoint 2 - Theta 2\n')   
#winput( bind=theta2 )



def theta3():
    #print("$$$$" + str(s))
    global T1
    global T2
    global T3
    t1 = T1
    t2 = T2
    t3 = T3
    #T3 = t3
    print(t3)

    # t1 = -(t1/180.0)*np.pi
    # t2 = (t2/180.0)*np.pi
    # t3 = -(t3/180.0)*np.pi


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

    # print('###########################################################')
    # print('Theta1: ', T1)
    # print('Theta2: ', T2)
    # print('Theta3: ', T3)
    # print('H0_1: \n', H0_1)
    # print('H0_2: \n', H0_2)
    # print('H0_3: \n', H0_3)
    # print('Joint 2 Position: ', joint1_pos)
    # print('Joint 3 Position: ', joint2_pos)
    # print('End Effector Position', end_effector_pos)
    # print('###########################################################')









'''
print('### JACOBIAN ###')
I = [[1,0,0],[0,1,0],[0,0,1]]
m0_0_1 = [[0],[0],[1]]
JR_0_1 = H0_1[:3,:3]
JD_0_1 = H0_1[0:3,3]
JR_0_2 = H0_2[:3,:3]
JD_0_2 = H0_2[0:3,3]
JR_0_3 = H0_3[:3,:3]
JD_0_3 = H0_3[0:3,3]

# Joint1
J_joint1_up = np.cross(np.dot(I, m0_0_1), JD_0_3, axis=0)
J_joint1_down = np.dot(I, m0_0_1)
J_joint1 = np.concatenate((J_joint1_up, J_joint1_down), axis=0)
print(J_joint1)

# Joint2
J_joint2_up = np.cross(np.dot(JR_0_1, m0_0_1), (JD_0_3-JD_0_1), axis=0)
J_joint2_down = np.dot(JR_0_1, m0_0_1)
J_joint2 = np.concatenate((J_joint2_up, J_joint2_down), axis=0)
print(J_joint2)

# Joint3
J_joint3_up = np.cross(np.dot(JR_0_2, m0_0_1), (JD_0_3-JD_0_2), axis=0)
J_joint3_down = np.dot(JR_0_2, m0_0_1)
J_joint3 = np.concatenate((J_joint3_up, J_joint3_down), axis=0)
print(J_joint3)

J = np.concatenate((J_joint1, J_joint2, J_joint3), axis=1)
print(J)

t = 0.001
v = 0.001
point_on_line = [1, 0, 0]

#dot_matrix = [[-1*v*np.sin(v*t)], [1*v*np.cos(v*t)], [0]]

dot_matrix = [[v*(-1/sqrt(2))], [0], [v*(-1/sqrt(2))]]
print(np.delete(J[:3,:3], 1, 0))
print(J[:3,:3])
print(np.linalg.pinv(J[:3,:3]))
theta_dot_matrix = np.dot(np.linalg.inv(J[:3,:3]), dot_matrix)
print(theta_dot_matrix)
print(theta_dot_matrix[0][0])
'''




#time.sleep(5)
draw_line()



  



#scene.append_to_caption('\n\nJoint 3 - Theta 3\n')   
#winput( bind=theta3 )

#scene.append_to_caption('\n\nWrite angles and hit enter to manipulate joints.\n')