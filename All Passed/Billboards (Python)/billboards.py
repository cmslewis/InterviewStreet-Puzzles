# File: billboards.py
# Author: Chris Lewis (cmslewis@gmail.com)
# -----------------------------------------------------------------------------
# This program offers a solution to the "Billboards" challenge on the 
# InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
# dashboard/#problem/4f2c2e3780aeb). Here is the problem description, verbatim:
# 
# ==
# ADZEN is a very popular advertising firm in your city. In every road you can 
# see their advertising billboards. Recently they are facing a serious 
# challenge, MG Road the most used and beautiful road in your city has been 
# almost filled by the billboards and this is having a negative effect on the 
# natural view.
# 
# On people's demand ADZEN has decided to remove some of the billboards in such 
# a way that there are no more than K billboards standing together in any part 
# of the road.
# 
# You may assume the MG Road to be a straight line with N billboards.Initially 
# there is no gap between any two adjecent billboards.
# 
# ADZEN's primary income comes from these billboards so the billboard removing 
# process has to be done in such a way that the billboards remaining at end 
# should give maximum possible profit among all possible final 
# configurations.Total profit of a configuration is the sum of the profit values 
# of all billboards present in that configuration.
# 
# Given N,K and the profit value of each of the N billboards, output the maximum 
# profit that can be obtained from the remaining billboards under the conditions 
# given.
#
# INPUT DESCRIPTION:
# Ist line contain two space seperated integers N and K. Then follow N lines 
# describing the profit value of each billboard i.e ith line contains the profit 
# value of ith billboard.
# 
# SAMPLE INPUT:
# 6 2
# 1
# 2
# 3
# 1
# 6
# 10 
# 
# SAMPLE OUTPUT:
# 21
# 
# EXPLANATION:
# 
# In given input there are 6 billboards and after the process no more than 2 
# should be together.
# So remove 1st and 4th billboards giving a configuration _ 2 3 _ 6 10 having a 
# profit of 21. No other configuration has a profit more than 21.So the answer 
# is 21.
# 
# CONSTRAINTS:
# 1 <= N <= 1,00,000(10^5)
# 1 <= K <= N
# 0 <= profit value of any billboard <= 2,000,000,000(2*10^9)
# 
# START = 0
# END   = 1
# SUM   = 2
# ==

def main():
  # Read in the number of billboards and the maximum cluster size.
  N, K = [int(n) for n in raw_input().split()]
  
  # Read in the values of each billboard (insert a dummy billboard with a value 
  # of 0 at the beginning).
  billboards = [0] * (N + 1)
  for i in range(1, N+1):
    billboards[i] = int(raw_input())
  
  D    = [[]] * (N+1)  # DP table
  D[0] = [ [0, K, 0] ] # Base case: A sum of 0.
  
  # Visit each billboard position from 1 to N, determining the optimal sum for 
  # each block of K billboards.
  for i in range(1, N+1):
    
    # Initialize the current column with a block from K to K,
    # with the sum equal to the previous sum.
    currStage = [ [K, K, D[i-1][-1][SUM]] ]
    
    for block in D[i-1]:
      if block[END] > 0:
        
        # Determine the optimal sum (i.e. should we use the current billboard or 
        # not?).
        maxProfit = max(billboards[i] + block[SUM], D[i-1][-1][SUM])
        
        newStart = max(0, block[START] - 1)
        newEnd   = max(0, block[END] - 1)
        
        # If the optimal sum hasn't improved, simply extend the last block's 
        # start position leftward by one.
        if maxProfit == currStage[-1][SUM]:
          currStage[-1][START] = newStart
        
        # Otherwise, insert a new block in the current column, shifted one 
        # position to the left. 
        else:
          currStage.append(
            [ 
              newStart,
              newEnd, 
              maxProfit
            ]
          )
    
    # Save the current column for future reference.
    D[i] = currStage
  
  print D[N][-1][SUM]


if __name__ == "__main__":
  main()
