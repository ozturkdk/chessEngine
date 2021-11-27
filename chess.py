class Board():
    def __init__(self):
        #self.board = [ ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        #               ['p', 'p', 'p', '-', 'p', 'p', 'p', 'p'],
        #               ['-', '-', '-', '-', '-', '-', '-', '-'],
        #               ['-', '-', '-', '-', '-', '-', '-', '-'],
        #               ['-', '-', 'R', '-', '-', '-', '-', '-'],
        #               ['-', '-', '-', 'p', '-', '-', '-', '-'],
        #               ['P', 'P', 'P', '-', '-', 'P', 'P', 'P'],
        #               ['-', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'] ]

        self.board = [ ['-', '-', '-', '-', '-', '-', '-', '-'],
                       ['-', '-', '-', '-', '-', '-', '-', '-'],
                       ['-', '-', '-', '-', '-', '-', '-', '-'],
                       ['-', '-', '-', '-', '-', '-', '-', '-'],
                       ['-', '-', '-', '-', '-', '-', '-', '-'],
                       ['-', '-', 'K', 'r', '-', '-', '-', '-'],
                       ['-', '-', 'P', '-', '-', '-', '-', '-'],
                       ['-', '-', '-', '-', '-', '-', '-', '-'] ]
        self.whiteToMove = True

def LegalMoves(board, whiteToMove):
    allMoves = []
    
    if whiteToMove:
        ownPieces = ['K', 'Q', 'R', 'B', 'N', 'P']
        capturablePieces = ['k', 'q', 'r', 'b', 'n', 'p']
    else:
        ownPieces = ['k', 'q', 'r', 'b', 'n', 'p']
        capturablePieces = ['K', 'Q', 'R', 'B', 'N', 'P']

    for i in range(8):
        for j in range(8):
            if board[i][j] == ownPieces[0]:
                allMoves = allMoves + kingMoves(board, capturablePieces, i, j)
            if board[i][j] == ownPieces[1]:
                allMoves = allMoves + queenMoves(board, capturablePieces, i, j)
            if board[i][j] == ownPieces[2]:
                allMoves = allMoves + rookMoves(board, capturablePieces, i, j)
            if board[i][j] == ownPieces[3]:
                allMoves = allMoves + bishopMoves(board, capturablePieces, i, j)
            if board[i][j] == ownPieces[4]:
                allMoves = allMoves + knightMoves(board, capturablePieces, i, j)
            if board[i][j] == ownPieces[5]:
                allMoves = allMoves + pawnMoves(board, capturablePieces, i, j)
    print(allMoves)

def kingMoves(board, capturablePieces, i, j):
    kingMoves = []
    for k, l in zip([0, 0, 1, -1, 1, 1, -1, -1], [1, -1, 0, 0, 1, -1, 1, -1]):
            try:
                if all(x >= 0 for x in [i + k, j + l]):
                    if board[i + k][j + l] in ['-'] + capturablePieces:
                        kingMoves.append([[i, j], [i + k, j + l]])
            except IndexError:
                break
    return kingMoves 

def queenMoves(board, capturablePieces, i, j):
    queenMoves = rookMoves(board, capturablePieces, i, j) + bishopMoves(board, capturablePieces, i, j)
    return queenMoves 

def rookMoves(board, capturablePieces, i, j):
    rookMoves = []
    for k, l in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        for m in range(1, 7):
            try:
                if all(x >= 0 for x in [i + (k * m), j + (l * m)]):
                    if board[i + (k * m)][j + (l * m)] == '-':
                        rookMoves.append([[i, j], [i + (k * m), j + (l * m)]])
                    elif board[i + (k * m)][j + (l * m)] in capturablePieces:
                         rookMoves.append([[i, j], [i + (k * m), j + (l * m)]])
                         break
                    else:
                        break
            except IndexError:
                break
    return rookMoves 

def bishopMoves(board, capturablePieces, i, j):
    bishopMoves = []
    for k, l in zip([1, 1, -1, -1], [1, -1, 1, -1]):
        for m in range(1, 7):
            try:
                if all(x >= 0 for x in [i + (k * m), j + (l * m)]):
                    if board[i + (k * m)][j + (l * m)] == '-':
                        bishopMoves.append([[i, j], [i + (k * m), j + (l * m)]])
                    elif board[i + (k * m)][j + (l * m)] in capturablePieces:
                         bishopMoves.append([[i, j], [i + (k * m), j + (l * m)]])
                         break
                    else:
                        break
            except IndexError:
                break
    return bishopMoves 

def knightMoves(board, capturablePieces, i, j):
    knightMoves = []
    for k, l in zip([1, 1, 2, 2, -1, -1, -2, -2], [2, -2, 1, -1, 2, -2, 1, -1]):
        try:
            if all(x >= 0 for x in [i + k, j + l]):
                if board[i + k][j + l] in ['-'] + capturablePieces: 
                    knightMoves.append([[i, j], [i + k, j + l]])
        except IndexError:
            pass
    return knightMoves

def pawnMoves(board, capturablePieces, i, j):
    pawnMoves = []
    
    if board[i][j].isupper():
        up, lastRank = -1, 0
    else:
        up, lastRank = 1, 7

    if  i + up >= lastRank:
        #Moving without capturing
        if board[i + up][j] == '-':
            pawnMoves.append([[i, j], [i + up, j]])
            if i == 6 and board[i + (2 * up)][j] == '-':
                pawnMoves.append([[i, j], [i + (2 * up), j]])

        #Capture eastside.
        if j in range(7) and board[i + up][j + 1] in capturablePieces:
            pawnMoves.append([[i, j], [i - 1, j + 1]])
        
        #Capture westside.
        if j in range(1,8) and board[i + up][j - 1] in capturablePieces:
            pawnMoves.append([[i, j], [i - 1, j - 1]])

    return pawnMoves

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