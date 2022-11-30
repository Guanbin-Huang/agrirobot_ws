import time, sys, os
from ros import rosbag
import roslib, rospy
roslib.load_manifest('sensor_msgs')
from sensor_msgs.msg import Image, CameraInfo


from cv_bridge import CvBridge
import cv2

FRONT_TOPIC = '/rs_nav_front/color/image_raw'
FRONT_INFO_TOPIC = '/rs_nav_front/color/camera_info'
BACK_TOPIC  = '/rs_nav_back/color/image_raw'
BACK_INFO_TOPIC  = '/rs_nav_back/color/camera_info'


info = CameraInfo() # for simplicity, just a dummy input
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




def CreateVideoBag(bagname = r"../mybag_front_back.bag"):
    '''Creates a bag file with n video files'''
    bag = rosbag.Bag(bagname, 'w')
    cap1 = cv2.VideoCapture("/home/huanyu-pc/agrirobot_ws/tools/front1.mp4")
    cap2 = cv2.VideoCapture("/home/huanyu-pc/agrirobot_ws/tools/back1.mp4")
    
    cb = CvBridge()

    prop_fps = 24

    ret = True
    frame_id = 0
    while(ret):
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        
        if (not ret1) or (not ret2):
            break

        # print(frame1) # h, w, c
        frame1 = cv2.resize(frame1, dsize = (640, 480)) # w h
        frame2 = cv2.resize(frame2, dsize = (640, 480)) # w h



        stamp = rospy.rostime.Time.from_sec(float(frame_id) / prop_fps)

        frame_id += 1
        
        ########################### RGB #############################
        image1 = cb.cv2_to_imgmsg(frame1, encoding='bgr8')
        image2 = cb.cv2_to_imgmsg(frame2, encoding='bgr8')

        image1.header.stamp = stamp
        image2.header.stamp = stamp

        image1.header.frame_id = "front_camera"
        image2.header.frame_id = "back_camera"

        ########################### write all in to the bag ###################
        


        bag.write(FRONT_TOPIC, image1, stamp)
        bag.write(BACK_TOPIC,  image2, stamp)
        bag.write(FRONT_INFO_TOPIC,  info, stamp)
        bag.write(BACK_INFO_TOPIC,   info, stamp)


    cap1.release()
    cap2.release()
    bag.close()

if __name__ == "__main__":
    CreateVideoBag()