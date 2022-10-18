# Lane detection 

The images obtained from web camera using ros image Subscriber went through a series of process 
to detect lanes in real time.

There are several methods available for lane detection.

1. Thresholding and warping lanes
2. Canny edge detector
3. Sliding window


In this project we used canny edge detector. The images Subscribed went through a series of steps.

>Grayscale Images
To reduce computational requirements
>prespective Transform 
The prespective of the lane in the image. Is transformed to a birds eye view.
>GaussianFilter
To remove any noise present in the Image we used gaussian noise filter with a kernel size of (5x5). 
>canny edge detector
The edges present in the image is detected using canny
>Hough lines
The detected edges are drwn on the Image using Hough lines.rho=1,theta=np.pi/180,threshold=140,minLineLength=100,maxLineGap=10 these values gives many small line segments which are ideal for polynomial curve fitting. 