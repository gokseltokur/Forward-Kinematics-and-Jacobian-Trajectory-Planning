# Forward-Kinematics-and-Jacobian-Trajectory-Planning

## Scara Robot - Forward Kinematics
```python
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
```

  My Scara Robot consists of 3 degree of freedom and 5 links among them. I draw a kinematic diagram of the robot and I initialized link lengths as a1, a2, a3, a4 and a5. I calculated rotation matrices R0_1, R1_2 and R2_3 of the robot as
shown in above. Then, I calculated d0_1, d1_2 and d2_3. I concatenated these matrices to get homogeneous transformation matrices of the robot.
  To visualize the robot I used VPython library of Python language. I used rotation and transformation parts of the homogeneous transformation matrices to visualize the robot.
  
 ## Articulated Robot - Forward Kinematics
 ```python
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
```
  Articulated Robot consists of 3 degree of freedom and 3 links among them. I draw a kinematic diagram of the robot and I initialized link lengths as a1, a2, and a3. I calculated rotation matrices R0_1, R1_2 and R2_3 of the robot as shown in Figure 5. Then, I calculated d0_1, d1_2 and d2_3. I concatenated these matrices toget homogeneous transformation matrices of the robot.
 
![articulatedrobotarm1](/imgs/1.png)
Model of the articulated robot with Theta1 parameter 0 degree, Theta2 parameter 0and Theta3 parameter 0 degree as shown in left. Homogeneous transformation matrices and positions of joints and end effector as shown in right in this state.

![articulatedrobotarm2](/imgs/2.png)
Model of the articulated robot with Theta1 parameter 180 degree, Theta2 parameter 45 and Theta3 parameter -60 degree as shown in left. Homogeneous transformation matrices and positions of joints and end effector as shown in right in this state.
