
from collections import Counter

class Node:
  # Possible statuses 
  UNVISITED = 0
  CAN_REACH_TARGET = 1
  VISITED   = 2
  
  def __init__(self, id):
    self.status   = Node.UNVISITED
    self.outEdges = Counter()
    self.inEdges  = Counter()
    self.id       = id
    self.position = None
  
  def __repr__(self):
    return "Node %d" % (self.id)#, self.status)
  
  def addChildNode(self, neighbor):
    """ Tested: OK """
    self.outEdges[neighbor] += 1
    neighbor.inEdges[self]  += 1
  
  def numEdgesToChild(self, neighbor):
    return self.outEdges[neighbor]
  


# Function: LabelReachableNodes(sourceNode)
# Usage: LabelReachableNodes(node)
# ------------------------------------------------------------------------------
# Recursively explores the digraph backwards along each directional edge 
# starting at the specified destination node, and changes the status of all 
# encountered nodes to Node.CAN_REACH_TARGET.
def LabelReachableNodes(destNode):
  destNode.status = Node.CAN_REACH_TARGET
  
  for neighbor in destNode.inEdges.keys():
    if neighbor.status == Node.UNVISITED:
      LabelReachableNodes(neighbor)


# Function: TopologicalSort(sourceNode)
# Usage: sortedNodes = TopologicalSort(node)
# ------------------------------------------------------------------------------
# Returns a list of nodes sorted in order of their minimum distance from the 
# specified source node, with the source node as the first element in the list. 
def TopologicalSort(sourceNode):
  """ Tested: OK """
  # Mark the source node as visited in case we run into it again.
  sourceNode.status = Node.VISITED
  
  sortedNodes = []
  
  # If we construct our list by recursively appending the children of all 
  # outgoing neighbors, then we'll end up with a list of nodes sorted in order 
  # of increasing distance from the specified source node, which is exactly what 
  # we want.
  for neighbor in sourceNode.outEdges.keys():
    if neighbor.status == Node.CAN_REACH_TARGET:
      sortedNodes = TopologicalSort(neighbor) + sortedNodes
  
  # We've recursively appended all children of the current source node to the 
  # sorted list. We finish by adding the source node itself to the beginning.
  return [sourceNode] + sortedNodes



MOD_VALUE = int(10e9)

def CountDistinctPaths(sourceNode, destNode, nodes):
  # Mark the nodes that can reach the specified destination node using a DFS.
  LabelReachableNodes(destNode)
  #print "\nAFTER LABELING:"
  #for node in nodes:
  #  print node.id,
  #  if node.status == Node.UNVISITED: print "UNVISITED"
  #  elif node.status == Node.CAN_REACH_TARGET: print "CAN_REACH_TARGET"
  #  elif node.status == Node.VISITED: print "VISITED"

  # If there is no path from the source node to the destination node, go ahead 
  # and return a count of 0.
  if not sourceNode.status == Node.CAN_REACH_TARGET:
    return 0
  
  # Topologically sort the nodes starting from the source node.
  sortedNodes = TopologicalSort(sourceNode)
  #print "\nAFTER TOPOLOGICAL SORT:"
  #for node in sortedNodes:
  #  print node.id,
  #print
  
  startPos = 0
  for i in range(0, len(sortedNodes)):
    sortedNodes[i].position = i
  #print "\nAFTER INDEXING:"
  #for node in sortedNodes:
  #  print node.position,
  #print
  
  # 3. Starting from the position of node s in the topological sort, perform the 
  #    dynamic programming algorithm to compute d for each node.
  #print "\nCOUNTING PATHS:"
  PATHS = Counter()
  PATHS[sourceNode] = 1
  for i in range(len(sortedNodes)):
    currNode = sortedNodes[i]
    
    #print sourceNode, "=>", currNode, ":"
    
    # 4. If at any point a back edge is encountered, then there are an infinite 
    #    number of paths.
    for childNode in currNode.outEdges.keys():
      if childNode.status != Node.UNVISITED and childNode.position <= i:
        return "INFINITE PATHS"
    
    # Count the paths from the source node to node i, and save that number.
    paths = sourceNode.numEdgesToChild(currNode) # 0 if no edges shared
    
    #print "  (EDGES)", paths, ","
    
    for parentNode, numEdges in currNode.inEdges.items():
    #  print "   ", parentNode, numEdges
      paths += PATHS[parentNode] * numEdges
    
    #print "  (EDGES+PATHS)", paths
    
    PATHS[currNode] = paths % MOD_VALUE
    
    #print "  PATHS[" + str(currNode) + "] = " + str(PATHS[currNode])
    
  # 5. d(t) indicates the number of paths from s to t.
  return PATHS[destNode] % MOD_VALUE


def main():
  # Read in the number of nodes and the number of edges to expect.
  numNodes, numEdges = [int(n) for n in raw_input().split()]
  
  # Initialize each of the N nodes.
  nodes = [Node(i) for i in range(1, numNodes + 1)]
  
  # Read in and initialize each of the M edges.
  for i in range(numEdges):
    fromID, toID = [int(n) for n in raw_input().split()]
    nodes[fromID - 1].addChildNode(nodes[toID - 1])
  
  s = nodes[0]
  t = nodes[numNodes - 1]
  
  print CountDistinctPaths(s, t, nodes)

if __name__ == "__main__":
  main()
