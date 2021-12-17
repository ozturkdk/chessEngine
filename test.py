from chess import *

board = [ ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
          ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
          ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'] ]

whiteToMove = True
newBoard = Board(board, whiteToMove)
newBoard.makeMove('b1', 'c3')

newBoard.whiteToMove = False
newBoard.makeMove('e7', 'e5')

newBoard.whiteToMove = True
newBoard.makeMove('a2', 'a4')

newBoard.whiteToMove = False
newBoard.makeMove('g7', 'g6')

newBoard.whiteToMove = True
newBoard.makeMove('a4', 'a5')

newBoard.whiteToMove = False
newBoard.makeMove('b7', 'b5')

newBoard.whiteToMove = True
newBoard.makeMove('a5', 'b6')

newBoard.whiteToMove = False
newBoard.makeMove('f8', 'g7')

newBoard.whiteToMove = True
newBoard.makeMove('b2', 'b3')

newBoard.whiteToMove = False
newBoard.makeMove('g8', 'h6')

newBoard.whiteToMove = True
newBoard.makeMove('c1', 'b2')

newBoard.whiteToMove = False
newBoard.makeMove('e8', 'g8')

newBoard.whiteToMove = True
newBoard.makeMove('d2', 'd4')

newBoard.whiteToMove = False
newBoard.makeMove('a7', 'a5')

newBoard.whiteToMove = True
newBoard.makeMove('d1', 'd2')

newBoard.whiteToMove = False
newBoard.makeMove('a5', 'a4')

newBoard.whiteToMove = True
newBoard.makeMove('e1', 'c1')

newBoard.whiteToMove = False
newBoard.makeMove('a4', 'b3')

newBoard.whiteToMove = True
newBoard.makeMove('c1', 'b1')

newBoard.whiteToMove = False
newBoard.makeMove('b8', 'a6')

newBoard.whiteToMove = True
newBoard.makeMove('b1', 'a1')

newBoard.whiteToMove = False
newBoard.makeMove('a6', 'b4')

newBoard.whiteToMove = True
newBoard.makeMove('e1', 'c1')