/* File: 2s_complement.cpp
 * Author: Chris Lewis (cmslewis@gmail.com)
 * -----------------------------------------------------------------------------
 * This program offers a solution to the "2's Complement" practice problem on 
 * the InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
 * dashboard/#problem/4e91289c38bfd). The problem asks us to count the total 
 * number of 1's bits in the 2's complement representations of all numbers 
 * between two integers, inclusive, that the user provides.
 * 
 * We use a recursive approach, which considers three cases. For the first case, 
 * we check whether the provided number is zero, and immediately return 0 
 * because there are no 1's in the 2's complement representation of the integer 
 * 0. For the second case, we check whether the provided number is even, in 
 * which case we use the GNU compiler's __builtin_popcount function to count the 
 * number of 1's in the number, then continue the recursion with the next 
 * integer one less than the current one.
 * 
 * Finally, if the current number is odd, then we consider every integer from 0 
 * to a, inclusive, as follows. First, because 0 is included in this set, we 
 * note that there will always be an even number of elements. Moreover, exactly 
 * half of the elements will be even numbers, and half will be odd. 
 * Interestingly, if we let each of these numbers have n bits (with leading 0's 
 * if necessary), then the leftmost n-1 bits for each number in the subset of 
 * even numbers will also appear for some number in the subset of odd numbers. 
 * This is clear because every odd number must end in a 1 and will thus have an 
 * even number with the exact same (n-1)-bit "prefix" that ends in a 0. This 
 * allows us to count the number of ones in these prefixes and then double since 
 * the same prefixes appear in both aforementioned subsets. This is the 2 * 
 * solve(a / 2) term. Finally, we add the total number of rightmost 1's in the 
 * set, which is simply the number of odd numbers: (a + 1) / 2.
 */

#include <iostream>
using namespace std;

long long NumOneBitsInRange(int a)
{
  // Base Case: a is zero.
  if (a == 0) return 0;
  
  // 2nd Case: a is even.
  if (a % 2 == 0) return __builtin_popcount(a) + NumOneBitsInRange(a - 1);
  
  // 3rd Case: a is odd.
  return (((long long)a + 1) / 2) + (2 * NumOneBitsInRange(a / 2));
}

long long NumOneBitsInRange(int a, int b)
{
  // If a is not negative...
  if (a >= 0)
  {
    // Count the number of 1's bits in all integers from 0 to b.
    long long total = NumOneBitsInRange(b);
    
    // If a is a positive integer, then subtract from the current total the 
    // number of 1's bits in all integers from 0 to a-1. 
    return (a > 0) ? total -= NumOneBitsInRange(a - 1) : total;
  }
  
  // Otherwise, if a is negative, then on a 32-bit system each negative number 
  // between a and zero will have 32 1's bits less the number of bits in the 
  // range from 0 to the binary representation of positive a.
  long long total = (32LL * -(long long)a) - NumOneBitsInRange(~a);
  
  // Handle the other number b similarly.
  if (b > 0)
    total += NumOneBitsInRange(b);
  else if (b < -1)
  {
    ++b;
    total -= (32LL * -(long long)b) - NumOneBitsInRange(~b);
  }
  return total;
}

int main()
{
  int numTests, a, b;
  
  cin >> numTests;
  
  while (numTests != 0)
  {
    cin >> a >> b;
    cout << NumOneBitsInRange(a, b) << endl;
    --numTests;
  }
  
  return 0;
}