#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def simple_publisher():
    # Initialize ROS node
    rospy.init_node('simple_publisher')

    # Create a publisher on the topic "numbers"
    pub = rospy.Publisher('numbers', Int32, queue_size=10)
    pub2= rospy.Publisher('numbers2', Int32, queue_size=10)

    # Rate at which to publish messages (1 Hz in this example)
    rate = rospy.Rate(1)

    # Publish values from 1 to 100 with a 1-second delay between each
    for i in range(1, 101):
        msg = Int32()
        msg.data = i
        pub.publish(msg)
        pub2.publish(msg)
        rospy.loginfo(i)
        rate.sleep()

if __name__ == '__main__':
    try:
        simple_publisher()
    except rospy.ROSInterruptException:
        pass

