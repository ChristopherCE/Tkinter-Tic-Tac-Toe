'''
Name: Christopher Alexman
ID: 2694498
Date: July 22, 2018
Assignment 17 & 18
Description: This program simulated the game tic-tac-toe using functions and tkinter. 
'''

from tkinter import *

def resetGame() :
    global isXTurn, numClicks, isDone

    for row in range(0, 3) :
        for col in range(0, 3) :
            grid[row][col].config(text = ' ')

    numClicks = 0
    isXTurn = True
    isDone = False

    lblStatus.config(text = 'X\'s Turn')

def markSpace(rw, col) :
    global isXTurn, numClicks, isDone

    if(isDone == True) :
        return lblStatus.config(text = 'Game Over!')

    space = grid[rw][col].cget('text')

    if(space == ' ') :
        if(isXTurn == True) :
            grid[rw][col].config(text = 'X', fg = 'red')
            lblStatus.config(text = 'O\'s Turn')
            isXTurn = False
        else :
            grid[rw][col].config(text = 'O', fg = 'blue')
            lblStatus.config(text = 'X\'s Turn')
            isXTurn = True
    else :
        lblStatus.config(text = 'Invalid Move')
        return

    numClicks += 1
    gameOver(rw, col)

def gameOver(rw, col) :
    global numClicks
    global isDone
    winner = ' '

    if(grid[0][0].cget('text')  == grid[1][1].cget('text') and grid[1][1].cget('text') == grid[2][2].cget('text')) :
        winner = grid[0][0].cget('text')
    elif(grid[2][0].cget('text')  == grid[1][1].cget('text') and grid[1][1].cget('text') == grid[0][2].cget('text')) :
        winner = grid[2][0].cget('text')

    else :
        for r in range(0, 3) :
            if(grid[r][0].cget('text') != ' ' and grid[r][0].cget('text') == grid[r][1].cget('text') and grid[r][1].cget('text') == grid[r][2].cget('text')):
                winner = grid[r][0].cget('text')
            elif(grid[0][r].cget('text') != ' ' and grid[0][r].cget('text') == grid[1][r].cget('text') and grid[1][r].cget('text') == grid[2][r].cget('text')):
                winner = grid[0][r].cget('text')

    isDone = True
    if(winner == ' ' and numClicks >= 9) :
       lblStatus.config(text = 'Tie Game')
    elif(winner != ' ') :
        lblStatus.config(text = winner + ' Wins!')
    else :
        lblStatus.config(text = 'X\'s Turn' if isXTurn else 'O\'s Turn')
        isDone = False  

grid = [ [ 0 for i in range(3) ] for j in range(3)]

numClicks = 0

isDone = False

isXTurn = True

root = Tk()
root.title('Tic-Tac-Toe')
root.geometry('355x420')

topFrame = Frame(root, width = 320, height = 40)
topFrame.place(x = 12, y = 12)
topFrame.pack()

lblStatus = Label(topFrame, text = 'X\'s Turn', bg = 'yellow', fg = 'blue', font = 'serif')
lblStatus.pack()

mainFrame = Frame(root, width = 330, height = 330, bg = 'black')
mainFrame.place(x = 10, y = 42)

for rw in range(0, 3) :
    for col in range(0, 3) :
        grid[rw][col] =  Button(mainFrame, text=" ", relief = 'solid',  command = lambda r=rw, c=col: markSpace(r, c))
        grid[rw][col].config(font = "monospace 36 bold", fg = 'red', height = 1,  width = 3)
        grid[rw][col].place(x = rw*105 + 10, y = col*105+10)

btnRestart = Button(root, text = 'Restart', command = resetGame, width = 30)
btnRestart.place(x = 45, y = 380)

root.mainloop()