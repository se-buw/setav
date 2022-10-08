#!/usr/bin/env python3

from logging import shutdown
from mimetypes import init
from xmlrpc.client import boolean
from numpy import rate
import rospy 
from std_msgs.msg import Int32
from pynput.keyboard import Key, Listener

motor_speed=100
def on_press(key):
    pub_speed= rospy.Publisher("speed_values",Int32,queue_size=1)
    pub_steering=rospy.Publisher("steer_values",Int32,queue_size=1)
    rospy.loginfo("publishing the key")
    global motor_speed
    motor_steering=0

    if key == Key.up:
        if(motor_speed<1000):
            motor_speed=motor_speed+100
        pub_speed.publish(motor_speed)
    elif key == Key.down :
        if(motor_speed>-1000):
            motor_speed=motor_speed-100
        pub_speed.publish(motor_speed)
    elif key == Key.right:
        motor_steering=-10;
        pub_steering.publish(motor_steering)
    elif key == Key.left: 
        motor_steering=10;
        pub_steering.publish(motor_steering)
    elif key== Key.space:
        motor_speed=0 
        pub_speed.publish(motor_speed)
if __name__=="__main__":
    rospy.init_node("key_publisher",anonymous=True)
    try:
        with Listener(on_press=on_press) as listener:listener.join()
    except rospy.ROSInterruptException:
           pass
           print("Stop publishing keyboard")
    

