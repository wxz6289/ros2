
# colcon 快速参考手册（ROS 2）

## 概要

- `colcon` 是 ROS 2 推荐的工作区构建与管理工具，用于发现包、并行构建、运行测试并生成 `install/` 安装空间。
- 常见工作区目录：`src/`、`build/`、`install/`、`log/`。

## 常用子命令与示例

- 构建工作区：

```bash
colcon build
```

- 只构建指定包：

```bash
colcon build --packages-select my_pkg
```

- 构建包及其依赖：

```bash
colcon build --packages-up-to my_pkg
```

- 跳过某包：

```bash
colcon build --packages-skip problem_pkg
```

- 并行控制与性能：

```bash
colcon build --parallel-workers 4
```

- 开发用：符号链接安装（Python 包修改立即生效）：

```bash
colcon build --symlink-install
```

- 传递底层构建系统参数（CMake 示例）：

```bash
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release
```

- 列出发现的包：

```bash
colcon list
```

- 运行包的测试：

```bash
colcon test --packages-select my_pkg
```

- 查看测试结果：

```bash
colcon test-result --verbose
```

- 生成包依赖图（dot）：

```bash
colcon graph --dot | dot -Tpng -o deps.png
```

## 常用选项速查

- 包选择：`--packages-select`、`--packages-up-to`、`--packages-skip`
- 并行：`--parallel-workers N`
- 安装行为：`--merge-install`、`--symlink-install`
- 自定义目录：`--build-base`、`--install-base`、`--log-base`
- 传递给底层：`--cmake-args`、`--ament-cmake-args`、`--pytest-args`
- 输出/事件：`--event-handlers console_cohesion+`

## 典型工作流程

1. 在工作区根（包含 `src/`）运行：

```bash
colcon build
```

2. 构建完成后加载环境：

```bash
source install/setup.bash
```

3. 运行节点或 CLI：

```bash
ros2 run my_pkg my_node
```

仅构建并调试单包示例：

```bash
colcon build --packages-select my_pkg --symlink-install
source install/setup.bash
ros2 run my_pkg my_node
```

## 调试与常见问题

- 无法找到包/命令：确认执行了 `source install/setup.bash`。
- 构建失败：查看 `log/` 目录下的详细日志，或使用：

```bash
colcon build --event-handlers console_cohesion+
```

- launch 文件错误（如找不到 `generate_launch_description()`）：
	- `ros2 launch` 正确用法是 `ros2 launch <package> <launch_file>` 而不是直接给文件路径。
	- Launch 脚本应放在包的 `launch/` 目录下，并暴露 `generate_launch_description()` 函数。
	- 示例：

```bash
ros2 launch my_package my_launch.launch.py
```

- 权限问题：确保 launch 脚本可读、必要时可执行：

```bash
chmod +x src/my_package/launch/my_launch.launch.py
```

## 小提示

- 在持续开发时，常用 `--symlink-install` 配合 `--packages-select` 快速迭代小范围改动。
- 当工作区很大时，使用 `--parallel-workers` 控制负载或只构建改动包以节省时间。

## 参考命令速览

```bash
# 构建全部
colcon build

# 只构建 my_pkg
colcon build --packages-select my_pkg

# 并行 8 个 worker
colcon build --parallel-workers 8

# 列出包
colcon list

# 运行测试并查看结果
colcon test --packages-select my_pkg
colcon test-result --verbose
```

----

文件位置示例（工作区根）：`src/` 下放包，launch 放到包的 `launch/`。

如需把本文件转换为更长的教程或加入包级别示例（CMakeLists / setup.py 示例），告诉我我会继续扩展。
