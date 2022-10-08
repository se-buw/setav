#!/usr/bin/env python3
import cv2 as cv
import numpy as np
import rospy
import math
from sensor_msgs.msg import CompressedImage 

class steering:
    def __init__(self,initial=0):
        self.initial=initial
  
    def regression(self,image, lines):
        left=[]
        right = []
        left_side = np.array([left,np.int32])
        left_side = left_side .reshape((-1, 1, 2))
        right_side=np.array([right,np.int32])
        right_side = right_side.reshape((-1, 1, 2))
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            parameters = np.polyfit((x1, x2), (y1, y2), 1)
            slope = parameters[0]
            if slope < 0:
                left+=[[x1,y1],[x2,y2]]
            else:
                right+=[[x1,y1],[x2,y2]]
        image=np.polyfit(image,[left_side],False,(0,255,0),3)
        image=np.polyfit(image,[right_side],False,(0,255,0),3)
        return np.array(left,right)
    
    def steer(self,regression):
        curves=[]
        for value in regression:
            x=[]
            y=[]
            for index,element in np.ndenumerate(value):
                if(index==0):
                    x.append(element)
                else:
                    y.append(element)
            curve=np.polyfit(x,y,2)
            curves.append(curve)
        add=curves[1]+curves[2]
        mid_poly=add/2
        print(mid_poly)
        poly=np.poly1d(mid_poly)
        i=0
        for i in 600:
            if poly.subs(x,i)!=600:
                i+=1
            else:
                return i

    def angle(self,steer):
        final=self.steer/35.30
        if (self.initial-final)>0:
            return math.atan(final/34)
        else:
            return self.initial

