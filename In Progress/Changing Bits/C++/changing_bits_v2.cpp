
#include <bitset>
#include <climits> // for 'CHAR_BIT'
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Bitset
{
public:
  /* Constructor */
  Bitset(int numElements);
  Bitset(string binaryString);
  
  /* Bit accessors */
  int  get(int bitIndex);
  void set(int bitIndex);
  void flip(int bitIndex);
  void reset(int bitIndex);
  int operator [] (int bitIndex);
  
  /* Global modifiers */
  void setAll();
  void flipAll();
  void resetAll();
  
  /* Miscellaneous */
  int size();
  
private:
  typedef uint32_t word_t;
  const static int kWordSizeInBits = sizeof(word_t) * CHAR_BIT;
  
  int numElements;
  vector<word_t> data;
  
  int wordIndex(int bitIndex);
  int wordOffset(int bitIndex);
};

Bitset::Bitset(int numElements) :
  numElements(numElements), data(numElements / kWordSizeInBits + 1, 0)
{
}

Bitset::Bitset(string bitString) :
  numElements(bitString.length()), data(numElements / kWordSizeInBits + 1, 0)
{
  int bitset_i = 0;
  for (int string_i = bitString.length() - 1; string_i >= 0; --string_i)
  {
    if (bitString[string_i] == '1')
      set(bitset_i);
    
    ++bitset_i;
  }
}

int Bitset::wordIndex(int bitIndex)
{
  return bitIndex / kWordSizeInBits;
}

int Bitset::wordOffset(int bitIndex)
{
  return bitIndex % kWordSizeInBits;
}

int Bitset::get(int bitIndex)
{
  int offset = wordOffset(bitIndex);
  return (data[wordIndex(bitIndex)] & (1 << offset)) >> offset;
}

void Bitset::set(int bitIndex)
{
  data[wordIndex(bitIndex)] |= 1 << wordOffset(bitIndex);
}

void Bitset::flip(int bitIndex)
{
  data[wordIndex(bitIndex)] ^= 1 << wordOffset(bitIndex);
}

void Bitset::reset(int bitIndex)
{
  data[wordIndex(bitIndex)] &= ~(1 << wordOffset(bitIndex));
}

void Bitset::setAll()
{
  for (vector<uint32_t>::iterator itr = data.begin(); itr != data.end(); ++itr)
    *itr = -1;
}

void Bitset::flipAll()
{
  for (vector<uint32_t>::iterator itr = data.begin(); itr != data.end(); ++itr)
    *itr = ~(*itr);
}

void Bitset::resetAll()
{
  for (vector<uint32_t>::iterator itr = data.begin(); itr != data.end(); ++itr)
    *itr = 0;
}

int Bitset::size()
{
  return numElements;
}

int Bitset::operator [] (int bitIndex)
{
  return get(bitIndex);
}

/* ---------------------------------------------------------------------------*/

int GetBitOfSum(Bitset& A, Bitset& B, int idx)
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

void PrintBitset(Bitset& bitset, int numElements)
{ 
  for (int i = numElements-1; i >= 0; --i)
    cout << bitset[i];
  cout << endl;
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
  
  /* Initialize binary numbers A and B as bitsets with the specified length. 
   */
  Bitset A = Bitset(strA);
  Bitset B = Bitset(strB);
  
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
      
      if (operation == "set_a" && A[idx] != bitValue)
        A.flip(idx);
      
      else if (operation == "set_b" && B[idx] != bitValue)
        B.flip(idx);
    }
  }
  cout << endl;
  
  return 0;
}
