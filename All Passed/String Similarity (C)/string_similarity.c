/* File: string_similarity.c
 * Author: Chris Lewis (cmslewis@gmail.com)
 * -----------------------------------------------------------------------------
 * This program offers a solution to the "String Similarity" challenge on the 
 * InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
 * dashboard/#problem/4edb8abd7cacd). Here is the problem description, verbatim:
 * 
 * For two strings A and B, we define the similarity of the strings to be the 
 * length of the longest prefix common to both strings. For example, the 
 * similarity of strings "abc" and "abd" is 2, while the similarity of strings 
 * "aaa" and "aaab" is 3.
 * 
 * Calculate the sum of similarities of a string S with each of it's suffixes.
 * 
 * INPUT:
 * The first line contains the number of test cases T. Each of the next T lines 
 * contains a string each.
 * 
 * OUTPUT:
 * Output T lines containing the answer for the corresponding test case.
 * 
 * CONSTRAINTS:
 * 1 <= T <= 10
 * The length of each string is at most 100000 and contains only lower case 
 * characters.
 * 
 * SAMPLE INPUT:
 * 2
 * ababaa
 * aa
 * 
 * SAMPLE OUTPUT:
 * 11
 * 3
 * 
 * EXPLANATION:
 * For the first case, the suffixes of the string are "ababaa", "babaa", "abaa", 
 * "baa", "aa" and "a". The similarities of each of these strings with the 
 * string "ababaa" are 6,0,3,0,1,1 respectively. Thus the answer is 6 + 0 + 3 + 
 * 0 + 1 + 1 = 11.
 * 
 * For the second case, the answer is 2 + 1 = 3.
 */

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MIN(X,Y) ((X) < (Y) ? (X) : (Y))

const int kMaxCandidateLength = 100000;

/* Function: GetLine()
 * Usage: string s = GetLine();
 * -----------------------------------------------------------------------------
 * Reads a line of user input from standard input.
 */
char * GetLine()
{
  /* Allocate memory for the new line, plus one byte for a null terminator. */
  char *line = malloc(kMaxCandidateLength + 1);
  
  /* Abort immediately if memory allocation failed. */
  if (line == NULL) return NULL;
  
  /* Read a line of text from standard input. */
  if (fgets(line, kMaxCandidateLength, stdin))
  {
    /* Locate the newline character in the input string (presumably, it will be 
     * the last character).
     */
    char *newLine = strchr(line, '\n');
    
    /* If found, overwrite the newline character with a null terminator. */
    if (newLine) *newLine = '\0';
    
    /* Otherwise, insert a null terminator at the end of the memory block. */
    else line[kMaxCandidateLength] = '\0';
    
    /* Reduce the block to the size of the input string to save memory. */
    line = (char *)realloc(line, strlen(line) + 1);
  }
  
  return line;
}

/* Function: GetInteger()
 * Usage: int n = GetInteger();
 * -----------------------------------------------------------------------------
 * Reads a user-inputted integer value from standard input. If the inputted 
 * value is not a valid integer, the function will continually reprompt the user 
 * for a valid integer until one is finally inputted.
 */
int GetInteger()
{
  while (true)
  {
    /* Get a line from the user and try converting it to an integer. */
    char * line = GetLine();
    int result = atoi(line);
    free(line);
    
    /* If conversion succeeded, return the resultant integer. */
    if (result != 0) return result;
    
    /* Otherwise, reprompt the user until a valid integer is entered. */
    else
    {
      printf("Please enter an integer.\n");
      printf("Retry: ");
    }
  }
}

/* Function: RunSuffixSimilarityTest()
 * Usage: int testResult = RunSuffixSimilarityTest();
 * -----------------------------------------------------------------------------
 * This function is quite specific to the test objectives at hand and exists 
 * solely to encapsulate some functionality away from the main function to make 
 * the program easier for humans to read. The function takes in a candidate 
 * string and returns the sum of similarities of that string with each of its 
 * suffixes.
 * 
 * For example, given the word "mom" as the candidate, this function would 
 * calculate the similarity scores between "mom" and each of its suffixes, "mom" 
 * "om", and "m." The scores for each of these suffixes would be 3, 0, and 1, 
 * respectively (see the description of the StringSimilarity function for a more 
 * detailed explanation of how string similarity is defined). The function would 
 * then return 4, the sum of 3 + 0 + 1, as the total score for the provided 
 * candidate string.
 */
int RunSuffixSimilarityTest(const char * candidate)
{
  int i, j;
  int totalScore = 0;
  
  /* Cache the length of the candidate string for speed. */
  int candidateLength = strlen(candidate);
  
  /* Sum the similarity scores between the string and each of its suffixes. */
  for (i = 0; i < candidateLength; ++i)
  {
    /* Get the current suffix, and cache its length. */
    char * suffix    = (char *)candidate + i;
    int suffixLength = candidateLength - i;
    
    /* Calculate the string similarity for the current suffix. */
    int similarity = 0;
    for (j = 0; j < suffixLength; ++j)
    {
      if (candidate[j] == suffix[j])
        ++similarity;
      else break;
    }
    
    /* Add this similarity score to the total. */
    totalScore += similarity;
  }
  
  /* Return the sum of all suffix similarity scores for this string. */
  return totalScore;
}

int main()
{
  int i;
  
  /* Get the number of test cases to perform. */
  int numTests = GetInteger();
  
  /* Run each test case in turn. */
  for (i = 0; i < numTests; ++i)
  {
    char * candidate = GetLine();
    
    int totalScore = RunSuffixSimilarityTest(candidate);
    printf("%d\n", totalScore);
    
    free(candidate);
  }
  
  return 0;
}
