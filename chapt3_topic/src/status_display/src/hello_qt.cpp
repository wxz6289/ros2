#include <QApplication>
#include <QLabel>
#include <QString>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    QString message = "Hello, Qt with C++17!";
    QLabel* label = new QLabel(message);
    label->setWindowTitle("Hello Qt");
    label->resize(300, 100);
    label->show();
    return app.exec();
}