#!/usr/bin/env python

import rospy
import actionlib
import time
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseWithCovarianceStamped, Quaternion
from tf.transformations import quaternion_from_euler, euler_from_quaternion
from math import radians

LOCATIONS = [
	[8.05, 0, 2, 0],
	[8.05, 26, 2, 0],
	[-1,95, 26, 2, 0],
	[-1,95, 0, 2, 0],
	[-1,95, 26, 2, 0],
	[-11,95, 26, 2, 0],
	[-11,95, 0, 2, 0],
	[-11,95, 0, 0.81, 0]
]

def setupGoal(position):
        x, y, z, yaw = position
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y
        goal.target_pose.pose.position.z = z
        angle = radians(yaw)  # angles are expressed in radians
        quaternion = quaternion_from_euler(0.0, 0.0, 0.0, angle)  # roll, pitch, yaw
        goal.target_pose.pose.orientation = Quaternion(*quaternion.tolist())
        return goal

client = actionlib.SimpleActionClient('objetivo_lider', MoveBaseAction)

for l in LOCATIONS:
    goal = setupGoal(l)

    client.wait_for_server()
    client.send_goal(goal)
    client.wait_for_result()
    nav_result = client.get_result()
    if nav_result:
        print('Continuando rota...')
    else:
        print('Erro na rota!')
        break
