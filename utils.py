import numpy as np
from scipy.linalg import expm
import modern_robotics as mr

"""
Use 'expm' for matrix exponential.
Angles are in radian, distance are in meters.
"""

# y  z x
# base = 3.61 0.8 -3.78 (right, up, back)

def Get_MS():
# =================== Your code starts here ====================#
# Fill in the correct values for S1~6, as well as the M matrix
    base = np.array([3.61, 0.8, -3.78])
    w_1 = np.array([0, 0, 1]).T
    w_2 = np.array([0, 1, 0]).T
    w_3 = np.array([0, 1, 0]).T
    w_4 = np.array([0, 1, 0]).T
    w_5 = np.array([0, 0, 1]).T
    w_6 = np.array([0, 1, 0]).T

    q_1 = np.array([0, 0, 0.152] ).T

    q_2 = np.array([0, 0.120, 0.152]).T

    q_3 = np.array([0.244, 0.120, 0.152]).T
    
    q_4 = np.array([0.457, 0.027, 0.152]).T

    q_5 = np.array([0.457, 0.11, 0.152]).T

    q_6 = np.array([0.457, 0.11, 0.069]).T

    v_1 = np.cross(w_1, -1 * q_1)
    v_2 = np.cross(w_2, -1 * q_2)
    v_3 = np.cross(w_3, -1 * q_3)
    v_4 = np.cross(w_4, -1 * q_4)
    v_5 = np.cross(w_5, -1 * q_5)
    v_6 = np.cross(w_6, -1 * q_6)

    s1 = np.concatenate((w_1, v_1))
    s2 = np.concatenate((w_2, v_2))
    s3 = np.concatenate((w_3, v_3))
    s4 = np.concatenate((w_4, v_4))
    s5 = np.concatenate((w_5, v_5))
    s6 = np.concatenate((w_6, v_6))

    S = np.stack( (s1, s2, s3,s4,s5,s6))
    M = np.array([ [-1, 0, 0, 0.457],
                   [0, 1, 0,  0.20],
                   [0, 0, -1, 0.069],
                   [0, 0, 0, 1] ] )
    return M, S
"""
Function that calculates an elbow up Inverse Kinematic solution for the UR3
"""
def inverse(X, Y, Z):
    L1 = 0.152
    L3 = 0.244
    L5 = 0.213
    L6 = 0.083
    L7 = 0.083

    Xcen = X
    Ycen = Y - 0.228
    Zcen = Z + 0.083

    # find theta 1
    cen_len = np.sqrt( (Xcen ** 2 + Ycen ** 2) )
    small_theta = np.degrees( np.arcsin( (0.027+0.083) / cen_len ) )
    big_theta = np.degrees(np.arctan2(Ycen, Xcen))
    theta1 =  (big_theta - small_theta)

    # find 3end
    ext_3end = np.sqrt( Xcen ** 2 + Ycen ** 2 - (0.027+0.083)**2 )
    X3end = np.cos( np.radians(theta1) ) * ext_3end
    Y3end = np.sin( np.radians(theta1) ) * ext_3end
    Z3end = Zcen
    
    # find theta 3
    c = np.sqrt((np.sqrt(X3end ** 2 + Y3end ** 2))**2 + (Z3end - L1)**2)
    theta3 = 180 - np.degrees(np.arccos( (L3 ** 2 + L5 ** 2 - c ** 2)/(2* L3 * L5) ) )

    # find theta 2
    theta2_small =np.degrees( np.arctan2((Z3end-L1), (np.sqrt(X3end ** 2 + Y3end ** 2) ) ))
    theta2_big = np.degrees( np.arccos( (L3 ** 2 + c ** 2 - L5 ** 2)/(2* L3 * c) ) )
    theta2 = -(theta2_small+theta2_big)


    # find theta 4
    theta4 = -theta2 - theta3

    # define theta 5 6 = 0
    theta5 = 0
    theta6 = 0


    M, S = Get_MS()
    S = S.T

    return ( np.radians(theta1), np.radians(theta2), np.radians(theta3), np.radians(theta4), np.radians(theta5), np.radians(theta6))
    