import time, sys, os
from ros import rosbag
import roslib, rospy
roslib.load_manifest('sensor_msgs')
from sensor_msgs.msg import Image

from cv_bridge import CvBridge
import cv2

FRONT_TOPIC = '/rs_nav_front/color/image_raw'
BACK_TOPIC  = '/rs_nav_back/color/image_raw'

def CreateVideoBag(bagname = "mybag.bag"):
    '''Creates a bag file with n video files'''
    bag = rosbag.Bag(bagname, 'w')
    cap1 = cv2.VideoCapture("/home/huanyu-pc/agrirobot_ws/src/db_camera/scripts/front.mp4")
    cap2 = cv2.VideoCapture("/home/huanyu-pc/agrirobot_ws/src/db_camera/scripts/back.mp4")
    
    cb = CvBridge()

    prop_fps = 24

    ret = True
    frame_id = 0
    while(ret):
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if (not ret1) or (not ret2):
            break

        stamp = rospy.rostime.Time.from_sec(float(frame_id) / prop_fps)

        frame_id += 1
        image1 = cb.cv2_to_imgmsg(frame1, encoding='bgr8')
        image2 = cb.cv2_to_imgmsg(frame2, encoding='bgr8')

        image1.header.stamp = stamp
        image2.header.stamp = stamp

        image1.header.frame_id = "front_camera"
        image2.header.frame_id = "back_camera"

        bag.write(FRONT_TOPIC, image1, stamp)
        bag.write(BACK_TOPIC,  image2, stamp)


    cap1.release()
    cap2.release()
    bag.close()

if __name__ == "__main__":
    CreateVideoBag()