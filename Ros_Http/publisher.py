#!/usr/bin/env python3

import rospy
import urllib3
from std_msgs.msg import Int32
ev3='192.168.0.111'
http = urllib3.PoolManager()
feilds = {}


def move(data):
  feilds['speed']=data.data
  print("its calling me move")

def steer(data):
  feilds['steering']=data.data
  print("its calling me steer")

def httpSend():
  try:
    rospy.loginfo(feilds)
    http.request('GET', 'http://'+ev3+'/drive', fields=feilds)
  except:
      print("cannot connect to ev3" )
  


if __name__ == '__main__':
  rospy.init_node("subscriber",anonymous=True)
  rospy.Subscriber("speed_values",Int32,move)
  rospy.Subscriber("steer_values",Int32,steer)
  while not rospy.is_shutdown():
    if len(feilds) != 0:
      httpSend()
      feilds={}
      rospy.loginfo("sent http request")
      rospy.Rate(5)
  
