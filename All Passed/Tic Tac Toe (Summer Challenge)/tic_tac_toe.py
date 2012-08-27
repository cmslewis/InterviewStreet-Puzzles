# File: tic_tac_toe.py
# Author: Chris Lewis (cmslewis@gmail.com)
# -----------------------------------------------------------------------------
# This program offers a solution to the "Tic Tac Toe" Summer Games challenge on 
# the InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
# dashboard/#problem/4edb8abd7cacd). Here is the problem description, verbatim:
#
# Tic-tac-toe, also called wick wack woe (in some Asian countries) and noughts 
# and crosses (in the British Commonwealth countries) and X's and O's in the 
# Republic of Ireland, is a pencil-and-paper game for two players, X and O, who 
# take turns marking the spaces in a 3x3 grid.
# 
# The X player usually goes first. The player who succeeds in placing three 
# respective marks in a horizontal, vertical, or diagonal row wins the game.
# 
# The following example game is won by the first player, X:
#
# _ _ X   O _ X   O _ X   O _ X   O _ X   O _ X
# _ _ _   _ _ _   _ _ _   _ O _   _ O O   _ O O
# _ _ _   _ _ _   X _ _   X _ X   X _ X   X=X=X  (<- X wins)  
# 
# In this game, you will be given the board state as input. You are expected to 
# make the next move of the tic tac toe.
# 
# INPUT FORMAT: 
# The first line in the input will be an integer. 1 or 2.
# If the first line is 1, then you are the first player and all 1's on the board 
# belong to you.
# If the first line is 2, then you are the second player and all 2's on the 
# board belong to you.
# 
# The following 3 lines defines the board state. Each line containts 3 inetgers. 
# The characters can be either (1, 2, or -1) 1 means the box position is 
# occupied by the first player. 2 means the box position is occupied by the 
# second player. -1 means the box is not yet occupied.
# 
# Output format: 2 integers( row column ) separated by a single space, which 
# specifies the position of the board you want to make your move. ( 0 indexed )
# 
# INPUT 00:
# 1
# -1 -1 -1
# -1 -1 -1
# -1 1 2
# 
# OUTPUT 00: 
# 0 0 
# 
# EXPLANATION 00:
# The board results in the following state after the above move 
# 1 -1 -1 
# -1 -1 -1
# -1 1 2

# The number of squares along each edge of the board
BOARD_SIZE = 3

# Enumerations of each row and column index, for readability. For example, given 
# a 2D array called "board" of size BOARD_SIZE * BOARD_SIZE, you could access 
# the top left cell with "board[TOP][LEFT]".
TOP    = 0  # Top row
LEFT   = 0  # Left column
CENTER = 1  # Center row or center column
RIGHT  = 2  # Right Column
BOTTOM = 2  # Bottom row

# Enumerations for each of the two diagonals on the board. These cannot be used 
# as indexes, but instead are intended as identifiers to be passed into the 
# GetDiagonal() function.
DOWNWARD_DIAGONAL = 0
UPWARD_DIAGONAL   = 1

# Enumerations of the numerals that correspond to empty or player-owned squares.
# These values in particular are specified in the problem definition at the 
# beginning of this file.
EMPTY    = -1  # An empty square
PLAYER_1 = 1   # A square belonging to player 1
PLAYER_2 = 2   # A square belonging to player 2

# Function: CreateBoard( player )
# Usage: board = CreateBoard(player)
# ------------------------------------------------------------------------------
# Returns a 2D array of empty squares, with size BOARD_SIZE x BOARD_SIZE. To 
# access any cell, use the enumerated row and column indices. For instace, to 
# access the top-left cell, use board[TOP][LEFT].
def CreateBoard():
  # Return an N x N array of empty squares.
  return [[EMPTY] * BOARD_SIZE for x in xrange(BOARD_SIZE)]


# Function: GetOpponent( player )
# Usage: opponent = GetOpponent( PLAYER_1 ) // Returns PLAYER_2
# ------------------------------------------------------------------------------
# Returns the enumerated value corresponding to the provided player's opponent.
# For instance, passing PLAYER_1 to the function will return PLAYER_2, and vice 
# versa.
def GetOpponent( player ):
  return PLAYER_2 if player == PLAYER_1 else PLAYER_1


# Function: GetRow( board, whichRow )
# Usage: row = GetRow(board, TOP)
# ------------------------------------------------------------------------------
# Returns a list of length BOARD_SIZE containing the values in the provided row 
# of the board. The first element corresponds to the value in the leftmost 
# square of the row, the second to the value in the center square, and the third 
# to the value in the rightmost square.The whichRow parameter should be TOP for 
# the top row, CENTER for the center row, or BOTTOM for the bottom row.
def GetRow( board, whichRow ):
  return board[whichRow]


# Function: GetColumn( board, whichCol )
# Usage: col = GetColumn(board, LEFT)
# ------------------------------------------------------------------------------
# Returns a list of length BOARD_SIZE containing the values in the provided 
# column of the board. The first element corresponds to the value in the topmost 
# square of the column, the second to the value in the center square, and the 
# third to the value in the bottom square. The whichCol parameter should be LEFT 
# for the left column, CENTER for the center column, or RIGHT for the right 
# column.
def GetColumn( board, whichCol ):
  return [board[TOP][whichCol],
          board[CENTER][whichCol],
          board[BOTTOM][whichCol]]


# Function: GetDiagonal( board, whichDiag )
# Usage: diag = GetGetDiagonal(board, DOWNWARD_DIAGONAL)
# ------------------------------------------------------------------------------
# Returns a list of length BOARD_SIZE containing the values in the provided 
# diagonal of the board. The first element corresponds to the value in the 
# leftmost square of the diagonal (either top-left or bottom-left), the second 
# to the value in the center square, and the third to the value in the rightmost 
# square (either top-right or bottom-right). The whichDiag parameter should be 
# DOWNWARD_DIAG for the diagonal that starts in the top-left square and extends 
# to the bottom-right cell, or UPWARD_DIAGONAL for the other diagonal.
def GetDiagonal( board, whichDiag ):
  if whichDiag == DOWNWARD_DIAGONAL:
    return [board[TOP][LEFT], board[CENTER][CENTER], board[BOTTOM][RIGHT]]
  else:
    return [board[BOTTOM][LEFT], board[CENTER][CENTER], board[TOP][RIGHT]]


# Function: SquareIsEmpty( board, whichRow, whichCol )
# Usage: if SquareIsEmpty(board, TOP, LEFT): ...
# ------------------------------------------------------------------------------
# Returns true if and only if the specified square in the board is empty, as 
# opposed to having either player's value (i.e. PLAYER_1 or PLAYER_2) in it.
def SquareIsEmpty( board, whichRow, whichCol ):
  return board[whichRow][whichCol] == EMPTY


# Function: BoardIsEmpty( board )
# Usage: if BoardIsEmpty(board): ...
# ------------------------------------------------------------------------------
# Returns true if and only if every single square in the provided board is 
# empty.
def BoardIsEmpty( board ):
  for row in board:
    if row.count(EMPTY) != BOARD_SIZE: return False
  return True


# Function: PlayerHasSquare( board, whichRow, whichCol, player )
# Usage: if PlayerHasSquare(board, TOP, LEFT, PLAYER_1): ...
# ------------------------------------------------------------------------------
# Returns true if and only if the specified player has played in the provided 
# square.
def PlayerHasSquare( board, whichRow, whichCol, player ):
  return board[whichRow][whichCol] == player


# Function: NumEmptySquares( board )
# Usage: numEmpty = NumEmptySquares(board)
# ------------------------------------------------------------------------------
# Returns the number of empty squares remaining on the provided board.
def NumEmptySquares( board ):
  return sum([row.count(EMPTY) for row in board])


# Function: CreateMove( whichRow, whichCol )
# Usage: move = CreateMove(TOP, LEFT)
# ------------------------------------------------------------------------------
# A simple helper function that returns a 2-tuple of the form (whichRow, 
# whichCol), representing a single possible move.
def CreateMove( whichRow, whichCol ):
  return (whichRow, whichCol)


# Function: FindWinningMoves( boar, player )
# Usage: moves = FindWinningMoves(board, player)
# ------------------------------------------------------------------------------
# Returns a list of all possible squares that would result in an immediate 
# victory for the specified player if he or she were to move there. Each move is 
# represented as a 2-tuple containing one row index and one column index, in 
# that order.
def FindWinningMoves( board, player ):
  # Keep track of all possible winning moves.
  moves = []
  
  # Check for a winning move in each row.
  for whichRow in [TOP, CENTER, BOTTOM]:
    row = GetRow( board, whichRow )
    if row.count(player) == 2 and row.count(EMPTY) == 1:
      moves.append( CreateMove(whichRow, row.index(EMPTY)) )
  
  # Check for a winning move in each column.
  for whichCol in [LEFT, CENTER, RIGHT]:
    col = GetColumn(board, whichCol)
    if col.count(player) == 2 and col.count(EMPTY) == 1:
      moves.append( CreateMove(col.index(EMPTY), whichCol) )
  
  # Check for a winning move in each diagonal.
  for whichDiag in [DOWNWARD_DIAGONAL, UPWARD_DIAGONAL]:
    diag = GetDiagonal(board, whichDiag)
    
    if diag.count(player) == 2 and diag.count(EMPTY) == 1:
      
      if whichDiag == DOWNWARD_DIAGONAL:
        index = diag.index(EMPTY)
        moves.append( CreateMove(index, index) )
      
      elif whichDiag == UPWARD_DIAGONAL:
        index = diag.index(EMPTY)
        moves.append( CreateMove(BOARD_SIZE - index - 1, index) )
  
  # If we haven't found a winning move yet, return none. 
  return None if moves is None or len(moves) == 0 else moves


# Function: FindForkingMoves( boar, player, defensiveMode=False )
# Usage: moves = FindForkingMoves(board, player, True)
# ------------------------------------------------------------------------------
# Returns a list of all possible squares that would create two possible victory  
# conditions in the specified player's very next turn if he or she were to move 
# there. Each move is represented as a 2-tuple containing one row index and one 
# column index, in that order.
# 
# The defensiveMode parameter should be set to True if the specified player is 
# actually the opponent of the player whose turn it is. In this case, instead of 
# returning the exact square(s) where the opponent could move to create a fork, 
# the function will adjust its move suggestions to avoid certain special cases 
# where the opponent could counterattack with yet another forking move on the 
# next turn. For example, in the following board configuration:
# 
# X _ _
# _ O _
# _ _ X
#
# X can create a forking move by going in either remaining corner. O could 
# thus defend against one of the opponent's forking moves by playing in 
# either corner, as follows:
# 
# X _ O
# _ O _
# _ _ X
# 
# However, this still leaves X with the ability to create another fork by 
# playing in the other corner:
# 
# X _ O
# _ O _
# X _ X
# 
# If O had played in any side square instead, he could have prevented 
# this. This is exactly the special case that this function will defend against 
# if defensiveMode is set to True.
def FindForkingMoves( board, player, defensiveMode=False ):
  moves = []
  
  # Handle two special cases.
  if defensiveMode and NumEmptySquares( board ) == 6:
    # Since we're in defensive mode, "player" should refer to the opponent.
    # We therefore need to switch the player and opponent references to view the 
    # board from defensive player's perspective for these two checks.  
    opponent = player
    player   = GetOpponent( player )
    
    # These checks essentially ensure that, given a board in either of the 
    # following configurations:
    #
    # 1 0 0      0 0 1
    # 0 2 0  or  0 2 0
    # 0 0 1      1 0 0
    #
    # The function will avoid the possibility of a double-fork counterattack by 
    # suggesting a move in an arbitrary side square.
    if board[TOP][LEFT]      == opponent and \
       board[CENTER][CENTER] == player   and \
       board[BOTTOM][RIGHT]  == opponent:
      return [ CreateMove(TOP, CENTER) ]
    
    if board[TOP][RIGHT]     == opponent and \
       board[CENTER][CENTER] == player   and \
       board[BOTTOM][LEFT]   == opponent:
      return [ CreateMove(TOP, CENTER) ]
    
    # Reset the original player reference.
    player = opponent
  
  # Try creating a fork with one move.
  for row in [TOP, CENTER, BOTTOM]:
    for col in [LEFT, CENTER, RIGHT]:
      if board[row][col] == EMPTY:
        
        # Temporarily make a move in that square (SQUARE A)
        board[row][col] = player
        
        # Count the number of ways the current player can win.
        tempMoves = FindWinningMoves( board, player )
              
        # If there are two ways to win:
        if tempMoves is not None and len(tempMoves) >= 2:
          board[row][col] = EMPTY
          moves.append( CreateMove(row, col) )
        
        # Undo the first of our two temporary moves.
        board[row][col] = EMPTY
  
  # Return all possible forking moves, or None if no such moves were found.
  return None if moves is None or len(moves) == 0 else moves


# Function: FindBestMove( boar, player )
# Usage: moves = FindBestMove(board, player)
# ------------------------------------------------------------------------------
# This function is the only one that the client should have to call to solve the 
# problem as defined at the beginning of this file. It uses Wikipedia's optimal 
# Tic-Tac-Toe strategy, which proritizes various moves based on the current 
# state of the provided board. The player parameter should correspond to the 
# enumerated value of the player whose turn it is (i.e. PLAYER_1 or PLAYER_2)
def FindBestMove( board, player ):  
  opponent = GetOpponent( player )
  
  # a. Play Center on Empty Board
  if BoardIsEmpty( board ): return [CENTER, CENTER]
  
  # b. If the player has two in a row, play the third to get three in a row.
  moves = FindWinningMoves(board, player)
  if moves: return moves[0]
  
  # c. If the opponent has two in a row, play the third to block them.
  moves = FindWinningMoves(board, opponent)
  if moves: return moves[0]
  
  # d. Create an opportunity where you can win in two ways.
  moves = FindForkingMoves(board, player)
  if moves: return moves[0]
  
  # e. Block an opponent's fork.
  moves = FindForkingMoves(board, opponent, defensiveMode=True)
  if moves: return moves[0]
  
  # f. Play the center.
  if SquareIsEmpty(board, CENTER, CENTER): return [CENTER, CENTER]
  
  # g. If the opponent is in the corner, play the opposite corner.
  if PlayerHasSquare(board, TOP, LEFT, opponent) \
     and SquareIsEmpty(board, BOTTOM, RIGHT): return [BOTTOM, RIGHT]
     
  if PlayerHasSquare(board, TOP, RIGHT, opponent) \
     and SquareIsEmpty(board, BOTTOM, LEFT): return [BOTTOM, LEFT]
     
  if PlayerHasSquare(board, BOTTOM,  LEFT, opponent) \
     and SquareIsEmpty(board, TOP, RIGHT): return [TOP, RIGHT]
     
  if PlayerHasSquare(board, BOTTOM, RIGHT, opponent) \
     and SquareIsEmpty(board, TOP, LEFT): return [TOP, LEFT]
  
  # h. Play in a corner square.
  if SquareIsEmpty(board,    TOP,  LEFT): return [TOP, LEFT]
  if SquareIsEmpty(board,    TOP, RIGHT): return [TOP, RIGHT]
  if SquareIsEmpty(board, BOTTOM,  LEFT): return [BOTTOM, LEFT]
  if SquareIsEmpty(board, BOTTOM, RIGHT): return [BOTTOM, RIGHT]
  
  # i. Play in a middle square on any of the 4 sides.
  if SquareIsEmpty(board,    TOP, CENTER): return [TOP, CENTER]
  if SquareIsEmpty(board, BOTTOM, CENTER): return [BOTTOM, CENTER]
  if SquareIsEmpty(board, CENTER,   LEFT): return [CENTER, LEFT]
  if SquareIsEmpty(board, CENTER,  RIGHT): return [CENTER, RIGHT]
  
  # j. If the execution reaches this point, then there are no squares remaining.
  return None


def main():
  # Read in correctly formatted input as described in the problem definition at 
  # the beginning of this file.
  player = int(raw_input())
  board  = CreateBoard()
  
  for i in range(BOARD_SIZE):
    row = raw_input()
    j = 0
    for square in row.split():
      board[i][j] = int(square)
      j = j+1
  
  # Print out the row and column corresponding to the best move for the 
  # specified player on the provided board.
  move = FindBestMove( board, player )
  print move[0], move[1]


if __name__ == "__main__":
  main()
