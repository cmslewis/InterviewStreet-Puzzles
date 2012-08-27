#!/bin/python

import bisect
import math

INSERT_OP = 'a'
DELETE_OP = 'r'
ERROR_MSG = 'Wrong!'

def PerformOperation( sortedList, operation, value ):
  index = bisect.bisect_left( sortedList, value )
  
  if operation == INSERT_OP:
    # Insert the value into the list, maintaining sorted order.
    sortedList.insert( index , value )
  
  elif operation == DELETE_OP:
    # Only delete the value if it exists in the list.
    if value not in sortedList:
      return ERROR_MSG
    else:
      sortedList.pop(index)
  
  # If any values are left, return the median.
  nValues = len(sortedList)
  if nValues == 0:
    return ERROR_MSG
  elif (nValues % 2) == 0:
    median = float( sortedList[(nValues/2) - 1] + sortedList[nValues/2] ) / 2
    if median == math.ceil(median):
      median = int(median)
    return median
  else:
    return sortedList[nValues/2]


def main():
  N = int(raw_input())
  
  input_ops  = []
  input_vals = []
  
  # Read in all input lines.
  for i in range(0, N):
  	tmp = raw_input()
  	op, val = [xx for xx in tmp.split(' ')]
  	input_ops.append(op)
  	input_vals.append(int(val))
  
  # Print out the median after each operation.
  sortedList = []
  for i in range(N):
    op  = input_ops[i]
    val = input_vals[i]
    
    # Insert or remove the current value, as specified by the operation.
    print PerformOperation( sortedList, op, val )
  


if __name__ == "__main__":
  SolvePuzzle()
