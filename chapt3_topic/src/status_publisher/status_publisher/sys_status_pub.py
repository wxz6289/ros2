import rclpy
from rclpy.node import Node
from status_interfaces.msg import SystemStatus
import psutil
import platform

class SystemStatusPub(Node):
    def __init__(self, node_name='sys_status_pub'):
        super().__init__(node_name)
        self.publisher_ = self.create_publisher(SystemStatus, 'sys_status', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = SystemStatus()
        msg.cpu_percent = psutil.cpu_percent(interval=None)
        msg.memory_percent = psutil.virtual_memory().percent
        msg.memory_total = psutil.virtual_memory().total / 1024 / 1024  # in MB
        msg.memory_available = psutil.virtual_memory().available / 1024 / 1024  # in MB
        msg.stamp = self.get_clock().now().to_msg()
        msg.host_name = platform.node()
        msg.memory_total = psutil.virtual_memory().total / 1024 / 1024  # in MB
        msg.memory_available = psutil.virtual_memory().available / 1024 / 1024  # in MB
        msg.net_sent = psutil.net_io_counters().bytes_sent / 1024 / 1024  # in MB
        msg.net_recv = psutil.net_io_counters().bytes_recv / 1024 / 1024  # in MB
        self.publisher_.publish(msg)
        self.get_logger().info(f'Hostname: {msg.host_name}, Total Memory: {msg.memory_total}MB, Available Memory: {msg.memory_available}MB, Net Sent: {msg.net_sent}MB, Net Recv: {msg.net_recv}MB')

def main(args=None):
    rclpy.init(args=args)
    sys_status_pub = SystemStatusPub()
    rclpy.spin(sys_status_pub)
    sys_status_pub.destroy_node()
    rclpy.shutdown()