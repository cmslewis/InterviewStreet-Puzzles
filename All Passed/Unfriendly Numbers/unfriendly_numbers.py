# File: unfriendly_numbers.py
# Author: Chris Lewis (cmslewis@gmail.com)
# -----------------------------------------------------------------------------
# This program offers a solution to the "Unfriendly Numbers" challenge on the 
# InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
# dashboard/#problem/4f7272a8b9d15). Here is the problem description, verbatim:
# 
# ==
# There is one friendly number and N unfriendly numbers. We want to find how 
# many numbers are there which exactly divide the friendly number, but does not 
# divide any of the unfriendly numbers.
# 
# INPUT FORMAT
# The first line of input contains two numbers N and K seperated by spaces. N is 
# the number of unfriendly numbers, K is the friendly number.
# The second line of input contains N space separated unfriendly numbers.
# 
# OUTPUT FORMAT
# Output the answer in a single line.
# 
# CONSTRAINTS
# 1 <= N <= 10^6
# 1 <= K <= 10^13
# 1 <= unfriendly numbers <= 10^18
# 
# SAMPLE INPUT
# 8 16
# 2 5 7 4 3 8 3 18
#  
# SAMPLE OUTPUT
# 1
# 
# EXPLANATION
# Divisors of the given friendly number 16, are { 1, 2, 4, 8, 16 } and the 
# unfriendly numbers are {2, 5, 7, 4, 3, 8, 3, 18}. Now 1 divides all unfriendly 
# numbers, 2 divide 2, 4 divide 4, 8 divide 8 but 16 divides none of them. So 
# only one number exists which divide the friendly number but does not divide 
# any of the unfriendly numbers. So the answer is 1.
# ==

from math      import *  # for 'sqrt'
from fractions import *  # for 'gcd'

# Function: GetFactors(x)
# Usage: factors = GetFactors(12)
# ------------------------------------------------------------------------------
# Returns a set containing all factors of the specified number, in O(sqrt(x)) 
# time.
def GetFactors(x):
  factors = set([x])
  
  # Cache the square root of the specified integer for efficiency.
  sqrtX = int(sqrt(x))
  
  # We can find all factors of x by iterating from 1 to the square root of x, 
  # inclusive.
  for i in range(1, sqrtX + 1):
    
    if x % i == 0:
      factors.add(i)
      factors.add(x / i)
  
  return factors


def main():
  # Read in the number of unfriendly numbers to expect, the friendly number, and 
  # all of the unfriendly numbers.
  numUnfriendlies, friendly = [int(i) for i in raw_input().split()]
  unfriendlies = [int(i) for i in raw_input().split()]
  
  # Before we do anything else, we'll need to find all factors of the friendly 
  # number we've been given. We can do this naively in O(sqrt(N)) time, where N 
  # is the value of the friendly number. This runtime is plenty sufficient for 
  # our purposes.
  friendlyFactors = GetFactors(friendly)
  
  # Now we need to find all unfriendly factors that we should disregard should 
  # they appear in our list of friendly factors. The key insight here is that we 
  # don't actually need to factor each unfriendly number in its entirety; that 
  # would simply take too long. Instead, we can optimize our approach by first 
  # finding the greatest common factor (or greatest common divisor, or GCD) 
  # between our friendly number and each unfriendly number, and then finding the 
  # factors of each GCD in much less time. By definition, the GCD of two numbers 
  # is the largest positive integer that divides the numbers without a 
  # remainder, so finding the GCD allows us to avoid considering any numbers in 
  # the interval (GCD, U] for some unfriendly number U.
  unfriendlyFactors = set()
  
  for unfriendly in unfriendlies:
    # Find the GCD between the friendly number and this unfriendly number.
    g = gcd(friendly, unfriendly)
    
    # Add the factors of this GCD (including the GCD itself) to the set of 
    # unfriendly factors we'll have to avoid.
    unfriendlyFactors.add(g)
    unfriendlyFactors.update(GetFactors(g))
  
  # Finally, we find the difference between the set of friendly factors and the 
  # set of unfriendly factors we accumulated, and print out the size of this set 
  # as the solution.
  print len(friendlyFactors - unfriendlyFactors)


if __name__ == "__main__":
  main()
