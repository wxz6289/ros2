import os
import launch
import launch_ros
from ament_index_python import get_package_share_directory

def generate_launch_description():
    urdf_package_path = get_package_share_directory('hello_robot')
    urdf_path = os.path.join(urdf_package_path, 'urdf', 'hello_robot.urdf')
    default_rviz_config_path = os.path.join(urdf_package_path, 'config', 'display_robot.rviz')
     
    action_declare_arg_mode_path = launch.actions.DeclareLaunchArgument(
       name="model",
       default_value=str(urdf_path),
       description="load robot urdf file"
    )

    substitution_command_result = launch.substitutions.Command(['xacro ', launch.substitutions.LaunchConfiguration('model')])
    robot_description_value = launch_ros.parameter_descriptions.ParameterValue(substitution_command_result, value_type=str) 

    action_robot_state_publisher = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[{'robot_description': robot_description_value}],
        output='screen'
    )   

    action_robot_joint_state_publisher = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
    )

    action_rivz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', default_rviz_config_path]
    )

    return launch.LaunchDescription([
        action_declare_arg_mode_path,
        action_robot_state_publisher,
        action_robot_joint_state_publisher,
        action_rivz_node
    ])

