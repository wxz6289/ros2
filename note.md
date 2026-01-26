# cmake

CMakeLists.txt
```txt
cmake_minimum_required(VERSION 3.8)
project(hello)
add_executable(hello_cmake hello.cpp)
```

```zsh
cmake .
cmake build .
make

```

环境变量
$ROS_DISTRO
$ROS_VERSION
AMENT_PREFIX_PATH 查找功能包

输出环境变量
printenv

```sh
ros2 run demo_nodes_py listener
ros2 run demo_nodes_cpp talker
```

```zsh
ros2 run turtlesim turtlesim_node
ros2 run turlesim turtle_teleop_key
```

默认脚本
.bashrc

export RCUTILS_CONSOLE_OUTPUT_FORMATE=[{function_name}:{line_number}]:{message}

ros中安装pip
```bash
apt-get update
sudo apt install python3-pip
python3 -m pip install --user xxx
```

vsc 打开新Terminal`Ctrl+Shift+5`


```bash
ros2 pkg list | grep rclcpp
sudo apt update
sudo apt install ros-humble-rclcpp

apt update && apt install -y ros-humble-rclcpp

ros2 node list
ros2 node info /ros_node2

```

rc
`/opt/ros/humble/include/**`

```bash
ros2 pkg
ros2 pkg create --help
ros2 pkg create pkg_python --build-type ament_python --license Apache-2.0
colcon build
source install/setup.zsh
ros2 run pkg_python python_node
export PYTHONPATH=$PYTHONPATH:/ros2_ws/src/pkg_python/install/lib/python3.12/site-packages
```

```bash
ros2 pkg create pkg_cpp --build-type ament_cmake --license Apache-2.0
ldd cpp_node
ros2 pkg prefix pkga-cpp
```

colcon
```zsh
sudo apt update
sudo apt install -y python3-colcon-common-extensions python3-colcon-clean
colcon info
colcon build
colcon build --help | grep select
colcon build --packages-select pkg_python
colcon build --packages-skip broken_pkg
# 限制内存
colcon build --executor sequential

python -m http.server
apt-get update --fix-missing
sudo apt install python3-requests
```

Topic
- 发布者
- 订阅者
- 话题名称
- 话题类型

```sh
ros2 pkg list | grep turtlesim
echo $ROS_DISTRO
sudo apt install ros-jazzy-turtlesim
ros2 run turtlesim turtlesim_node
ros2 pkg executables turtlesim

```

解决禁用Fast DDS的SHM问题
```sh
df -h /dev/shm

export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
export FASTRTPS_DEFAULT_PROFILES_FILE=/tmp/fastdds_no_shm.xml

cat << 'EOF' > /tmp/fastdds_no_shm.xml
<?xml version="1.0" encoding="UTF-8" ?>
<profiles xmlns="http://www.eprosima.com/XMLSchemas/fastRTPS_Profiles">
  <transport_descriptors>
    <transport_descriptor>
      <transport_id>udp_transport</transport_id>
      <type>UDPv4</type>
    </transport_descriptor>
  </transport_descriptors>

  <participant profile_name="no_shm_profile" is_default_profile="true">
    <rtps>
      <useBuiltinTransports>false</useBuiltinTransports>
      <userTransports>
        <transport_id>udp_transport</transport_id>
      </userTransports>
    </rtps>
  </participant>
</profiles>
EOF

echo 'export RMW_IMPLEMENTATION=rmw_fastrtps_cpp' >> ~/.zshrc
echo 'export FASTRTPS_DEFAULT_PROFILES_FILE=/tmp/fastdds_no_shm.xml' >> ~/.zshrc


ros2 run turtlesim turtlesim_node
ros2 run turtlesion trutlesim_teleop_key
ros2 topic echo /turtle1/pose
ros2 topic list
ros2 topic info /turtle1/cmd_vel
ros2 interface show /turtle1/cmd_vel
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: { x: 1.0, y: 0 }}"
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: { x: 0.5, y: 1}, angular: { z: -0.5 }}"
ros2 topic pub --help

```

```sh
ros2 pkg create learn_topic --build-type ament_python --dependencies rclpy example_interfaces --license Apache-2.0
colcon build
ros2 interface list

sudo apt update
sudo apt install ros-jazzy-example-interfaces
apt list --installed| grep example_interfaces

ros2 interface list | grep example_interfaces
ros2 topic hz /novel
```

```sh
colcon build --base-paths src/chapt3_topic/src --packages-se
lect status_interfaces --symlink-install
source install/setup.zsh 
ros2 interface show status_interfaces/msg/SystemStatus

```

‵‵`sh
rqt
rviz2

```

简化机器人开发

避障 
