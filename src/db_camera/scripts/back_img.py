#!/usr/bin/python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

cap = cv2.VideoCapture(2)
print(cap.isOpened())
bridge = CvBridge()

def talker():
    rospy.init_node("back_cam_node", anonymous=False)

    pub = rospy.Publisher("color/image_raw", Image, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        ret, frame = cap.read()
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