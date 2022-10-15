#!/usr/bin/env python3

import rospy
import urllib3
from std_msgs.msg import Int32
http = urllib3.PoolManager()
speed = 0
steering = 0

def steerLeft():
  global steering
  if steering > -30:
    steering -= 10

def steerRight():
  global steering
  if steering < 30:
    steering += 10

def accelerate():
  global speed
  if speed < 150:
    speed += 25
  
def stop():
  global speed
  steering = 0
  speed = 0

def move(data):
  print(f'Received key : {data}')
  global speed
  global steering	
  # print(f'{data}')
  if data.data == 1:
    accelerate()
  elif data.data == 2:
    steerLeft()
  elif data.data == 3:
    steerRight()
  elif data.data == 0:
    stop()
  else:
    print('Unknown command executed')
  httpSend()  

def httpSend():
  try:
    ev3='192.168.0.111'
    global speed
    global steering
    fields = {
    	"speed": speed,
    	"steering": steering
    }
    http.request('GET', 'http://'+ev3+'/drive', fields=fields)
  except Exception as e:
    print(e)
  
if __name__ == '__main__':
  rospy.init_node("subscriber", anonymous=True)
  rospy.Subscriber("lidarscan", Int32, move)
  rospy.Subscriber("user_input", Int32, move)
  rospy.Rate(5)
  rospy.spin()
  # while not rospy.is_shutdown():
  #   if len(feilds) != 0:
  #     httpSend()
  #     feilds={}
  #     rospy.loginfo("sent http request")
  #     rospy.Rate(5)
  
