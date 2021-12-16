"""ur3_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Camera
import numpy as np
from scipy.linalg import expm
from utils import inverse
import time
import PySimpleGUI as sg
# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

camera = robot.getDevice('camera')
camera.enable(4*timestep)

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

#grap
# grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0.4, angle5=0.4, angle6=0.4, angle7=0.5, angle8=0.5, angle9=0.5, angle10=0, angle11=0)

#release
# grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0, angle5=0, angle6=0, angle7=0, angle8=0, angle9=0, angle10=0, angle11=0)

input = 0

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Enter 1 for beer, 2 for water, and 3 for a mix.')],
            [sg.Text('Enter your choice: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Input Box', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    input = int(values[0])
    if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Ok': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()

print(input)
# open gripper
grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0, angle5=0, angle6=0, angle7=0, angle8=0, angle9=0, angle10=0, angle11=0)
robot.step(1100)

#get cup
theta1, theta2, theta3, theta4, theta5, theta6 = inverse(0.20, 0.3, 0.1)
move_arm(theta1, theta2, theta3, theta4, theta5, theta6  )
robot.step(1100) 
theta1, theta2, theta3, theta4, theta5, theta6 = inverse(0.24, 0.45, 0.1)
move_arm(theta1, theta2, theta3, theta4, theta5, theta6  )
robot.step(1100)
grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0.4, angle5=0.4, angle6=0.4, angle7=0.5, angle8=0.5, angle9=0.5, angle10=0, angle11=0)
robot.step(1100)

theta1, theta2, theta3, theta4, theta5, theta6 = inverse(0.3, 0.1, 0.3)
move_arm(theta1, theta2, theta3, theta4, theta5, theta6  )
robot.step(1100)
theta1, theta2, theta3, theta4, theta5, theta6 = inverse(0.3, 0.1, 0.1)
move_arm(theta1, theta2, theta3, theta4, theta5, theta6  )
robot.step(1100)
grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0, angle5=0, angle6=0, angle7=0, angle8=0, angle9=0, angle10=0, angle11=0)
robot.step(1100)
theta1, theta2, theta3, theta4, theta5, theta6 = inverse(0.3, 0.1, 0.35)
move_arm(theta1 + 0.1, theta2, theta3, theta4, theta5, theta6  )
robot.step(1100)


if input == 1:
    # get beer bottle
    move_arm(theta1, 0, -np.pi/2, 0, 0, 0)
    robot.step(1100)
    move_arm(-np.pi, 0, -np.pi/2, 0, 0, 0)
    robot.step(1100)
    move_arm(-np.pi, 0, 0, 0, 0, 0)
    robot.step(1100)
    move_arm(-3/4*np.pi+0.03, 0, 0, 0, -np.pi/5, 0)
    robot.step(1100)
    grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0.4, angle5=0.4, angle6=0.4, angle7=1, angle8=1, angle9=1, angle10=0, angle11=0)
    robot.step(1100)
    theta1, theta2, theta3, theta4, theta5, theta6 = inverse(0.3, 0.1, 0.3)
    move_arm(theta1-0.5, theta2, theta3, theta4, theta5, theta6  )
    robot.step(1100)
    move_arm(theta1-0.2, theta2, theta3, theta4, theta5+0.35, -np.pi/2  )
    robot.step(1100)

    # return beer bottle
    move_arm(theta1-0.5, theta2, theta3, theta4, theta5+0.35, theta6  )
    robot.step(1100)
    move_arm(-3/4*np.pi+0.03, 0, 0, 0, -np.pi/5, 0)
    robot.step(1100)
    grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0, angle5=0, angle6=0, angle7=0, angle8=0, angle9=0, angle10=0, angle11=0)
    robot.step(1100)
    move_arm(-np.pi, 0, 0, 0, 0, 0.1)
    robot.step(1100)
    move_arm(-np.pi, 0, -np.pi/2, 0, 0, 0)
    robot.step(1100)

elif input == 2:
    # get water bottle
    move_arm(0, -np.pi, 0, np.pi, 0, 0)
    robot.step(1100)
    move_arm(-np.pi/3-0.02, -np.pi, 0, np.pi, 0, 0)
    robot.step(1100)
    grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0.4, angle5=0.4, angle6=0.4, angle7=0.5, angle8=0.5, angle9=0.5, angle10=0, angle11=0)
    robot.step(1100)
    theta1, theta2, theta3, theta4, theta5, theta6 = inverse(0.3, 0.1, 0.3)
    move_arm(theta1-0.5, theta2, theta3, theta4, theta5, theta6  )
    robot.step(1100)
    move_arm(theta1-0.3, theta2, theta3, theta4, theta5+0.35, -np.pi/2  )
    robot.step(1100)

    # return water bottle
    move_arm(theta1-0.5, theta2, theta3, theta4, theta5+0.35, theta6  )
    robot.step(1100)
    move_arm(-np.pi/3-0.02, -np.pi, 0, np.pi, 0, 0)
    robot.step(1100)
    grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0, angle5=0, angle6=0, angle7=0, angle8=0, angle9=0, angle10=0, angle11=0)
    robot.step(1100)
    move_arm(0, -np.pi, 0, np.pi, 0.1, 0)
    robot.step(1100)
    move_arm(0, 0, -np.pi/2, 0, 0, 0)
    robot.step(1100)

elif input == 3:
    # get water bottle
    move_arm(0, -np.pi, 0, np.pi, 0, 0)
    robot.step(1100)
    move_arm(-np.pi/3-0.02, -np.pi, 0, np.pi, 0, 0)
    robot.step(1100)
    grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0.4, angle5=0.4, angle6=0.4, angle7=0.5, angle8=0.5, angle9=0.5, angle10=0, angle11=0)
    robot.step(1100)
    theta1, theta2, theta3, theta4, theta5, theta6 = inverse(0.3, 0.1, 0.3)
    move_arm(theta1-0.5, theta2, theta3, theta4, theta5, theta6  )
    robot.step(1100)
    move_arm(theta1-0.3, theta2, theta3, theta4, theta5+0.35, -np.pi/2  )
    robot.step(1100)

    # return water bottle
    move_arm(theta1-0.5, theta2, theta3, theta4, theta5+0.35, theta6  )
    robot.step(1100)
    move_arm(-np.pi/3-0.02, -np.pi, 0, np.pi, 0, 0)
    robot.step(1100)
    grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0, angle5=0, angle6=0, angle7=0, angle8=0, angle9=0, angle10=0, angle11=0)
    robot.step(1100)
    move_arm(0, -np.pi, 0, np.pi, 0.1, 0)
    robot.step(1100)
    move_arm(0, 0, -np.pi/2, 0, 0, 0)
    robot.step(1100)

    # get beer bottle
    move_arm(-np.pi, 0, -np.pi/2, 0, 0, 0)
    robot.step(1100)
    move_arm(-np.pi, 0, 0, 0, 0, 0)
    robot.step(1100)
    move_arm(-3/4*np.pi+0.03, 0, 0, 0, -np.pi/5, 0)
    robot.step(1100)
    grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0.4, angle5=0.4, angle6=0.4, angle7=1, angle8=1, angle9=1, angle10=0, angle11=0)
    robot.step(1100)
    theta1, theta2, theta3, theta4, theta5, theta6 = inverse(0.3, 0.1, 0.3)
    move_arm(theta1-0.5, theta2, theta3, theta4, theta5, theta6  )
    robot.step(1100)
    move_arm(theta1-0.2, theta2, theta3, theta4, theta5+0.35, -np.pi/2  )
    robot.step(1100)

    # return beer bottle
    move_arm(theta1-0.5, theta2, theta3, theta4, theta5+0.35, theta6  )
    robot.step(1100)
    move_arm(-3/4*np.pi+0.03, 0, 0, 0, -np.pi/5, 0)
    robot.step(1100)
    grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0, angle5=0, angle6=0, angle7=0, angle8=0, angle9=0, angle10=0, angle11=0)
    robot.step(1100)
    move_arm(-np.pi, 0, 0, 0, 0, 0.1)
    robot.step(1100)
    move_arm(-np.pi, 0, -np.pi/2, 0, 0, 0)
    robot.step(1100)
else:
    raise ValueError("unknown input")
# grab the cup again
theta1, theta2, theta3, theta4, theta5, theta6 = inverse(0.3, 0, 0.1)
move_arm(theta1, theta2, theta3, theta4, theta5-0.4, theta6 )
robot.step(1100)

theta1, theta2, theta3, theta4, theta5, theta6 = inverse(0.3, 0.1, 0.1)
move_arm(theta1+0.1, theta2, theta3, theta4, theta5-0.05, theta6  )
robot.step(1100)
grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0.4, angle5=0.4, angle6=0.4, angle7=0.5, angle8=0.5, angle9=0.5, angle10=0, angle11=0)
robot.step(1100)
move_arm(0,0,0,0,np.pi/2,0)
robot.step(1100)
grap(angle1=-0.3, angle2=-0.3, angle3=-0.3, angle4=0, angle5=0, angle6=0, angle7=0, angle8=0, angle9=0, angle10=0, angle11=0)
