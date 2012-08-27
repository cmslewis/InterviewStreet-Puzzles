#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>
using namespace std;

typedef unsigned long long BigInteger;

void PrintVector(vector<BigInteger>& vec)
{
  copy(vec.begin(), vec.end(), ostream_iterator<BigInteger>(cout, " "));
  cout << endl;
}

BigInteger GetMaximumProfit(vector<int>& billboards, int maxClusterSize)
{
  BigInteger prevMaxProfit = 0;
  
  /* While the DP algorithm calls for a table, we will only ever refer to the 
   * previous stage. Thus, we can just keep track of two columns: the previous 
   * stage and the current stage.
   */
  vector<BigInteger> stageColumn = vector<BigInteger>(maxClusterSize + 1);
  
  /* Initialize the values for the base case. */
  stageColumn[0] = 0;
  for (int i = 1; i <= maxClusterSize; ++i)
  {
    stageColumn[i] = billboards[0];
    
    /* Keep track of the maximum profit possible in this stage. */
    if (stageColumn[i] > prevMaxProfit)
      prevMaxProfit = stageColumn[i];
  }
  
  for (int i = 1; i < billboards.size(); ++i)
  {
    /* Cache the value of the current billboard fo efficiency. */
    int billboardValue = billboards[i];
    
    BigInteger prevMaxProfit = 0;
    for (int j = maxClusterSize; j >= 1; --j)
    {
      if (stageColumn[j] > prevMaxProfit)
        prevMaxProfit = stageColumn[j];
      
      stageColumn[j] = stageColumn[j-1] + billboardValue;
    }
    stageColumn[0] = prevMaxProfit;
  }
  
  return *max_element(stageColumn.begin(), stageColumn.end());
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
