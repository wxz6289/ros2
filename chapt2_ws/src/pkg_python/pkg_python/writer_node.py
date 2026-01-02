from pkg_python.person_node import PersonNode

class WriterNode(PersonNode):
  def __init__(self, node_name, name, age):
    super().__init__(node_name, name, age)

def main():
  node = WriterNode("writer", "Jhon", 36)
  node.eat("hamberg")