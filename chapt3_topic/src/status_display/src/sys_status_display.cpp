#include <QApplication>
#include <QLabel>
#include <QString>
#include <rclcpp/rclcpp.hpp>
#include <status_interfaces/msg/system_status.hpp>
#include <sstream>
#include <thread>
#include <QMetaObject>
#include <QObject>
#include <QtGlobal>
#include <QMetaType>

using SystemStatus = status_interfaces::msg::SystemStatus;

class SysStatusDisplay : public rclcpp::Node {
public:
    SysStatusDisplay(): Node("sys_status_display"), label_(nullptr) {
        subscriber_ = this->create_subscription<SystemStatus>(
            "/sys_status", 10, [this](const SystemStatus::SharedPtr msg) -> void {
                QString status = get_qstr_from_msg(msg);
                if (label_) {
                    QMetaObject::invokeMethod(label_, "setText", Qt::QueuedConnection, Q_ARG(QString, status));
                }
            });
    }

    void init_gui() {
        if (!label_) {
            label_ = new QLabel();
            label_->setText(get_qstr_from_msg(std::make_shared<SystemStatus>()));
            label_->show();
        }
    }

    QString get_qstr_from_msg(const SystemStatus::SharedPtr msg) {
        std::stringstream show_str;
        show_str << "Host Name: " << msg->host_name << "\n"
                         << "CPU Usage: " << msg->cpu_percent << "%\n"
                         << "Memory Usage: " << msg->memory_percent << "%\n"
                         << "Total Memory: " << msg->memory_total << " MB\n"
                         << "Available Memory: " << msg->memory_available << " MB\n"
                         << "Network Sent: " << msg->net_sent << " MB\n"
                         << "Network Received: " << msg->net_recv << " MB\n";
        return QString::fromStdString(show_str.str());
    }

private:
    QLabel* label_;
    rclcpp::Subscription<SystemStatus>::SharedPtr subscriber_;
};

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    rclcpp::init(argc, argv);
    auto node = std::make_shared<SysStatusDisplay>();
    node->init_gui();

    std::thread spin_thread([node]() { rclcpp::spin(node); });

    int ret = app.exec();

    rclcpp::shutdown();
    if (spin_thread.joinable()) {
        spin_thread.join();
    }
    return ret;
}