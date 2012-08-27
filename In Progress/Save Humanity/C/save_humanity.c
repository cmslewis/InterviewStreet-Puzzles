


// DOES NOT WERRRRK YET!




/* File: save_humanity.py
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

#include <stdbool.h> // for 'bool', 'true', and 'false'
#include <stdio.h>   // for 'printf' and 'scanf'
#include <stdlib.h>  // for 'malloc', 'realloc'
#include <string.h>  // for 'strlen'

/* The maximum number of characters that may differ between two substrings. */ 
const int kMismatchTolerance = 1;

/* The maximum length for both the word and the substring. */
const int kMaxCandidateLength = 100000;

/* Function: GetLine()
 * Usage: string s = GetLine();
 * -----------------------------------------------------------------------------
 * Reads a line of user input from standard input.
 */
char *GetLine()
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
int *FindSubstringMatches(char *word, char *substring, int tolerance,
                          int *numResults)
{
  /* Cache the word and substring lengths for efficiency. */
  int wordLength   = strlen(word);
  int substrLength = strlen(substring);
  
  /* Initialize the results array to store the most instances of the substring 
   * that could possibly elements. We will resize the results array later if 
   * necessary.
   */
  *numResults = 0;
  int *results = malloc((wordLength - substrLength + 1) * sizeof(int));
  if (results == NULL) return NULL;
  
  /* For each possible starting index in the specified word... */
  int startIndex;
  for (startIndex = 0; startIndex < wordLength; ++startIndex)
  {
    /* Reset the metadata used during the match-checking operations.*/
    int numMatches    = 0;
    int numMismatches = 0;
    bool resetFlag    = false;
    
    /* For each character in the substring we're trying to find... */
    int i;
    for (i = startIndex; i < wordLength; ++i)
    {
      /* Reindex from 0 to access characters in the provided substring. */
      int substring_i = i - startIndex;
      
      /* Case 0. Check for stopping conditions on the current substring. */
      if (resetFlag || substring_i >= substrLength)
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
      if (substring_i == substrLength - 1 &&
          numMatches >= substrLength - tolerance)
      {
        results[*numResults] = startIndex;
        *numResults++;
      }
    }
    
    results = realloc(results, (*numResults) * sizeof(int));
    return results;
  }
  
  return results;
}

/* Function: PrintList(myList)
 * Usage: PrintList([1,2,3]);
 * -----------------------------------------------------------------------------
 * Prints each int in the provided vector, maintaining the elements' original 
 * ordering. The elements are separated by a single space.
 */
void PrintArray(int *myArray, int length)
{
  int i;
  
  for (i = 0; i < length; ++i)
    printf("%d ", myArray[i]);
  
  printf("\n");
}

int main()
{
  /* Read in the number of test cases first. */
  int numCases = GetInteger();
  
  int i;
  for (i = 0; i < numCases; ++i)
  {
    /* Read in the word to examine and the substring to search for. */
    char *word      = GetLine();
    char *substring = GetLine();
    //scanf("\n"); // Swallow the blank line.
    
    /* Find the indices at which the provided substring appears, with the 
     * default tolerance for mismatched characters (1 mismatch).
     */
    int numResults;
    int *results = FindSubstringMatches(word, substring,
                                        kMismatchTolerance, &numResults);
    
    /* Print the list of indices where matches occurred. */
    PrintArray(results, numResults);
    
    /* Free allocated memory. */
    free(word);
    free(substring);
    free(results);
  }
  
  
  return 0;
}