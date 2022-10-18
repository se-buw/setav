#!/usr/bin/env python3

from logging import shutdown
from mimetypes import init
from xmlrpc.client import boolean
from numpy import rate
import rospy 
from std_msgs.msg import Int32
from pynput.keyboard import Key, Listener


def on_press(key):
    pub_ui = rospy.Publisher("user_input",Int32,queue_size=1)
    if key == Key.up:
        rospy.loginfo("publishing up key")
        pub_ui.publish(1)
    elif key == Key.down:
        rospy.loginfo("publishing down key")
        pub_ui.publish(0)
    elif key == Key.left:
        rospy.loginfo("publishing left key")
        pub_ui.publish(2)
    elif key == Key.right:
        rospy.loginfo("publishing right key")
        pub_ui.publish(3)
        
if __name__=="__main__":
    rospy.init_node("user_input",anonymous=True)
    try:
        with Listener(on_press=on_press) as listener:listener.join()
    except rospy.ROSInterruptException:
           pass
           print("Stop publishing keyboard")
    

