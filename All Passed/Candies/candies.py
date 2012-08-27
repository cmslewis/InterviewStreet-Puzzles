# File: candies.py
# Author: Chris Lewis (cmslewis@gmail.com)
# -----------------------------------------------------------------------------
# This program offers a solution to the "Candies" challenge on the 
# InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
# dashboard/#problem/4fe12e4cbb829). Here is the problem description, verbatim:
# 
# ==
# Alice is a kindergarden teacher. She wants to give some candies to the 
# children in her class.  All the children sit in a line and each  of them  has 
# a rating score according to his or her usual performance.  Alice wants to give 
# at least 1 candy for each child.Children get jealous of their immediate 
# neighbors, so if two children sit next to each other then the one with the 
# higher rating must get more candies. Alice wants to save money, so she wants 
# to minimize the total number of candies.
# 
# INPUT:
# The first line of the input is an integer N, the number of children in Alice's 
# class. Each of the following N lines contains an integer indicates the rating 
# of each child.
# 
# OUTPUT:
# Output a single line containing the minimum number of candies Alice must give.
# 
# SAMPLE INPUT:
# 3
# 1
# 2
# 2
#  
# SAMPLE OUTPUT:
# 4
#  
# EXPLANATION:
# The number of candies Alice must give are 1, 2 and 1.
#  
# CONSTRAINTS:
# N and the rating  of each child are no larger than 10^5.
# ==
# 
# This implementation is based on one suggested by user JPvdMerwe in a 
# StackOverflow discussion, although it has been extended to address some 
# elusive edge cases that his algorithm did not correctly handle. Even so, I am 
# endlessly thankful to him for helping me get on the right track! To read the 
# discussion yourself, head to http://stackoverflow.com/questions/11292913/ 
# candies-interviewstreet.

# The maximum possible rating for any child in the class.
MAX_RATING = 100000

# A pseudo-infinite value that lies beyond the range of possible ratings.
INFINITY = MAX_RATING + 1

# Function: GetRating(i, ratings)
# Usage: rating = GetRating(0, ratings)
# ------------------------------------------------------------------------------
# A wrapper function that handles out-of-bounds index lookups in a manner 
# appropriate to the problem specifications. If i is a valid index in the  
# provided ratings array -- that is, if 0 <= i < len(ratings) -- then this 
# function returns ratings[i]. Otherwise, if i < 0 or i >= len(ratings), this 
# function returns INFINITY.
def GetRating(i, ratings):
  if i < 0 or i > len(ratings) - 1:
    return INFINITY
  return ratings[i] 


def main():
  # Read in the number of child ratings to expect.
  numChildren = int(raw_input())
  
  # Read in each student's rating.
  ratings = [0] * numChildren
  for i in range(numChildren):
    ratings[i] = int(raw_input())
  
  # Find the positions of all children whose ratings are strictly less than 
  # those of both children surrounding him. Note that the code below treats 
  # an out-of-bounds index as a child of infinity-high rating; thus, the first 
  # and last children could also be in a valley between their true neighbor 
  # (if the neighbor's rating is higher) and the impossibly impressive ghost 
  # child that "sits" just beyond each of them.
  valleys = []
  for i in range(numChildren):
    if GetRating(i, ratings) <= GetRating(i - 1, ratings) \
      and GetRating(i, ratings) <= GetRating(i + 1, ratings):
      valleys.append(i)
  
  # Now that we've located each valley (i.e. each child sitting between two 
  # children who each have a better rating than he does), we can go ahead and 
  # allot the minimum number of candies to each of such child. Afterward, we 
  # will need to reward each consecutively higher-rated child to the left of the 
  # current valley an increasingly large sum of candies. We do the same 
  # for the right side.
  candies = [0] * numChildren
  for valley_i in valleys:
    # Give the student in this valley only 1 candy to have and to hold forever.
    candies[valley_i] = 1
    
    # For a nice visual, let's think of a string of consecutive children whose 
    # ratings strictly increase as a "mountain" extending out of the current 
    # valley. Again, our goal is to reward commensurately more candies to each 
    # successive child as we climb higher up a mountain. When we pass the peak 
    # of the mountain (i.e. when we reach a child whose rating is lower than the 
    # previous child on the mountain), we stop.
    # 
    # First, resize the mountain extending to the left from the current valley. 
    # Warning: Since we're iterating from left to right in the outer foor loop, 
    # it's possible that some of the children we'll encounter in a moment might 
    # already have had their candy counts increased by being in the rightward 
    # mountain of a previous valley. In that case, give that child the maximum 
    # of his current candy count and the new count we intend to give him.  
    mountain_i = valley_i - 1
    while mountain_i >= 0 and ratings[mountain_i] > ratings[mountain_i+1]:
      # Give this student one more candy than the student to his right ONLY IF 
      # we would not be reducing his current candy count in doing so.
      candies[mountain_i] = max(candies[mountain_i], candies[mountain_i+1] + 1)
      
      # Continue to the next student to the left.
      mountain_i -= 1
    
    
    # We now do the exact same process for the mountain that extends to the 
    # right of the current valley. However, none of the rightward elements will 
    # have been visited yet, so we can ignore the extra max() safeguard that we 
    # had to use for the leftward mountain.
    mountain_i = valley_i + 1
    while mountain_i <= numChildren - 1 \
      and ratings[mountain_i] > ratings[mountain_i-1]:
      # Give this student one more candy than the student to his left.
      candies[mountain_i] = candies[mountain_i-1] + 1
      
      # Continue to the next student to the right.
      mountain_i += 1
  
  # We've now determined the optimal distribution of candies for the provided 
  # set of children. At this point, we simply print out the sum of each child's 
  # candy count as the solution to the problem.
  print sum(candies)

if __name__ == "__main__":
  main()
