/* File: Solution.java
 * Author: Chris Lewis (cmslewis@gmail.com)
 * -----------------------------------------------------------------------------
 * This program offers a solution to the "K Difference" challenge on the 
 * InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
 * dashboard/#problem/4e14b83d5fd12). Here is the problem description, verbatim:
 * 
 * ==
 * Given N numbers , [N<=10^5] we need to count the total pairs of numbers that 
 * have a difference of K. [K>0 and K<1e9]
 * 
 * INPUT FORMAT
 * 1st line contains N & K (integers).
 * 2nd line contains N numbers of the set. All the N numbers are assured to be 
 * distinct.
 * 
 * OUTPUT FORMAT
 * One integer saying the no of pairs of numbers that have a diff K.
 * 
 * SAMPLE INPUT #00:
 * 5 2
 * 1 5 3 4 2
 * 
 * SAMPLE OUTPUT #00:
 * 3
 * 
 * SAMPLE INPUT #01
 * 10 1
 * 363374326 364147530 61825163 1073065718 1281246024 1399469912 428047635 
 * 491595254 879792181 1069262793 
 * 
 * SAMPLE OUTPUT #01
 * 0
 * 
 * Read input from STDIN and write output to STDOUT.
 * ==
 * 
 * This implementation uses an O(n) algorithm to solve the problem (the solution 
 * is O(n) once all elements have been inserted into the set; however, there is 
 * O(log n) term for set insertion). The algorithm was originally presented by 
 * Eric Lippert in a StackOverflow thread:  http://stackoverflow.com/questions/ 
 * 7695723/optimizing-this-c-sharp-algorithm-k-difference. We maintain two sets, 
 * one with the original integers that the user inputs, and another with same 
 * values each incremented by the target difference. For instance, on SAMPLE 
 * INPUT #00, the first set would be {1, 5, 3, 4, 2} and the second set would be 
 * {1 + 2, 5 + 2, 3 + 2, 4 + 2, 2 + 2} == {3, 7, 5, 6, 4}. We then take the  
 * intersection of these sets to find all elements that, when incremented by the 
 * specified difference, still exist in the original set. In fact, this is 
 * precisely what the problem asks for. We then return the size of this 
 * intersection as the solution.
 */

import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;

public class Solution
{
  
  public static void main(String[] args)
  {
    int numElements, diff, x;
    Set<Integer> elements            = new HashSet<Integer>();
    Set<Integer> incrementedElements = new HashSet<Integer>();
    
    /* Initialize a scanner for reading from standard input. */
    Scanner in = new Scanner(System.in);
    
    /* Read in the number of elements to expect, and the target difference. */
    numElements = in.nextInt();
    diff        = in.nextInt();
    
    /* Read the integers into the elements set. For each integer, add the target 
     * difference to it and insert it into the incremented elements set.
     */
    for (int i = 0; i < numElements; ++i)
    {
      x = in.nextInt();
      
      elements.add(x);
      incrementedElements.add(x + diff);
    }
    
    /* Perform a set intersection between the original elements and the 
     * incremented elements to determine all elements for which there is 
     * another element that differs from it by the target amount.
     */
    elements.retainAll(incrementedElements);
    
    /* Print out the size of the intersection as the answer. */
    System.out.println(elements.size());
  }
  
  
}