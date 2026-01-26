urdf_to-grphviz

sudo apt install ros-$ROS_DISTRO-joint-state-publisher
sudo apt install ros-$ROS_DISTRO-robot-state-publisher

sudo apt install ros-$ROS_DISTRO-xacro


xacro hello_robot.xacro -o test.urdf

xacro --check /home/ros/ws/src/chapt6/install/hello_robot/share/hello_robot/urdf/fishbot.urdf.xacro
xacro /home/ros/ws/src/chapt6/install/hello_robot/share/hello_robot/urdf/fishbot.urdf.xacro > /dev/null
colcon build
ros2 launch hello_robot display_robot.launch.py model:=/home/ros/ws/src/chapt6/install/hello_robot/share/hello_robot/urdf/fishbot.urdf.xacro


```text
Gazebo (gz-sim)
   ↑        ↓
gz-ros2-control / ros_gz_bridge
   ↑        ↓
ROS 2 Jazzy (Nodes / Topics / Actions)
```
- Gazebo：物理仿真 + 可视化
- ROS 2：控制、规划、算法
- Bridge：通信桥梁

安装Gazebo
```sh
sudo apt install \
  gz-harmonic \
  ros-jazzy-ros-gz \
  ros-jazzy-gz-ros2-control
```

```sh
gz sim
gz sim empty.sdf
gz sim -v 4
```
```sh
ros2 run ros_gz_bridge parameter_bridge
```