# File: centre_of_mass.py
# Author: Chris Lewis (cmslewis@gmail.com)
# ------------------------------------------------------------------------------
# This program offers a solution to the "Centre of Mass" practice problem on the 
# InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
# dashboard/#problem/4fa4e6c9b4464). Here is the problem description, verbatim:
# 
# ==
# Your new weapon consist of K blocks each having a certain weight. However the 
# blocks are randomly arranged in a straight line so you are not happy with the 
# CentreOfMass of the weapon. 
# 
# CentreOfMass of the weapon is defined as (W1 * 1 + W2 * 2 + W3  * 3 + … +
# WK * K)/K, where Wi is the weight of ith block. The blocks are magical so they 
# require magical spells to redistribute them. A magical spell helps you to swap 
# the position of two blocks.
# 
# Oh! you have forgotten some of the magical spells and thus your power is 
# limited to swapping blocks at certain indices only.
# 
# You want to achieve the maximum value of CentreOfMass of your weapon by using 
# the spells as many times you like.
# 
# INPUT FORMAT
# First line of the Input contains K, the number of blocks.
# Next line contains K space separated integers, where ith integer is the weight 
# of the ith block. All weights are distinct and has value between 1 and K ( 
# inclusive ). 1 <= K <= 100.
# Then follow K strings each of length K. If jth character of ith row is Y, it 
# means you remember the spell to swap the blocks at ith and jth position.
# 
# OUTPUT FORMAT
# Print in a single line K space separated integers, describing the final 
# configuration of blocks that give the maximum value of CentreOfMass of the 
# weapon.
# 
# SAMPLE INPUT
# 3
# 3 1 2
# NNY
# NNN
# YNN
# 
# SAMPLE OUTPUT:
# 2 1 3
# 
# EXPLANATION:
# According to the swapping matrix, you are only allowed to swap at the 1st and 
# 3rd indices. You can exchange the first block with the last block to get the 
# arrangement 2 1 3 from 3 1 2. Earlier the CentreOfMass was (3*1+1*2+2*3)/3 = 
# 11/3 and the new one is (2*1+1*2+3*3)/3 = 13/3.
# ==
#  
# This implementation is based on a solution sketch from 
# https://docs.google.com/document/d/ 
# 1YVIqTCCuM7euDxCjzmqBFC07D2qmM8fBLizKUXOZvCg/edit?pli=1.

# Function: CompressSwapChains(permissionsGrid)
# Usage: CompressSwapChains(grid)
# ------------------------------------------------------------------------------
# Compresses chains of possible swaps in the provided permissions grid. For 
# example, if we know we can swap indices 1 and 2 as well as indices 2 and 3, 
# then set the permission flag allowing us to swap indices 1 and 3 directly.
def CompressSwapChains(permissionsGrid):
  for k in range(numBlocks):
    for i in range(numBlocks):
      for j in range(numBlocks):
        if permissionsGrid[i][k] == 1 and permissionsGrid[k][j] == 1:
          permissionsGrid[i][j] = 1


# Function: SortWithPermissions(array, permissionsGrid)
# Usage: SortWithPermissions([4, 5, 1, 3, 6, 2], grid)
# ------------------------------------------------------------------------------
# Performs a modified bubble sort to sort the elements in increasing order, 
# allowing swaps only if we have permission. The goal of this operation is to 
# move higher-valued elements as far rightward as possible, within the confines 
# of our given permissions.
def SortWithPermissions(array, permissionsGrid):
  for i in range(numBlocks):
    for j in range(i + 1, numBlocks):
      if blocks[i] > blocks[j] and permissionsGrid[i][j] == 1:
        tmp = blocks[i]
        blocks[i] = blocks[j]
        blocks[j] = tmp


# Function: PrintArray(array)
# Usage: PrintArray([4, 5, 1, 3, 6, 2])
# ------------------------------------------------------------------------------
# Prints all elements of the specified array in order, separated by spaces on 
# one line.
def PrintArray(array):
  for i in range(numBlocks):
    print blocks[i],      
  print


def main():
  # Read in the number of blocks to expect.
  numBlocks = int(raw_input())
  
  # Read in the weights for each block into a list.
  blocks = [int(b) for b in raw_input().split()]
  
  # Read in the swap permissions for each pair of indices.
  permissionsGrid = [[0] * numBlocks for x in xrange(numBlocks)]
  for i in range(numBlocks):
    ithPermissions = list(raw_input())
    for j in range(len(ithPermissions)):
      if ithPermissions[j] == 'Y':
        permissionsGrid[i][j] = 1
  
  # Compress chains of possible swaps for efficiency.
  CompressSwapChains(permissionsGrid)
  
  # Sort the values in increasing order as best we can. 
  SortWithPermissions(blocks, permissionsGrid)
  
  # Report the final block ordering.
  PrintArray(blocks)


if __name__ == "__main__":
  main()
