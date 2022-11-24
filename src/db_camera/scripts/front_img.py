#!/usr/bin/python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
print(cv2.__version__)

# uncomment this when using the fake crop row video
cap = cv2.VideoCapture("/home/huanyu-pc/agrirobot_ws/src/db_camera/scripts/dump_sample1.mp4")
# use abs path

# cap = cv2.VideoCapture(0) # comment this when using the fake crop row video
print(cap.isOpened())
bridge = CvBridge()

def talker():
    rospy.init_node("front_img_node", anonymous=False)

    pub = rospy.Publisher("color/image_raw", Image, queue_size=10)
    rate = rospy.Rate(10)

    ############################################################
    # uncomment this when using the fake crop row video
    cap.set(cv2.CAP_PROP_POS_FRAMES,8)  # Where frame_no is the frame you want, we want a static fake crop row
    ret, frame = cap.read()  # Read the frame
    ############################################################
    

    while not rospy.is_shutdown():
        # ret, frame = cap.read() # comment this when using the fake crop row video
        if not ret:
            break
        msg = bridge.cv2_to_imgmsg(frame, "bgr8")
        pub.publish(msg)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        if rospy.is_shutdown():
            cap.release()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass