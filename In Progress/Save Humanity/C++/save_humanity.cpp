/* File: save_humanity.cpp
 * Author: Chris Lewis (cmslewis@gmail.com)
 * -----------------------------------------------------------------------------
 * This program offers a solution to the "Save Humanity" challenge on the 
 * InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
 * dashboard/#problem/4f304a3d84b5e). Here is the problem description, verbatim:
 * 
 * Oh!! Mankind is in trouble again.This time its a deadly disease spreading at 
 * a rate never seen before. Efficient detectors for the virus responsible is 
 * the need of the hour. You are the lead at Central Hospital and need to find a 
 * fast and reliable way to detect the 'foot-prints' of the virus DNA in that of 
 * patient.
 * 
 * The DNA of the patient as well as of the virus consists of lower case 
 * letters. Since the data collected is raw there may be some errors. You will 
 * need to find all substrings in the patient DNA that exactly matches the virus 
 * DNA with the exception of at most one mismatch.
 * 
 * For example tolerating at most one mismatch, "aa" and "aa" are matching, "ab" 
 * and "aa" are matching, while "ab" and "ba" are not.
 * 
 * INPUT
 * The first line contains the number of test cases T. T cases follow. Each case 
 * contains two lines containing strings P(Patient DNA) and V(Virus DNA) . Each 
 * case is followed by a blank line.
 * 
 * OUTPUT
 * Output T lines, one corresponding to each case. For each case, output a space 
 * delimited list of starting indices (0 indexed) of substrings of P which are 
 * matching with V according to the condition mentioned above . The indices has 
 * to be in increasing order.
 * 
 * CONSTRAINTS
 * 1 <= T <= 10
 * P and V contain at most 100000 characters each.
 * All characters in P and V are lowercase letters.
 * 
 * SAMPLE INPUT
 * 3
 * abbab
 * ba
 * 
 * hello
 * world
 * 
 * banana
 * nan
 * 
 * SAMPLE OUTPUT
 * 1 2
 * 
 * 0 2
 * 
 * EXPLANATION
 * For the first case, the substrings of P starting at indices 1 and 2 are "bb" 
 * and "ba" and they are matching with the string V which is "ba".
 * For the second case, there are no matching substrings so the output is a 
 * blank line.
 */

#include <iostream>
#include <iterator>
#include <string>
#include <vector>
using namespace std;

/* The maximum number of characters that may differ between two substrings. */ 
const int kMismatchTolerance = 1;

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

/* Function: GetInteger()
 * Usage: int n = GetInteger();
 * -----------------------------------------------------------------------------
 * Reads an integer from standard input, or 0 if no valid integer was entered.
 */
int GetInteger()
{
  int result;
  int ignore = scanf("%d\n", &result);
  return result;
}

/* Function: FindSubstringMatches(word, substring)
 * Usage: results = FindSubstringMatches("banana");
 * -----------------------------------------------------------------------------
 * This function returns all indices in the provided word where a substring 
 * starting at that index exactly matches the provided substring, with 
 * the exception of at most one mismatch.
 */
vector<int> FindSubstringMatches(string word, string substring, int tolerance)
{
  vector<int> results;
  
  /* For each possible starting index in the specified word... */
  for (int startIndex = 0; startIndex < word.length(); ++startIndex)
  {
    /* Reset the metadata used during the match-checking operations.*/
    int numMatches    = 0;
    int numMismatches = 0;
    bool resetFlag    = false;
    
    /* For each character in the substring we're trying to find... */
    for (int i = startIndex; i < word.length(); ++i)
    {
      /* Reindex from 0 to access characters in the provided substring. */
      int substring_i = i - startIndex;
      
      /* Case 0. Check for stopping conditions on the current substring. */
      if (resetFlag || substring_i >= substring.length())
        break;
      
      /* Case 1. The current chracters match. */
      else if (word[i] == substring[substring_i])
        ++numMatches;
      
      /* Case 2. The current characters do not match, but we're still within 
       * the mismatch tolerance.
       */
      else if (numMismatches < tolerance)
        ++numMismatches;
      
      /* Case 3. The current characters do not match, and there has already 
       * been a previous mismatch in this substring.
       */
      else
        resetFlag = true;
      
      /* Record the previous start index if enough characters matched. */
      if (substring_i == substring.length() - 1 &&
          numMatches >= substring.length() - tolerance)
        results.push_back(startIndex);
    }
  }
  
  return results;
}

/* Function: PrintList(myList)
 * Usage: PrintList([1,2,3]);
 * -----------------------------------------------------------------------------
 * Prints each int in the provided vector, maintaining the elements' original 
 * ordering. The elements are separated by a single space.
 */
void PrintVector(vector<int> &myVector)
{
  copy(myVector.begin(), myVector.end(), ostream_iterator<int>(cout, " "));
  cout << endl;
}

int main()
{
  /* Read in the number of test cases first. */
  int numCases = GetInteger();
  
  for (int i = 0; i < numCases; ++i)
  {
    /* Read in the word to examine and the substring to search for. */
    string word      = GetLine();
    string substring = GetLine();
    if (i < numCases - 1)
      string blankLine = GetLine(); // Swallow the blank line.
    
    /* Find the indices at which the provided substring appears, with the 
     * default tolerance for mismatched characters (1 mismatch).
     */
    vector<int> results = FindSubstringMatches(word, substring, 
                                               kMismatchTolerance);
    
    /* Print the list of indices where matches occurred. */
    PrintVector(results);
  }
  
  return 0;
}