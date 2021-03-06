#!/usr/bin/env python

import rospy, math
from geometry_msgs.msg import Twist
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped
from std_msgs.msg import Header

class Control():
    def __init__(self):
        self.pub = rospy.Publisher("ackermann_cmd",\
                AckermannDriveStamped, queue_size =1 )
    	while not rospy.is_shutdown():

		drive_msg_stamped = AckermannDriveStamped()
		drive_msg = AckermannDrive()
                header_msg = Header()
		drive_msg.speed = 1
		drive_msg.steering_angle = 0.1
		drive_msg.acceleration = 0
		drive_msg.jerk = 0
		drive_msg.steering_angle_velocity = 0
		drive_msg_stamped.drive = drive_msg

		header_msg.stamp = rospy.Time.now()
                header_msg.frame_id = '1'
                drive_msg_stamped.header = header_msg


		pub = rospy.Publisher('/ackermann_cmd',AckermannDriveStamped, queue_size=1)
		pub.publish(drive_msg_stamped)      

if __name__ == '__main__':
    rospy.init_node('example')
    vs = Control()
    rospy.spin()

