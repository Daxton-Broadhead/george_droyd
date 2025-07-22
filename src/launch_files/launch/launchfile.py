import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from ros_gz_bridge.actions import RosGzBridge
from launch_ros.actions import Node


def generate_launch_description():

    keyboard_node = Node(
        package='key_press',
        executable='play_sound',
        name='play_sound',
        output='screen'
    )

    cv_node = Node(
        package='cpu_vision',
        executable='computer_vision',
        name='computer_vision',
        output='screen'
    )



    # Declare launch arguments FIRST
    declare_bridge_name_cmd = DeclareLaunchArgument(
        'bridge_name', default_value='gz_bridge_node', description='Name of ros_gz_bridge node'
    )

    declare_config_file_cmd = DeclareLaunchArgument(
        'config_file',
        default_value=os.path.join(
            FindPackageShare('launch_files').find('launch_files'),
            'config',
            'config_file.yaml'
        ),
        description='YAML config file for ros_gz_bridge'
    )

    # Create the launch description and add declarations first
    ld = LaunchDescription()
    ld.add_action(declare_bridge_name_cmd)
    ld.add_action(declare_config_file_cmd)
    ld.add_action(keyboard_node)
    ld.add_action(cv_node)

    # THEN use the LaunchConfiguration values
    ld.add_action(RosGzBridge(
        bridge_name=LaunchConfiguration('bridge_name'),
        config_file=LaunchConfiguration('config_file'),
    ))

    ld.add_action(ExecuteProcess(
        cmd=['gz', 'sim', 'sdf_files/building_robot.sdf'],
        output='screen'
    ))

    return ld
