
import sys

def GetBit(bitArray, i):
  return bitArray[len(bitArray) - i - 1]

def SetBit(bitArray, i, bit):
  if (0 <= bit and bit <= 1) and (0 <= i and i < len(bitArray)):
    bitArray[len(bitArray) - i - 1] = bit

def GetBitOfSum(A, B, i):
  
  isCarryingBit = False
  
  # Find the most-significant index below i where both bit arrays have a 0.
  startIndex = len(A) - 1
  for j in range(len(A) - i, len(A) - 1):
    if A[j] == 0 and B[j] == 0:
      startIndex = j
      break
  
  # print "  startIndex =", startIndex, ", range: ", range(startIndex, -1, -1),
  
  endIndex = max(-1, len(A) - i - 1)
  # print "  endIndex =", endIndex
  
  for j in range(startIndex, endIndex, -1):
    # print "  idx =", j, 
    if isCarryingBit:
      # print "   isCarryingBit", 
      if A[j] == 0 and B[j] == 0:
        # print "  A[j] == B[j] == 0", "--> notCarryingBit"
        isCarryingBit = False
      else:
        # print "  A[j] == 1 and/or B[j] == 1", "--> isCarryingBit"
        isCarryingBit = True
    else:
      # print "  notCarryingBit",
      if A[j] == 1 and B[j] == 1:
        # print "  A[j] == B[j] == 1", "--> isCarryingBit"
        isCarryingBit = True
      else:
        isCarryingBit = False
        # print "  A[j] == 0 and/or B[j] == 0", "--> notCarryingBit"
    
  if isCarryingBit and GetBit(A, i) == 1 and GetBit(B, i) == 1:
    return 1
  if isCarryingBit and GetBit(A, i) == 0 and GetBit(B, i) == 0:
    return 1
  if isCarryingBit and (GetBit(A, i) == 1 or GetBit(B, i) == 1):
    return 0
  if GetBit(A, i) == 1 and GetBit(B, i) == 0:
    return 1
  if GetBit(A, i) == 0 and GetBit(B, i) == 1:
    return 1
    
  return 0

def main():
  numBits, numQueries = [int(n) for n in raw_input().split()]
  
  A = [int(bit) for bit in list(raw_input())]
  B = [int(bit) for bit in list(raw_input())]
  
  for i in range(numQueries):
    tokens = raw_input().split()
    
    operation = tokens[0]
    idx       = int(tokens[1])
    if len(tokens) > 2:
      bit = int(tokens[2])
    
    if operation == 'set_a':
      SetBit(A, idx, bit)
    elif operation == 'set_b':
      SetBit(B, idx, bit)
    elif operation == 'get_c':
      sys.stdout.write(str(GetBitOfSum(A, B, idx)))
      
  print
  # print "A:", A, ", B:", B
  

if __name__ == "__main__":
  main()
