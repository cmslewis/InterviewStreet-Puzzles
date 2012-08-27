
class Node()
{
public:
  explicit Node(int id) : id(id), paths(0), status(Node::Status.UNVISITED)
  {
    // Intentionally left empty.
  }
  
  void addChild(const Node& childNode);
  {
    this.children[&childNode] += 1;
    childNode.parents[&this]  += 1;
  }
  
  void findReachingNodes()
  {
    this.status = Node::Status.CAN_REACH_TARGET;
    
    for (map<int, vector<>::iterator itr = this.parents.begin();
         itr != this.parents.end(); ++itr)
    {
      Node node = *(itr->first);
      if (node.status == Node::Status.UNVISITED)
      {
        node.findReachingNodes();
      }
    }
  }
  
  /* ... */
  
  static enum Status
  {
    UNVISITED,
    CAN_REACH_TARGET,
    VISITED
  };
  
  int id;
  int paths;
  Status status;
  map<Node *, int> children;
  map<Node *, int> parents;
}

int main()
{
  int numNodes, numEdges;
  
  /* Read in the number of nodes and the number of edges to expect. */
  cin >> numNodes >> numEdges;
  
  
  
  return 0;
}