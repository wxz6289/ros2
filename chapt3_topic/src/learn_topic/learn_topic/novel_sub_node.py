#!/home/ros/ros_pyenv/bin/python

import rclpy
from rclpy.node import Node
from queue import Queue
import threading
from example_interfaces.msg import String
import pyttsx3 as espeaking
import time

class NovelSubNode(Node):
  def __init__(self, node_name):
    super().__init__(node_name)
    self.get_logger().info(f"{node_name} start!")
    self.novels_queue = Queue()
    self.novel_subscriber = self.create_subscription(String, "novel", self.novel_callback)
    self.speech_thread = threading.Thread(target=self.speake_thread)
    self.speech_thread.start()

  def novel_callback(self, msg):
    self.novels_queue.put(msg.data)

  def speake_thread(self):
    speaker = espeaking.init()
    speaker.voice = 'zh'

    while rclpy.ok():
      if self.novels_queue.qsize() > 0 :
        text = self.novels_queue.get()
        self.get_logger().info(f"speak: {text}")
        speaker.say(text)
        speaker.runAndWait()
      else:
        time.sleep(1)

def main():
  rclpy.init()
  node = NovelSubNode('novel_sub')
  rclpy.spin(node)
  rclpy.shutdown()