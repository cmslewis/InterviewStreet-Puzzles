# File: vertical_sticks.py
# Author: Chris Lewis (cmslewis@gmail.com)
# ------------------------------------------------------------------------------
# This program offers a solution to the "Vertical Sticks" challenge on the 
# InterviewStreet website (URL: https://www.interviewstreet.com/challenges/
# dashboard/#problem/4eed18ded76fe). Here is the problem description, verbatim:
# 
# ==
# Given array of integers Y=y1,...,yn, we have n line segments such that 
# endpoints of segment i are (i, 0) and (i, yi). Imagine that from the top of 
# each segment a horizontal ray is shot to the left, and this ray stops when it 
# touches another segment or it hits the y-axis. We construct an array of n 
# integers, v1, ..., vn, where vi is equal to length of ray shot from the top of 
# segment i. We define V(y1, ..., yn) = v1 + ... + vn.
# 
# For example, if we have Y=[3,2,5,3,3,4,1,2], then v1, ..., v8 = 
# [1,1,3,1,1,3,1,2], as shown in the picture below:
# 
# For each permutation p of [1,...,n], we can calculate V(yp1, ..., ypn). If we 
# choose a uniformly random permutation p of [1,...,n], what is the expected 
# value of V(yp1, ..., ypn)?
# 
# INPUT FORMAT
# First line of input contains a single integer T (1 <= T <= 100). T test cases 
# follow.
# 
# First line of each test-case is a single integer N (1 <= N <= 50). Next line 
# contains positive integer numbers y1, ..., yN separated by a single space
# (0 < yi <= 1000).
# 
# OUTPUT FORMAT
# For each test-case output expected value of V(yp1, ..., ypn), rounded to two 
# digits after the decimal point.
# 
# SAMPLE INPUT
# 
# 6
# 3
# 1 2 3
# 3
# 3 3 3
# 3
# 2 2 3
# 4
# 10 2 4 4
# 5
# 10 10 10 5 10
# 6
# 1 2 3 4 5 6
# 
# SAMPLE OUTPUT
# 
# 4.33
# 3 .00
# 4.00
# 6.00
# 5.80
# 11.15
# 
# EXPLANATION
# Case 1: We have V(1,2,3) = 1+2+3 = 6, V(1,3,2) = 1+2+1 = 4, V(2,1,3) = 1+1+3 = 
# 5, V(2,3,1) = 1+2+1 = 4, V(3,1,2) = 1+1+2 = 4, V(3,2,1) = 1+1+1 = 3. Average 
# of these values is 4.33.
# Case 2: No matter what the permutation is, V(yp1, yp2, yp3) = 1+1+1 = 3, so 
# the answer is 3.00.
# Case 3: V(y1 ,y2 ,y3)=V(y2 ,y1 ,y3) = 5, V(y1, y3, y2)=V(y2, y3, y1) = 4, 
# V(y3, y1, y2)=V(y3, y2, y1) = 3, and average of these values is 4.00.
# ==

# Function: ExpectedRayLength(sticks)
# Usage: result = ExpectedRayLength([1, 5, 6, 2, 2])
# ------------------------------------------------------------------------------
# Returns the expected ray length for the provided list of sticks, according to 
# the problem description. The expected length is computed for each stick height 
# as (n + 1)/(k + 1), where n is the number of sticks and k is the number of 
# sticks with height greater than or equal to the height of the current stick. 
# Intuitively, this is akin to a ratio between the number of gaps between all 
# sticks and the number of gaps between sticks capable of stopping the ray from 
# the current stick in its tracks.
def ExpectedRayLength(sticks):
  
  # We will return this result as the expected ray length of the given list of 
  # sticks. 
  result = 0
  
  # Sort the sticks into decreasing order so that we can determine the height 
  # rank of each stick more easily.
  sticks.sort(reverse=True)
  
  # The height rank will at all times be equal to the number of sticks in the 
  # list with a height greater than or equal to the current stick. 
  heightRank = 1
  
  while heightRank <= len(sticks):
    # Determine the number of sticks with the same height (because the list has 
    # been sorted, they will all be in a contiguous streak).
    streakLength = 1
    
    # If we have multiple sticks with the same height, move to the end of the 
    # streak and count the streak length to help us determine the height rank  
    # that each element in the streak should have.
    while heightRank < len(sticks):
      height     = sticks[heightRank - 1]
      nextHeight = sticks[(heightRank - 1) + 1]
      
      if height != nextHeight: break
      
      streakLength += 1
      heightRank   += 1
    
    # Add streakLength instances of (n + 1)/(k + 1) to the result, where n is 
    # the number of sticks and k is the height rank of the final stick in the 
    # current streak.
    result += streakLength * float(len(sticks) + 1) / float(heightRank + 1)
    
    # Move to the next element in the sorted sticks list.
    heightRank += 1
  
  return result


def main():
  # Read in the number of test cases to expect.
  numCases = int(raw_input())
  
  # Report the expected ray length for each test case. 
  for i in range(numCases):
    unused = int(raw_input())
    sticks = [int(n) for n in raw_input().split()]
    
    print "%.2f" % ExpectedRayLength(sticks)


if __name__ == "__main__":
  main()
