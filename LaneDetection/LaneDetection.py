#!/usr/bin/env python3
import cv2 as cv
import numpy as np
import rospy
from sensor_msgs.msg import CompressedImage 





class lane:
    def __init__ (self,top_l,bottom_l,top_r,bottom_r):
        self.top_l=top_l
        self.bottom_l=bottom_l
        self.top_r=top_r
        self.bottom_r=bottom_r

# converting RGB image to Gray Scale Image

    def grayscale(self,image):  
        return cv.cvtColor(image,cv.COLOR_BGR2GRAY)    

# Getting the prespective of the lane from the top 
    def persective(self,image): 
        cv.circle(image,self.top_l,1,(0,255,0),-1)
        cv.circle(image,self.bottom_l,1,(0,255,0),-1)
        cv.circle(image,self.top_r,1,(0,255,0),-1)
        cv.circle(image,self.bottom_r,1,(0,255,0),-1)
        pts1=np.float32([self.top_l,self.bottom_l,self.top_r,self.bottom_r])
        pts2=np.float32([[0,0],[0,600],[800,0],[800,600]])
        matrix=cv.getPerspectiveTransform(pts1,pts2)
        return cv.warpPerspective(image,matrix,(800,600))

# Gaussian gilter to remove noise from the 
    def gaussianFilter(self,image): 
        return cv.GaussianBlur(image,(5,5),cv.BORDER_DEFAULT)

# canny edge detector to determine the edges in the images
    def canny(self,image):
        return cv.Canny(image,5,170)

# Making hough lines as per the edges detected
    def houghlines(self,image):
        return cv.HoughLinesP(image,rho=1,theta=np.pi/180,threshold=140,minLineLength=100,maxLineGap=10)

# drawing the lines as per the edges

    def drawLines(self,lines,image):
        if lines is not None:
            for line in lines:
                x1,y1,x2,y2 = line[0]
                cv.line(image, (x1,y1), (x2, y2), (0,255,0),5)
        return image
    

# Images ane send through methods one by one to determine lanes
def callback(data):
    detect=lane([175,100],[0,300],[515,100],[639,300])
    rospy.loginfo('Image received...')
    np_arr = np.fromstring(data.data, np.uint8)
    image= cv.imdecode(np_arr, cv.IMREAD_COLOR)
    birds_eye=detect.persective(image)
    gray=detect.grayscale(birds_eye)
    smooth=detect.gaussianFilter(gray)
    cv.imshow('smoothening',smooth)
    canny=detect.canny(smooth)
    cv.imshow('cannny edge',canny)
    hough=detect.houghlines(canny)
    print(hough)
    laneDetection=detect.drawLines(hough,birds_eye)
    cv.imshow('lanes',laneDetection)
    cv.imshow('image',image)
    cv.waitKey(1)
    cv.destroyAllWindows    

# Compressed Images are subscribed from the raspberry pi 
def main():   
    rospy.init_node("Images", anonymous=True)
    rospy.Subscriber('/usb_cam/image_raw/compressed',CompressedImage,callback,queue_size=10)
    
    rospy.spin()  


if __name__=='__main__':
    try:
        main()
    except rospy.ROSInitException:
        pass
