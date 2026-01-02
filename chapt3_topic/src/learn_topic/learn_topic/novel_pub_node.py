import rclpy
from rclpy.node import Node
from queue import Queue
import requests
from example_interfaces.msg import String

class NovelPubNode(Node):
  def __init__(self, node_name):
    super().__init__(node_name)
    self.get_logger().info(f"{node_name} start!")
    self.novels_queue = Queue()
    self.novel_publisher = self.create_publisher(String, "novel", 10)
    self.create_timer(5, self.timer_callback)

  def timer_callback(self):
    if self.novels_queue.qsize() > 0 :
      line = self.novels_queue.get()
      msg = String()
      msg.data = line
      self.novel_publisher.publish(msg)
      self.get_logger().info(f"publish: {msg}")


  def download(self, url):
    response = requests.get(url)
    response.encoding = "utf-8"
    text = response.text
    self.get_logger().info(f"download {url}, {len(text)}")
    for line in text.splitlines():
      self.novels_queue.put(line)


def main():
  rclpy.init()
  node = NovelPubNode('novel_pub')
  node.download("http://0.0.0.0:8000/novel1.txt")
  rclpy.spin(node)
  rclpy.shutdown()