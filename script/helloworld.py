#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('chat', String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        hello = "hello world ! %s" % rospy.get_time()
        pub.publish(hello)
        rospy.loginfo(hello)
        rate.sleep()

# 主要用於發布訊息。在程式碼中，
# 首先初始化了一個名為’talker’的節點，
# 然後創建了一個名為’chat’的發布者。
# 然後在一個迴圈中，只要ROS沒有關閉，
# 就會發布一個包含當前時間的"hello world"訊息，
# 並將該訊息記錄在日誌中。
# 每次發布訊息後，程式會暫停一段時間以維持特定的發布頻率。