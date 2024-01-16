#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "cpp_talker");
  ros::NodeHandle n;

  // First publisher
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);

  // Second publisher for a new topic
  ros::Publisher another_chatter_pub = n.advertise<std_msgs::String>("another_chatter", 1000);

  ros::Rate loop_rate(10);

  while (ros::ok())
  {
    // First message
    std_msgs::String msg1;
    std::stringstream ss1;
    ss1 << "cppPUB1 " << ros::Time::now();
    msg1.data = ss1.str();
    ROS_INFO("%s", msg1.data.c_str());
    chatter_pub.publish(msg1);

    // Second message
    std_msgs::String msg2;
    std::stringstream ss2;
    ss2 << "cppPUB2 " << ros::Time::now();
    msg2.data = ss2.str();
    ROS_INFO("%s", msg2.data.c_str());
    another_chatter_pub.publish(msg2);

    ros::spinOnce();
    loop_rate.sleep();
  }

  return 0;
}


// #include "ros/ros.h"
// #include "std_msgs/String.h"
// #include <sstream>

// int main(int argc, char **argv)
// {
//   ros::init(argc, argv, "cpp_talker");
//   ros::NodeHandle n;
//   ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);
//   ros::Rate loop_rate(10);

//   while (ros::ok())
//   {
//     std_msgs::String msg;
//     std::stringstream ss;
//     ss << "HW1 " << ros::Time::now();
//     msg.data = ss.str();

//     ROS_INFO("%s", msg.data.c_str());
//     chatter_pub.publish(msg);

//     ros::spinOnce();
//     loop_rate.sleep();
//   }

//   return 0;
// }



// #include "ros/ros.h"
// #include "std_msgs/String.h"
// #include <sstream>

// int main(int argc, char **argv)
// {
//   ros::init(argc, argv, "cpp_talker");
//   ros::NodeHandle n;
//   ros::Publisher chatter_pub = n.advertise<std_msgs::String>("topic", 1000);
//   ros::Rate loop_rate(10);

//   while (ros::ok())
//   {
//     std_msgs::String msg;
//     std::stringstream ss;
//     ss << "hello world " << ros::Time::now();
//     msg.data = ss.str();

//     ROS_INFO("%s", msg.data.c_str());
//     chatter_pub.publish(msg);
//     ros::spinOnce();
//     loop_rate.sleep();
//   }

//   return 0;
// }
