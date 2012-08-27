# File: quadrant_queries.py
# Author: Chris Lewis (cmslewis@gmail.com)
# ------------------------------------------------------------------------------
# This is my second attempt, using a segment tree.

from math import pow
from math import ceil
from math import log

# The query string denoting that we should perform an x-axis reflection.
X_AXIS_REFLECTION = "X"

# The query string denoting that we should perform a y-axis reflection.
Y_AXIS_REFLECTION = "Y"

# Enumerated indices for accessing x- or y-coordinates in a 2-tuple.
X = 0
Y = 1

X_AXIS  = 0
Y_AXIS  = 1
XY_AXES = 2

QUADRANT_1 = 0
QUADRANT_2 = 1
QUADRANT_3 = 2
QUADRANT_4 = 3

numPoints = 0

class SegmentTree:
  
  def __init__(self, xCoords, yCoords):
    self.numPoints = len(xCoords)
    self.numNodes  = max(1, int(self.numPoints * log(self.numPoints, 2)))
    
    self.Q = [[0,0,0,0] for i in xrange(self.numNodes)]
    self.L = [[0,0]     for i in xrange(self.numNodes)]
    
    self._PopulateQuadrantCounts(0, 0, self.numPoints-1, xCoords, yCoords)
  
  
  """ Tested: OK """
  def _PopulateQuadrantCounts(self, node, b, e, xCoords, yCoords):
    
    # print "_PopulateQuadrantCounts(%d), b=%d, e=%d" % (node, b+1, e+1)
    
    #if node >= self.numNodes:
    #  return
    
    # print "_PopulateQuadrantCounts(%d)" % (node)
    # print "  b=%d, e=%d" % (b,e)
    
    if b == e:
      x = xCoords[b]
      y = yCoords[b]
      
      if x > 0:
        if y > 0:
          self.Q[node][QUADRANT_1] += 1
          # print "  Q1 (%d, %d)" % (x, y)
        else:
          self.Q[node][QUADRANT_4] += 1
          # print "  Q4 (%d, %d)" % (x, y)
      else:
        if y > 0:
          self.Q[node][QUADRANT_2] += 1
          # print "  Q2 (%d, %d)" % (x, y)
        else:
          self.Q[node][QUADRANT_3] += 1
          # print "  Q3 (%d, %d)" % (x, y)
    
    else:
      # Recurse to the left subinterval.
      self._PopulateQuadrantCounts(self._LeftChild(node),
                                   b, (b+e)/2,
                                   xCoords, yCoords)
      
      # Recurse to the right subinterval.
      self._PopulateQuadrantCounts(self._RightChild(node),
                                   (b+e)/2 + 1, e,
                                   xCoords, yCoords)
      
      # Update the quadrant counts at the current node.
      self._UpdateQuadrantCounts(node)
    
  
  
  """ Tested: OK """
  def __repr__(self):
    s = "\n%d Points, %d Interval Nodes\n" % (self.numPoints, self.numNodes)
    s += ("=" * 20) + "\n"
    
    s += "  QUADRANT COUNTS:\n"
    for node in range(self.numNodes):
      s += "  " + str(node) + ": " + str(self.Q[node]) + "\n"
      
    s += "  LAZY FLAGS\n"
    for node in range(self.numNodes):
      s += "  " + str(node) + ": " + str(self.L[node]) + "\n"
      
    s += ("=" * 20) + "\n\n"
    
    return s
  
  
  """ Tested: OK """
  def PerformQuery(self, i, j, command):
    
    if command in ['X', 'Y']:
      self._RecPerformQuery(0, 0, self.numPoints-1, i-1, j-1, command, None)
      # print self
    elif command == 'C':
      counts = [0, 0, 0, 0]
      
      self._RecPerformQuery(0, 0, self.numPoints-1, i-1, j-1, command, counts)
      
      # Print out a space-separated line of quadrant counts.
      print ' '.join(map(str, counts))
  
  
  """ Tested: OK """
  def _RecPerformQuery(self, node, b, e, i, j, op, counts):
    
    # Precalculate both child-node indices for efficiency.
    leftChild  = self._LeftChild(node)
    rightChild = self._RightChild(node)
    
    # If both X and Y flags are set for this node, save time by performing both 
    # reflections at once.
    if self._LazyFlagIsSet(node, X_AXIS) and self._LazyFlagIsSet(node, Y_AXIS):
      self._ReflectRange(node, XY_AXES)
      
      for axis in [X_AXIS, Y_AXIS]:
        self._ToggleLazyFlag(node, axis)
        self._ToggleLazyFlag(leftChild,  axis)
        self._ToggleLazyFlag(rightChild, axis)
    
    # Otherwise, handle each axis individually.
    elif self._LazyFlagIsSet(node, X_AXIS):
        self._ReflectRange(node, X_AXIS)
        
        # Turn off the flag at this node.
        self._ToggleLazyFlag(node, X_AXIS)
        
        # Toggle the lazy flags of child nodes.
        self._ToggleLazyFlag(leftChild,  X_AXIS)
        self._ToggleLazyFlag(rightChild, X_AXIS)
      
    elif self._LazyFlagIsSet(node, Y_AXIS):
        self._ReflectRange(node, Y_AXIS)
        
        # Turn off the flag at this node.
        self._ToggleLazyFlag(node, Y_AXIS)
        
        # Toggle the lazy flags of child nodes.
        self._ToggleLazyFlag(leftChild,  Y_AXIS)
        self._ToggleLazyFlag(rightChild, Y_AXIS)
    
    # Return immediately if the current interval is already out of range.
    if (i > e) or (j < b):
      return
    
    # If the current interval is completely and maximally within the target 
    # range, then reflect the appropriate quadrant counts at this node, and 
    # toggle the children's lazy flags for the appropriate axis.
    if b >= i and e <= j:
      if op == 'X':
        self._ReflectRange(node, X_AXIS)
        self._ToggleLazyFlag(leftChild,  X_AXIS)
        self._ToggleLazyFlag(rightChild, X_AXIS)
      elif op == 'Y':
        self._ReflectRange(node, Y_AXIS)
        self._ToggleLazyFlag(leftChild,  Y_AXIS)
        self._ToggleLazyFlag(rightChild, Y_AXIS)
      else: # Count
        counts[QUADRANT_1] += self.Q[node][QUADRANT_1]
        counts[QUADRANT_2] += self.Q[node][QUADRANT_2]
        counts[QUADRANT_3] += self.Q[node][QUADRANT_3]
        counts[QUADRANT_4] += self.Q[node][QUADRANT_4]
        
    else:
      # Recurse to the left subinterval.
      self._RecPerformQuery(leftChild,
                            b, (b+e)/2,
                            i, j,
                            op, counts)
      
      # Recurse to the right subinterval.
      self._RecPerformQuery(rightChild,
                            (b+e)/2 + 1, e,
                            i, j,
                            op, counts)
      
      # Update the quadrant counts at the current node.
      self._UpdateQuadrantCounts(node)
  
  
  """ Tested: OK """
  def _ReflectRange(self, node, axis):
    if axis == XY_AXES:
      self._SwapQuadrantCounts(node, QUADRANT_1, QUADRANT_3)
      self._SwapQuadrantCounts(node, QUADRANT_2, QUADRANT_4)
      
    elif axis == X_AXIS:
      self._SwapQuadrantCounts(node, QUADRANT_1, QUADRANT_4)
      self._SwapQuadrantCounts(node, QUADRANT_2, QUADRANT_3)
      
    elif axis == Y_AXIS:
      self._SwapQuadrantCounts(node, QUADRANT_1, QUADRANT_2)
      self._SwapQuadrantCounts(node, QUADRANT_3, QUADRANT_4)
  
  
  """ Tested: OK """
  def _SwapQuadrantCounts(self, node, quadA, quadB):
    if node >= self.numNodes:
      return
    
    tmp = self.Q[node][quadA]
    self.Q[node][quadA] = self.Q[node][quadB]
    self.Q[node][quadB] = tmp
  
  
  """ Tested: OK """
  def _UpdateQuadrantCounts(self, node):
    
    leftChild  = self._LeftChild(node)
    rightChild = self._RightChild(node)
    
    if leftChild >= self.numNodes or rightChild >= self.numNodes:
      return
    
    self.Q[node][QUADRANT_1] = self.Q[leftChild][QUADRANT_1] + \
                               self.Q[rightChild][QUADRANT_1]
    
    self.Q[node][QUADRANT_2] = self.Q[leftChild][QUADRANT_2] + \
                               self.Q[rightChild][QUADRANT_2]
    
    self.Q[node][QUADRANT_3] = self.Q[leftChild][QUADRANT_3] + \
                               self.Q[rightChild][QUADRANT_3]
    
    self.Q[node][QUADRANT_4] = self.Q[leftChild][QUADRANT_4] + \
                               self.Q[rightChild][QUADRANT_4]
  
  
  """ Tested: OK """
  def _LeftChild(self, node):
    return 2 * node + 1
  
  
  """ Tested: OK """
  def _RightChild(self, node):
    return 2 * node + 2
  
  
  """ Tested: OK """
  def _LazyFlagIsSet(self, node, axis):
    if node >= self.numNodes:
      return False
    
    return self.L[node][axis] != 0
  
  
  """ Tested: OK """
  def _ToggleLazyFlag(self, node, axis):
    if node >= self.numNodes:
      return
    
    self.L[node][axis] ^= 1
  


def main():
  # Read in the number of points to expect.
  numPoints = int(raw_input())
  
  # Initialize one list to store x-coordinates and one to store y-coordinates.
  xCoords = [0] * numPoints
  yCoords = [0] * numPoints
  
  # Read in each x- and y-coordinate from standard input.
  for i in range(numPoints):
    xCoords[i], yCoords[i] = [int(token) for token in raw_input().split()]
  
  tree = SegmentTree(xCoords, yCoords)
  # print tree
  
  # Read in the number of queries to expect.
  numQueries = int(raw_input())
  
  #f = open('output', 'w')
  
  # Read in each query. 
  for k in range(numQueries):
    queryType, i, j = raw_input().split()
    i = int(i)
    j = int(j)
    
    #if queryType == 'C':
    #  f.write(tree.PerformQuery(i, j, queryType) + "\n")
    #else:
    tree.PerformQuery(i, j, queryType)
  
  #f.close()


if __name__ == "__main__":
  main()
