MISMATCH_TOLERANCE = 1

# Function: Z_Algorithm(word)
# Usage: table = Z_Algorithm("aabcaabxaaaz")
# ------------------------------------------------------------------------------
# The Z Algorithm finds, for each position in the specified word, the maximal 
# number of consecutive characters starting at that position that match any 
# prefix of the word.
def Z_Algorithm(word):
  if word == "": return None
  
  result = [0] * len(word)
  
  # The starting position of the longest match we're currently considering. 
  maxMatchStartPos = 0
  
  # The ending position of the longest match we're currently considering.
  maxMatchEndPos = 0
  
  # For the second index to the end of the word, consider the substring that 
  # starts at that index.
  for pos in range(1, len(word)):
    # The length of the longest prefix we can match starting from here. 
    lenMatched = 0
    
    # Case 1. If the current position lies beyond the position of the last 
    # character in the previous match we considered, then we should reset 
    # our length counter and treat this position as the beginning of a new 
    # match.
    if pos > maxMatchEndPos:
      # Find the length of the longest prefix we can match starting here.
      for prefix_pos in range(0, len(word)):
        # Break if we've reached the end of the word or a mismatch.
        if prefix_pos + pos >= len(word): break
        if word[prefix_pos] != word[prefix_pos + pos]: break
        
        # Otherwise, increment our counter of consecutive matched characters.
        lenMatched += 1
      
      # Remember where the longest match from this position started and ended.
      if prefix_pos > 0:
        maxMatchStartPos = pos
        maxMatchEndPos   = pos + lenMatched - 1
    
    # Case 2. If the previous condition was false, then we must still be within 
    # a substring that matches some number of consecutive characters in the 
    # prefix of the word.
    else:
      # Find the length of the matched substring that's still in front of us. 
      lenRemaining  = maxMatchEndPos - pos + 1
      
      # Find the score at the corresponding offset in the word's prefix.
      parallelScore = result[pos - maxMatchStartPos]
      
      # If the parallel score is smaller than the number of characters in the 
      # current substring that still lie beyond the current position, then 
      # constrain the score at the current position accordingly.
      if parallelScore < lenRemaining:
        lenMatched = parallelScore
      
      # Otherwise, if the previous score was greater than or equal to the length 
      # that should be remaining, then we proceed much as we did for Case 1, 
      # finding the longest prefix we can match starting from this position.
      else:
        
        # Our match will be at least as long as the portion of the previous 
        # longest match that still lies beyond the current position.  
        lenMatched = lenRemaining
        
        for prefix_pos in range(lenRemaining, len(word)):
          # Break if we've reached the end of the word or a mismatch.
          if prefix_pos + pos >= len(word): break
          if word[prefix_pos] != word[prefix_pos + pos]: break
          
          # Otherwise, increment our counter of consecutive matched characters.
          lenMatched += 1
        
        # Remember where the longest match from this position started and ended.
        maxMatchStartPos = pos
        maxMatchEndPos   = pos + lenMatched - 1
    
    result[pos] = lenMatched
  
  return result


# Function: FindSubstringMatches(word, substring)
# Usage: results = FindSubstringMatches("banana");
# -----------------------------------------------------------------------------
# This function returns all indices in the provided word where a substring 
# starting at that index exactly matches the provided substring, with 
# the exception of at most one mismatch.
def FindSubstringMatches(word, substring, tolerance):
  results = []
  
  # Cache the word and substring lengths for efficiency.
  wordLength   = len(word)
  substrLength = len(substring)
  
  # For each possible starting index in the specified word...
  for startIndex in range(wordLength):
    
    # Reset the metadata used during the match-checking operations.
    numMatches    = 0
    numMismatches = 0
    resetFlag     = False
    
    # For each character in the substring we're trying to find...
    for i in range(startIndex, wordLength):
      
      # Reindex from 0 to access characters in the provided substring.
      substring_i = i - startIndex
      
      # Case 0. Check for stopping conditions on the current substring.
      if resetFlag or substring_i >= substrLength:
        break
      
      # Case 1. The current chracters match.
      elif word[i] == substring[substring_i]:
        numMatches += 1
      
      # Case 2. The current characters do not match, but we're still within 
      # the mismatch tolerance.
      elif numMismatches < tolerance:
        numMismatches += 1
      
      # Case 3. The current characters do not match, and there has already 
      # been a previous mismatch in this substring.
      else:
        resetFlag = True
  
      # Record the previous start index if enough characters matched.
      if substring_i == substrLength - 1 \
      and numMatches >= substrLength - tolerance:
        results.append(startIndex)
  
  return results


# Function: PrintList(myList)
# Usage: PrintList([1,2,3]);
# -----------------------------------------------------------------------------
# Prints each element in the provided list, maintaining the list's original 
# ordering. The elements are separated by a single space.
def PrintList(myList):
  # Print each list element followed by a space. 
  for elem in myList:
    print elem,
  
  # Print a newline character at the end of the line.
  print


def main():
  # Read in the number of test cases first.
  numCases = int(raw_input())
  
  for i in range(numCases):
    # Read in the word to examine and the substring to search for.
    word      = raw_input()
    substring = raw_input()
    if i < numCases - 1: blankLine = raw_input() # Swallow the blank line.
    
    partialMatchTable = 
    
    # Find the indices at which the provided substring appears, with the default 
    # tolerance for mismatched characters (1 mismatch).
    results = FindSubstringMatches(word, substring, MISMATCH_TOLERANCE)
    
    # Print the list of indices where matches occurred.
    PrintList(results)
  


if __name__ == "__main__":
  main()
