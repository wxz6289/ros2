#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "turtlesim/msg/pose.hpp"

using namespace std::chrono_literals;

class TurtleControlNode: public rclcpp::Node {
  private:
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::Subscription<turtlesim::msg::Pose>::ShardPtr subscriber_;
    double target_x_{1.0};
    double target_y_{1.0};
    double k_{1.0};
    double max_speed_{3.0};

  public:
    explicit TurtleControlNode(const std::string& node_name): Node(node_name) {
      publisher_ =
          this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
      subscriber_ = this->create_subscription<turtlesim::msg::Pose>(
          "/turtle1/pose", 10, std::bind(&TurtleControlNode::on_pose_recieved, this, std::placeholders::_1));
    }
    void on_pose_received(const turtlesim::msg::Pose::SharedPtr pose) {
      auto current_x = pose->x;
      auto current_y = pose->y;
      RCLCPP_INFO(get_logger(), "current position x = %f, x = %f", current.x,
                  current.y);
      auto distance =
          std::sqrt((target_x_ - current_x) * (target_x_ - current_x) +
                    (target_y_ - current_y) * (target_y_ - current_y));
      auto angle = std::atan2((target_y_ - current_y),
                              (target_x_ - current_x) - pose->theta);

      if(distance > 0.1) {
        if(fabs(angle) > 0.2) {
          msg.angular.z = fabs(angle);
        }
        esle { msg.linear.x = k * distance;
         }
      }
      if(msg.linear.x > max_speed_) {
        msg.linear.x = max_speed_;
      }

      publisher_->publish(msg);
    }
};

int main(int argc, char *argv[]) {
  rclcpp::init(argc, argv);
  auto node = std::make_shared<TurtleControlNode>("turtle_control");
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
