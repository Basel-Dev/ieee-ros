import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, IncludeLaunchDescription
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch.conditions import IfCondition

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare, FindPackagePrefix
from launch.substitutions import PathJoinSubstitution, Command, LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    package_name = "slam_t18"

    world = LaunchConfiguration("world")
    rviz = LaunchConfiguration("rviz")

    world_path = os.path.join(
        get_package_share_directory(package_name),
        "worlds",
        "sumo_maze_world.sdf",
    )

    declare_world = DeclareLaunchArgument(
        "world",
        default_value=world_path,
        description="Full path to the Gazebo world file",
    )

    urdf_path = os.path.join(
        get_package_share_directory(package_name),
        "urdf",
        "robot.urdf",
    )

    robot_state_publisher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory(package_name),
                "launch",
                "rsp.launch.py",
            )
        ),
        launch_arguments={
            "use_sim_time": "true",
            "urdf": urdf_path,
        }.items(),
    )

    gazebo = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
        PathJoinSubstitution([
            FindPackageShare("ros_gz_sim"),
            "launch",
            "gz_sim.launch.py"
        ])
    ),
    launch_arguments={
            "gz_args": f"-r {world_path}"
        }.items()
    )

    bridge_config_file = os.path.join(
        get_package_share_directory("slam_t18"),
        "config",
        "gz_bridge.yaml"
    )

    ros_gz_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        parameters=[{
            'config_file': bridge_config_file
        }]
    )

    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-topic",
            "robot_description",
            "-name",
            "diff_bot",
            "-x",
            "-4.5",
            "-z",
            "0.2",
        ],
        output="screen",
    )

    rviz_config_file = os.path.join(
        get_package_share_directory(package_name),
        "rviz",
        "slam.rviz",
    )

    rviz2 = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", rviz_config_file],
        output="screen",
        parameters=[
            {
                'use_sim_time': True
            }
        ]
    )

    slam_config_file = os.path.join(
        get_package_share_directory(package_name),
        "config",
        "slam_config.yaml"
    )

    slam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('slam_toolbox'),
                'launch',
                'online_async_launch.py'
            )
        ),
        launch_arguments={
            'use_sim_time': 'true',
            'slam_params_file': slam_config_file
        }.items()
    )

    return LaunchDescription([
        declare_world,
        robot_state_publisher,
        ros_gz_bridge,
        gazebo,
        spawn_robot,
        rviz2,
        slam_launch
    ])