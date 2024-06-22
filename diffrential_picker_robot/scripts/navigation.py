#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

move_bindings = {
    'w': (1, 0, 0, 0),
    'a': (0, 0, 0, 1),
    's': (-1, 0, 0, 0),
    'd': (0, 0, 0, -1),
}

stop_bindings = {
    'x': (0, 0, 0, 0)
}

def get_key():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def ramp_down(pub, twist, duration=1.0):
    rate = rospy.Rate(10)
    for i in range(10):
        twist.linear.x *= 0.9
        twist.angular.z *= 0.9
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('keyboard_control', anonymous=True)
    pub = rospy.Publisher('/cmd_vel_inverted', Twist, queue_size=10)

    twist = Twist()

    try:
        print("Control Your Robot!")
        print("Press 'x' to stop the robot")

        while not rospy.is_shutdown():
            key = get_key()
            if key in move_bindings.keys():
                x, y, z, th = move_bindings[key]
                twist.linear.x = x
                twist.angular.z = th
                pub.publish(twist)
            elif key in stop_bindings.keys():
                ramp_down(pub, twist)
                twist = Twist()
                pub.publish(twist)
            else:
                if key == '\x03':
                    break

    except Exception as e:
        print(e)

    finally:
        twist = Twist()
        pub.publish(twist)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
