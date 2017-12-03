#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from lab_msgs.msg import *
from lab_srvs.srv import *

def repair_talk(data):
	try:
		repairSrv = rospy.ServiceProxy('repair_service', Fix)
		result = repairSrv(data.data)
		rospy.loginfo(result.message)
		
	except rospy.ServiceException, e:
		rospy.logerr("Service call failed: %s"%e)
	
def plane_talk(data):	
	if(data.gameOver == False):
		rospy.loginfo("\n\nWe found a new broken " + data.message + "\n\nWrite this code to fix: " + data.code + "\n") 
	else:
		rospy.loginfo("\n\n\nGame over\n\n\n")
	
def dispatcher():
	rospy.wait_for_service('repair_service')
	planeSub = rospy.Subscriber('dispatcher_robot_channel', FixMes, plane_talk)
	repairSub = rospy.Subscriber('dispatcher_repairer_channel', String, repair_talk)
	
	rospy.init_node('dispatcher', anonymous=True)
	rospy.spin()
		
if __name__ == '__main__':
	dispatcher()
	