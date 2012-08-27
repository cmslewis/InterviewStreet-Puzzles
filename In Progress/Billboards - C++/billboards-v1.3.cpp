#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <vector>
using namespace std;

typedef unsigned long long BigInteger;

template <typename T>
void PrintVector(vector<T>& vec)
{
  copy(vec.begin(), vec.end(), ostream_iterator<T>(cout, " "));
  cout << endl;
}

BigInteger RangeTotal(vector<int>& billboards, int rangeBegin, int rangeEnd)
{
  BigInteger sum = 0;
  
  for (int i = rangeBegin; i <= rangeEnd && i < billboards.size(); ++i)
    sum += billboards[i];
  
  return sum;
}

int GetBillboardValue(vector<int>& billboards, int index)
{
  if (index > billboards.size())
    return 0;
  
  return billboards[index];
}

BigInteger GetMaximumProfit(vector<int>& billboards, int maxClusterSize)
{
  vector<BigInteger> currStage(maxClusterSize + 1, 0);
  vector<BigInteger> prevStage(maxClusterSize + 1, 0);
  vector<int> bestIndices(maxClusterSize + 1, 0);
  
  /* Don't count the dummy billboard at the beginning of the vector. */
  int numBillboards = billboards.size() - 1;
  
  for (int blockStart = 0, blockEnd = maxClusterSize + 1;
       blockStart < numBillboards;
       blockStart = blockEnd, blockEnd += maxClusterSize + 1)
  {
    /* Get the sum of all billboards in the current block. */
    BigInteger blockSum = RangeTotal(billboards, blockStart + 1, blockEnd);
    
    /* Get the index of the last billboard in the block sum. */
    int iBoard = blockEnd;
    
    /* The best index is initially K, since all others are initially 0.*/
    bestIndices[maxClusterSize] = maxClusterSize;
    
    /* Add the sum of all billboards in the current block (except the last 
     * billboard) to the previous maximum profit.
     */
    currStage[maxClusterSize] = prevStage[maxClusterSize] +
                            (blockSum - GetBillboardValue(billboards, iBoard));
    
    /* Move backward in the current block, one billboard at a time. */
    for (int i = maxClusterSize - 1; i >= 0; --i)
    {
      /* Find the index of the previous billboard. */
      iBoard = blockStart + i + 1;
      
      /* Find the total profit of this block with the current billboard removed. 
       */
      BigInteger localSum = blockSum - GetBillboardValue(billboards, iBoard);
      
      /* If the profit after removing the current billboard is higher than the 
       * profit after removing any other billboard in this block, reset the 
       * localBestIndex to the current index.
       */
      int localBestIndex = bestIndices[i + 1];
      if (prevStage[i] > prevStage[localBestIndex])
        localBestIndex = i;
      
      /* Remember the total profit after removing this billboard. */
      currStage[i] = prevStage[localBestIndex] + localSum;
      
      /* Remember the best index for this position in the block. */
      bestIndices[i] = localBestIndex;
    }
    
    /* Move to the next stage. */
    currStage.swap(prevStage);
  }
  
  /* Return the maximum possible profit. */
  return *max_element(prevStage.begin(), prevStage.end());
}

int main()
{
  int numBillboards, maxClusterSize;
  
  /* Read in the number of billboards (N) to expect, as well as the maximum 
   * cluster size (K) allowed in our optimal solution.
   */
  cin >> numBillboards >> maxClusterSize;
  
  /* Read the value of each billboard into a vector. */
  vector<int> billboards;
  billboards.push_back(0);
  for (int i = 1; i <= numBillboards; ++i)
  { 
    int value; 
    cin >> value;
    
    if (value > 0)
      billboards.push_back(value);
  }
  
  PrintVector(billboards);
  
  cout << GetMaximumProfit(billboards, maxClusterSize) << endl;
  
  return 0;
}
