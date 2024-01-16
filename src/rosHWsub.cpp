//訂閱多個話題
#include "ros/ros.h"
#include "std_msgs/String.h"

void chatterCallback1(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("Chatter 1: [%s]", msg->data.c_str());
}

void chatterCallback2(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("Chatter 2: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "multi_subscriber");
  ros::NodeHandle n;

  ros::Subscriber sub1 = n.subscribe("topic1", 1000, chatterCallback1);
  ros::Subscriber sub2 = n.subscribe("topic2", 1000, chatterCallback2);

  ros::spin();

  return 0;
}



//訂閱一個話題
// #include "ros/ros.h"
// #include "std_msgs/String.h"

// void chatterCallback(const std_msgs::String::ConstPtr& msg)
// {
//   ROS_INFO("I heard: [%s]", msg->data.c_str());
// }

// int main(int argc, char **argv)
// {
//   ros::init(argc, argv, "cpp_listener");
//   ros::NodeHandle n;
//   ros::Subscriber sub = n.subscribe("HW1", 1000, chatterCallback); //要使用與pub同樣的話題
//   ros::spin();

//   return 0;
// }