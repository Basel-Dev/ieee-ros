from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():

    world = PathJoinSubstitution([
        FindPackageShare("gz_task_14"),
        "worlds",
        "t14.sdf"
    ])

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare("ros_gz_sim"),
                "launch",
                "gz_sim.launch.py"
            ])
        ),
        launch_arguments={
            "gz_args": ["-r ", world]
        }.items()
    )

    spawn_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare("turtlebot3_gazebo"),
                "launch",
                "spawn_turtlebot3.launch.py"
            ])
        ),
        launch_arguments={
            "x_pose": "-12",
            "y_pose": "4"
        }.items()
    )

    robot_move = Node(
        package="gz_task_14",
        executable="autonomous_rover",
        name="robot_move"
    
    )

    return LaunchDescription([
        gazebo,
        spawn_robot,
        robot_move
    ])