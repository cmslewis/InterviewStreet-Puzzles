
def UpdateSuffixArray(suffixSet, word):
  suffixes = [word[i:] for i in range(0, len(word))]
  
  for suffix in suffixes:
    suffixSet.add(suffix)

def FindKthSubstring(suffixArray, k):
  # Begin by generating a sorted suffix array from the provided word.
  # suffixes = sorted([word[i:] for i in range(0, len(word))])
  
  # We now leverage the fact that every substring of a string is a prefix of 
  # some suffix of that string. Moreover, a substring of length m can have no 
  # more than m prefixes. We can therefore find the lexicographically kth 
  # ordered substring by determining the last ordered suffix for which k is less 
  # than the sum of the length of that suffix and all suffixes that come 
  # lexicographically before it, and then returning the jth prefix of that 
  # suffix, where j is equal to k minus the sum of the lengths of all suffixes 
  # that came before the target suffix.
  j            = k
  targetSuffix = None
  
  for i in range(0, len(suffixArray)):
    suffix = suffixArray[i]
    if j <= len(suffix):
      targetSuffix = suffix
      break
    else:
      j -= len(suffix)
  
  return targetSuffix[:j] if targetSuffix != None else 'INVALID' 


def main():
  numStrings = int(raw_input())  # The total number of input strings.
  
  suffixSet = set()
  
  for i in xrange(numStrings):
    # O(n log n) for insertion of n elements into a set 
    # Add all suffixes of the ith input string to the suffix array. 
    UpdateSuffixArray(suffixSet, raw_input())
  
  # O(n log n) for sorting n suffixes
  sortedSuffixes = sorted(list(suffixSet))
  
  print sortedSuffixes
  
  
  numQueries = int(raw_input())
  
  for i in range(numQueries):
    print FindKthSubstring(sortedSuffixes, int(raw_input()))


if __name__ == "__main__":
  main()