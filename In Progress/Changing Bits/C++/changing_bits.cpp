
#include <bitset>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<bool> BinaryStringToVector(const string& bitString)
{
  int numBits = bitString.length();
  
  /* Initialize a new bit vector of the required length. */
  vector<bool> bitVec(numBits);
  
  /* To ease the handling of indices later on, we read the bits into the vector 
   * so that they end up in reverse order, with the least significant bit at 
   * bitVec[0] and the most significant bit at bitVec[numBits - 1]. This is 
   * consistent with the indexing as described in the problem definition.
   */
  for (int i = 0; i < numBits; ++i)
    bitVec[numBits - i - 1] = (bitString[i] == '1') ? true : false;
  
  return bitVec;
}

void PrintBinaryVector(vector<bool>& bitVec)
{
  vector<bool>::reverse_iterator itr;
  
  /* Since our bits are stored in reverse order, we need to iterate through our 
   * bit vector backwards to ensure that the bits in the printed number are 
   * correctly ordered from most significant bit on the left to least 
   * significant bit on the right.
   */
  for (itr = bitVec.rbegin(); itr != bitVec.rend(); ++itr)
    cout << (*itr == true ? '1' : '0');
  cout << endl;
}

int GetBitOfSum(vector<bool>& A, vector<bool>& B, int idx)
{
  int numBits = A.size();
  bool isCarryingBit = false;
  
  /* Find the most-significant index below i where both bit arrays have a 0. */
  int startIndex = 0;
  for (int i = idx - 1; i >= 0; --i)
  {
    if ( !A[i] && !B[i] )
    {
      startIndex = i;
      break;
    }
  }
  
  for (int i = startIndex; i < idx; ++i)
  {
    if (isCarryingBit)
      isCarryingBit = ( A[i] || B[i] );
    else
      isCarryingBit = ( A[i] && B[i] );
  }
  
  if (isCarryingBit)
    return ( A[idx] == B[idx] ) ? 1 : 0;
  else
    return ( A[idx] != B[idx] ) ? 1 : 0;
}

int main()
{
  int numBits, numQueries;
  string strA, strB;
  
  /* Read in the number of bits and the number of queries to expect from the 
   * first line.
   */
  cin >> numBits >> numQueries;
  
  /* Read in binary numbers A and B as strings from the next two lines. */ 
  cin >> strA >> strB;
  
  /* Initialize binary numbers A and B as bit vectors with the specified length. 
   */
  vector<bool> A = BinaryStringToVector(strA);
  vector<bool> B = BinaryStringToVector(strB);
  
  string operation;
  int idx, bitValue;
  for (int i = 0; i < numQueries; ++i)
  {
    cin >> operation >> idx;
    
    if (operation == "get_c")
      cout << GetBitOfSum(A, B, idx);
    else
    {
      cin >> bitValue;
      
      if (operation == "set_a")
        A[idx] = (bitValue == 1) ? true : false;
      
      else if (operation == "set_b")
        B[idx] = (bitValue == 1) ? true : false;
    }
  }
  cout << endl;
  
  return 0;
}
