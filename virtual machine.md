复制粘贴共享
要在虚拟机中启用复制粘贴共享功能，您需要安装 VMware Tools 或 Open VM Tools。以下是安装 Open VM Tools 的步骤：
```bash
sudo apt update
sudo apt install -y open-vm-tools open-vm-tools-desktop
sudo reboot
```

```bash
# 查看系统架构
dpkg --print-architecture
```

lsb-release
```sh
# 查看发行版信息
lsb_release -a
# 查看发行版代号
lsb_release -cs
# 查看发行版版本号
lsb_release -rs
# 查看发行版描述
ls_release -ds
# 另一种查看发行版代号的方法
echo $VERSION_CODENAME
grep VERSION_CODENAME /etc/os-release

# 安装 lsb-release 工具
sudo apt install lsb-release
```

安装ROS
```sh
locale
locale -h  locale --help
locale -a
sudo apt update
sudo apt install locales
sudo apt autoremove
sudo locale-gen en_US en_US.UTF-8
locale
sudo apt install software-properties-common
sudo add-apt-respository universe
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F\" '{print $4}')
echo $ROS_APT_SOURCE_VERSION
curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb"
sudo dpkg -i /tmp/ros2-apt-source.deb
sudo apt update && sudo apt install ros-dev-tools
# 安装ROS基础版 包含通信库、消息包和命令行工具，不含RViz和示例
sudo apt install ros-jazzy-ros-base
# 安装完整桌面版ROS 带RViz和示例
sudo apt install ros-jazzy-desktop
printenv | grep ROS
source /opt/ros/jazzy/setup.bash
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
source ~/.bashrc
# 卸载ROS
sudo apt remove ~nros-jazzy-* && sudo apt autoremove
sudo apt remove ros2-apt-source && sudo apt update && sudo apt autoremove
sudo apt upgrade
```

环境变量
```sh
export ROS_DOMAIN_ID=10
echo "export ROS_DOMAIN_ID=10" >> ~/.bashrc
# 设置自动发现范围为30米
export ROS_AUTOMATIC_DISCOVERY_RANGE=30
```


Ubuntu GUI在VMware中容易失去焦点
```sh
sudo nano /etc/vmware-tools/tools.conf
```

取消注释：
```conf
WaylandEnable = false
```

保存并关闭文件，然后重启虚拟机。
```sh
sudo reboot
```

ros2
用户管理、检查和交互ROS系统的命令行工具，可以用来启动节点、设置参数、查看主题等。

```sh
sudo apt update
sudo apt install ros-jazzy-turtlesim
ros2 pkg executables turtlesim
ros2 run turtlesim turtlesim_node
ros2 run turtlesim turtle_teleop_key
ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=turtle2/cmd_vel
ros2 node list
ros2 topic list
ros2 service list
ros2 action list
```

rqt是ROS2的图形化工具，可以用来可视化和调试ROS2系统，包括节点图、主题监视器、参数设置等。
```sh
sudo apt update
sudo apt install "~nros-jazzy-rqt*"
rqt
```

dm_conctrol强化学习库依赖于mujoco库。
