import tkinter, time, random
from tkinter import messagebox

def set_tile(row, col):
    global  gameOver, moves
    if gameOver:
        return
    if board[row][col]["text"] !="":    
        return
    board[row][col]["text"] = PlayerSign
    
    moves+=1
    if checkWin(PlayerSign,board):
        gameOver=True
        label["text"]="YOU WIN"
    if moves==9:
        checkTie(True)
        gameOver = True
    miniMaxMove()
    
def checkTie(game):
    if checkWin(AISign,board) == checkWin(PlayerSign,board) == False:
        if game: label["text"]="TIE!"
        return True
    return False

def miniMaxMove():
    global moves, gameOver
    if gameOver:
        return
    bestScore = -1000
    bestMoveX = -10
    bestMoveY = -10
    for row in range(3):
        for col in range(3):
            if board[row][col]["text"] == "":
                board[row][col]["text"] = AISign
                score = miniMax(board, 0, False)
                board[row][col]["text"] = ""
                if score > bestScore:
                    print("insideBestMOveChange")
                    bestScore = score
                    bestMoveX = row
                    bestMoveY = col
    if bestMoveX != -10 and bestMoveY != -10:
        board[bestMoveX][bestMoveY]["text"] = AISign
        if checkWin(AISign,board):
            gameOver=True
            label["text"]="YOU LOSE"
        moves+=1

def isBoardFull():
    for i in range(3):
        for j in range(3):
            if board[i][j]["text"]== "":
                return False
    return True

def miniMax(mboard, depth, isMax):
    if checkWin(AISign,mboard):
        return 100000
    elif checkWin(PlayerSign,mboard):
        return -100000
    elif isBoardFull():
        return 0

    if isMax:
        bestScore = -1000
        for row in range(3):
            for col in range(3):
                if mboard[row][col]["text"] == "":
                    mboard[row][col]["text"] = AISign
                    score = miniMax(mboard, depth+1, False)
                    mboard[row][col]["text"] = ""
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 1000
        for row in range(3):
            for col in range(3):
                if mboard[row][col]["text"] == "":
                    mboard[row][col]["text"] = PlayerSign
                    score = miniMax(mboard, depth+1, True)
                    mboard[row][col]["text"] = ""
                    bestScore = min(score, bestScore)
        return bestScore
    
def checkWin(sign, mboard):
    for i in range(3):
        if mboard[i][0]["text"] == mboard[i][1]["text"] == mboard[i][2]["text"] and mboard[i][0]["text"]==sign:
            return True
    for i in range(3):
        if mboard[0][i]["text"] == mboard[1][i]["text"] == mboard[2][i]["text"] and mboard[0][i]["text"]==sign:   
            return True
    if mboard[0][0]["text"] == mboard[1][1]["text"] == mboard[2][2]["text"] and mboard[0][0]["text"]==sign:
        return True
    if mboard[2][0]["text"] == mboard[1][1]["text"] == mboard[0][2]["text"] and mboard[2][0]["text"]==sign:
        return True
    return False

def new_game():
    global moves, gameOver
    print("restart pressed")
    for row in range(3):
        for col in range(3):
            board[row][col]["text"] = ""
            moves = 0
            gameOver = False

    label["text"] = "GAME ON!"


gameOver = False
moves = 0
PlayerSign = "X"
AISign = "O"

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

colorBlue = "#4584b6"
colorYellow = "#ffde57"
colorGray = "#343434"
colorLightGray = "646464"
colorBlack = "#000000"


#creates buttons
window = tkinter.Tk()
turns = 0
window.title("Tic Tac Toe")
window.resizable(False, False)
frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = "GAME ON!", font = ("Consolas", 20), background = colorBlack, foreground = "white")
label.grid(row=0, column=0, columnspan = 3, sticky = "we")
for row in range(3): 
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text = "", font = ("Consolas", 50, "bold"), bg = 'blue', foreground = colorBlue, width = 4, height = 2, command=lambda row=row, column = column: set_tile(row, column))
        board[row][column].grid(row=row+1, column = column)



#restart game button
button = tkinter.Button(frame, text = "RESTART", font=("Consolas", 20), background = colorYellow, foreground=colorBlack, command= new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")#sticky stretches the button out to both sides
#we means west to eats, ns means north to south``


#Centers window
frame.pack()
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2)-(window_width/2))
window_y = int((screen_height/2)-(window_height/2))


window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


window.mainloop()
