
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    t1 = Node(
        package='turtlesim',
        executable='turtlesim_node',
        parameters=[os.path.join(get_package_share_directory('cpp01_launch'), 'config', 'n2.yml')],
        # name='n2',
        exec_name='turtlesim_node',
        output='screen'
    )
    cmd = ExecuteProcess(
        cmd = [FindExecutable(name='ros2'), 'topic', 'echo', '/turtle1/pose'],
        # cmd=['ros2', 'topic', 'echo', '/turtle1/pose'],
        output='both',
        shell=True
    )
    return LaunchDescription([
        t1,
        cmd 
    ])  