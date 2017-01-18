# tictactoe.py
# Tic Tac Toe for 2 human players

def printBoard(board):
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("-----------")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("-----------")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
   

def getMove(currentName, board):
    print(currentName + ", it is your turn.") 
    acceptMove = False
    while acceptMove == False:
        row = int(input("Pick a row (1,2,3): "))
        col = int(input("Pick a column (1,2,3): "))
        if row >= 1 and row <= 3 and col >= 1 and col <= 3:
            row = row - 1
            col = col - 1
            if board[row][col] == "X" or board[row][col] == "O":
                print("Spot is taken, choose another.")
            else:
                acceptMove = True
        else:
            print("Not a valid spot on the board.")
    return[row, col]

def checkWin(board, currentPlayer):
    if board[0][0] == currentPlayer and board[0][1] == currentPlayer and board[0][2] == currentPlayer:
        return True
    elif board[0][0] == currentPlayer and board[1][0] == currentPlayer and board[2][0] == currentPlayer:
        return True
    elif board[0][0] == currentPlayer and board[1][1] == currentPlayer and board[2][2] == currentPlayer:
        return True
    elif board[0][1] == currentPlayer and board[1][1] == currentPlayer and board[2][1] == currentPlayer:
        return True
    elif board[2][0] == currentPlayer and board[2][1] == currentPlayer and board[2][2] == currentPlayer:
        return True
    elif board[0][2] == currentPlayer and board[1][1] == currentPlayer and board[2][0] == currentPlayer:
        return True
    elif board[0][2] == currentPlayer and board[1][2] == currentPlayer and board[2][2] == currentPlayer:
        return True
    else:
        return False
    
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

xPlayer = input("Enter x player's name: ")
oPlayer = input ("Enter o player's name: ")

currentPlayer = "X"
currentName = xPlayer
winner = None

for i in range(9):
    printBoard(board)
    
    move = getMove(currentName, board)
    row = move[0]
    col = move[1]

    board[row][col] = currentPlayer

    winHappened = checkWin(board, currentPlayer)
    if winHappened:
        winner = currentPlayer
        break

    if currentPlayer == "X":
        currentPlayer = "O"
        currentName = oPlayer
    else:
        currentPlayer = "X"
        currentName = xPlayer
    
if winner == None:
    print("The game has ended in a draw.")
    printBoard(board)
else:
    print("\n" + currentName + " has won!")
    printBoard(board)

    



        
