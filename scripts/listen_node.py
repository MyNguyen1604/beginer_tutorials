#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
#from turtlesim.msg import Pose
def callback(data):
	#rospy.loginfo("Vi tri cua node %f \n %f",data.linear, data.angular)
	print("linear")
	print(data.linear)
	#print("\n")
	print("angular")
	print(data.angular)
	print("\n")
def listener():
	rospy.init_node('listener_node', anonymous=True) 
	rospy.Subscriber('/turtle1/cmd_vel', Twist, callback) #rostopic list | rostopic type /turtle1/cmd_vel
# Topic turtle1/pose se co tin nhan la turtlesim/Pose
	rospy.spin()
if __name__ == '__main__':
    listener()
	
