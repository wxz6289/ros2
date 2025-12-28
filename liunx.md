## Linux
操作系统：管理计算机硬件和软件资源的系统软件，提供用户与计算机交互的界面。
内核：操作系统的核心部分，负责管理系统资源和硬件通信。驱动硬件的软件组件,负责管理系统的进程、内存、设备驱动程序、文件和网络系统，决定着系统的性能和稳定性。

CPU架构：计算机处理器的设计和组织方式，决定了指令集、寄存器数量和数据路径等特性。常见的CPU架构有x86/i386、ARM、AMD64、AARCH64、RISC/CISC、MIPS等。

[CPU指令集及架构](https://www.cnblogs.com/johnnyzen/p/13224632.html)

- 权限管理
su - 切换用户身份
sudo 以超级用户权限执行命令
chmod 修改文件权限
chown 修改文件所有者
chgrp 修改文件所属组

- 软件管理
apt-get (Debian/Ubuntu) 软件包管理工具
yum (CentOS/RHEL) 软件包管理工具
dpkg (Debian/Ubuntu) 低级软件包管理工具
rpm (CentOS/RHEL) 低级软件包管理工具
snap 通用软件包管理工具
flatpak 通用软件包管理工具
brew MacOS和Linux的软件包管理工具


- apt-get
apt-get update 更新软件包列表
apt-get upgrade 升级已安装的软件包
apt-get dist-upgrade 升级系统，处理依赖关系变化
apt-get install 安装软件包  -d 仅下载不安装 -f 强制安装
apt-get remove 卸载软件包
apt-get autoremove 自动删除不再需要的软件包
apt-get clean 清理本地软件包缓存
apt-get check 检查已安装的软件包依赖关系
apt-get show 显示软件包信息
apt-get search 搜索软件包
apt-cache showpkg 显示软件包详细信息
apt-cache depends 显示软件包依赖关系
apt-cache rdepends 显示反向依赖关系

- dpkg
dpkg -i 安装软件包
dpkg -r 卸载软件包
dpkg -P 完全卸载软件包，包括配置文件
dpkg -l 列出已安装的软件包
dpkg -s 显示软件包状态信息
dpkg -L 列出软件包安装的文件
dpkg -S 查找文件所属的软件包
dpkg -C 检查未完全安装的软件包
dpkg -unpack 解包软件包但不安装
dpkg -c 列出软件包内容
dpkg --configure 配置已解包但未配置的软件包

apt-get和dpkg的区别：
apt-get 是高级包管理工具，处理依赖关系，适合日常使用。
dpkg 是低级包管理工具，不处理依赖关系，适合手动安装和管理软件包。

默认所有软件包缓存路径：`/var/cache/apt/archives/`

源码安装软件包：

```bash
sudo apt-get install build-essential # 安装编译工具和库
make all
make install && make install-init && make install-commandmode &&make install-config
```

1. 下载源码包（通常是.tar.gz或.tar.bz2格式）
2. 解压源码包：`tar -xvf package.tar.gz`
3. 进入源码目录：`cd package`
4. 配置编译选项：`./configure` --prefix=/usr/local/package # 可选参数指定安装路径 --help 查看更多选项
5. 编译源码：`make`
6. 安装软件包：`sudo make install`

- 网络管理
ifconfig 查看和配置网络接口
ip 查看和配置网络接口
ping 测试网络连通性
netstat 查看网络连接和统计信息
ss 查看网络连接和统计信息
traceroute 跟踪数据包路径
nslookup 查询DNS记录
dig 查询DNS记录

## ROS

ROS是一个开源的机器人操作系统框架，提供了硬件抽象、设备驱动、库、可视化工具和消息传递等功能，简化了机器人软件开发过程。ROS支持多种编程语言，如C++和Python，广泛应用于机器人研究和开发领域。

解决了机器人各个组件之间的通信问题，使得开发者可以专注于算法和功能的实现，而不必担心底层的通信细节。

- 感知 ：通过传感器获取环境信息，如摄像头、激光雷达、深度相机、IMU、里程计、碰撞感知、建图等。
- 规划/决策 ：根据感知信息制定行动计划，如路径规划、定位、任务分配等。
- 控制 ：执行规划的动作，如运动控制、操作机械臂等。
- 模拟 ：使用仿真环境测试和验证机器人算法和功能。


### ROS版本
- ROS 1：最初版本，广泛使用，支持多种机器人平台和传感器。
- ROS 2：改进版本，增强了实时性、安全性和分布式计算能力，适用于更复杂的机器人应用。

ROS2 版本:

- Jazzy Jalisco (Release: 2024-05, EOL: 2029-05)
- Iron Irwini (Release: 2023-06, EOL: 2028-06)
- Humble Hawksbill (Release: 2022-05, EOL: 2027-05)
- Galactic Geochelone (Release: 2021-05, EOL: 2022-11)
- Foxy Fitzroy (Release: 2020-06, EOL: 2023-05)
- Dashing Diademata (Release: 2019-05, EOL: 2021-05)
- Crystal Clemmys (Release: 2018-12, EOL: 2019-12)
- Bouncy Bolson (Release: 2018-07, EOL: 2019-07)
- Ardent Apalone (Release: 2017-12, EOL: 2018-12)
