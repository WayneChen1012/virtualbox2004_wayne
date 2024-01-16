#!/usr/bin/env python3
import rospy
from tutorial.srv import AddTwoInts,AddTwoIntsResponse

# #加法
def handle_add_two_ints(req):
    print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))) ###Returning [%s ? %s = %s] 改？處
    return AddTwoIntsResponse(req.a * req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()

## 減法
## def handle_add_two_ints(req):
##     result = req.a - req.b
##     print("Returning [%s - %s = %s]" % (req.a, req.b, result))
##     return AddTwoIntsResponse(result)

## def add_two_ints_server():
##     rospy.init_node('subtract_two_ints_server')
##     s = rospy.Service('subtract_two_ints', AddTwoInts, handle_add_two_ints)
##     print("Ready to subtract two ints.")
##     rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()