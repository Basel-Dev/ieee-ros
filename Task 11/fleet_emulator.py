import rclpy
import math
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32
from rclpy.executors import SingleThreadedExecutor
from traffic_manager import RobotState, Decision, evaluate_traffic

## Predetermined IDs so the robots can subscribe to each other
ROBOT_INITS = {
    1: RobotState(0.0, 2.0, 0.0, 1),
    2: RobotState(0.0, 5.0, 0.0, 2)
}

class RobotNode(Node):
    def __init__(self, id, x, y, theta, priority):
        super().__init__(f"robot_{id}")
        self.id = id
        self.x = x
        self.y = y
        self.theta = theta
        self.priority = priority

        self.pose_publisher = self.create_publisher(Pose2D, f"/robot_{id}/pose", 10)
        self.priority_publisher = self.create_publisher(Int32, f"/robot_{id}/priority", 10)

        ## This is the dictionary where the other robots poses/priorities are saved
        self.fleet_view = {}

        self.pose_subscriptions = []
        self.priority_subscriptions = []

        ## Looping on every robot to subscribe to each of their topics and make a specific callback for each of them

        for robot_id, robot_state in ROBOT_INITS.items():
            if robot_id == id: continue
            self.fleet_view[robot_id] = robot_state ## Or this would be a RobotState with None values if this was a dynamic setup

            poseSub = self.create_subscription(Pose2D, f"/robot_{robot_id}/pose", self.make_pose_callback(robot_id), 10)
            prioritySub = self.create_subscription(Int32, f"/robot_{robot_id}/priority", self.make_priority_callback(robot_id), 10)

            self.pose_subscriptions.append(poseSub)
            self.priority_subscriptions.append(prioritySub)


        period = 1
        self.create_timer(period, self.timer_callback)


    def get_robot_state(self):
        return RobotState(self.x, self.y, self.theta, self.priority)
    
    ## Making callback funcs unique to each robot, so the node would know which message came from which robot node 
    ## Callback function goes to the unique robot id, and inserts their pose/priority in the fleet_view dictionary
    def make_pose_callback(self, robot_id):
        def callback(msg: Pose2D):
            fleet_view_entry = self.fleet_view[robot_id] 
            fleet_view_entry.x = msg.x
            fleet_view_entry.y = msg.y
            fleet_view_entry.theta = msg.theta
        return callback

    def make_priority_callback(self, robot_id):
        def callback(msg: Int32):
            self.fleet_view[robot_id].priority = msg.data
        return callback

    def timer_callback(self):
        logger = self.get_logger()

        ## Publishing Pose
        pose_msg = Pose2D()

        pose_msg.x = self.x
        pose_msg.y = self.y
        pose_msg.theta = self.theta

        self.pose_publisher.publish(pose_msg)
        
        ## Publishing Priority
        priority_msg = Int32()
        priority_msg.data = self.priority

        self.priority_publisher.publish(priority_msg)

        ## Yielding Protocol Log
        evaluation_decisions = evaluate_traffic(self.get_robot_state(), self.fleet_view)
        
        if not evaluation_decisions:
            logger.info("[CLEAR] No Robots in Safety Zone.")
        else:
            for decision in evaluation_decisions:
                robot_id = decision.robot_id
                match decision.status:
                    case "YIELD":
                        logger.warning(f"[DANGER] Higher-Priority \"robot_{robot_id}\" in Safety Zone! Yielding...")
                    case "PROCEED_LOWER":
                        logger.info(f"[CLEAR] Lower-Priority \"robot_{robot_id}\" in Safety Zone!")
                    case "DANGER_EQUAL":
                        ## Multiple ways to handle this just logging in general
                        logger.warning(f"[DANGER] Equal-Priority \"robot_{robot_id}\" in Safety Zone! Resolving conflict...")
   

def main():
    rclpy.init()
    executor = SingleThreadedExecutor()
    for ID, init in ROBOT_INITS.items():
        robot_node = RobotNode(ID, init.x, init.y, init.theta, init.priority)
        executor.add_node(robot_node)

    try:
        executor.spin()
    except: KeyboardInterrupt

        
if __name__ == "__main__":
    main()