#!/usr/bin/env python3
  

from unittest import case
import rospy
import urllib3
from pynput.keyboard import Key, Listener

ev3='192.168.0.111'
http = urllib3.PoolManager()
motor_speed : int = 500
motor_steering : int = 0

def on_press(key):  
  global motor_speed
  global motor_steering
  changedSteering=False
  changedSpeed=False
  if key == Key.up:
    motor_speed+=100
    changedSpeed=True
  elif key == Key.down:
    motor_speed-=100
    changedSpeed=True
  elif key == 's':
    motor_speed=0 
    changedSpeed=True
  elif key == Key.left:
    motor_steering-=5
    changedSteering=True
  elif key == Key.right:
    motor_steering+=5;
    changedSteering=True
  fields = {};
  if changedSpeed:
    fields['speed'] = motor_speed
  if changedSteering:
    fields['steering'] = motor_steering
  if (changedSteering | changedSpeed):
    try:
        http.request('GET', 'http://'+ev3+'/drive', fields=fields)
    except:
        print("cannot connect to ev3" )

if __name__ == '__main__':
       rospy.init_node('publisher', anonymous=True)
       try:
            with Listener(on_press=on_press) as listener:listener.join()
       except rospy.ROSInterruptException:
           pass
           print("Stop publishing keyboard")
