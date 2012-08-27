
#include <iostream>
#include <set>
#include <string>
#include <sstream>
#include <utility>
using namespace std;

typedef pair<const char *, int> SubstringData;

struct SubstringComparator
{
  bool operator() (SubstringData s1, SubstringData s2)
  {
    return string(s1.first, s1.second) < string(s2.first, s2.second);
  }
};

typedef set<SubstringData, SubstringComparator> SubstringSet;

/* Function: GetLine()
 * Usage: string s = GetLine();
 * -----------------------------------------------------------------------------
 * Reads a line of user input from standard input.
 */
string GetLine()
{
  string result;
  getline(cin, result);
  return result;
}

int GetInteger()
{
  stringstream converter;
  converter << GetLine();
  
  int result;
  converter >> result;
  
  return result;
}

void ExtractSubstrings(const string & s,
                       set<string> &strings, SubstringSet &substrings)
{
  const string &sInserted = *(strings.insert(s).first);
  
  for (int beginIndex = 0; beginIndex < sInserted.length(); ++beginIndex)
    for (int length = 1; length + beginIndex <= sInserted.length(); ++length)
      substrings.insert(
        SubstringData(sInserted.c_str() + beginIndex, length)
      );
}

string FindKthSubstring(const int k, const SubstringSet &substrings)
{
  if (k > substrings.size())
    return "INVALID";
  
  SubstringSet::iterator itr = substrings.begin();
  for (int i = 1; i < k; ++i)
    ++itr;
  
  return string(itr->first, itr->second);
}

int main()
{  
  set<string> strings;
  SubstringSet substrings;
  
  /* Read in the number of strings to expect. */
  int numStrings = GetInteger();
  
  /* Read each string into a set, and maintain a separate set of pointers and 
   * lengths that can uniquely identify each substring.
   */
  for (int i = 0; i < numStrings; ++i)
    ExtractSubstrings( GetLine(), strings, substrings );
  
  /* Read in the number of queries to expect. */
  int numQueries = GetInteger();
  
  /* Print out the kth lexicographically ordered substring as per each query. */ 
  for ( int i = 0; i < numQueries; ++i )
    cout << FindKthSubstring( GetInteger(), substrings ) << endl;
  
  return 0;
}
