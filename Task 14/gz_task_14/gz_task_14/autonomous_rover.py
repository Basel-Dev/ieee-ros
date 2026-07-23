import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped

class RobotMovement(Node):
    def __init__(self):
        super().__init__("robot_move")
        self.cmd_vel_publisher = self.create_publisher(TwistStamped, "/cmd_vel", 10)
        self.running = False
        self.sequence = [
            (self.go_forward, 4.9),
            (self.turnLeft, 1.1),
            (self.go_forward, 5),
            (self.turnRight, 1.15),
            (self.go_forward, 9.5),
            (self.turnRight, 1),
            (self.go_forward, 9.5),
            (self.turnRight, 1.1),
            (self.go_forward, 5),
            (self.turnRight, 1.1),
            (self.go_forward, 7.2)
            ]
        self.step = 0

    def go_forward(self, total_time):
        self.total_time = total_time
        self.start_time = self.get_clock().now()
        self.running = True
        self.forward_timer = self.create_timer(.1, self.forward_timer_callback)

    def forward_timer_callback(self):
        elapsed = (self.get_clock().now() - self.start_time).nanoseconds / 1e9
        if elapsed >= self.total_time:
            self.cmd_vel_publisher.publish(TwistStamped())
            self.running = False
            self.step += 1
            self.forward_timer.cancel()
        else:
            msg = TwistStamped()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = "base_link"

            msg.twist.linear.x = 1.5
            self.cmd_vel_publisher.publish(msg)
            

    def turn(self, right, total_time):
        msg = TwistStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "base_link"

        if right:
            msg.twist.angular.z = (-3.1415 / 2)
        else:
            msg.twist.angular.z = (3.1415 / 2)

        self.running = True
        self.cmd_vel_publisher.publish(msg)
        self.start_time = self.get_clock().now()
        self.total_time = total_time
        self.wait_timer = self.create_timer(.1, self.waitWhileTurn)

    def turnRight(self, total_time):
        self.turn(True, total_time)

    def turnLeft(self, total_time):
        self.turn(False, total_time)

    def waitWhileTurn(self):
        elapsed = (self.get_clock().now() - self.start_time).nanoseconds / 1e9
        if elapsed >= self.total_time:
            self.running = False
            self.step += 1
            self.cmd_vel_publisher.publish(TwistStamped())
            self.wait_timer.cancel()

    def start_sequence(self):
        self.sequence_timer = self.create_timer(.1, self.sequence_callback)

    def sequence_callback(self):
        if self.step >= len(self.sequence):
            self.sequence_timer.cancel()
            self.cmd_vel_publisher.publish(TwistStamped())
        else:
            if not self.running:
                func, arg = self.sequence[self.step]
                func(arg)
    
def main():
    rclpy.init()
    robot_movement = RobotMovement()
    robot_movement.start_sequence()

    rclpy.spin(robot_movement)
    robot_movement.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

