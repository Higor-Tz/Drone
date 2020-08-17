#!/usr/bin/env python

import sys
import rospy
import actionlib
import actionlib_tutorials.msg
from gazebo_msgs.msg import ModelState
from std_msgs.msg import Int16
from gazebo_msgs.srv import GetModelState
from geometry_msgs.msg import PoseStamped
import tf

modelname = ''


#class SimpleActionClient(, ):
#class MoveBaseAction(objetivo):
#	def init(self, name):
#		self._action_name = name
#		self._as = actionlib.SimpleActionServer(self._action_name, actionlib_tutorials.msg.MoveBaseAction, execute_cb=self.execute_cb, auto_start = False)
#		self._as.start()
#	def execute_cb(self, goal):




def quaternion2euler(orientation):
	quaternion = (orientation.x,orientation.y,orientation.z,orientation.w)
	euler = tf.transformations.euler_from_quaternion(quaternion)
	roll = euler[0]
	pitch = euler[1]
	yaw = euler[2]
	return roll, pitch, yaw

def callback(objetivo):
	global indexold,flagBlock
	print objetivo

	pub = rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=1)#10
	rospy.wait_for_service('gazebo/get_model_state')
	
	GetState = rospy.ServiceProxy('gazebo/get_model_state', GetModelState)
	selfState = GetState(modelname, 'world')
	#selfState = objetivo
	#State = objetivo

	print "chegou aki"
	comando = ModelState()
	comando.pose.position.y = selfState.pose.position.y
	comando.pose.position.z = selfState.pose.position.z
	comando.pose.position.x = selfState.pose.position.x	

	#comando.pose.position.y = State.pose.position.y
	#comando.pose.position.z = State.pose.position.z
	#comando.pose.position.x = State.pose.position.x	

	comando.pose.orientation.x = selfState.pose.orientation.x
	comando.pose.orientation.y = selfState.pose.orientation.y
	comando.pose.orientation.z = selfState.pose.orientation.z
	comando.pose.orientation.w = selfState.pose.orientation.w

	#self_roll, self_pitch, self_yaw = quaternion2euler(State.pose.orientation)
	self_roll, self_pitch, self_yaw = quaternion2euler(selfState.pose.orientation)
	obj_roll, obj_pitch, obj_yaw = quaternion2euler(objetivo.pose.orientation)

	comando.twist.linear.x = 0.5*(objetivo.pose.position.x - selfState.pose.position.x)
	comando.twist.linear.y = 0.5*(objetivo.pose.position.y - selfState.pose.position.y)
	comando.twist.linear.z = 0.5*(objetivo.pose.position.z - selfState.pose.position.z)	
	#print selfState.pose.position.x
	#print selfState.pose.position.y
	print selfState.pose.position.z
	print objetivo.pose.position.z
	#comando.twist.linear.x = 0.5*(objetivo.pose.position.x - State.pose.position.x)
	#comando.twist.linear.y = 0.5*(objetivo.pose.position.y - State.pose.position.y)
	#comando.twist.linear.z = 0.5*(objetivo.pose.position.z - State.pose.position.z)		

	#comando.twist.angular.x = 0.25*(obj_roll - self_roll)
	#comando.twist.angular.y = 0.25*(obj_pitch - self_pitch)
	#comando.twist.angular.z = 0.25*(obj_yaw - self_yaw)

	comando.model_name = modelname
	
	pub.publish(comando)

	if(comando.twist.linear.x < 0.01 and comando.twist.linear.y < 0.01 and comando.twist.linear.z < 0.01):
		indexold += 1

	flagBlock = 0			


# def controle(modelname):
# 	rospy.init_node(modelname , anonymous=True)
# 	objetivoMsgs = "objetivo_" + modelname
# 	rospy.Subscriber('gazebo/waypoint', PoseStamped, callback)#objetivoMsgs, mudou antigo Pose
	
# 	#print rospy.search_param("modelName")
# 	#modelname = rospy.get_param("modelName")
	
# 	rospy.spin()


# if name == 'main':
	
# 	global indexold 
# 	indexold = 0
# 	print sys.argv
# 	if len(sys.argv) > 1:
# 		modelname = sys.argv[1]
# 		print 'modelname:' + modelname
# 	else:
# 		print "Favor fornecer o nome de um model ativo"
# 		sys.exit(1)
# 	#try:
# 	#	controle()
# 	#except rospy.ROSInterruptException:
# 	#	pass
# 	controle(modelname)



##### EXEMPLO


def RunDrone():
	print "Entrou em RunDrone"
	global indexold,flagBlock
	if(flagBlock == 0):
		print "Passou flagBlock"
		var = Int16()
		var.data = indexold
		pubind.publish(var)
		flagBlock = 1


def controle(modelname):
	print "Entrou na funcao"

	rospy.init_node(modelname , anonymous=True)
	rate = rospy.Rate(5) # 0.1hz
	#rospy.spin()

	while not rospy.is_shutdown():
		RunDrone()
		rate.sleep()

if __name__ == '__main__':

	global indexold,flagBlock
	indexold = 0
	flagBlock = 0
	#print sys.argv
	if len(sys.argv) > 1:
		modelname = sys.argv[1]
		print 'modelname:' + modelname
	else:
		print "Favor fornecer o nome de um model ativo"
		sys.exit(1)	

	objetivoMsgs = "objetivo_" + modelname

	pubind = rospy.Publisher('gazebo/link', Int16, queue_size=1)
	rospy.Subscriber('roteiro/waypoint', PoseStamped, callback)#objetivoMsgs, mudou antigo Pose	

	try:
		print "entrou"
		controle(modelname)
	except rospy.ROSInterruptException:
		pass