from chess import *

board = [ ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
          ['p', 'p', 'p', '-', 'p', 'p', 'p', 'p'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', 'R', '-', '-', '-', '-', '-'],
          ['-', '-', '-', 'p', '-', '-', '-', '-'],
          ['P', 'P', 'P', '-', '-', 'P', 'P', 'P'],
          ['-', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'] ]

board = [ ['-', '-', '-', '-', 'k', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['R', '-', '-', '-', 'K', '-', '-', 'R'] ]

whiteToMove = True
newBoard = Board(board, whiteToMove)
newBoard.makeMove('e1', 'g1')

newBoard.whiteToMove = False
newBoard.makeMove('e8', 'e7')

newBoard.whiteToMove = True
newBoard.makeMove('a1', 'a2')

