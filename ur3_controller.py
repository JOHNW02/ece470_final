"""ur3_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import numpy as np
from scipy.linalg import expm
from utils import inverse
import time
# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())


joint1 = robot.getDevice("shoulder_pan_joint")
joint2 = robot.getDevice("shoulder_lift_joint")
joint3 = robot.getDevice("elbow_joint")
joint4 = robot.getDevice("wrist_1_joint")
joint5 = robot.getDevice("wrist_2_joint")
joint6 = robot.getDevice("wrist_3_joint")

# gripper motors
palm_finger_1_joint = robot.getDevice("palm_finger_1_joint")
finger_1_joint_1 = robot.getDevice("finger_1_joint_1")
finger_1_joint_2 = robot.getDevice("finger_1_joint_2")
finger_1_joint_3 = robot.getDevice("finger_1_joint_3")
palm_finger_2_joint = robot.getDevice("palm_finger_2_joint")
finger_2_joint_1 = robot.getDevice("finger_2_joint_1")
finger_2_joint_2 = robot.getDevice("finger_2_joint_2")
finger_2_joint_3 = robot.getDevice("finger_2_joint_3")
finger_middle_joint_1 = robot.getDevice("finger_middle_joint_1")
finger_middle_joint_2 = robot.getDevice("finger_middle_joint_2")
finger_middle_joint_3 = robot.getDevice("finger_middle_joint_3")

def move_arm(angle1, angle2, angle3, angle4, angle5, angle6):
    joint1.setPosition(angle1)
    joint2.setPosition(angle2)
    joint3.setPosition(angle3)
    joint4.setPosition(angle4)
    joint5.setPosition(angle5)
    joint6.setPosition(angle6)


def grap(angle1=0, angle2=0, angle3=0, angle4=0, angle5=0, angle6=0, angle7=0, angle8=0, angle9=0, angle10=0, angle11=0):
    
    finger_1_joint_3.setPosition(angle1)
    finger_2_joint_3.setPosition(angle2)
    finger_middle_joint_3.setPosition(angle3)

    finger_1_joint_2.setPosition(angle4)
    finger_2_joint_2.setPosition(angle5)
    finger_middle_joint_2.setPosition(angle6)
    
    finger_1_joint_1.setPosition(angle7)
    finger_2_joint_1.setPosition(angle8)
    finger_middle_joint_1.setPosition(angle9)
    
    palm_finger_2_joint.setPosition(angle10)
    palm_finger_1_joint.setPosition(angle11)


grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0.4, angle5=0.4, angle6=0.4, angle7=0.5, angle8=0.5, angle9=0.5, angle10=0, angle11=0)
robot.step(400)    
move_arm(-np.pi/8, -np.pi/6, 0, 0, 0, 0)
robot.step(400)
move_arm(-np.pi/4, -np.pi/6, 0, 0, 0, 0)
robot.step(400)
move_arm(-np.pi/4, 0, 0, 0, 0,0)
robot.step(400) 
grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0, angle5=0, angle6=0, angle7=0, angle8=0, angle9=0, angle10=0, angle11=0)
# T_bottle_1 = np.array([ [1, 0, 0, 0.5],
#                         [0, 1, 0, 0.2],
#                         [0, 0, 1, 0.2],
#                         [0, 0, 0, 1] ] )
# thetalist = np.array( [0, 0, 0, 0, 0, 0] )
# angles, success = inverse(thetalist, T_bottle_1)

# move_arm( float(angles[0]), float(angles[1]), float(angles[2]), float(angles[3]),\
#             float(angles[4]), float(angles[5]))

# robot.step(2000)
# T_bottle_1 = np.array([ [1, 0, 0, 0.5],
#                         [0, 1, 0, 0],
#                         [0, 0, 1, 0.2],
#                         [0, 0, 0, 1] ] )
# thetalist = np.array( [0, 0, 0, 0, 0, 0] )
# angles, success = inverse(thetalist, T_bottle_1)

# move_arm( float(angles[0]), float(angles[1]), float(angles[2]), float(angles[3]),\
#             float(angles[4]), float(angles[5]))

