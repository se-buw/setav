import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Int32

def calculate_strength(arr, max_val, min_val, start, end):
  total = 0
  avg = (max_val + min_val) / 2
  for i in range(start, end):
    if arr[i] < 0.5:
      total += 1
    else:
      total += 0
  return total

def callback(msg):
  pub_scan = rospy.Publisher("lidarscan",Int32,queue_size=1)
  arr = msg.ranges
  max_val = msg.range_max
  min_val = msg.range_min
  global steering
  global speed
  right = calculate_strength(arr, max_val, min_val, 1097, 1147) / 50
  left = calculate_strength(arr, max_val, min_val, 0, 50) / 50
  print(f'{left}, {right}')
  if left > 0:
    rospy.loginfo("publishing left key")
    pub_scan.publish(2)
  elif right > 0:
    rospy.loginfo("publishing left key")
    pub_scan.publish(3)

if __name__ == '__main__':  
  rospy.init_node('subscriber', anonymous=True)
  sub = rospy.Subscriber('/scan', LaserScan, callback)
  rospy.Rate(5)
  rospy.spin()