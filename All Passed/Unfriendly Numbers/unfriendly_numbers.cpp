/* File: unfriendly_numbers.cpp
 * Author: Chris Lewis (cmslewis@gmail.com)
 * -----------------------------------------------------------------------------
 * This program offers a solution to the "Unfriendly Numbers" challenge on the 
 * InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
 * dashboard/#problem/4f7272a8b9d15). Here is the problem description, verbatim:
 * 
 * ==
 * There is one friendly number and N unfriendly numbers. We want to find how 
 * many numbers are there which exactly divide the friendly number, but does not 
 * divide any of the unfriendly numbers.
 * 
 * INPUT FORMAT
 * The first line of input contains two numbers N and K seperated by spaces. N 
 * is the number of unfriendly numbers, K is the friendly number.
 * The second line of input contains N space separated unfriendly numbers.
 * 
 * OUTPUT FORMAT
 * Output the answer in a single line.
 * 
 * CONSTRAINTS
 * 1 <= N <= 10^6
 * 1 <= K <= 10^13
 * 1 <= unfriendly numbers <= 10^18
 * 
 * SAMPLE INPUT
 * 8 16
 * 2 5 7 4 3 8 3 18
 *  
 * SAMPLE OUTPUT
 * 1
 * 
 * EXPLANATION
 * Divisors of the given friendly number 16, are { 1, 2, 4, 8, 16 } and the 
 * unfriendly numbers are {2, 5, 7, 4, 3, 8, 3, 18}. Now 1 divides all 
 * unfriendly numbers, 2 divide 2, 4 divide 4, 8 divide 8 but 16 divides none of 
 * them. So only one number exists which divide the friendly number but does not 
 * divide any of the unfriendly numbers. So the answer is 1.
 * ==
 */

#include <algorithm>  // for 'set_difference'
#include <cmath>      // for 'sqrt'
#include <iostream>
#include <set>
#include <vector>
using namespace std;

/* Function: gcd(unsigned int u, unsigned int v)
 * Usage: int g = gcd(20, 15);
 * -----
 * This function is borrowed from the Wikipedia article entitled "Binary GCD 
 * algorithm" (http://en.wikipedia.org/wiki/Binary_GCD_algorithm).
 * 
 * Following is an implementation of the algorithm in C, taking two
 * (non-negative) integer arguments u and v. It first removes all common factors 
 * of 2 using identity 2, then computes the GCD of the remaining numbers using 
 * identities 3 and 4, and combines these to form the final answer.
 */
unsigned long long int gcd(unsigned long long int u, unsigned long long int v)
{
  int shift;
  
  /* GCD(0,v) == v; GCD(u,0) == u, GCD(0,0) == 0 */
  if (u == 0) return v;
  if (v == 0) return u;
  
  /* Let shift := lg K, where K is the greatest power of 2
        dividing both u and v. */
  for (shift = 0; ((u | v) & 1) == 0; ++shift) {
    u >>= 1;
    v >>= 1;
  }
  
  while ((u & 1) == 0)
    u >>= 1;
  
  /* From here on, u is always odd. */
  do {
    /* remove all factors of 2 in v -- they are not common */
    /*   note: v is not zero, so while will terminate */
    while ((v & 1) == 0)  /* Loop X */
      v >>= 1;
    
    /* Now u and v are both odd. Swap if necessary so u <= v,
      then set v = v - u (which is even). For bignums, the
      swapping is just pointer movement, and the subtraction
      can be done in-place. */
    if (u > v) {
      unsigned long long int t = v; v = u; u = t;  // Swap u and v.
    }
    v = v - u;                       // Here v >= u.
  } while (v != 0);
  
  /* restore common factors of 2 */
  return u << shift;
}

/* Function: GetFactors(unsigned long long int x,
 *                      set<unsigned long long int>& factors)
 * Usage: set<unsigned long long int> factors;
 *        GetFactors(12, factors);
 * -----------------------------------------------------------------------------
 * Updates the provided set to include all factors of the specified number.
 */
void GetFactors(unsigned long long int x, set<unsigned long long int>& factors)
{
  /* Cache the square root of the specified integer for efficiency. */
  unsigned long long int sqrtX = (unsigned long long int)sqrt(x);
  
  /* We can find all factors of x by iterating from 1 to the square root of x,  
   * inclusive.
   */
  for (unsigned long long int i = 1; i <= sqrtX; ++i)
  {
    if (x % i == 0)
    {
      factors.insert(i);
      factors.insert(x/i);
    }
  }
}

/* Function: IntersectSets(const set<int>& set1, const set<int>& set2)
 * Usage: set<int> intersection = IntersectSets(set1, set2);
 * -----------------------------------------------------------------------------
 * A simple wrapper function that returns a new set containing only the elements 
 * that exist in both set1 and set2.
 */
template <typename T>
set<T> SetDifference(const set<T>& set1, const set<T>& set2)
{
  set<T> difference;
  set_difference(set1.begin(), set1.end(),
                 set2.begin(), set2.end(),
                 insert_iterator<set<T> >(difference,
                                          difference.begin()));
  return difference;
}

int main()
{
  /* We use unsigned long long int types throughout to handle 10^18 upper bound 
   * on the input (the maximum value for unsigned long long int's is 2^64, or 
   * approximately 1.8e19). In contrast, the maximum value of a typical 32-bit 
   * int is only about 4e9).
   */
  unsigned long long int numUnfriendlies, friendly;
  
  /* Read in the number of unfriendly numbers to expect and the friendly number. 
   */
  cin >> numUnfriendlies;
  cin >> friendly;
  
  /* Read in all of the unfriendly numbers into a vector. */
  vector<unsigned long long int> unfriendlies(numUnfriendlies);
  for (unsigned long long int i = 0; i < numUnfriendlies; ++i)
    cin >> unfriendlies[i];
  
  /* Before we do anything else, we'll need to find all factors of the friendly 
   * number we've been given. We can do this naively in O(sqrt(N)) time, where N 
   * is the value of the friendly number. This runtime is plenty sufficient for 
   * our purposes.
   */
  set<unsigned long long int> friendlyFactors;
  GetFactors(friendly, friendlyFactors);
  
  /* Now we need to find all unfriendly factors that we should disregard should 
   * they appear in our list of friendly factors. The key insight here is that 
   * we don't actually need to factor each unfriendly number in its entirety; 
   * that would simply take too long. Instead, we can optimize our approach by 
   * first finding the greatest common factor (or greatest common divisor, or 
   * GCD) between our friendly number and each unfriendly number, and then 
   * finding the factors of each GCD in much less time. By definition, the GCD 
   * of two numbers is the largest positive integer that divides the numbers 
   * without a remainder, so finding the GCD allows us to avoid considering any 
   * numbers in the interval (GCD, U] for some unfriendly number U.
   */
  set<unsigned long long int> unfriendlyFactors;
  for (vector<unsigned long long int>::iterator itr = unfriendlies.begin();
       itr != unfriendlies.end(); ++itr)
  {
    unsigned long long int unfriendly = *itr;
    
    /* Find the GCD between the friendly number and this unfriendly number. */
    unsigned long long int g = gcd(friendly, unfriendly);
    
    /* Add the factors of this GCD (including the GCD itself) to the set of 
     * unfriendly factors we'll have to avoid.
     */
    unfriendlyFactors.insert(g);
    GetFactors(g, unfriendlyFactors);
  }
  
  /* Finally, we find the difference between the set of friendly factors and the 
   * set of unfriendly factors we accumulated, and print out the size of this 
   * set as the solution.
   */
  set<unsigned long long int> difference = SetDifference(friendlyFactors, unfriendlyFactors);
  cout << difference.size() << endl;
  
  return 0;
}