#!/usr/bin/env python3
import csv
import rospy
from math import pow, atan2, sqrt
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from geometry_msgs.msg import Pose2D

PI = 3.1415926535897

class TurtleBot:
    def __init__(self):
        rospy.init_node('turtle_drawer', anonymous=True) 

        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) 
        
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)

        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def update_pose(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def euclidean_distance(self, goal_pose):
        res = sqrt(pow((goal_pose.x - self.pose.x), 2) +  
                   pow((goal_pose.y - self.pose.y), 2))
        return res
    
    def angular_distance(self, goal_pose):
        return abs(self.pose.theta - self.steering_angle(goal_pose))

    def linear_vel(self,goal_pose, constant=2):
        res = self.euclidean_distance(goal_pose)
        return constant * res
    
    def steering_angle(self, goal_pose):
        res = atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) 
        return res

    def angular_vel(self, goal_pose, constant=5):
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)
        
    
    def drawer(self):
        point_list = []
        
        distance_tolerance = 0.08
        angle_tolerance = 0.01

        vel_msg = Twist() 

        with open('result_corner.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            point_list = list(reader)
        goal_pose = Pose()

        for i in range(1, len(point_list)):
            goal_pose.x = float(point_list[i][0]) / 30 + 0.5
            goal_pose.y = float(point_list[i][1]) / 30 + 0.5

            while self.angular_distance(goal_pose) >= angle_tolerance:

                vel_msg.linear.x = 0
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = self.angular_vel(goal_pose)

                self.velocity_publisher.publish(vel_msg)
                self.rate.sleep()

            vel_msg.angular.z = 0
            self.velocity_publisher.publish(vel_msg)

            print(self.pose.theta)
            print(self.steering_angle(goal_pose))

            while self.euclidean_distance(goal_pose) >= distance_tolerance:
                vel_msg.linear.x = self.linear_vel(goal_pose)
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0
                
                self.velocity_publisher.publish(vel_msg)
                self.rate.sleep()
            print(str(self.pose.x) + "  " + str(self.pose.y))
            print(str(goal_pose.x) + "  " + str(goal_pose.y))

            vel_msg.linear.x = 0
            self.velocity_publisher.publish(vel_msg)

        rospy.spin()

if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.drawer()
    except rospy.ROSInterruptException:
        pass