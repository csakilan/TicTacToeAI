import tkinter, time



def set_tile(row, col):
    global currPlayer
    
    if game_over:
        return
    
    if board[row][col]["text"] !="":    
        return
    
    board[row][col]["text"] = currPlayer
    
    

    if currPlayer == playerO:
        currPlayer = playerX
    else:
        currPlayer = playerO
        aiMove()

    label['text'] = currPlayer+"'s turn"
    # print("check winner")
      
    checkWinner()
def aiMove():
    print("inside Ai move")
    pass
def checkWinner():
    global turns, game_over
    

    for row in range(3):
        if(board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"]!= ""):
            game_over = True
            label.config(text = board[row][0]["text"]+" is the winner!", foreground=colorYellow)
    for col in range(3):
        if(board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"] and board[0][col]["text"]!= ""):
            game_over = True
            label.config(text = board[0][col]["text"]+" is the winner!", foreground=colorYellow)
    if( board[0][0]["text"]!= "" and (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"])):

        game_over = True
        label.config(text = board[0][0]["text"]+" is the winner!", foreground=colorYellow)
    if(board[2][0]["text"]!="" and (board[2][0]["text"] == board[1][1]["text"] == board[0][2]["text"])):
        game_over = True
        label.config(text = board[2][0]["text"]+" is the winner!", foreground=colorYellow)
    
    turns+=1
    if(turns == 9):
        game_over == True
        label.config(text="Tie!", foreground=colorYellow)
    

    # print("this is currPlayer: "+currPlayer)
def new_game():
    global turns, game_over
    print("restart pressed")
    for row in range(3):
        for col in range(3):
            board[row][col]["text"] = ""
            turns = 0
            game_over = False
            currPlayer = playerX
            label.config(text = currPlayer+" 's turn", foreground="white")

    print(game_over)
    pass



playerX = 'X'
playerO = 'O'
currPlayer = playerX

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

colorBlue = "#4584b6"
colorYellow = "#ffde57"
colorGray = "#343434"
colorLightGray = "646464"
colorBlack = "#000000"
window = tkinter.Tk()


turns = 0
game_over = False

window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
  
label = tkinter.Label(frame, text = currPlayer+" 's turn", font = ("Consolas", 20), background = colorBlack, foreground = "white")
label.grid(row=0, column=0, columnspan = 3, sticky = "we")
for row in range(3): 
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text = "", font = ("Consolas", 50, "bold"), background = colorGray, foreground = colorBlue, width = 4, height = 2, command=lambda row=row, column = column: set_tile(row, column))
        board[row][column].grid(row=row+1, column = column)




button = tkinter.Button(frame, text = "restart", font=("Consolas", 20), background = colorYellow, foreground=colorBlack, command= new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")#sticky stretches the button out to both sides
#we means west to eats, ns means north to south
frame.pack()
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2)-(window_width/2))
window_y = int((screen_height/2)-(window_height/2))


window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")



window.mainloop()# keeps window open even after code ends





