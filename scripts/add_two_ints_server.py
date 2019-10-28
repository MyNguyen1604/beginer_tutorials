#!/usr/bin/env python

from beginner_tutorials.srv import *
import rospy

def handle_add_two_ints(req):#handle_add_two_ints is called with instances of AddTwoIntsRequest and returns instances (yeu cau) of AddTwoIntsResponse
	print "Returning [%s + %s = %s]" %(req.a, req.b, (req.a + req.b))
	return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
	rospy.init_node('add_two_ints_server', anonymous = True)

    	##Declare service
	#This declares a new service named add_two_ints with the AddTwoInts service type
	s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints) #Khi co mot yeu cau tren topic add_two_ints, voi du lieu yeu cau la AddTwoInts, thi ta goi ham xu ly yeu cao handle_add_two_ints de xu ly yeu cau, voi du lieu vao ham xu ly nay la AddTwoInts. Hay noi cach khac, khi co mot du lieu AddTwoInts duoc gui tren topic add_two_ints thi ROS Master se nhan biet no, dong thoi no yeu cau Node add_two_ints_server nhan thong tin va xu ly. Node add_two_ints_server sau khi nhan yeu cau tu ROS Master, no se lay thong tin dich vu can duoc xu ly va gui no vao ham xu ly dich vu handlel_add_two_ints. Ham nay sau khi xu ly du lieu se tra ve ket qua la dich vu can duoc cung cap (AddTwoIntsResponse())

	print "Ready to add two ints."

	rospy.spin() #Ket thuc node khii ctrl + C (keeps your code from exiting until the service is shutdown)

if __name__ == "__main__":
	add_two_ints_server()
