from numpy import *   # imports all function so we don't have to use np.function()
import math

from visual_kinematics import Robot
import numpy as np
np.set_printoptions(precision=3, suppress=True)



# Link lengths
a1 = 6.2  # length of link a1 in cm
a2 = 5.2  # length of link a2 in cm
a3 = 0  # length of link a3 in cm
a4 = 6.9  # length of link a4 in cm
a5 = 0  # length of link a5 in cm
a6 = 6.8  # length of link a6 in cm

# Angles
theta_1 = 0  # theta 1 angle in degrees
theta_2 = 90  # theta 2 angle in degrees
theta_3 = 90  # theta 3 angle in degrees

theta_1 = (theta_1/180)*math.pi  # theta 1 in radians
theta_2 = (theta_2/180)*math.pi  # theta 2 in radians
theta_3 = (theta_3/180)*math.pi  # theta 3 in radians

# DH Parameter Table for 3 DOF Planar
PT = np.array([[theta_1, 0, a2, a1],
      [theta_2, 0, a4, a3],
      [theta_3, 0, a6, a5]])

# PT = [[theta_1, 0, a2, a1],
#       [theta_2, 0, a4, a3],
#       [theta_3, 0, a6, a5]]

# Homogeneous Transformation Matrices
i = 0
H0_1 = [[math.cos(PT[i][0]), -math.sin(PT[i][0])*math.cos(PT[i][1]), math.sin(PT[i][0])*math.sin(PT[i][1]), PT[i][2]*math.cos(PT[i][0])],
        [math.sin(PT[i][0]), math.cos(PT[i][0])*math.cos(PT[i][1]), -math.cos(PT[i][0])*math.sin(PT[i][1]), PT[i][2]*math.sin(PT[i][0])],
        [0, math.sin(PT[i][1]), math.cos(PT[i][1]), PT[i][3]],
        [0, 0, 0, 1]]

i = 1
H1_2 = [[math.cos(PT[i][0]), -math.sin(PT[i][0])*math.cos(PT[i][1]), math.sin(PT[i][0])*math.sin(PT[i][1]), PT[i][2]*math.cos(PT[i][0])],
        [math.sin(PT[i][0]), math.cos(PT[i][0])*math.cos(PT[i][1]), -math.cos(PT[i][0])*math.sin(PT[i][1]), PT[i][2]*math.sin(PT[i][0])],
        [0, math.sin(PT[i][1]), math.cos(PT[i][1]), PT[i][3]],
        [0, 0, 0, 1]]

i = 2
H2_3 = [[math.cos(PT[i][0]), -math.sin(PT[i][0])*math.cos(PT[i][1]), math.sin(PT[i][0])*math.sin(PT[i][1]), PT[i][2]*math.cos(PT[i][0])],
        [math.sin(PT[i][0]), math.cos(PT[i][0])*math.cos(PT[i][1]), -math.cos(PT[i][0])*math.sin(PT[i][1]), PT[i][2]*math.sin(PT[i][0])],
        [0, math.sin(PT[i][1]), math.cos(PT[i][1]), PT[i][3]],
        [0, 0, 0, 1]]

print("H0_1 =")
print(matrix(H0_1))
print("H1_2 =")
print(matrix(H1_2))
print("H2_3 =")
print(matrix(H2_3))

H0_2 = dot(H0_1,H1_2)
H0_3 = dot(H0_2,H2_3)

print("H0_3 =")
print(matrix(H0_3))


#robot = Robot(PT)

theta = np.array([theta_1, theta_2, theta_3])

#f = robot.forward(theta)

#robot.show()



zdata = []
xdata = []
ydata = []

H0_1 = np.array(H0_1)
a = []
print(np.array(H0_1))
print(np.array(H0_2[:,3]))
#a.append([H0_1[0][3], H0_1[1][3], H0_1[2][3], H0_1[3][3]])
print("AAAAAAA")
a.append(H0_1[:,3])
a.append(H0_2[:,3])
a.append(H0_3[:,3])

print(a)

for i in a:
    xdata = a[0]
    ydata = a[1]
    zdata = a[2]

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

fig = pyplot.figure(figsize=(6,6))
ax = Axes3D(fig)

#ax = plt.axes(projection='3d')

ax.plot(xdata, ydata, zdata)

# Data for a three-dimensional line


# Data for three-dimensional scattered points

ax.scatter(xdata, ydata, zdata)
pyplot.show()