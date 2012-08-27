# File: meeting_point.py
# Author: Chris Lewis (cmslewis@gmail.com)
# ------------------------------------------------------------------------------
# This is my first attempt, using the naive O(n) approach.

# The query string denoting that we should perform an x-axis reflection.
X_AXIS_REFLECTION = "X"

# The query string denoting that we should perform a y-axis reflection.
Y_AXIS_REFLECTION = "Y"

def main():
  # Read in the number of points to expect.
  numPoints = int(raw_input())
  
  # Initialize one list to store x-coordinates and one to store y-coordinates.
  xCoords = [0] * numPoints
  yCoords = [0] * numPoints
  
  # Read in each x- and y-coordinate from standard input.
  for i in range(numPoints):
    xCoords[i], yCoords[i] = [int(token) for token in raw_input().split()]
  
  # Read in the number of queries to expect.
  numQueries = int(raw_input())
  
  # Read in and perform each query. 
  for i in range(numQueries):
    queryType, i, j = raw_input().split()
    
    # The provided indices will be 1-indexed, so we subtract 1 to get their 
    # 0-indexed equivalents.
    i = int(i) - 1
    j = int(j) - 1
    
    if queryType == X_AXIS_REFLECTION:
      # Reflect points i through j (inclusive) across the X axis by flipping the 
      # y-coordinate.
      for k in range(i, j + 1):
        yCoords[k] *= -1
      
    elif queryType == Y_AXIS_REFLECTION:
      # Reflect points i through j (inclusive) across the Y axis by flipping the 
      # x-coordinate.
      for k in range(i, j + 1):
        xCoords[k] *= -1
      
    else:
      # Report the number of points lying in each quadrant.
      quadrant1Count = 0
      quadrant2Count = 0
      quadrant3Count = 0
      quadrant4Count = 0
      
      for k in range(i, j + 1):
        x = xCoords[k]
        y = yCoords[k]
        
        if   x > 0 and y > 0: quadrant1Count += 1
        elif x < 0 and y > 0: quadrant2Count += 1
        elif x < 0 and y < 0: quadrant3Count += 1
        elif x > 0 and y < 0: quadrant4Count += 1
      
      print quadrant1Count, quadrant2Count, quadrant3Count, quadrant4Count 
    

if __name__ == "__main__":
  main()