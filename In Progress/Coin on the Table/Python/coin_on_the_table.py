
from copy import deepcopy

class Game:
  
  DESTINATION = '*'
  MOVE_UP     = 'U'
  MOVE_DOWN   = 'D'
  MOVE_LEFT   = 'L'
  MOVE_RIGHT  = 'R'
  
  POSSIBLE_MOVES = [MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT]
  
  def __init__(self, N, M, k):
    self.board     = [[None] * M for i in xrange(N)]
    self.destCell  = None
    self.currCell  = [0, 0] # This needs to be a list so we can modify it.
    self.numRows   = N
    self.numCols   = M
    self.timeLimit = k
  
  def LoadBoard(self):
    # Setup the board row by row.
    for row in range(self.numRows):
      # Read in the initial characters for this row.
      rowChars = list(raw_input())
      
      # Setup each cell in this row.
      for col in range(self.numCols):
        self.board[row][col] = rowChars[col]
        
        # If we found the destination, remember where it is.
        if rowChars[col] == Game.DESTINATION:
          self.destCell = (row, col)
        
    
  
  def PrintBoard(self, otherBoard=None):
    # Use the board argument if one was provided.
    board = otherBoard if otherBoard else self.board
    
    horizontalBorder = '+' + ('-' * (2*self.numCols - 1)) + '+'
    
    print horizontalBorder
    
    # Print each row with a left and right border.
    for row in range(self.numRows):
      print '|' + ' '.join(map(str, board[row])) + '|'
    
    print horizontalBorder
    print ""
  
  def GetNecessaryOperations(self):
    return self._RecGetNecessaryOperations(0, 0, 0)
  
  def _RecGetNecessaryOperations(self, row, col, t):
    # tab = "  " * (t)
    
    # Base Case: If we're out of time, then we don't need to continue.
    if t > self.timeLimit:
      # print tab, (row, col), "OUT OF TIME!"
      return -1
    
    # Base Case: If we're at the destination, then no operations are necessary.
    if self._AtDestination(row, col):
      # print tab, (row, col), "AT DESTINATION!"
      return 0
    
    if not self._InBoard(row, col):
      # print tab, (row, col), "OFF BOARD!"
      return -1
    
    # Base Case: Return failure if we've already been to this cell.
    if self._CellIsMarked(row, col):
      # print tab, (row, col), "MARKED CELL!"
      return -1
    
    else:
      # Remember the character that was originally in this cell.
      originalChar = self.board[row][col]
      
      # print tab, (row, col), originalChar
      
      opsNeeded = [0, 0, 0, 0]
      
      for i in range(len(Game.POSSIBLE_MOVES)):
        char = Game.POSSIBLE_MOVES[i]
        
        # Change this cell to the current character and mark it to indicate that 
        # we've been here before.
        self._MarkCell(row, col, char)
        
        if char == Game.MOVE_UP:
          addlOpsNeeded = self._RecGetNecessaryOperations(row-1,col,t+1)
        elif char == Game.MOVE_DOWN:
          addlOpsNeeded = self._RecGetNecessaryOperations(row+1,col,t+1)
        elif char == Game.MOVE_LEFT:
          addlOpsNeeded = self._RecGetNecessaryOperations(row,col-1,t+1)
        elif char == Game.MOVE_RIGHT:
          addlOpsNeeded = self._RecGetNecessaryOperations(row,col+1,t+1)
        
        if addlOpsNeeded == -1:
          opsNeeded[i] = -1
        elif char == originalChar:
          opsNeeded[i] = 0 + addlOpsNeeded
        else:
          opsNeeded[i] = 1 + addlOpsNeeded
      
      # Reset the cell to its original state before we modified it.
      self.board[row][col] = originalChar
      
      validOpCounts = [count for count in opsNeeded if count >= 0]
      
      if len(validOpCounts) > 0:
        return min(validOpCounts)
      else:
        return -1
  
  def _InBoard(self, row, col):
    return (row >= 0 and row < self.numRows) and \
           (col >= 0 and col < self.numCols)
  
  def _AtDestination(self, row, col):
    return row == self.destCell[0] and col == self.destCell[1]
  
  def _MarkCell(self, row, col, char):
    # We use lowercase as our marking mechanism. If a character is uppercase, 
    # then we haven't been there in the traversal yet. 
    self.board[row][col] = char.lower()
  
  def _CellIsMarked(self, row, col):
    return self.board[row][col].islower()
  

def main():
  N, M, k = [int(n) for n in raw_input().split()]
  
  game = Game(N, M, k)
  game.LoadBoard()
   
  print game.GetNecessaryOperations()
  

if __name__ == "__main__":
  main()
