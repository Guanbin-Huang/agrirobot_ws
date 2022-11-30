# agri_bot

Note:
    - in order to have a good run, the following is recommended.
    - [for ROS debug] python extension v2021.8.1159798656, otherwise python2 cannot be debugged.
    - ROS v0.7.0

- 11/24
    - create rosbag to debug such that we don't need to rely on camera.
    - tools/mp4_2_rosbag.py is used to create rosbag. For simplicity, the front and back camera share the same camera_info which might be used for calibrating.
