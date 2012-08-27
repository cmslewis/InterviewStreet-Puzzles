/* File: Solution.java
 * Author: Chris Lewis (cmslewis@gmail.com)
 * -----------------------------------------------------------------------------
 * This program offers a solution to the "Equations" challenge on the 
 * InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
 * dashboard/#problem/4e14a0058572a). Here is the problem description, verbatim:
 * 
 * ==
 * Find the no of positive integral solutions for the equations (1/x) + (1/y) = 
 * 1/N! (read 1 by n factorial) Print a single integer which is the no of 
 * positive integral solutions modulo 1000007.
 * 
 * INPUT
 * N 
 * OUTPUT
 * Number of positive integral solutions for (x,y) modulo 1000007
 * 
 * CONSTRAINTS
 * 1 <= N <= 10^6
 *  
 * SAMPLE INPUT 00
 * 1
 * SAMPLE OUTPUT 00
 * 1
 * 
 * SAMPLE INPUT 01
 * 32327
 * SAMPLE OUTPUT 01
 * 656502
 *  
 * SAMPLE INPUT 02
 * 40921
 * SAMPLE OUTPUT 02
 * 686720
 * ==
 * 
 * To solve this problem, let us first try to solve a separate, related one: 
 * given an integer m, how many positive integers divide evenly into m? We can 
 * derive the solution from the prime factorization of m. If there are j 
 * distinct primes in the range [0, m], then each of these primes must be raised 
 * to some certain integral exponent k_i >= 0 in the prime factorization of m. 
 * Thus:
 * 
 *   m = p_1^(k_1) * p_2^(k_2) * ... * p_j^(k_j)
 * 
 * For example, if m = 10, then the primes in consideration are {2, 3, 5, 7},
 * so m = 2^1 * 3^0 * 5^1 * 7^0.
 * 
 * This representation allows us to reason about the factors of m as well. In 
 * particular, we can conclude from the representation above that all factors of 
 * m will have between 0 and k_1 factors of prime p_1, between 0 and k_2 factors 
 * of p_2, and so on up to prime p_j. In total, the number of divisors (or 
 * solutions) of m is:
 * 
 * (k_1 + 1)(k_2 + 1)...(k_j + 1)
 * 
 * Furthermore, we can extend this reasoning to determine the number of divisors 
 * of m^2 (this apparent digression will prove useful in a moment). Since 
 * m^2 = m*m, we can conclude that m^2 has the following prime factorization:
 * 
 *   m^2 = m*m = (p_1^(k_1) * p_2^(k_2) * ... * p_j^(k_j)) *
 *               (p_1^(k_1) * p_2^(k_2) * ... * p_j^(k_j))
 *
 * Combining like exponent bases, we can reduce this to:
 * 
 *   m^2 = p_1^(2*k_1) * p_2^(2*k_2) * ... * p_j^(2*k_j)
 * 
 * This means that all factors of m^2 can have up to twice as many factors of 
 * each prime in there prime factorizations. Thus, the number of divisors is:
 * 
 * (2*k_1 + 1)(2*k_2 + 1)...(2*k_j + 1)
 * 
 * Coming back to the original problem, we are tasked with finding the number of 
 * integer solutions to (1/x) + (1/y) = 1/N!. Let's see if we can rearrange the 
 * terms in this equation to yield something a bit more useful:
 * 
 *       (1/x) + (1/y) = 1/N!
 *         y/xy + x/xy = 1/N!
 *            (x+y)/xy = 1/N!
 *      (xN! + yN!)/xy = 1
 *           xN! + yN! = xy
 *  xN! + yN! + (N!)^2 = xy + (N!)^2
 *              (N!)^2 = xy - xN! - yN! + (N!)^2
 *              (N!)^2 = (x - N!)(y - N!)
 * 
 * Now that's more like it! If we find the prime factorization of N!, we can 
 * plug the exponent values into the equation for the number of divisors of 
 * (N!)^2, which is in fact the number of solutions to the equation.
 * 
 * Thus, our algorithm is as follows:
 * 
 *   Find all primes in the interval [0, N].
 *   Find exponents of each prime number in the prime factorization of (N!)^2
 *   Plug each exponent into the expression (2*k_1 + 1)(2*k_2 + 1)...(2*k_j + 1)
 *   Print the result
 */

import java.math.BigInteger;
import java.util.Iterator;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.Collections; // for 'Collections.nCopy'

class Solution
{
  private static final BigInteger MODULUS_TERM = new BigInteger("1000007"); 
  
  public static void main(String[] args)
  {
    /* Initialize a scanner for reading from standard input. */
    Scanner sc = new Scanner(System.in);
    
    int N = sc.nextInt();
    
    System.out.println( numDivisors(N) );
  }
  
  /* Method: numSolutions(N)
   * Usage: x = numSolutions(4)
   * ---------------------------------------------------------------------------
   * Returns the number of possible divisors of (N!)^2 (modulo 1000007), which 
   * is exactly the number of solutions to the equation (1/x) + (1/y) = 1/N!.
   */
  static int numDivisors(int N)
  {
    List<Integer> primes = getPrimesUpTo(N);
    
    /* Get the number of instances of each prime number in the factorization of
     * N!.
     */
    Map<Integer, Integer> primeExponents = new HashMap<Integer, Integer>();
    for (int p : primes)
      primeExponents.put( p, getPrimeExponent(N, p) );
    
    /* Compute the number of integer soutions to the equation (we use long long 
     * types as a safeguard against integer overflows).
     */
    BigInteger result      = new BigInteger("1");
    BigInteger scaleFactor = new BigInteger("2");
    BigInteger addend      = new BigInteger("1");
    
    Iterator it = primeExponents.values().iterator();
    while (it.hasNext())
    {
      BigInteger term =
        new BigInteger("" + it.next())
        .multiply(scaleFactor)
        .add(addend);
      
      result = result.multiply(term);
      
      /* Doing a modulus operation after each multiplication is equivalent to 
       * doing only one at the very end, but the former approach offers yet 
       * another safeguard against integer overflows.
       */
      result = result.mod(MODULUS_TERM);
    }
    
    return result.intValue();
  } 
  
  /* Method: getPrimeExponent(N, p)
   * Usage: int e = getPrimeExponent(4, 2);
   * ---------------------------------------------------------------------------
   * Returns the exponent of the specified prime number p in the prime 
   * factorization of N!.
   */
  static int getPrimeExponent(int N, int p)
  {
    int remainingN = N;
    int exponent = 0;

    while (remainingN > 1)
    {
      remainingN /= p;
      exponent += remainingN;
    }

    return exponent;
  }
  
  /* Method: getPrimesUpTo(rangeEnd)
   * Usage: List<Integer> primes = getPrimesUpTo(4)
   * ---------------------------------------------------------------------------
   * Returns a list of all prime numbers in the range [0, rangeEnd].
   */
  static List<Integer> getPrimesUpTo(int rangeEnd)
  {
    List<Boolean> isPrime =
      new ArrayList<Boolean>(Collections.nCopies(rangeEnd + 1, true));
    
    /* Keep track of all primes in a separate list. */
    List<Integer> primes = new ArrayList<Integer>();
    
    /* 2 is the only even prime number. We can consider it in a special case, 
     * and then ignore all successive even numbers in the sieve.
     */
    if (2 <= rangeEnd)
      primes.add(2);
    
    /* Every prime number greater than 2 must be odd, so we'll iterate through 
     * odd numbers only to save time.
     */
    for (int i = 3; i <= rangeEnd; i += 2) {
      if (isPrime.get(i) == true) {
        primes.add(i);
        
        /* Mark all multiples of i as NOT prime. */
        for (int multiple = i; multiple <= rangeEnd; multiple += i)
          isPrime.set( multiple, false );
      }
    }
    
    return primes;
  }
}
