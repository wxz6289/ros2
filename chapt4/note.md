```sh
ros2 service list -t
# 服务参数查看
ros2 interface show turtlesim/srv/Spawn
# 服务调用
ros2 service call /spawn turtlesim/srv/Spawn "{x: 1, y: 1}"

ros2 serivce call 
ros2 service echo 
ros2 service info
ros2 service list
ros2 service type
```

```sh
ros2 param describe /turtlesim background_r
ros2 param get /turtlesim background_r
ros2 param set /turtlesim background_r 255
ros2 param get /turtlesim background_r 255
ros2 param dump /turtlesim > turtlesim_para.yaml
cat turtlesim_para.yaml
ros2 run turtlesim turtlesim_node --ros-args --params-file turtlesim_param.yaml
unset FASTRTPS_DEFAULT_PROFILES_FILE
ros2 param -h
rqt
```

```sh
ros2 pkg create learn_interface --dependencies  sensor_msgs rosidl_default_generators --license Apache-2.0 
colcon build
source ./install/setup.zsh
ros2 interface show learn_interface/srv/FaceDetector

```

```sh
autoload -Uz compinit
compinit
```


fix [XMLPARSER Error] realpath failed No such file or directory -> Function loadDefaultXMLFile
```sh
unset FASTRTPS_DEFAULT_PROFILES_FILE
```

VSC 快捷键
Alt + U 大写
Alt + L 小写

中英文切換 
Shift + Cmd 