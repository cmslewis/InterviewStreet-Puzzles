/* File: string_reduction.cpp
 * Author: Chris Lewis (cmslewis@gmail.com)
 * -----------------------------------------------------------------------------
 * This program offers a solution to the "Median" challenge on the 
 * InterviewStreet website (URL: https://www.interviewstreet.com/challenges/
 * dashboard/#problem/4eac48496bee2). Here is the problem description, verbatim:
 * 
 * ==
 * Given a string consisting of a,b and c's, we can perform the following 
 * operation: Take any two adjacent distinct characters and replace it with the
 * third character. For example, if 'a' and 'c' are adjacent, they can replaced 
 * with 'b'. What is the smallest string which can result by applying this 
 * operation repeatedly?
 * 
 * INPUT
 * The first line contains the number of test cases T. T test cases follow. Each 
 * case contains the string you start with.
 * 
 * OUTPUT
 * Output T lines, one for each test case containing the smallest length of the 
 * resultant string after applying the operations optimally.
 * 
 * CONSTRAINTS
 * 1 <= T <= 100
 * The string will have at most 100 characters.
 * 
 * SAMPLE INPUT
 * 3
 * cab
 * bcab
 * ccccc
 * 
 * SAMPLE OUTPUT
 * 2
 * 1
 * 5
 * 
 * EXPLANATION
 * For the first case, you can either get cab -> cc or cab -> bb, resulting in a 
 * string of length 2.
 * For the second case, one optimal solution is: bcab -> aab -> ac -> b. No more 
 * operations can be applied and the resultant string has length 1.
 * For the third case, no operations can be performed and so the answer is 5.
 * ==
 */

#include <iostream>
#include <map>
#include <string>
using namespace std;

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

/* Function: GetInteger()
 * Usage: int n = GetInteger();
 * -----------------------------------------------------------------------------
 * Returns the length of the optimal reduction of the provided string according 
 * the rules specified in the problem description.
 */
int OptimalReductionLength(const string &s)
{
  /* Initialize a character counter for this string. */
  map<char, int> charCounts;
  
  /* Set all map values to 0 just to spare us the checking later on. */
  charCounts.insert(make_pair('a', 0));
  charCounts.insert(make_pair('b', 0));
  charCounts.insert(make_pair('c', 0));
  
  /* Count the occurrences of each character in the provided string. */
  for (int i = 0; i < s.length(); ++i)
    ++charCounts[s[i]];
  
  /* Case 1. If our string consists entirely of 1 character, then there is no 
   * hope of reducing it at all, so we return the length of s as the length of 
   * the optimal reduction.
   */
  if (charCounts['a'] == s.length() ||
      charCounts['b'] == s.length() ||
      charCounts['c'] == s.length())
  {
    return s.length();
  }
  
  /* Case 2. If all counts are even (zero inclusive) or all counts are odd, then 
   * we will only be able to reduce the string to 2 characters.
   */
  if (charCounts['a'] % 2 == charCounts['b'] % 2 &&
      charCounts['a'] % 2 == charCounts['c'] % 2)
  {
    return 2;
  }
  
  /* Case 3. In all other cases, we can reduce the string to a length of 1. */
  return 1;
}

int main()
{
  /* Read in the number of test cases to expect. */
  int numCases = GetInteger();
  
  for (int i = 0; i < numCases; ++i)
    /* Read in the next string and immediately print out the length of its 
     * optimal reduction.
     */
    cout << OptimalReductionLength(GetLine()) << endl;
  
  return 0;
}
