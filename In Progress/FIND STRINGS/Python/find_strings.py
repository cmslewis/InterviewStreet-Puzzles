
def main():
  
  substrings = set()
  
  # Read in the number of strings to expect.
  numStrings = int(raw_input())
  
  for i in range(numStrings):
    s = raw_input()
    
    # Add all substrings of s to our set of substrings in O(m_i^2) time, where 
    # m_i is the length of s.
    for firstCharIndex in range(0, len(s)):
      for lastCharIndex in range(firstCharIndex, len(s)):
        substrings.add( s[firstCharIndex:(lastCharIndex+1)] )
  
  print "\nSUBSTRINGS:"
  for substr in substrings:
    print substr
  
  
  
  

if __name__ == "__main__":
  main()
