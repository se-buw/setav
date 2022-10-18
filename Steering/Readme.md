# Steering using Lanes

The hough lines obtained is not continuous. 

So i have separated the lines detected based on their slopes.

if the slope is less than zero it is left lane and if the slope is grater than zero its right lane.

Straight lines of left lane is appended into left array vice versa to the right

then i had used polynomial curve fitting through each array which results two polynomial equations. 

We will get the mid polynomial 