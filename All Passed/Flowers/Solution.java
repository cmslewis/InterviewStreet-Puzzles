/* File: Solution.java
 * Author: Chris Lewis (cmslewis@gmail.com)
 * -----------------------------------------------------------------------------
 * This program offers a solution to the "Flowers" challenge on the 
 * InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
 * dashboard/#problem/4fd05444acc45). Here is the problem description, verbatim:
 * 
 * ==
 * You and your K-1 friends want to buy N flowers. Flower number i has host ci. 
 * Unfortunately the seller does not like a customer to buy a lot of flowers, so 
 * he tries to change the price of flowers for customer who had bought flowers 
 * before. More precisely if a customer has already bought x flowers, he should 
 * pay (x+1)*ci dollars to buy flower number i.
 * 
 * You and your K-1 firends want to buy all N flowers in such a way that you 
 * spend the as few money as possible.
 * 
 * INPUT
 * The first line of input contains two integers N and K.
 * next line contains N positive integers c1,c2,...,cN respectively.
 * 
 * OUTPUT
 * Print the minimum amount of money you (and your friends) have to pay in order 
 * to buy all n flowers.
 * 
 * SAMPLE INPUT
 * 3 3
 * 2 5 6
 * 
 * SAMPLE OUTPUT
 * 13
 * 
 * EXPLANATION
 * In the example each of you and your friends should buy one flower. in this 
 * case you have to pay 13 dollars.
 * 
 * CONSTRAINTS
 * 1 <= N, K  <= 100
 * Each ci is not more than 1,000,000
 * ==
 *
 * This implementaton uses a simple greedy algorithm to find the optimal price 
 * for which a group of K patrons can purchase all N flowers. The intuition is 
 * that we want each person to get as few of the most expensive flowers as 
 * possible, as early as possible (the most expensive flowers would otherwise be 
 * most affected by the shop owner's draconian price-increase policy). Thus, 
 * given the N base prices for the N flowers, we sort them in descending order 
 * and then repeatedly cycle through the lineup of patrons, continuously 
 * distributing each successive flower until all flowers have been purchased.
 */

import java.util.Collections; // for 'nCopies', 'sort', and 'reverseOrder'
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Solution
{
  public static void main(String[] args)
  {
    /* Initialize a scanner for reading from standard input. */
    Scanner in = new Scanner(System.in);
    
    /* Read in the number of flowers to expect and the number of patrons. */
    int numFlowers = in.nextInt();
    int numPatrons = in.nextInt();
    
    /* Read in the prices for all N flowers. */
    List<Integer> flowers = 
      new ArrayList<Integer>(Collections.nCopies(numFlowers, 0));
    for (int i = 0; i < numFlowers; ++i)
      flowers.set(i, in.nextInt());
    
    /* Sort the flowers in order of descending cost in preparation for our 
     * greedy approach.
     */
    Collections.sort(flowers, Collections.reverseOrder());
    
    /* Because we're using a greedy approach and having the patrons buy flowers 
     * in a cyclic fashion, we only need a single variable to track how many 
     * flowers each patron has purchased (this will be incremented to 0 
     * momentarily).
     */
    int flowersPerPatron = -1;
    
    /* Now start distributing flowers amongst the patrons in a greedy fashion. 
     */
    int totalSpent = 0;
    for (int flower_i = 0; flower_i < numFlowers; ++flower_i)
    {
      /* Let the next patron in the lineup purchase this flower. */
      int patron_i = flower_i % numPatrons;
      
      /* If we've looped around to the first patron, then every patron in the 
       * lineup must have purchased an additional flower by now. Therefore, we 
       * increment our count of flowers purchased per patron.
       */
      if (patron_i == 0)
        ++flowersPerPatron;
      
      /* Calculate the price of the current flower according to the problem 
       * description, taking into account the flower's actual price as well as 
       * the number of flowers this patron has already purchased.
       */
      int flowerPrice = (flowersPerPatron + 1) * flowers.get(flower_i);
      
      /* Add the flower's adjusted price to the total. */
      totalSpent += flowerPrice;
    }
    
    System.out.println(totalSpent);
  }
}
