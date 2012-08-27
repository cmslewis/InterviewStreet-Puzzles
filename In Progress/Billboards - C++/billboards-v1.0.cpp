
#include <iostream>
#include <iterator>
#include <vector>
using namespace std;

typedef unsigned long long BigInteger;

BigInteger GetMaximumProfit(vector<int>& billboards, int maxClusterSize)
{
  BigInteger maxProfit = 0;
  
  /* While the DP algorithm calls for a table, we will only ever refer to the 
   * previous stage. Thus, we can just keep track of two columns: the previous 
   * stage and the current stage.
   */
  vector<BigInteger> prevStage = vector<BigInteger>(maxClusterSize + 1);
  vector<BigInteger> currStage = vector<BigInteger>(maxClusterSize + 1);
  
  /* Initialize the values for the base case. */
  prevStage[0] = 0;
  for (int i = 1; i <= maxClusterSize; ++i)
  {
    prevStage[i] = billboards[0];
    
    /* Keep track of the maximum profit possible in this stage. */
    if (prevStage[i] > maxProfit)
      maxProfit = prevStage[i];
  }
  
  for (int i = 1; i < billboards.size(); ++i)
  {
    /* Cache the value of the current billboard fo efficiency. */
    int billboardValue = billboards[i];
    
    /* If we don't include this billboard in the optimal sequence, then the 
     * value of this decision will be the maximum profit so far.
     */
    currStage[0] = maxProfit;
    
    maxProfit = 0;
    for (int j = 1; j <= maxClusterSize; ++j)
    {
      currStage[j] = prevStage[j-1] + billboardValue;
      
      /* Keep track of the maximum profit possible in this stage. */
      if (currStage[j] > maxProfit)
        maxProfit = currStage[j];
    }
    
    /* Transfer the current stage values to the previous stage vector (this is 
     * done in constant time).
     */
    prevStage.swap(currStage);
  }
  
  return maxProfit;
}

int main()
{
  int numBillboards, maxClusterSize;
  
  /* Read in the number of billboards (N) to expect, as well as the maximum 
   * cluster size (K) allowed in our optimal solution.
   */
  cin >> numBillboards >> maxClusterSize;
  
  /* Read the value of each billboard into a vector. */
  vector<int> billboards = vector<int>(numBillboards);
  for (int i = 0; i < numBillboards; ++i)
    cin >> billboards[i];
  
  cout << GetMaximumProfit(billboards, maxClusterSize) << endl;
  
  return 0;
}