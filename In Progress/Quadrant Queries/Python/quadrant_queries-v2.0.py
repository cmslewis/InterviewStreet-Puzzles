# File: quadrant_queries.py
# Author: Chris Lewis (cmslewis@gmail.com)
# ------------------------------------------------------------------------------
# This is my second attempt, using a Kempe tree. For more information, see: 
# http://bababadalgharaghtakamminarronnkonnbro.blogspot.com/2012/06/ 
# kempe-tree-data-structure-for.html.

from math import pow
from math import ceil
from math import log

# The query string denoting that we should perform an x-axis reflection.
X_AXIS_REFLECTION = "X"

# The query string denoting that we should perform a y-axis reflection.
Y_AXIS_REFLECTION = "Y"

# Enumerated indices for accessing x- or y-coordinates in a 2-tuple.
X = X_AXIS = 0
Y = Y_AXIS = 1

QUADRANT_1 = 0
QUADRANT_2 = 1
QUADRANT_3 = 2
QUADRANT_4 = 3

numPoints = 0

class SegmentTree:
  
  def __init__(self, numPoints):
    self.N = numPoints
    
    # Construction of Q
    # 0: Points 1,2,3,4
    # 1: Points 1,2
    # 2: Points 3,4
    # 3: Point 1
    # 4: Point 2
    # 5: Point 3
    # 6: Point 4
    self.Q = [
      [1, 1, 1, 1], # 0. Root Node
      [1, 1, 0, 0], # 1. Left Child of Root Node
      [0, 0, 1, 1], # 2. Right Child of Root Node
      [1, 0, 0, 0], # 3. Left  Child of Node 1
      [0, 1, 0, 0], # 4. Right Child of Node 1
      [0, 0, 1, 0], # 5. Left  Child of Node 2
      [0, 0, 0, 1]  # 6. Right Child of Node 2
    ]
    
    self.L = [
      [0, 0],
      [0, 0],
      [0, 0],
      [0, 0],
      [0, 0],
      [0, 0],
      [0, 0]
    ]
  
  
  def __repr__(self):
    s = "\n%d Elements, %d Interval Nodes\n============================\n" \
        % (self.N, len(self.Q))
    for node in range(len(self.Q)):
      s += str(node) + ":" + str(self.Q[node]) + "\n"
    
    s += "\nLazy Bits\n=========\n"
    for node in range(len(self.L)):
      s += str(node) + ":" + str(self.L[node]) + "\n"
    
    s += "\n"
    
    return s
  
  
  def Test(self):
    #for node in range(len(self.Q)):
    #  if node % 2 == 0: self._SetLazyFlag(node, X_AXIS)
    #  else: self._SetLazyFlag(node, Y_AXIS)
    
    # self._SetLazyFlag(0, X_AXIS)
    #     l = self._LeftChildIndex(0)
    #     self._PropagateLazyFlags(0, l)
    #     self._PropagateLazyFlags(l, self._LeftChildIndex(l))
    #     
    print "LAZY FLAGS"
    for node in range(len(self.Q)):
      print node, ":", self._LazyFlagIsSet(node, X_AXIS), self._LazyFlagIsSet(node, Y_AXIS)
  
  
  def PerformQuery(self, i, j, queryType):
    ans = [0, 0, 0, 0]
    self._RecPerformQuery(0, 0, self.N - 1, i, j, queryType, ans)
    print self
    if queryType == 'C':
      for i in range(len(ans)):
        print ans[i],
      print
  
  def _RecPerformQuery(self, node, rangeBegin, rangeEnd, i, j, operation, ans):
    
    print "\n",rangeBegin+1, "-->", rangeEnd+1,\
           "(Goal:", i+1, "-->", j+1,")"
    
    if self._LazyFlagIsSet(node, X_AXIS) or self._LazyFlagIsSet(node, Y_AXIS):
      print "  CASE 1. Lazy flag is set"
      # Propagate lazy flags down to this node's children.
      if rangeBegin != rangeEnd:
        self._PropagateLazyFlags(node, self._LeftChildIndex(node))
        self._PropagateLazyFlags(node, self._RightChildIndex(node))
      
      # Reflect points in this range if the lazy flags indicate we should.
      if self._LazyFlagIsSet(node, X_AXIS): self._ReflectRange(node, X_AXIS)
      if self._LazyFlagIsSet(node, Y_AXIS): self._ReflectRange(node, Y_AXIS)
      
      # Reset the lazy flags of this range when we're done.
      self._ResetLazyFlags(node)
    
    # Return if our range bounds overlap.
    if rangeEnd < i or j < rangeBegin:
      print "  ^^===BASE CASE: INTERVAL NOT IN RANGE===^^"
      return
    
    if i <= rangeBegin and j >= rangeEnd:
      print "  vv===SUCCESS: INTERVAL FULLY IN RANGE===vv"
      if operation == 'C':
        ans[0] += self.Q[node][QUADRANT_1]
        ans[1] += self.Q[node][QUADRANT_2]
        ans[2] += self.Q[node][QUADRANT_3]
        ans[3] += self.Q[node][QUADRANT_4]
      
      elif operation == 'X':
        print "  X OPERATION!"
        self._SetLazyFlag( node,  X_AXIS )
      
      elif operation == 'Y':
        print "Y OPERATION!"
        self._SetLazyFlag( node,  Y_AXIS )
      
      return
    
    print "  RECURSING TO CHILDREN"
    # Recursively continue to each child of the current node.
    self._RecPerformQuery(self._LeftChildIndex(node),
                          rangeBegin, (rangeBegin+rangeEnd)/2,
                          i, j, operation, ans)
    self._RecPerformQuery(self._RightChildIndex(node),
                          (rangeBegin+rangeEnd)/2 + 1, rangeEnd,
                          i, j, operation, ans)
    
    # Set the quadrant counts on this interval to the sum of the number of 
    # points per quadrant in each child interval.
    print "POST-BACKTRACKING: GATHER COUNTS OF CHILDREN"
    """ This part tested: OK """
    self.Q[node][QUADRANT_1] = self.Q[self._LeftChildIndex(node) ][QUADRANT_1]+\
                               self.Q[self._RightChildIndex(node)][QUADRANT_1]
    
    self.Q[node][QUADRANT_2] = self.Q[self._LeftChildIndex(node) ][QUADRANT_2]+\
                               self.Q[self._RightChildIndex(node)][QUADRANT_2]
    
    self.Q[node][QUADRANT_3] = self.Q[self._LeftChildIndex(node) ][QUADRANT_3]+\
                               self.Q[self._RightChildIndex(node)][QUADRANT_3]
    
    self.Q[node][QUADRANT_4] = self.Q[self._LeftChildIndex(node) ][QUADRANT_4]+\
                               self.Q[self._RightChildIndex(node)][QUADRANT_4]
  
  
  def _ReflectRange(self, node, axis):
    if axis == X_AXIS:
      self._SwapQuadrantCounts(node, QUADRANT_1, QUADRANT_4)
      self._SwapQuadrantCounts(node, QUADRANT_2, QUADRANT_3)
      
    elif axis == Y_AXIS:
      self._SwapQuadrantCounts(node, QUADRANT_1, QUADRANT_2)
      self._SwapQuadrantCounts(node, QUADRANT_3, QUADRANT_4)
  
  
  def _SwapQuadrantCounts(self, node, quadA, quadB):
    tmp = self.Q[node][quadA]
    self.Q[node][quadA] = self.Q[node][quadB]
    self.Q[node][quadB] = tmp
  
  
  """ Tested: OK """
  def _LazyFlagIsSet(self, node, axis):
    return self.L[node][axis] != 0
  
  
  """ Tested: OK """
  def _LeftChildIndex(self, node):
    return 2 * node + 1
  
  
  """ Tested: OK """
  def _RightChildIndex(self, node):
    return 2 * node + 2
  
  
  """ Tested: OK """
  def _SetLazyFlag(self, node, axis):
    self.L[node][axis] |= 1
  
  """ Tested: OK """
  def _PropagateLazyFlags(self, parentNode, childNode):
    # Propagate the lazy flag to the left child.
    self.L[childNode][X_AXIS] ^= self.L[parentNode][X_AXIS]
    self.L[childNode][Y_AXIS] ^= self.L[parentNode][Y_AXIS]
    
    # Constrain the flag value to [0,1].
    self.L[childNode][X_AXIS] &= 1
    self.L[childNode][Y_AXIS] &= 1
  
  
  """ Tested: OK """
  def _ResetLazyFlags(self, node):
    self.L[node][X_AXIS] = 0
    self.L[node][Y_AXIS] = 0
  

def main():
  # Read in the number of points to expect.
  numPoints = 4# int(raw_input())
  
  # Initialize one list to store x-coordinates and one to store y-coordinates.
  xCoords = [1, -1, -1,  1]# [0] * numPoints
  yCoords = [1,  1, -1, -1]# [0] * numPoints
  
  # Read in each x- and y-coordinate from standard input.
  #for i in range(numPoints):
  #  xCoords[i], yCoords[i] = [int(token) for token in raw_input().split()]
  
  tree = SegmentTree(numPoints)
  
  # Read in the number of queries to expect.
  numQueries = int(raw_input())
  
  # Read in each query. 
  for k in range(numQueries):
    queryType, i, j = raw_input().split()
    
    # The provided indices will be 1-indexed, so we subtract 1 to get their 
    # 0-indexed equivalents.
    i = int(i) - 1
    j = int(j) - 1
     
    tree.PerformQuery(i, j, queryType)
  

if __name__ == "__main__":
  main()