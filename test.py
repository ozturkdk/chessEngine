from chess import *

board = [ ['-', '-', '-', '-', '-', '-', '-', 'k'],
          ['-', '-', 'p', 'P', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['-', 'p', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', '-'],
          ['P', '-', '-', '-', '-', '-', '-', '-'],
          ['-', '-', '-', '-', '-', '-', '-', 'K'] ]


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
newBoard.makeMove('e2', 'e4')

whiteToMove = False
newBoard = Board(board, whiteToMove)
newBoard.makeMove('e7', 'e5')

whiteToMove = True
newBoard = Board(board, whiteToMove)
newBoard.makeMove('f1', 'c4')

whiteToMove = False
newBoard = Board(board, whiteToMove)
newBoard.makeMove('g8', 'f6')

whiteToMove = True
newBoard = Board(board, whiteToMove)
newBoard.makeMove('d1', 'h5')

whiteToMove = False
newBoard = Board(board, whiteToMove)
newBoard.makeMove('a7', 'a6')

whiteToMove = True
newBoard = Board(board, whiteToMove)
newBoard.makeMove('h5', 'f7')

whiteToMove = False
newBoard = Board(board, whiteToMove)
newBoard.makeMove('e8', 'f7')

