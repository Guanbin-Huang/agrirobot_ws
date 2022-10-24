#!/usr/bin/python
import rospy
import cv2
from sensor_msgs.msg import CameraInfo

rospy.init_node("back_info_node", anonymous= False)

pub = rospy.Publisher("color/camera_info", CameraInfo, queue_size=10)
rate = rospy.Rate(60)
while not rospy.is_shutdown():
    info = CameraInfo()

    info.header.frame_id = "db_back_frame_id"
    info.height          = 480
    info.width           = 640
    info.D = [-0.31151159348168256, 0.09103183321654552, -0.002141755644042331, 0.0013374141100405744, 0.0]
    info.K = [416.8386321912152, 0.0, 309.44548335833605, 0.0, 416.3094882651935, 258.7652131128805, 0.0, 0.0, 1.0]
    info.R = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
    info.P = [327.7568054199219, 0.0, 306.55892782481715, 0.0, 0.0, 367.287841796875, 262.69865009441855, 0.0, 0.0, 0.0, 1.0, 0.0]
    info.binning_x = 0
    info.binning_y = 0
    info.roi.x_offset = 0
    info.roi.y_offset = 0
    info.roi.height = 0
    info.roi.width  = 0
    info.roi.do_rectify = False 
    
    pub.publish(info)
    rate.sleep()
