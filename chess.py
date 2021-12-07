class Board():
    def __init__(self, board, whiteToMove):
        self.board = board
        self.whiteToMove = whiteToMove
        self.history = []

        self.whiteKingsideCastling = True
        self.whiteQueensideCastling = True
        self.blackKingsideCastling = True
        self.blackQueensideCastling = True

    def makeMove(self, moveFrom, moveTo):
        allLegalMoves = self.legalMoves()
        newMove = [self.chessToArray(moveFrom), self.chessToArray(moveTo)]
        if newMove in allLegalMoves:
            self.history.append(newMove)
            self.checkForCastling(newMove)
            self.updateBoard(self.chessToArray(moveFrom), self.chessToArray(moveTo))
            #Print statement
            print('\n'.join(' '.join(map(str,sl)) for sl in self.board))
            print('................')
            return self.board
        else:
            print("Not a legal move")

    def kingsPosition(self):
        king = 'K' if self.whiteToMove else 'k'
        for array in self.board:
            if king in array:
                kingSquare = [self.board.index(array), array.index(king)]

        return kingSquare

    def checkForCastling(self, newMove):
        #Check if white kingside castling is legal:
        if self.whiteKingsideCastling == True and any(x in [[7,4], [7,7]] for x in [newMove[0], newMove[1]]):
            self.whiteKingsideCastling = False

        #Check if white queenside castling is legal:
        if self.whiteQueensideCastling == True and any(x in [[7,4], [7,0]] for x in [newMove[0], newMove[1]]):
            self.whiteQueensideCastling = False

        #Check if black kingside castling is legal:
        if self.blackKingsideCastling == True and any(x in [[0,4], [0,7]] for x in [newMove[0], newMove[1]]):
            self.blackKingsideCastling = False

        #Check if black queenside castling is legal:
        if self.blackQueensideCastling == True and any(x in [[0,4], [0,0]] for x in [newMove[0], newMove[1]]):
            self.blackQueensideCastling = False

    def attackedSquares(self, moves):
        attackingMoves = []
        for m in range(len(moves)):
            attackingMoves.append(moves[m][1])
        return attackingMoves

    def pieceMoves(self):
        allMoves = []
        
        if self.whiteToMove:
            ownPieces = ['K', 'Q', 'R', 'B', 'N', 'P']
            capturablePieces = ['k', 'q', 'r', 'b', 'n', 'p']
        else:
            ownPieces = ['k', 'q', 'r', 'b', 'n', 'p']
            capturablePieces = ['K', 'Q', 'R', 'B', 'N', 'P']

        for i in range(8):
            for j in range(8):
                if self.board[i][j] == ownPieces[0]:
                    allMoves = allMoves + self.kingMoves(capturablePieces, i, j)
                if self.board[i][j] == ownPieces[1]:
                    allMoves = allMoves + self.queenMoves(capturablePieces, i, j)
                if self.board[i][j] == ownPieces[2]:
                    allMoves = allMoves + self.rookMoves(capturablePieces, i, j)
                if self.board[i][j] == ownPieces[3]:
                    allMoves = allMoves + self.bishopMoves(capturablePieces, i, j)
                if self.board[i][j] == ownPieces[4]:
                    allMoves = allMoves + self.knightMoves(capturablePieces, i, j)
                if self.board[i][j] == ownPieces[5]:
                    allMoves = allMoves + self.pawnMoves(capturablePieces, i, j)
        return allMoves

    def legalMoves(self):
        legalMoves = []

        #Find all whites moves:
        allMoves = self.pieceMoves()
        for move in allMoves:

            #Check in current state if white is in check.
            currentKingSquare = self.kingsPosition()

            self.whiteToMove = not self.whiteToMove
            currentMoves = self.pieceMoves()
            currentAttackingMoves = self.attackedSquares(currentMoves)
            if currentKingSquare in currentAttackingMoves:
                continue

            #Make a hypothetical white move:
            self.whiteToMove = not self.whiteToMove
            hypotheticalBoard = Board([x[:] for x in self.board], self.whiteToMove)
            hypotheticalBoard.updateBoard(move[0], move[1])

            #Blacks turn. Find all blacks moves:
            hypotheticalBoard.whiteToMove = not hypotheticalBoard.whiteToMove
            hypotheticalMoves = hypotheticalBoard.pieceMoves()
            
            #Whites turn: Check if King is in check.
            hypotheticalBoard.whiteToMove = not hypotheticalBoard.whiteToMove
            hypotheticalKingSquare = hypotheticalBoard.kingsPosition()
            hypotheicalAttackingMoves = hypotheticalBoard.attackedSquares(hypotheticalMoves)

            if hypotheticalKingSquare not in hypotheicalAttackingMoves:
                legalMoves.append(move)

        if self.whiteKingsideCastling and [[7,4],[7,5]] not in legalMoves:
            try:
                legalMoves.remove([[7,4],[7,6]])
            except ValueError:
                pass

        if self.whiteQueensideCastling and [[7,4],[7,3]] not in legalMoves:
            try:
                legalMoves.remove([[7,4],[7,2]])
            except ValueError:
                pass

        if self.blackKingsideCastling and [[0,4],[0,5]] not in legalMoves:
            try:
                legalMoves.remove([[0,4],[0,6]])
            except ValueError:
                pass

        if self.blackQueensideCastling and [[0,4],[0,3]] not in legalMoves:
            try:
                legalMoves.remove([[0,4],[0,2]])
            except ValueError:
                pass
            
        return legalMoves 

    def kingMoves(self, capturablePieces, i, j):
        kingMoves = []

        for k, l in zip([0, 0, 1, -1, 1, 1, -1, -1], [1, -1, 0, 0, 1, -1, 1, -1]):
            if all(x >= 0 and x <= 7 for x in [i + k, j + l]):
                if self.board[i + k][j + l] in ['-'] + capturablePieces:
                    kingMoves.append([[i, j], [i + k, j + l]])

        if self.whiteToMove == True:
            if self.whiteKingsideCastling == True:
                if all(x in ['-'] for x in [self.board[7][5], self.board[7][6]]):
                    kingMoves.append([[7,4],[7,6]])

            if self.whiteKingsideCastling == True:
                if all(x in ['-'] for x in [self.board[7][1], self.board[7][2], self.board[7][3]]):
                    kingMoves.append([[7,4],[7,2]])

        if self.whiteToMove == False:
            if self.blackKingsideCastling == True:
                if all(x in ['-'] for x in [self.board[0][5], self.board[0][6]]):
                    kingMoves.append([[0,4],[0,6]])

            if self.blackQueensideCastling == True:
                if all(x in ['-'] for x in [self.board[0][1], self.board[0][2], self.board[0][3]]):
                    kingMoves.append([[0,4],[0,2]])
        
        return kingMoves

    def queenMoves(self, capturablePieces, i, j):
        queenMoves = self.rookMoves(capturablePieces, i, j) + self.bishopMoves(capturablePieces, i, j)
        return queenMoves 

    def rookMoves(self, capturablePieces, i, j):
        rookMoves = []
        for k, l in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            for m in range(1, 8):
                try:
                    if all(x >= 0 for x in [i + (k * m), j + (l * m)]):
                        if self.board[i + (k * m)][j + (l * m)] == '-':
                            rookMoves.append([[i, j], [i + (k * m), j + (l * m)]])
                        elif self.board[i + (k * m)][j + (l * m)] in capturablePieces:
                            rookMoves.append([[i, j], [i + (k * m), j + (l * m)]])
                            break
                        else:
                            break
                except IndexError:
                    break
        return rookMoves 

    def bishopMoves(self, capturablePieces, i, j):
        bishopMoves = []
        for k, l in zip([1, 1, -1, -1], [1, -1, 1, -1]):
            for m in range(1, 8):
                try:
                    if all(x >= 0 for x in [i + (k * m), j + (l * m)]):
                        if self.board[i + (k * m)][j + (l * m)] == '-':
                            bishopMoves.append([[i, j], [i + (k * m), j + (l * m)]])
                        elif self.board[i + (k * m)][j + (l * m)] in capturablePieces:
                            bishopMoves.append([[i, j], [i + (k * m), j + (l * m)]])
                            break
                        else:
                            break
                except IndexError:
                    break
        return bishopMoves 

    def knightMoves(self, capturablePieces, i, j):
        knightMoves = []
        for k, l in zip([1, 1, 2, 2, -1, -1, -2, -2], [2, -2, 1, -1, 2, -2, 1, -1]):
            try:
                if all(x >= 0 for x in [i + k, j + l]):
                    if self.board[i + k][j + l] in ['-'] + capturablePieces: 
                        knightMoves.append([[i, j], [i + k, j + l]])
            except IndexError:
                pass
        return knightMoves

    def pawnMoves(self, capturablePieces, i, j):
        pawnMoves = []
        
        if self.board[i][j].isupper():
            up, lastRank = -1, 0
        else:
            up, lastRank = 1, 7

        if  i + up >= lastRank:
            #Moving without capturing
            if self.board[i + up][j] == '-':
                pawnMoves.append([[i, j], [i + up, j]])
                if i == 6 and self.board[i + (2 * up)][j] == '-':
                    pawnMoves.append([[i, j], [i + (2 * up), j]])

            #Capture eastside.
            if j in range(7) and self.board[i + up][j + 1] in capturablePieces:
                pawnMoves.append([[i, j], [i - 1, j + 1]])
            
            #Capture westside.
            if j in range(1,8) and self.board[i + up][j - 1] in capturablePieces:
                pawnMoves.append([[i, j], [i - 1, j - 1]])

        return pawnMoves

    def updateBoard(self, fromSq, toSq):
        #White Kingside Castling (Rook move)
        if fromSq == [7,4] and toSq == [7,6]:
            movedPiece = self.board[7][7]
            self.board[7][7] = '-'
            self.board[7][5] = movedPiece 
        #White Queenside Castling (Rook move)
        if fromSq == [7,4] and toSq == [7,2]:
            movedPiece = self.board[7][0]
            self.board[7][0] = '-'
            self.board[7][3] = movedPiece
        #Black Kingside Castling (Rook move)
        if fromSq == [0,4] and toSq == [0,6]:
            movedPiece = self.board[0][7]
            self.board[0][7] = '-'
            self.board[0][5] = movedPiece
        #Black Queenside Castling (Rook move)
        if fromSq == [0,4] and toSq == [0,2]:
            movedPiece = self.board[0][0]
            self.board[0][0] = '-'
            self.board[0][3] = movedPiece

        movedPiece = self.board[fromSq[0]][fromSq[1]]
        self.board[fromSq[0]][fromSq[1]] = '-'
        self.board[toSq[0]][toSq[1]] = movedPiece 

    def chessToArray(self, chessSq): 

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

        return [rankToArray[chessSq[1]], fileToArray[chessSq[0]]]