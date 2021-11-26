class Board():
    def __init__(self):
        self.board = [ ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                       ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                       ['-', '-', '-', '-', '-', '-', '-', '-'],
                       ['-', '-', '-', '-', '-', '-', '-', '-'],
                       ['-', '-', '-', '-', '-', '-', '-', '-'],
                       ['-', '-', '-', '-', '-', '-', '-', '-'],
                       ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                       ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'] ]

def updateBoard(board, fromSq, toSq):
    movedPiece = board[chessToArray(fromSq)[1]][chessToArray(fromSq)[0]]
    
    board[chessToArray(fromSq)[1]][chessToArray(fromSq)[0]] = '-'
    board[chessToArray(toSq)[1]][chessToArray(toSq)[0]] = movedPiece

def chessToArray(chessSq): 

    fileToArray = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7
    }

    rankToArray = {
        "8": 0,
        "7": 1,
        "6": 2,
        "5": 3,
        "4": 4,
        "3": 5,
        "2": 6,
        "1": 7
    }

    return fileToArray[chessSq[0]], rankToArray[chessSq[1]]