from launch import LaunchDescription

from ament_index_python.packages import get_package_share_directory
import os
from launch_ros.actions import Node

import yaml

def generate_launch_description():

    config_path = os.path.join(
        get_package_share_directory("autonomous_traffic_manager"),
        "config",
        "robots.yaml"
    )

    with open(config_path, "r") as file:
        robots = yaml.safe_load(file)

    global_params = robots["GLOBAL_PARAMS"]
    robot_nodes = []
    for robot_id, params in robots.items():
        if robot_id == "GLOBAL_PARAMS":
            continue

        combined_params = {
            **global_params,
            **params,
            "other_robots": [r for r in robots.keys() if r != "GLOBAL_PARAMS" and r != robot_id]
        }
        
        robot_nodes.append(Node(
            package="autonomous_traffic_manager",
            executable="fleet_emulator",
            namespace=robot_id,
            parameters=[combined_params]
        ))


    return LaunchDescription(robot_nodes)