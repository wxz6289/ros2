from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    n1 = Node(
        package='turtlesim',
        executable='turtlesim_node',
        exec_name='turtlesim_node',
        ros_arguments=['--log-level', 'info', "--remap", "__ns:=/t2"],
        # ros_arguments=['--ros-args', '--log-level', 'info', "--remap", "__ns:=/t1"],
        # parameters=[{
        #     'background_r': 120,
        #     'background_g': 210,
        #     'background_b': 230
        # }],
        # parameters=['/home/ros/ws/src/py01_launch/config/n2.yml'],  
        parameters=[os.path.join(get_package_share_directory('py01_launch'), 'config', 'n2.yml')],
        name='n2',
        output='screen'
    )
    return LaunchDescription([
        n1
    ])