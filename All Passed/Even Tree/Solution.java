/* File: Solution.java
 * Author: Chris Lewis (cmslewis@gmail.com)
 * -----------------------------------------------------------------------------
 * This program offers a solution to the "Even Tree" challenge on the 
 * InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
 * dashboard/#problem/4fffc24df25cd). Here is the problem description, verbatim:
 * 
 * ==
 * You are given a tree (a simple connected graph with no cycles).You have to 
 * remove as many edges from the tree as possible to obtain a forest with the 
 * condition that: Each connected component of the forest contains even number 
 * of vertices
 * 
 * Your task is to calculate the number of removed edges in such a forest.
 * 
 * INPUT:
 * The first line of input contains two integers N and M. N is the number of 
 * vertices and M is the number of edges. 2 <= N <= 100. 
 * Next M lines contains two integers ui and vi which specifies an edge of the 
 * tree. (1-based index)
 * 
 * OUTPUT:
 * Print a single integer which is the answer
 * 
 * SAMPLE INPUT:
 * 10 9
 * 2 1
 * 3 1
 * 4 3
 * 5 2
 * 6 1
 * 7 2
 * 8 6
 * 9 8
 * 10 8
 * 
 * SAMPLE OUTPUT:
 * 2
 * 
 * EXPLANATION:
 * On removing the edges (1, 3) and (1, 6), we can get the desired  * result.
 * 
 * ORIGINAL TREE: 
 *       1
 *     / | \
 *    2  3  6
 *   /|  |  |
 *  7 5  4  8
 *          |\
 *          9 10
 * 
 * DECOMPOSED TREE:
 *       1
 *     /    
 *    2  3  6
 *   /|  |  |
 *  7 5  4  8
 *          |\
 *          9 10
 * 
 * Note: The tree in the input will be such that it can always be decomposed 
 * into components containing even number of nodes.
 * == 
 * 
 * This implementation uses two rounds of BFS to solve the problem: one to 
 * determine the size of all subtrees in the graph and another to count the 
 * number of edges we can remove by locating all nodes that serve as the root 
 * node of an even subgraph (that is, a subgraph with an even number of nodes). 
 * Thus, the runtime of the algorithm is just the runtime of BFS, which is 
 * O(n) for a tree, where n is the number of nodes.
 */

import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Stack;
import java.util.Scanner;

public class Solution
{
  /* Method: GetSubtreeSizes(edges)
   * Usage: Map<Integer, Integer> subtreeSizes = new HashMap<Integer,Integer>();
   *        getSubtreeSizes(edges, subtreeSizes);
   * ---------------------------------------------------------------------------
   * Returns a Python dict that maps each nodeID to the size of the subtree 
   * rooted at that node.
   */
  private static void getSubtreeSizes(Map<Integer, List<Integer>> edges,
    Map<Integer, Integer> subtreeSizes)
  {
    recGetSubtreeSizes(1, edges, subtreeSizes);
  }
  
  /* Method: RecGetSubtreeSizes(nodeID, edges, subtreeSizes)
   * Usage: RecGetSubtreeSizes(1, edges, subtreeSizes);
   * ---------------------------------------------------------------------------
   * A helper function for GetSubtreeSizes(). Recursively explores the tree 
   * with the specified edges, starting at the node with the provided nodeID. 
   * Ultimately, this function will update the provided subtreeSizes dict with 
   * the size of the subtree beginning at each node in the tree.
   */
  private static void recGetSubtreeSizes(int nodeID,
    Map<Integer, List<Integer>> edges, Map<Integer, Integer> subtreeSizes)
  {
    if ( !edges.containsKey(nodeID) )
      subtreeSizes.put( nodeID, 1 );
    
    else
    {
      int subtreeSize = 0;
      
      /* Compute the size of the subtree beginning at each child node. */
      List<Integer> childNodes = edges.get(nodeID);
      for (int i = 0; i < childNodes.size(); ++i)
      {
        int childID = childNodes.get( i );
        recGetSubtreeSizes(childID, edges, subtreeSizes);
        subtreeSize += subtreeSizes.get( childID );
      }
      
      /* Update the size of the subtree beginning at the current node (adding 1 
       * to account for the current node).
       */
      subtreeSizes.put(nodeID, 1 + subtreeSize);
    }
  }
  
  /* Method: NumEdgesRemoved(edges, subtreeSizes)
   * Usage: int numRemoved = numEdgesRemoved(edges, subtreeSizes);
   * ---------------------------------------------------------------------------
   * Returns the maximum number of edges that can be removed from the tree with 
   * the specified edges, such that the resultant forest consists only of trees 
   * that each have an even number of nodes.
   */
  private static int numEdgesRemoved(Map<Integer, List<Integer>> edges,
     Map<Integer, Integer> subtreeSizes)
  {
    int numRemoved = 0;
    
    /* Perform an iterative BFS starting at the root node. */
    Stack<Integer> nodeStack = new Stack<Integer>();
    
    nodeStack.push( 1 );
    while (!nodeStack.isEmpty())
    {
      /* Pop off the top element from the stack. */
      int nodeID = nodeStack.pop();
      
      /* Base Case: Leaf node. */
      if (!edges.containsKey(nodeID))
        continue;
      
      else
      {
        /* Count the number of edges we can remove from the subtree beginning at 
         * each child node.
         */
        List<Integer> childNodes = edges.get(nodeID);
        for (int i = 0; i < childNodes.size(); ++i)
        {
          int childID = childNodes.get( i );
          
          /* Remove the edge between the current root node and the current child 
           * node the resultant subtree will have an even number of nodes in it.
           */
          if (subtreeSizes.get(childID) % 2 == 0)
            numRemoved += 1;
          
          nodeStack.push( childID );
        }
      }
    }
    
    return numRemoved;
  }
  
  public static void main(String[] args)
  {
    /* Initialize a scanner for reading from standard input. */
    Scanner in = new Scanner(System.in);
    
    /* Read in the number of nodes and edges to expect. */
    int numNodes = in.nextInt();
    int numEdges = in.nextInt();
    
    Map<Integer, List<Integer>> edges = new HashMap<Integer, List<Integer>>();
    
    for (int i = 0; i < numEdges; ++i)
    {
      /* Read in the two end nodes that the next edge connects. */
      int  nodeID = in.nextInt();
      int childID = in.nextInt();
      
      /* Swap the nodeID and the childID to ensure we build the tree such that 
       * the ID of each node is less than that of each of its children. 
       */
      if (nodeID > childID)
      {
        int temp = nodeID; nodeID = childID; childID = temp;
      }
      
      if ( !edges.containsKey(nodeID) )
        edges.put( nodeID, new ArrayList<Integer>() );
      
      /* Keep track of this edge in a data structure. */
      edges.get( nodeID ).add( childID );
    }
    
    /* Compute the size of the subtree starting at each node. */
    Map<Integer, Integer> subtreeSizes = new HashMap<Integer, Integer>();
    getSubtreeSizes(edges, subtreeSizes);
    
    /* Report the maximum number of edges we can remove, and still leave a 
     * forest in which each tree has an even number of nodes.
     */
    System.out.println( numEdgesRemoved(edges, subtreeSizes) );
  }
}
