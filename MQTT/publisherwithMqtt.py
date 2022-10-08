#!/usr/bin/env python3
  
import rospy
import paho.mqtt.client as mqtt
from std_msgs.msg import Float64
import json

mqttBroker="mqtt.eclipseprojects.io"
client = mqtt.Client("Say_Hello")
client.connect(mqttBroker) 
   
def talker():
        pub = rospy.Publisher('chatter', Float64, queue_size=1)
        rospy.init_node('publisher', anonymous=True)
        rate = rospy.Rate(8) 
        while not rospy.is_shutdown():
            motor_speed = 1000
            rospy.loginfo(motor_speed)
            pub.publish(client.publish("ros_mqtt",motor_speed))
            rate.sleep()
   
if __name__ == '__main__':
       try:
           talker()
       except rospy.ROSInterruptException:
           pass
           print("Stop publishing keyboard")
