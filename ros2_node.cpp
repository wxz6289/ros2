#include "iostream"
int main(int argc, char** argv) {
  std::cout<<"参数数量:"<<argc<<std::endl;
  std::cout<<"程序名:"<<argv[0]<<std::endl;
  std::string argc1 = argv[1];
  if(argc1 == "--help") {
    std::cout<<"帮助信息"<<std::endl;
  }
  return 0;
}