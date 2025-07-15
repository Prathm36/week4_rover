#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from std_msgs.msg import Float64MultiArray
import math
import time

class Controller(Node):
    def __init__(self):
        super().__init__('controller')
        self.publisher_ = self.create_publisher(
            Float64MultiArray,
            '/rover/control_input',
           10
        )

        self.listener_callback()

    def listener_callback(self):
        control = Float64MultiArray()
        
        fl_steer, fr_steer, rl_steer, rr_steer, fl_drive, fr_drive, rl_drive, rr_drive =0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
        control.data = [fl_steer, fr_steer, rl_steer, rr_steer, fl_drive, fr_drive, rl_drive, rr_drive]
        control.data[4], control.data[5], control.data[6], control.data[7] =1.0,1.0,1.0,1.0
        self.publisher_.publish(control)
        self.get_logger().info("Starting.")
        time.sleep(10)
        self.publisher_.publish(control)
        self.get_logger().info("Moving 2 meters forward.")
        time.sleep(10)
        control.data[4], control.data[5], control.data[6], control.data[7] =0.0,0.0,0.0,0.0
        control.data[0], control.data[1], control.data[2], control.data[3] = math.pi, math.pi, math.pi, math.pi
         
        self.publisher_.publish(control)
        self.get_logger().info("Turning wheels to angle -90 degrees.")
        time.sleep(10)
        control.data[4], control.data[5], control.data[6], control.data[7] =1.0,1.0,1.0,1.0
        control.data[0], control.data[1], control.data[2], control.data[3] =0.0,0.0,0.0,0.0
         
        self.publisher_.publish(control)
        self.get_logger().info("Moving 2 meters forward.")
        time.sleep(10)
        control.data[4], control.data[5], control.data[6], control.data[7] =0.0,0.0,0.0,0.0
        control.data[0], control.data[1], control.data[2], control.data[3] = math.pi, math.pi, math.pi, math.pi
         
        self.publisher_.publish(control)
        self.get_logger().info("Turning wheels back to angle 90 degrees.")
        time.sleep(10)
        control.data[4], control.data[5] =-1.0,-1.0
        control.data[6], control.data[7] =1.0,1.0
        control.data[0], control.data[1], control.data[2], control.data[3] =0.0,0.0,0.0,0.0
         
        self.publisher_.publish(control)
        self.get_logger().info("Rotating rover in place using differential drive.")
        time.sleep(10)
        control.data[4], control.data[5], control.data[6], control.data[7] =1.0,1.0,1.0,1.0
        control.data[0], control.data[1] = -math.pi/4, -math.pi/4
        control.data[2], control.data[3] = math.pi/4, math.pi/4
         
        self.publisher_.publish(control)
        self.get_logger().info("Rotating rover in place using independent steering.")
        time.sleep(10)
        control.data[0], control.data[1] = math.pi/2, math.pi/2
         
        self.publisher_.publish(control)
        self.get_logger().info("Rotating all wheels to 45 degree and Rover Signing off.......")
        time.sleep(10)



def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = Controller()


    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()