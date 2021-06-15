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

print(np.matrix(H0_3))

#print('Position of end effector ', (H0_3[:,3]))
#print('Position of end effector ', ((H0_3[:,3])[0], (H0_3[:,3])[1], (H0_3[:,3])[2]))


#print('Position of joint2 ', (H0_1[:,3]))

joint2_pos = vector((H0_1[:,3])[0], (H0_1[:,3])[2], (H0_1[:,3])[1])
joint3_pos = vector((H0_2[:,3])[0], (H0_2[:,3])[2], (H0_2[:,3])[1])
end_effector_pos = vector((H0_3[:,3])[0], (H0_3[:,3])[2], (H0_3[:,3])[1])