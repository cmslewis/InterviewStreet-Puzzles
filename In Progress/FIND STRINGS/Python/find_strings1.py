
def substrings(string):
  substrings = set()
  
  # Discover substrings by increasing length.
  for substringLength in range(1, len(string) + 1):
    # Add all substrings of this length.
    for i in range(len(string) - substringLength + 1):
      substrings.add( string[i:i+substringLength] )
  
  return substrings


def main():
  n = int(raw_input())  # The total number of input strings.
  S = set()             # The set of all unique substrings.
  
  for i in range(n):
    # Generate all substrings for this string.
    S_i = substrings(raw_input())
    
    # Add these substrings into the set of all substrings.
    S = S.union(S_i)
  S_ordered = sorted(S)
  
  q = int(raw_input())  # The number of queries.
  
  queries = [int(raw_input()) for k in range(q)]
    
  for k in queries:
    if k > len(S_ordered):
      print 'INVALID'
    else:
      print S_ordered[k - 1]


if __name__ == "__main__":
  main()