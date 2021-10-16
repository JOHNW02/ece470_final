#!/usr/bin/env python
import numpy as np
from scipy.linalg import expm
from lab3_header import *

"""
Use 'expm' for matrix exponential.
Angles are in radian, distance are in meters.
"""

def Get_MS():
	# =================== Your code starts here ====================#
	# Fill in the correct values for S1~6, as well as the M matrix
	
	M  = np.array([[0, -1, 0, 390],
		  		   [0, 0, -1, 401],
		           [1, 0, 0, 215.5],
		           [0, 0, 0, 1]])

	#s1 = np.array([0, 0, 1,  150, 150, 0])
	#s2 = np.array([0, 1, 0, -162, 0,  -150])
	#s3 = np.array([0, 1, 0, -162, 0,   94])
	#s4 = np.array([0, 1, 0, -162, 0,   307])
	#s5 = np.array([1, 0, 0,  0,   162, -260])
	#s6 = np.array([0, 1, 0, -162, 0,   390])


	S1 = np.array([ [0,-1, 0, 150], \
					[1, 0, 0, 150], \
					[0, 0, 0, 0], \
					[0, 0, 0, 0]]) 

	S2 = np.array([ [0, 0, 1, -162], \
					[0, 0, 0, 0], \
					[-1, 0, 0, -150], \
					[0, 0, 0, 0]]) 
	
	S3 = np.array([ [0,0, 1, -162], \
					[0, 0, 0, 0], \
					[-1, 0, 0, 94], \
					[0, 0, 0, 0]]) 
	
	S4 = np.array([ [0, 0, 1, -162], \
					[0, 0, 0, 0], \
					[-1, 0, 0, 307], \
					[0, 0, 0, 0]]) 
	
	S5 = np.array([ [0,0, 0, 0], \
					[0, 0, -1, 162], \
					[0, 1, 0, -260], \
					[0, 0, 0, 0]]) 
	
	S6 = np.array([ [0, 0, 1, -162], \
					[0, 0, 0, 0], \
					[-1, 0, 0, 390], \
					[0, 0, 0, 0]]) 
	
	S = [S1, S2, S3, S4, S5, S6]

	# ==============================================================#
	return M, S


"""
Function that calculates encoder numbers for each motor
"""
def lab_fk(theta1, theta2, theta3, theta4, theta5, theta6):

	# Initialize the return_value


	return_value = [None, None, None, None, None, None]

	# =========== Implement joint angle to encoder expressions here ===========
	print("Foward kinematics calculated:\n")

	# =================== Your code starts here ====================#

	M, S = Get_MS()

	theta = [theta1, theta2, theta3, theta4, theta5, theta6]
	
	temp = np.eye(4)

	for i in range(6):
		temp = np.matmul(temp,expm(S[i]*theta[i]))

	
	T = temp.dot(M)
	


	# ==============================================================#

	print(str(T) + "\n")

	return_value[0] = theta1 + PI
	return_value[1] = theta2
	return_value[2] = theta3
	return_value[3] = theta4 - (0.5*PI)
	return_value[4] = theta5
	return_value[5] = theta6

	return return_value
