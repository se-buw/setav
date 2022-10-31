# Connecting ros and ev3 using http server on the ev3  and publish the commands on pc using ros.
for passing commands to the motor we have used arrow buttons on the pc.

Pynput is used as a module for lisening key strokes and publish the message.

This way the car moves forward, backwards and steer.

we observe that there a time lage of 1 second.

Altough this is initial implementation we did not use the data from the rp_lidar.

In coming days we will integrate to make the vehicle autonomous.

