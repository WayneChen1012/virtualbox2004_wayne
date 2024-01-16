#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback_chatter(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard on chatter: %s", data.data)

def callback_another_chatter(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard on another_chatter: %s", data.data)

def listener():
    rospy.init_node('py_listener', anonymous=True)

    # Subscriber for the first topic
    rospy.Subscriber("chatter", String, callback_chatter)

    # Subscriber for the second topic
    rospy.Subscriber("another_chatter", String, callback_another_chatter)

    rospy.spin()

if __name__ == '__main__':
    listener()


# #!/usr/bin/env python3
# import rospy
# from std_msgs.msg import String

# def callback(data):
#     rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.data)

# def listener():
#     rospy.init_node('py_listener', anonymous=True)
#     rospy.Subscriber("chatter", String, callback)
#     rospy.spin()

# if __name__ == '__main__':
#     listener()
