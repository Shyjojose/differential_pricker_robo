#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from pynput.keyboard import Key, Listener

# Initialize node
rospy.init_node('keyboard_control', anonymous=True)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(10)  # 10hz

def on_press(key):
    twist = Twist()
    try:
        if key.char == "w":
            twist.linear.x = 1.0  # Move forward
        elif key.char == "s":
            twist.linear.x = -1.0  # Move backward
        elif key.char == "a":
            twist.angular.z = 1.0  # Turn left
        elif key.char == "d":
            twist.angular.z = -1.0  # Turn right
        pub.publish(twist)
    except AttributeError:
        pass

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False
    # Stop the robot when the key is released
    twist = Twist()
    pub.publish(twist)

if __name__ == '__main__':
    # Collect events until released
    with Listener(on_press=on_press, on_release=on_release) as listener:
        rospy.spin()