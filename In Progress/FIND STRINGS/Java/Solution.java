
import java.util.ArrayList;
import java.util.List;
import java.util.Collections; // for 'nCopies'
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

class Solution
{
  public static void main(String[] args)
  {
    /* Initialize a scanner for reading from standard input. */
    Scanner in = new Scanner(System.in);
    
    /* Read in the number of strings to expect from standard input. */
    int numStrings = in.nextInt();
    
    /* Read in each string, and add all substrings to a single, cumulative set. 
     */
    Set<String> substrings = new TreeSet<String>();
    for (int i = 0; i < numStrings; ++i)
    {
      String s = in.next();
      
      for (int beginIndex = 0; beginIndex < s.length(); ++beginIndex)
        for (int endIndex = beginIndex; endIndex < s.length(); ++endIndex)
          substrings.add( s.substring(beginIndex, endIndex+1) );
    }
    
    // System.out.println("\nSUBSTRINGS FOUND:");
    // for (String substr : substrings)
    //   System.out.println( substr );
    // System.out.println();
    
    /* Read in the number of queries to expect from standard input. */
    int numQueries = in.nextInt();
    
    /* Read all queries into an ArrayList for later processing. */
    List<Integer> queries =
      new ArrayList<Integer>(Collections.nCopies(numQueries, 0));
    for (int i = 0; i < numQueries; ++i)
      queries.set(i, in.nextInt() );
    
    /* Sort the queries into ascending order for faster processing. */
    Collections.sort(queries);
    
    // System.out.println("\nSORTED QUERIES:");
    // for (Integer q : queries)
    //   System.out.println( q );
    // System.out.println();
    
    /* Iterate through each substring, printing it out if O(n)
    for (String substr : substrings)
    {
      
    }
    
  }
}