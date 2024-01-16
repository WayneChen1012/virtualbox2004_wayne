#!/usr/bin/env python
import sys
import rospy
from tutorial.srv import *

def subtract_two_ints_client(x, y):
    rospy.wait_for_service('subtract_two_ints')
    try:
        subtract_two_ints = rospy.ServiceProxy('subtract_two_ints', AddTwoInts)
        resp1 = subtract_two_ints(x, y)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s-%s"%(x, y))
    print("%s - %s = %s"%(x, y, subtract_two_ints_client(x, y)))
