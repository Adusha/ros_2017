#!/usr/bin/env python
import rospy
import sys
from std_msgs.msg import String
from lab_msgs.msg import FixMes
from lab_srvs.srv import *
from random import choice
from random import randint
from string import ascii_lowercase
from time import sleep

codes = []

def repair(req):
	resp = FixResponse()
	for code in codes:
		if (code == req.repair_code):
			codes.remove(code)
			resp.message = "Fixing....Finished."
			return resp
			
	resp.message = "Wrong code. You broke this!!!"
	return resp


def publisher():
	pub = rospy.Publisher('dispatcher_robot_channel', FixMes, queue_size=20)
	srv = rospy.Service('repair_service', Fix, repair)
	
	rospy.init_node("plane", anonymous=True)
	errorCount = 0
	wait = 0
	i = 0
	messages = ["Ship", "Tank", "Car", "Plane"]
	while not rospy.is_shutdown():
		newCode = ''.join(choice(ascii_lowercase) for i in range(6))
		codes.append(newCode)
		sleep(randint(4,10))
		
		size = 0
		for x in codes:
			size += 1
			
		if (size > 6):
			msg = FixMes()
			msg.gameOver = True
			pub.publish(msg)
			rospy.signal_shutdown("FAILED")
			
		msg = FixMes()
		msg.code = newCode
		msg.message = choice(messages)
		msg.gameOver = False
		pub.publish(msg)
			
		
			
if __name__ == '__main__':
	try:
		publisher()
	except rospy.ROSInterruptException:
		pass
	
