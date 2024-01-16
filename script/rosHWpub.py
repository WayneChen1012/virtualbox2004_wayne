# 發布兩個話題
#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    pub1 = rospy.Publisher('topic1', String, queue_size=10)
    pub2 = rospy.Publisher('topic2', String, queue_size=10)
    rospy.init_node('py_talker', anonymous=True) ###創建一個名為 py_talker 的 ROS 節點
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        msg1 = "Hello on topic 1 %s" % rospy.get_time()
        msg2 = "Hello on topic 2 %s" % rospy.get_time()

        rospy.loginfo(msg1)
        pub1.publish(msg1)

        rospy.loginfo(msg2)
        pub2.publish(msg2)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass




## 發布一個話題
## #!/usr/bin/env python3
## import rospy
## from std_msgs.msg import String

## def talker():
##     pub = rospy.Publisher('HW1', String, queue_size=10) #節點以10hz的頻率發布到chatter話題
##     rospy.init_node('py_talker', anonymous=True) #節點名稱為py_talker
##     rate = rospy.Rate(10) # 10hz
##     while not rospy.is_shutdown():
##         str = "S %s" % rospy.get_time()
##         rospy.loginfo(str)
##        pub.publish(str)
##         rate.sleep()

# if __name__ == '__main__':
#     try:
#         talker()
#     except rospy.ROSInterruptException:
#         pass
