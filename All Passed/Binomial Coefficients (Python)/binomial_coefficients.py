# File: binomial_coefficients.py
# Author: Chris Lewis (cmslewis@gmail.com)
# -----------------------------------------------------------------------------
# This program offers a solution to the "Binomial Coefficients" challenge on the 
# InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
# dashboard/#problem/4fe19c4f35a0e). Here is the problem description, verbatim:
# 
# ==
# In mathematics, binomial coefficients are a family of positive integers that 
# occur as coefficients in the binomial theorem. (n choose k) denotes the number 
# of ways of choosing k objects from n different objects.
# 
# However when n and k are too large, we often save them after modulo operation 
# by a prime number P. Please calculate how many binomial coefficients of n 
# become to 0 after modulo by P.
# 
# INPUT
# The first of input is an integer T , the number of test cases.
# Each of the following T lines contains 2 integers,  n and prime P.
# 
# OUTPUT
# For each test case, output a line contains the number of  s (0<=k<=n)  each of 
# which after modulo operation by P is 0.
# 
# SAMPLE INPUT
# 3
# 2 2
# 3 2
# 4 3
# 
# SAMPLE OUTPUT
# 1
# 0
# 1
# 
# CONSTRAINTS
# T is less than 100
# n is less than 10^500
# P is less than 10^9
# ==
# 
# This implementation relies on a *spectacular* algorithm outlined by Daniel 
# Fischer on Stack Overflow (URL: http://stackoverflow.com/questions/11867162/ 
# finding-binomial-co-effecient-modulo-prime-number-interview-street-challenge). 
# Admittedly, there are a couple of ways to approach this problem, but this is 
# definitely the most elegant approach I've seen. See the Stack Overflow answer 
# for a detailed sketch of the reasoning behind the algorithm and a sketch of 
# the algorithm itself.

def NumDivisibleCoefficients(n, P):
  m = n
  numCoeffsNotDividingP = 1
  
  while m > 0:
    numCoeffsNotDividingP *= ((m % P) + 1)
    m /= P
  
  return (n + 1 - numCoeffsNotDividingP)

def main():
  # Read in the number of test cases to expect.
  numCases = int(raw_input())
  
  # Report the solution for each test case.
  for i in range(numCases):
    n, P = [int(token) for token in raw_input().split()]
    
    print NumDivisibleCoefficients(n, P)
    
  


if __name__ == "__main__":
  main()
