import tkinter, time, random
from tkinter import messagebox

def set_tile(row, col):
    global currPlayer, gameOver, moves

    if gameOver:
        return
    if board[row][col]["text"] !="":    
        return

    board[row][col]["text"] = PlayerSign
    
    moves+=1
    if moves>4:checkWinner()
    currPlayer = 1

    aiMove()

def aiMove():
    global moves, gameOver, currPlayer
    if gameOver:
        return
    movePicked = False
    while(movePicked == False):
        randRow = random.randint(0,2)
        randCol = random.randint(0,2)
        if board[randRow][randCol]["text"] == "":
            board[randRow][randCol]["text"] = AISign
            movePicked = True
    if moves>4:checkWinner()
    moves+=1
    movePicked = False
    currPlayer = 0

def checkWinner():
    global gameOver
    print("check winner")
    for i in range(3):
        if board[i][0]["text"] == board[i][1]["text"] == board[i][2]["text"] and board[i][0]["text"]!="":
            print("Player won")
            if currPlayer == 0:
                label['text'] = "YOU WIN!"
            else:
                label['text'] = "YOU LOSE"
            gameOver = True
            
    for i in range(3):
        if board[0][i]["text"] == board[1][i]["text"] == board[2][i]["text"] and board[0][i]["text"]!="":
            print("Player won")
            if currPlayer == 0:
                label['text'] = "YOU WIN!"
            else:
                label['text'] = "YOU LOSE"
            gameOver = True
            
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"]!="":
        print("Player won")
        if currPlayer == 0:
            label['text'] = "YOU WIN!"
        else:
            label['text'] = "YOU LOSE"
        gameOver = True
        
    if board[2][0]["text"] == board[1][1]["text"] == board[0][2]["text"] and board[2][0]["text"]!="":
        print("Player won")
        if currPlayer == 0:
            label['text'] = "YOU WIN!"
        else:
            label['text'] = "YOU LOSE"
        gameOver = True
    if moves == 9 and gameOver == False:
        gameOver = True
        label['text'] = "TIE!!"
        

def new_game():
    global moves, gameOver, currPlayer
    print("restart pressed")
    for row in range(3):
        for col in range(3):
            board[row][col]["text"] = ""
            moves = 0
            gameOver = False
            currPlayer = 0

    label["text"] = "GAME ON!"

#0 is player, 1 is AI
currPlayer = 0
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
