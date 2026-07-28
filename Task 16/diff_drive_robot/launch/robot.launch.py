import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

from launch_ros.actions import Node


def generate_launch_description():

    package_name = "diff_drive_robot"

    world = LaunchConfiguration("world")
    rviz = LaunchConfiguration("rviz")

    world_path = os.path.join(
        get_package_share_directory(package_name),
        "worlds",
        "empty.world",
    )

    declare_world = DeclareLaunchArgument(
        "world",
        default_value=world_path,
        description="Full path to the Gazebo world file",
    )

    declare_rviz = DeclareLaunchArgument(
        "rviz",
        default_value="False",
        description="Open RViz if set to True",
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
        os.path.join(
            get_package_share_directory("ros_gz_sim"),
            "launch",
            "gz_sim.launch.py",
        )
    ),
    launch_arguments={
        "gz_args": ["-r -v 4 ", world],
    }.items(),
)

    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-topic",
            "robot_description",
            "-name",
            "diff_bot",
            "-z",
            "0.2",
        ],
        output="screen",
    )

    rviz_config_file = os.path.join(
        get_package_share_directory(package_name),
        "rviz",
        "bot.rviz",
    )

    rviz2 = GroupAction(
        condition=IfCondition(rviz),
        actions=[
            Node(
                package="rviz2",
                executable="rviz2",
                arguments=["-d", rviz_config_file],
                output="screen",
            )
        ],
    )

    config_file = PathJoinSubstitution([
            FindPackageShare("diff_drive_robot"),
            "config",
            "gz_bridge.yaml"
        ])

    ros_gz_bridge = Node(
            package="ros_gz_bridge",
            executable="parameter_bridge",
            parameters=[{
                'config_file': config_file
            }]
        )

    return LaunchDescription([
        declare_world,
        declare_rviz,
        ros_gz_bridge,

        robot_state_publisher,
        gazebo,
        spawn_robot,
        rviz2,
    ])