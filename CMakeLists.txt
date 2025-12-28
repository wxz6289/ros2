cmake_minimum_required(VERSION 3.8)
project(ros2_app)

add_executable(ros2_cpp_node ros2_node2.cpp)

find_package(rclcpp REQUIRED)
message(STATUS ${rclcpp_INCLUDE_DIRS})
message(STATUS ${rclcpp_LIBRARIES})

# target_include_directories(ros2_cpp_node PUBLIC ${rclcpp_INCLUDE_DIRS})
# target_link_libraries(ros2_cpp_node ${rclcpp_LIBRARIES})
ament_target_dependencies(ros2_cpp_node rclcpp)

# install(TARGETS ros2_cpp_node DESTINATION lib/${PROJECT_NAME})

# ament_package()