# Lane detection 


There are sevaral methods to detect lanes 
1. Thresholding
2. Canny edge 
3. Sliding window

we have used Canny edge detector

The Image obtained from Web cam goes through a series of process 

>Grayscale
>Prespective transformation 
perspective of image is transformed by chossing poins manually.
>Gaussian Blur
To remove noise i have used a kernel size of (5x5) 
>Canny edge
The edges obtained from canny.
>Hough lines
rho=1,theta=np.pi/180,threshold=140,minLineLength=100,maxLineGap=10 with this threshold limit we will get many small lines for polynomial curve fitting. I got these values by testing.
