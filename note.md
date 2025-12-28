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

```zsh
ros2 run turtlesim turtlesim_node
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
ros2 okg prefix pkga-cpp
```

colcon
```zsh
colcon build
colcon build --help | grep select
colcon build --packages-select pkg_python
```