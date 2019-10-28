#!/usr/bin/env python

import sys
import rospy
from beginner_tutorials.srv import *

#For clients you don't have to call init_node()
def add_two_ints_client(x, y):
	rospy.wait_for_service('add_two_ints') #doi service thuc hien xong yeu cau truoc do
	try:
		add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)## gan bien add_two_ints, create a handle for calling the service

	#use this handle just like a normal function and call it
		resp1 = add_two_ints(x, y) #bien add_two_ints bay gio  dai dien cho dich vu van goi. O day, ta gui 
		return resp1.sum
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e

#Because we've declared the type of the service to be AddTwoInts, it does the work of generating the AddTwoIntsRequest object for you (you're free to pass in your own instead). The return value is an AddTwoIntsResponse object. If the call fails, a rospy.ServiceException may be thrown, so you should setup the appropriate try/except block.
def usage():
	return "%s [x y]"%sys.argv[0]

if __name__ =="__main__":
	if len(sys.argv) == 3: #lay tham so truc tiep tu command
		x = int(sys.argv[1])
		y = int(sys.argv[2])
	else:
		print usage()#In ra cau truc cua client, phai bao gom cac tham so x y
		sys.exit(1) #Khi khong nhap tham so se ket thuc yeu cau
	print "Requesting %s + %s" %(x, y)
	print "%s + %s = %s" %(x, y, add_two_ints_client(x, y))
