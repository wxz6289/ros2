import rclpy
from rclpy.node import Nodeb

def main():
  rclpy.init()
  node = Node("python_node")
  node.get_logger().info("hello, python")
  node.get_logger().warn("hello, python waraing")
  rclpy.spin(node)
  rclpy.shutdown()

if __name__ == "__main__":
  main()