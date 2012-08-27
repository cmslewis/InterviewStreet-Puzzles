# File: string_similarity.py
# Author: Chris Lewis (cmslewis@gmail.com)
# -----------------------------------------------------------------------------
# This program offers a solution to the "String Similarity" challenge on the 
# InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
# dashboard/#problem/4edb8abd7cacd). Here is the problem description, verbatim:
# 
# For two strings A and B, we define the similarity of the strings to be the 
# length of the longest prefix common to both strings. For example, the 
# similarity of strings "abc" and "abd" is 2, while the similarity of strings 
# "aaa" and "aaab" is 3.
# 
# Calculate the sum of similarities of a string S with each of it's suffixes.
# 
# INPUT:
# The first line contains the number of test cases T. Each of the next T lines 
# contains a string each.
# 
# OUTPUT:
# Output T lines containing the answer for the corresponding test case.
# 
# CONSTRAINTS:
# 1 <= T <= 10
# The length of each string is at most 100000 and contains only lower case 
# characters.
# 
# SAMPLE INPUT:
# 2
# ababaa
# aa
# 
# SAMPLE OUTPUT:
# 11
# 3
# 
# EXPLANATION:
# For the first case, the suffixes of the string are "ababaa", "babaa", "abaa", 
# "baa", "aa" and "a". The similarities of each of these strings with the 
# string "ababaa" are 6,0,3,0,1,1 respectively. Thus the answer is 6 + 0 + 3 + 
# 0 + 1 + 1 = 11.
# 
# For the second case, the answer is 2 + 1 = 3.
#
 
# Function: RunSuffixSimilarityTest()
# Usage: testResult = RunSuffixSimilarityTest()
# -----------------------------------------------------------------------------
# This function is quite specific to the test objectives at hand and exists 
# solely to encapsulate some functionality away from the main function to make 
# the program easier for humans to read. The function takes in a candidate 
# string and returns the sum of similarities of that string with each of its 
# suffixes.
# 
# For example, given the word "mom" as the candidate, this function would 
# calculate the similarity scores between "mom" and each of its suffixes, "mom" 
# "om", and "m." The scores for each of these suffixes would be 3, 0, and 1, 
# respectively (see the description of the StringSimilarity function for a more 
# detailed explanation of how string similarity is defined). The function would 
# then return 4, the sum of 3 + 0 + 1, as the total score for the provided 
# candidate string.
def RunSuffixSimilarityTest(candidate):
  
  # Cache the length of the provided string for speed.
  candidateLength = len(candidate) 
  
  # Initialize the total score to the length of the candidate string (the string 
  # is perfectly similar itself).
  totalScore = candidateLength
  
  # Intialize character "pointers" to compare successive characters between the 
  # candidate string and the current suffix (note that we can start on the 
  # second suffix, which starts at the 2nd character, or the 1st index in the 
  # 0-indexed string).
  candidatePtr = 0
  suffixPtr    = 1
  
  # Keep track of where the current suffix begins for later reference.
  suffixStart  = 1
  
  # Calculate the similarity score between the candidate string and each suffix.
  while (suffixPtr < candidateLength or candidatePtr > 0):
    charsMatch = (candidate[candidatePtr] == candidate[suffixPtr])
    
    if charsMatch:
      # The characters match, so increment the total score for the string.
      totalScore   += 1
      
      # Prepare to compare the next character of the candidate string to the 
      # next character of the current suffix.
      candidatePtr += 1 
      suffixPtr    += 1
    
    if not charsMatch or suffixPtr >= candidateLength:
      # Start again with the next suffix.
      suffixStart += 1
      
      # Reset the candidate and suffix pointers.
      candidatePtr = 0
      suffixPtr    = suffixStart
  
  # Return the sum of all suffix similarity scores for this string.
  return totalScore

def main():
  # Get the number of test cases to perform.
  numTests = int(raw_input())
  
  # Run each test case in turn.
  for i in range(numTests):
    print RunSuffixSimilarityTest(raw_input())


if __name__ == "__main__":
  main()
