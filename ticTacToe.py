import random

def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
def inputPlayerLetter():
    letter=""
    while not (letter == 'X' or letter == 'O'):
        print("Do you want to be 'X' or 'O' ?")
        letter=input().upper()
    if letter=="X":
        return ["X","O"]
    else:
        return["O","X"]
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return "player"
    else:
        return "player"
def playAgain():
    print("Do you want to play again ?" + "(Y or N)")
    return input().lower().startswith("y")
def makeMove(board, letter, move):
    board[move]=letter
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal
def getBoardCopy(board):
    dupeBoard=[]
    for i in board :
        dupeBoard.append(i)
    return dupeBoard
def isSpaceFree(board, move):
    return board[move]==" "
def getPlayerMove(board):
    c = 0
    while c == 0:
        print("What is your next move ? (1-9)")
        move = int(input())
        if 0 < move < 10 and isSpaceFree(board, move):
            c = 1
            return int(move)
def chooseRandomMoveFromList(board, movesList):
    possibleMoves=[]
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
def getComputerMove(board, computerLetter):
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None:
        return move
    if isSpaceFree(board,5):
        return 5
    return chooseRandomMoveFromList(board,[2,4,6,8])
def isBoardFull(board):
    for i in range (1,10):
        if isSpaceFree(board,i):
            return False
    return True

while True:

    theBoard = 10*[" "]
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print("The "+turn+" goes first !")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == "player":
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("YOU WIN THE GAME !!!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("THE GAME IS A TIE !!")
                    break
                else:
                    turn = "computer"
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("!! YOU LOSE !!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie !")
                    break
                else:
                    turn = "player"
    if not playAgain():
        break