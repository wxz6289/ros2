import rclpy
from rclpy.node import Node

class PersonNode(Node):
  def __init__(self, node_name: str,  name: str, age: int) -> None:
    super().__init__(node_name)
    self.name = name
    self.age =age

  def eat(self, food_name: str):
    self.get_logger().info(f"Name is {self.name}, age is {self.age} , and eating {food_name}")
    # print(f"Name is {self.name}, age is {self.age} , and eating {food_name}")

def main():
  node = PersonNode("person","King", 23)
  node.eat("apple")
  rclpy.spin(node)
  rclpy.shutdown()