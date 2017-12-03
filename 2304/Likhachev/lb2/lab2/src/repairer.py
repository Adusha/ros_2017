#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def repairer():
	pub = rospy.Publisher('dispatcher_repairer_channel', String, queue_size=20)
	rospy.init_node("plane", anonymous=True)
	
	while not rospy.is_shutdown():
		code = raw_input("Enter code: ")
		pub.publish(String(code))
			
if __name__ == '__main__':
	try:
		repairer()
	except rospy.ROSInterruptException:
		pass
	
