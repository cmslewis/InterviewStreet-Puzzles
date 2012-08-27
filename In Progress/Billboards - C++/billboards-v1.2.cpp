#include <algorithm>
#include <iostream>
#include <iterator>
#include <set>
#include <vector>
using namespace std;

typedef unsigned long long BigInteger;

void PrintVector(vector<BigInteger>& vec)
{
  copy(vec.begin(), vec.end(), ostream_iterator<BigInteger>(cout, " "));
  cout << endl;
}

void PrintHeap(multiset<BigInteger>& heap)
{
  copy(heap.begin(), heap.end(), ostream_iterator<BigInteger>(cout, " "));
  cout << endl;
}

BigInteger GetMaximumProfit(vector<int>& billboards, int maxClusterSize)
{
  /* Do the opposite: insert spaces no more than K positions apart, then 
   * minimize the sum of the values of billboards we have removed.
   */
  vector<BigInteger> dp = vector<BigInteger>(billboards.size() + 1);
  multiset<BigInteger> heap;
  
  BigInteger totalProfit = 0;
  
  int numBillboards = billboards.size();
  
  /* Add a dummy billboard at the end. */
  billboards.push_back(0);
  
  for (int i = 0; i <= numBillboards; ++i)
  {
    /* Extract the minimum element from the heap. */
    BigInteger minCost = (heap.size() > 0) ? *(heap.begin()) : 0;
    
    /* Keep track of the total value of all billboards. */
    totalProfit += billboards[i];
    
    /* Determine the optimal cost for this position. */
    dp[i] = minCost + billboards[i];
    
    cout << dp[i] << ", ";
    
    /* Ensure the heap as at most k elements at all times. */
    if (heap.size() > maxClusterSize)
      heap.erase(dp[i - maxClusterSize - 1]);
    
    PrintHeap(heap);
    
    /* Add this cost to the heap. */
    heap.insert(dp[i]);
  }
  cout << endl;
  
  return totalProfit - dp[numBillboards];
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
