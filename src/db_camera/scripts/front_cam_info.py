#!/usr/bin/python
import rospy
import cv2
from sensor_msgs.msg import CameraInfo

rospy.init_node("front_info_node", anonymous= False)

pub = rospy.Publisher("color/camera_info", CameraInfo, queue_size=10)
rate = rospy.Rate(60)
while not rospy.is_shutdown():
    info = CameraInfo()

    info.header.frame_id = "db_front_frame_id"
    info.height          = 480
    info.width           = 640
    info.D = [-0.31977657198490184, 0.10441625781364063, -0.000833304146618523, -0.0023824198721771254, 0.0]
    info.K = [404.29911577238823, 0.0, 322.021204616439, 0.0, 403.4469279176424, 256.78996703712505, 0.0, 0.0, 1.0]
    info.R = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
    info.P = [316.16326904296875, 0.0, 318.7422552121643, 0.0, 0.0, 352.0448913574219, 261.3150658560171, 0.0, 0.0, 0.0, 1.0, 0.0]
    info.binning_x = 0
    info.binning_y = 0
    info.roi.x_offset = 0
    info.roi.y_offset = 0
    info.roi.height = 0
    info.roi.width  = 0
    info.roi.do_rectify = False 
    
    pub.publish(info)
    rate.sleep()
