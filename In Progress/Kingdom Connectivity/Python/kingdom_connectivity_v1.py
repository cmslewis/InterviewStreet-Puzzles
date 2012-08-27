# File: kingdom_connectivity.py
# Author: Chris Lewis (cmslewis@gmail.com)
# -----------------------------------------------------------------------------
# This program offers a solution to the "Kingdom Connectivity" challenge on the 
# InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
# dashboard/#problem/4f40dfda620c4). Here is the problem description, verbatim:
# 
# ==
# It has been a prosperous year for King Charles and he is rapidly expanding his 
# kingdom. A beautiful new kingdom has been recently constructed and in this 
# kingdom there are many cities connected by a number of one-way roads. Two 
# cities may be directly connected by more than one roads, this is to ensure 
# high connectivity.
# 
# In this new kingdom King Charles has made one of the cities at his financial 
# capital and one as warfare capital and he wants high connectivity between 
# these two capitals. The connectivity of a pair of cities say city A and city B 
# is defined as the number of different paths from city A to city B. A path may 
# use a road more than once if possible. Two paths are considered different if 
# they do not use exactly the same sequence of roads.
# 
# There are N cities numbered 1 to N in the new kingdom and M one-way roads. 
# City 1 is the monetary capital and city N is the warfare capital.
# 
# You being one of the best programmers in new kingdom need to answer the 
# connectivity of financial capital and warfare capital ,i.e number of different 
# paths from city 1 to city N.
# 
# INPUT DESCRIPTION
# First line contains two integers N and M.
# 
# Then follow M lines ,each having two integers say x and y, 1<=x,y<=N , 
# indicating there is a road from city x to city y.
# 
# OUTPUT DESCRIPTION
# Print the number of different paths from city 1 to city N modulo 
# 1,000,000,000 (10^9).If there are infinitely many different paths print 
# "INFINITE PATHS"(quotes are for clarity).
# 
# SAMPLE INPUT
# 5 5
# 1 2
# 2 4
# 2 3
# 3 4
# 4 5
# 
# SAMPLE OUTPUT
# 2
# 
# SAMPLE INPUT
# 5 5
# 1 2
# 4 2
# 2 3
# 3 4
# 4 5
# 
# SAMPLE OUTPUT
# INFINITE PATHS
# 
# CONSTRAINTS
# 2 <= N <= 10,000 (10^4)
# 1 <= M <= 100,000 (10^5) 
# 
# Two cities may be connected by more than two roads and in that case those 
# roads are to be considered different for counting distinct paths
# ==
#
# This implementation is based on information from a blog post written by Arron 
# Norwell entitled "Counting s-t Paths in a (Possibly Cyclic) Directed Graph" 
# (http://anorwell.com/indexbs.php?id=51).

from collections import Counter

# The value by which we should modulo once we've counted the paths.
MOD_VALUE = int(10e9)
INFINITE_PATHS_ERROR = "INFINITE PATHS"

class Node:
  
  def __init__(self, id):
    self.id          = id
    self.visited     = False
    self.reachable   = False
    self.outEdges    = Counter()
    self.inEdges     = Counter()
    self.sortedIndex = None
  
  def addChildNode(self, neighbor):
    """ Tested: OK """
    self.outEdges[neighbor] += 1
    neighbor.inEdges[self]  += 1
  
  def numEdgesToChild(self, neighbor):
    return self.outEdges[neighbor]
  


# Function: LabelReachableNodes(sourceNode)
# Usage: LabelReachableNodes(node)
# ------------------------------------------------------------------------------
# Recursively explores the digraph along each directional edge starting at the 
# specified source node, and changes the status of all encountered nodes to 
# Node.REACHABLE. Thus, any node not labeled Node.REACHABLE after this function 
# is run, is not reachable from the source node.
def LabelReachableNodes(sourceNode):
  sourceNode.visited   = True
  sourceNode.reachable = True
  
  for neighbor in sourceNode.outEdges.keys():
    if not neighbor.visited:
      LabelReachableNodes(neighbor)
      
  sourceNode.visited = False


# Function: TopologicalSort(sourceNode)
# Usage: sortedNodes = TopologicalSort(node)
# ------------------------------------------------------------------------------
# Returns a list of nodes sorted in order of their minimum distance from the 
# specified source node, with the source node as the first element in the list. 
def TopologicalSort(sourceNode):
  """ Tested: OK """
  # Mark the source node as visited in case we run into it again.
  sourceNode.visited = True
  
  sortedNodes = []
  
  # If we construct our list by recursively appending the children of all 
  # outgoing neighbors, then we'll end up with a list of nodes sorted in order 
  # of increasing distance from the specified source node, which is exactly what 
  # we want.
  for neighbor in sourceNode.outEdges.keys():
    if neighbor.reachable and not neighbor.visited:
      sortedNodes = TopologicalSort(neighbor) + sortedNodes
  
  # We've recursively appended all children of the current source node to the 
  # sorted list. We finish by adding the source node itself to the beginning.
  return [sourceNode] + sortedNodes


# Function: CountDistinctPaths(sourceNode, destNode)
# Usage: numPaths = CountDistinctPaths(nodes[0], nodes[-1])
# ------------------------------------------------------------------------------
# Returns the number of distinct paths from the specified source node to the 
# specified destination node.
def CountDistinctPaths(sourceNode, destNode):
  # Mark the nodes that can reach the specified destination node using a DFS.
  LabelReachableNodes(sourceNode)
  
  # If there is no path from the source node to the destination node, go ahead 
  # and return a count of 0.
  if not destNode.reachable:
    return 0
  
  # Topologically sort the nodes starting from the source node.
  sortedNodes = TopologicalSort(sourceNode)
  
  # Track of each node's index in the topological ordering to help us check for 
  # cycles. 
  for i in range(0, len(sortedNodes)):
    sortedNodes[i].sortedIndex = i
  
  # Starting from the source node, compute the number of paths to each node in 
  # the topological ordering.
  PATHS = Counter()
  PATHS[sourceNode] = 1
  for i in range(len(sortedNodes)):
    currNode = sortedNodes[i]
    
    # If we ever reach a node that appeared earlier in the topological ordering, 
    # then we've hit a cycle, and there are infinitely many paths.
    for childNode in currNode.outEdges.keys():
      if childNode.visited and childNode.sortedIndex <= i:
        return -1
    
    # Count the edges from the source node to the current node
    paths = sourceNode.numEdgesToChild(currNode)
    
    # Each parent node will have a certain number of incoming paths. We can 
    # multiply this count by the number of edges from a given parent node to the 
    # current node to determine the number of distinct paths we could produce 
    # from those combinations.
    for parentNode, numEdges in currNode.inEdges.items():
      paths += PATHS[parentNode] * numEdges
    
    # Save the number of paths from the source node to this node.
    PATHS[currNode] = paths
    
  # Return the number of paths to the destination node.
  return PATHS[destNode]


def main():
  # Read in the number of nodes and the number of edges to expect.
  numNodes, numEdges = [int(n) for n in raw_input().split()]
  
  # Initialize each of the N nodes.
  nodes = [Node(i) for i in range(1, numNodes + 1)]
  
  # Read in and initialize each of the M edges.
  for i in range(numEdges):
    fromID, toID = [int(n) for n in raw_input().split()]
    nodes[fromID - 1].addChildNode(nodes[toID - 1])
  
  # Print the number of paths, or an error message if cycles were found.
  result = CountDistinctPaths(nodes[0], nodes[-1])
  if result < 0:
    print INFINITE_PATHS_ERROR
  else:
    print result % MOD_VALUE


if __name__ == "__main__":
  main()
