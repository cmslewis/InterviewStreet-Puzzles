# File: string_reduction.py
# Author: Chris Lewis (cmslewis@gmail.com)
# ------------------------------------------------------------------------------
# This program offers a solution to the "Median" challenge on the 
# InterviewStreet website (URL: https://www.interviewstreet.com/challenges/
# dashboard/#problem/4eac48496bee2). Here is the problem description, verbatim:
# 
# ==
# Given a string consisting of a,b and c's, we can perform the following 
# operation: Take any two adjacent distinct characters and replace it with the
# third character. For example, if 'a' and 'c' are adjacent, they can replaced 
# with 'b'. What is the smallest string which can result by applying this 
# operation repeatedly?
# 
# INPUT
# The first line contains the number of test cases T. T test cases follow. Each 
# case contains the string you start with.
# 
# OUTPUT
# Output T lines, one for each test case containing the smallest length of the 
# resultant string after applying the operations optimally.
# 
# CONSTRAINTS
# 1 <= T <= 100
# The string will have at most 100 characters.
# 
# SAMPLE INPUT
# 3
# cab
# bcab
# ccccc
# 
# SAMPLE OUTPUT
# 2
# 1
# 5
# 
# EXPLANATION
# For the first case, you can either get cab -> cc or cab -> bb, resulting in a 
# string of length 2.
# For the second case, one optimal solution is: bcab -> aab -> ac -> b. No more 
# operations can be applied and the resultant string has length 1.
# For the third case, no operations can be performed and so the answer is 5.
# ==

from collections import Counter

def OptimalReductionLength(s):
  # Initialize a character counter for this string.
  charCounts = Counter(a=0, b=0, c=0)
  
  # Count the number of occurrences of each character from the alphabet in s.
  for j in range(len(s)):
    charCounts[s[j]] += 1
  
  # Case 1. If our string consists entirely of 1 character, then there is no 
  # hope of reducing it at all, so we return the length of s as the length of 
  # the optimal reduction.
  if charCounts['a'] == len(s) \
  or charCounts['b'] == len(s) \
  or charCounts['c'] == len(s):
    return len(s)
  
  # Case 2. If all counts are even (zero inclusive) or all counts are odd, then 
  # we will only be able to reduce the string to 2 characters.
  if charCounts['a'] % 2 == charCounts['b'] % 2 \
  and charCounts['a'] % 2 == charCounts['c'] % 2:
    return 2
  
  # Case 3. In all other cases, we can reduce the string to a length of 1.
  return 1

def main():
  # Read in the number of test cases to expect.
  numCases = int(raw_input())
  
  for i in range(numCases):
    # Read in the next string from standard input.
    s = raw_input()
    
    print OptimalReductionLength(s)
    


if __name__ == "__main__":
  main()