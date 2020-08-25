#!/usr/bin/env python

import rospy
import actionlib
import time
import actionlib_tutorials.msg
from std_msgs.msg import Int16
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseWithCovarianceStamped, Quaternion, PoseStamped
from tf.transformations import quaternion_from_euler, euler_from_quaternion
from math import radians



#rospy.init_node('roteiro' , anonymous=True)

# def setupGoal(position):
#         x, y, z, yaw = position #linha do Locations
#         goal = MoveBaseGoal()
#         goal.target_pose.header.frame_id = 'map'
#         goal.target_pose.pose.position.x = x
#         goal.target_pose.pose.position.y = y
#         goal.target_pose.pose.position.z = z
#         angle = radians(yaw)  # angles are expressed in radians
#         quaternion = quaternion_from_euler(0, 0, angle)  # roll, pitch, yaw
#         goal.target_pose.pose.orientation = Quaternion(*quaternion.tolist())
#         return goal

def setupGoal(index):
        goal = PoseStamped()

        LOCATIONS = [
        	[8.05, 0, 0.800001, 0],
			[8.05, 0, 2, 0],
			[8.05, 26, 2, 0],
			[-1.95, 26, 2, 0],
			[-1.95, 0, 2, 0],
			[-1.95, 26, 2, 0],
			[-11.95, 26, 2, 0],
			[-11.95, 0, 2, 0],
			[-11.95, 0, 0.81, 0]
		]
		
#		x, y, z, yaw = position #linha do Locations
#        goal = MoveBaseGoal()
        goal.header.frame_id = 'map'
        goal.pose.position.x = LOCATIONS[index][0]
        goal.pose.position.y = LOCATIONS[index][1]
        goal.pose.position.z = LOCATIONS[index][2]
        #angle = radians(yaw)  # angles are expressed in radians
        #quaternion = quaternion_from_euler(0, 0, angle)  # roll, pitch, yaw
        #goal.target_pose.pose.orientation = Quaternion(*quaternion.tolist())
        return goal

#client = actionlib.SimpleActionClient('objetivo_lider', actionlib_tutorials.msg.MoveBaseAction)

def comunicacao(index):
	goal = setupGoal(index)
	pub.publish(goal)
	print "publicou"
	

def callback(index): # tratamento da recepicao
	indexnew = int(index.data)
	print "entrou em callback"
	comunicacao(indexnew)


# def callback(index): # tratamento da recepicao
# 	global indexold
# 	indexnew = int(index.data)
# 	print "entrou em callback"
# 	if(indexnew!=indexold):
# 		indexold = indexnew
# 		print "recebeu o novo index"
# 		comunicacao(indexnew)
# 		print "saiu da comunicacao"
# 		print indexold

#for l in LOCATIONS:
#    goal = setupGoal(l)

#    client.wait_for_server()
#    client.send_goal(goal)
#    client.wait_for_result()
#    nav_result = client.get_result()
#    if nav_result:
#        print('Continuando rota...')
#    else:
#        print('Erro na rota!')
#        break

if __name__ == '__main__':
#	print sys.argv
	global indexold
	indexold = -1
	rospy.Subscriber('gazebo/link', Int16, callback)# apelido do topico "gazebo/link" , tipo Int16 (inscreve neste canal de comunicacao)
	pub = rospy.Publisher('roteiro/waypoint', PoseStamped, queue_size=1)# publica no topico (canal de comunicacao) "gazebo/waypoint" 
	rospy.init_node('roteiro' , anonymous=True)
	print "chegou aki"
	rospy.spin()
	




