/* File: median.cpp
 * Author: Chris Lewis (cmslewis@gmail.com)
 * -----------------------------------------------------------------------------
 * This program offers a solution to the "Median" challenge on the 
 * InterviewStreet website (URL: https://www.interviewstreet.com/challenges/
 * dashboard/#problem/4fcf919f11817). Here is the problem description, verbatim:
 *
 * ==
 * The median of M numbers is defined as the middle number after sorting them in 
 * order, if M is odd or the average number of the middle 2 numbers (again after 
 * sorting) if M is even. You have an empty number list at first. Then you can 
 * add or remove some number from the list. For each add or remove operation, 
 * output the median of numbers in the list.
 *
 * EXAMPLE:
 * For a set of m = 5 numbers, { 9, 2, 8, 4, 1 } the median is the third number 
 * in sorted set { 1, 2, 4, 8, 9 } which is 4. Similarly for set of
 * m = 4, { 5, 2, 10, 4 }, the median is the average of second and the third 
 * element in the sorted set { 2, 4, 5, 10 } which is (4+5)/2 = 4.5  
 * 
 * INPUT:
 * The first line is an integer n indicates the number of operations. Each of 
 * the next n lines is either "a x" or "r x" which indicates the operation is 
 * add or remove.
 *
 * OUTPUT:
 * For each operation: If the operation is add output the median after adding x 
 * in a single line. If the operation is remove and the number x is not in the 
 * list, output "Wrong!" in a single line. If the operation is remove and the 
 * number x is in the list, output the median after deleting x in a single line. 
 * (if the result is an integer DO NOT output decimal point. And if the result 
 * is a double number , DO NOT output trailing 0s.)
 * 
 * CONSTRAINTS:
 * 0 < n <= 100,000
 * For each "a x" or "r x" , x will fit in 32-bit integer.
 *
 * SAMPLE INPUT:
 * 7
 * r 1
 * a 1
 * a 2
 * a 1
 * r 1
 * r 2
 * r 1
 *
 * SAMPLE OUTPUT:
 * Wrong!
 * 1
 * 1.5
 * 1
 * 1.5
 * 1
 * Wrong!
 *
 * Note: As evident from the last line of the input, if after remove operation 
 * the list becomes empty you have to print "Wrong!" ( quotes are for clarity ).
 * ==
 * 
 * This implementation uses the following approach, adapted from the algorithm 
 * outlined on the "Just Codes..." blog at (http://justprogrammng.blogspot.com/ 
 * 2012/06/interviewstreet-median-challenge-part-2.html#.UAiTyJlYsqI). We 
 * maintain two multisets (where each set is capable of holding multiple 
 * instances of the same value). The first set, the "minset," will at all times 
 * contain the n/2 lowest values, and the second set, the "maxset" will contain 
 * the remaining n/2 greatest values. Provided that we are diligent about our 
 * maintenance of these sets, then the median value will always be accessible as 
 * either the maximum value of the minset or the minimum value of the maxset.
 * 
 * Concretely, the algorithm works as follows:
 * 
 * Initialize a minset and a maxset.
 * For each input operation:
 *   (1) If the operation is an insert operation:
 *       (a) If the value exceeds the current maximum value in the minset:
 *           - Add the value to the maxset.
 *       (b) Else:
 *           - Add the value to the minset.
 *   (2) Else if the operation is a remove operation:
 *       (a) If the value is in the minset:
 *           - Remove one instance of the value from the minset.
 *       (b) Else if the value is in the maxset:
 *           - Remove one instance of the value from the maxset.
 *       (c) Else:
 *           - The value has not been seen before, so we do nothing.
 *   (3) Now, we resize each set to be as close to n/2 as possible:
 *       (a) If the maxset is bigger than the minset:
 *           - Move one instance of the maxset's smallest value to the minset.
 *       (b) If the minset is has two or more elements than the maxset:
 *           - Move one instance of the minset's greatest value to the maxset.
 * If both sets are empty:
 * - There is no median, so return none.
 * Else if the minset is bigger than the maxset:
 * - Return the maximum value of the minset as the median.
 * Else:
 * - Return the minimum value of the maxset as the median.
 */

#include <iostream>
#include <iomanip>
#include <iterator>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

/* The input command denoting that an insert operation should be performed. */ 
const string kInsertOperation = "a";

/* The input command denoting that a remove operation should be performed. */ 
const string kDeleteOperation = "r";

/* The output text denoting that an operation failed. */ 
const string kErrorMessage = "Wrong!";

/* A shorthand for syntatical convenience when handling set iterators. */
typedef multiset<int>::iterator SetIterator;

/* Function: FindMinElement(multiset<int>& set)
 * Usage: SetIterator minValuePos = FindMinElement(maxSet);
 * -----------------------------------------------------------------------------
 * Returns an iterator pointing to the smallest element in the provided 
 * multiset.
 */
SetIterator FindMinElement(const multiset<int>& set)
{
  return set.begin();
}

/* Function: FindMaxElement(multiset<int>& set)
 * Usage: SetIterator maxValuePos = FindMinElement(maxSet);
 * -----------------------------------------------------------------------------
 * Returns an iterator pointing to the greatest element in the provided 
 * multiset.
 */
SetIterator FindMaxElement(const multiset<int>& set)
{
  /* The set.end() iterator by convention points to the "position" one after the 
   * last element in the provided container. Thus, to access the last element, 
   * we simply decrement the iterator by one position.
   */
  SetIterator itr = set.end();
  --itr;
  
  return itr;
}

/* Function: PerformInsert(int value,
 *                         multiset<int>& minSet,
 *                         multiset<int>& maxSet)
 * Usage: bool success = PerformInsert(value, minSet, maxSet);
 * -----------------------------------------------------------------------------
 * Inserts one instance of the specified value into the minset or the maxset, 
 * according to the following logic: if the value exceeds the current maximum 
 * value in the minset, then add the value to the maxset; otherwise, add the 
 * value to the minset. The function returns true if the insert operation was 
 * successful, and false otherwise.
 */
bool PerformInsert(int value, multiset<int>& minSet, multiset<int>& maxSet)
{
  if (minSet.empty() || value <= *FindMaxElement(minSet))
    minSet.insert(value);
  else
    maxSet.insert(value);
  
  /* Always return true. */
  return true;
}

/* Function: PerformDelete(int value,
 *                         multiset<int>& minSet,
 *                         multiset<int>& maxSet)
 * Usage: bool success = PerformDelete(value, minSet, maxSet);
 * -----------------------------------------------------------------------------
 * Removes one instance of the specified value from the minset or the maxset, 
 * according to the following logic: if the value is in the minset, remove one 
 * instance of the value from the minset; else if the value is in the maxset, 
 * remove one instance of the value from the maxset; otherwise, the value has 
 * not been seen before, so we do nothing. The function returns true if the 
 * insert operation was successful, and false otherwise.
 */
bool PerformDelete(int value, multiset<int>& minSet, multiset<int>& maxSet)
{
  SetIterator valuePos;
  
  /* If the number is in minset, remove it. */
  valuePos = minSet.find(value);
  if (valuePos != minSet.end())
  {
    minSet.erase(valuePos);
    return true;
  }
  
  /* Else if the number is in maxset, remove it. */
  valuePos = maxSet.find(value);
  if (valuePos != maxSet.end())
  {
    maxSet.erase(valuePos);
    return true;
  }
  
  /* Otherwise, return failure. */
  return false;
}

/* Function: ResizeSets(multiset<int>& minSet, multiset<int>& maxSet)
 * Usage: ResizeSets(minSet, maxSet);
 * -----------------------------------------------------------------------------
 * Resizes the provided minset and maxset so that their sizes are as similar as 
 * possible, while still keeping the n/2 lowest values in the minset and the 
 * remaining n/2 greatest values in the maxset. If n is even, then this function 
 * will resize the sets to each be of size n/2; if n is odd, then this function 
 * will resize the minset to contain floor(n/2) + 1 elements and the maxset to 
 * contain floor(n/2) elements. Note that this function will perform at most ONE 
 * transfer operation; therefore, this function should be called immediately 
 * after any single operation is performed (i.e. inserting or removing an 
 * element).
 */
void ResizeSets(multiset<int>& minSet, multiset<int>& maxSet)
{
  if (maxSet.size() > minSet.size())
  {
    /* Get the minimum value from the max set. */
    SetIterator minValuePos = FindMinElement(maxSet);
    
    /* Transfer the value from the max set to min set. */
    minSet.insert(*minValuePos);
    maxSet.erase(minValuePos);
  }
  
  if (minSet.size() > maxSet.size() + 1)
  {
    /* Get the maximum value from the min set. */
    SetIterator maxValuePos = FindMaxElement(minSet);
    
    /* Transfer the value from the min set to max set. */
    maxSet.insert(*maxValuePos);
    minSet.erase(maxValuePos);
  }
}

/* Function: GetFormattedMedian(const multiset<int>& minSet,
 *                              const multiset<int>& maxSet)
 * Usage: GetFormattedMedian(minSet, maxSet);
 * -----------------------------------------------------------------------------
 * Returns a string representation of the median value between the provided 
 * minset and maxset, consistent with the output specifications from the problem 
 * description. 
 */
string GetFormattedMedian(const multiset<int>& minSet,
                          const multiset<int>& maxSet)
{
  stringstream s;
  
  if (minSet.size() > maxSet.size())
    s << fixed << *FindMaxElement(minSet);
  
  else if (minSet.size() < maxSet.size())
    s << fixed << *FindMinElement(maxSet);
  
  else
  {
    /* Cast the numerator as a long to prevent integer overflow when summing. */
    long long sum = (long long)(*FindMaxElement(minSet))
                    + *FindMinElement(maxSet);
    
    /* Now we can ensure the median will hold the correct 32-bit value. */
    double median = (double)(sum / 2.0);
    
    if (median != (int)median)
      s << setprecision(1);
    else
      s << setprecision(0);
    
    /* Ensures that the median will be printed in decimal notation, as opposed 
     * to scientific notation.
     */
    s << fixed << median;
  }
    
  return s.str();
}

/* Function: PerformSingleOperation(string operation,
 *                                  int value,
 *                                  multiset<int>& minSet,
 *                                  multiset<int>& maxSet)
 * Usage: string median = PerformSingleOperation(op, x, minSet, maxSet)
 * -----------------------------------------------------------------------------
 * Performs the specified operation (insert or remove) with the specified value, 
 * and returns a formatted string representation of the new median value after 
 * performing the operation.
 */
string PerformSingleOperation(string operation, int value,
                              multiset<int>& minSet, multiset<int>& maxSet)
{
  bool operationSucceeded;
  
  /* Handle an insert operation. */
  if (operation == kInsertOperation)
    operationSucceeded = PerformInsert(value, minSet, maxSet);
  
  /* Handle a delete operation. */
  else if (operation == kDeleteOperation)
    operationSucceeded = PerformDelete(value, minSet, maxSet);
  
  /* Resize each set to be of size n/2. */
  ResizeSets(minSet, maxSet);
  
  /* Return an error message if necessary. */
  if (!operationSucceeded || (minSet.empty() && maxSet.empty()))
    return kErrorMessage;
  
  /* Otherwise return the median as a string. */
  return GetFormattedMedian(minSet, maxSet);
}

/* Function: PerformOperations(const vector<string>& operations,
 *                             const vector<int>& values)
 * Usage: PerformOperations(ops, vals);
 * -----------------------------------------------------------------------------
 * Accepts a vector of insert/delete operations and a vector of numerical values 
 * as input, then performs the specified operations in order, outputting the 
 * median that results after each operation is performed.
 */
void PerformOperations(const vector<string>& operations,
                       const vector<int>& values)
{
  /* Initialize our two sets. */
  multiset<int> minSet, maxSet;
  
  /* Print out the median after each operation. */
  for (int i = 0; i < operations.size(); ++i)
  {
    cout << PerformSingleOperation(operations[i], values[i], minSet, maxSet);
    cout << endl;
  }
}

int main()
{
  /* Read in the number of forthcoming operation lines. */ 
  int numOperations;
  cin >> numOperations;
  
  /* Initialize vectors to hold the operations and values. */ 
  vector<string> operations(numOperations);
  vector<int> values(numOperations);
  
  /* Read in each operation. */ 
  for (int i = 0; i < numOperations; ++i)
    cin >> operations[i] >> values[i];
  
  PerformOperations(operations, values);
  
  return 0;
}
