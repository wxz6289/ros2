
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    t1 = Node(
        package='turtlesim',
        executable='turtlesim_node',
        ros_arguments=['--log-level', 'info', "--remap", "__ns:=/t2"],
        parameters=[os.path.join(get_package_share_directory('cpp01_launch'), 'config', 'n2.yml')],
        name='n2',
        exec_name='turtlesim_node',
        output='screen'
    )
    return LaunchDescription([
        t1
    ])  