from Tkinter import *
import random as r
import sys
import time

root = Tk()
text = [[None]*8 for i in range(8)]
buttons = [[None]*8]*8
moves_left = 54
sys.setrecursionlimit(15000)
rows, cols = (8,8)
real_board = [['-' for x in range(cols)] for y in range(rows)]
# user_board = [['-' for x in range(cols)] for y in range(rows)]
visit_board = [['0' for x in range(cols)] for y in range(rows)]
mines = [[0 for x in range(2)] for y in range(10)] 


def alert_popup(title, message, path):
    """Generate a pop-up window for special messages."""
    global root
    root_a = Tk()
    root_a.title(title)
    w = 800     # popup window width
    h = 400     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root_a.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    m += path
    w = Label(root_a, text=m, width=120, height=10)
    w.pack()
    b = Button(root_a, text="OK", command= lambda:[root_a.destroy(), root.destroy()], width=10).pack(side = BOTTOM)    
    # root_a.destroy()
    # b.pack()
    

def isMine(x_pos, y_pos):
    if(isValid(x_pos, y_pos) and real_board[x_pos][y_pos] == '*'):
        return True
    return False

def isValid(x_pos, y_pos):
    return (x_pos >= 0) and (y_pos >= 0) and (x_pos < 8) and (y_pos < 8)

def numberOfMines(x_pos, y_pos):
    count = 0
    if isMine(x_pos - 1, y_pos):
        count = count + 1

    if isMine(x_pos, y_pos - 1):
        count = count + 1

    if isMine(x_pos + 1, y_pos):
        count = count + 1

    if isMine(x_pos , y_pos + 1):
        count = count + 1

    if isMine(x_pos - 1, y_pos - 1):
        count = count + 1

    if isMine(x_pos + 1, y_pos + 1):
        count = count + 1

    if isMine(x_pos - 1, y_pos + 1):
        count = count + 1

    if isMine(x_pos + 1, y_pos - 1):
        count = count + 1

    return count
    
def isGameOver(x_inp, y_inp):
    return real_board[x_inp][y_inp] == '*'

def gameLost(x_inp, y_inp):
    global root
    global buttons
    text[x_inp][y_inp].set("*")
    for i in range(10):
        text[mines[i][0]][mines[i][1]].set("*")
    time.sleep(1.5)
    alert_popup("Game Over", "YOU LOST ", "BETTER LUCK NEXT TIME")
    
def gameWon():
    alert_popup("Game Won", "YOU GOT IT", "OH YES")

def playMinesUntil(x_inp, y_inp):
    global moves_left
    global root
    global buttons
    # print(moves_left)
    if(moves_left == 1):
        gameWon()

    if(isMine(x_inp, y_inp)):
        gameLost(x_inp, y_inp)

    elif (isValid(x_inp , y_inp)):
       
        if visit_board[x_inp][y_inp] == 1 :
            return
        visit_board[x_inp][y_inp] = 1
        count_number = numberOfMines(x_inp, y_inp)
        moves_left = moves_left - 1
        text[x_inp][y_inp].set(count_number)
    
        if count_number == 0:
            if isMine(x_inp - 1, y_inp) == False:
                playMinesUntil(x_inp - 1, y_inp)

            if isMine(x_inp, y_inp - 1) == False:
                playMinesUntil(x_inp, y_inp -1)

            if isMine(x_inp + 1, y_inp) == False:
                playMinesUntil(x_inp + 1, y_inp)

            if isMine(x_inp , y_inp + 1) == False:
                playMinesUntil(x_inp, y_inp + 1)

            if isMine(x_inp - 1, y_inp - 1) == False:
                playMinesUntil(x_inp - 1, y_inp - 1)

            if isMine(x_inp + 1, y_inp + 1) == False:
                playMinesUntil(x_inp + 1, y_inp + 1)

            if isMine(x_inp - 1, y_inp + 1) == False:
                playMinesUntil(x_inp - 1, y_inp + 1)

            if isMine(x_inp + 1, y_inp - 1) == False:
                playMinesUntil(x_inp + 1, y_inp - 1)

def searchX(key):
    for i in range(8):
        if(key == mines[i][0]):
            return key
    return -1

def searchY(key):
    for i in range(8):
        if(key == mines[i][1]):
            return key
    return -1

def initialize():
    global moves_left
    global text
    global buttons
    moves_left = 54
    for i in range(10):
        while True:
            x_pos = r.randint(0,rows-1)
            y_pos = r.randint(0, cols-1)
            if (searchX(x_pos ) == -1) or (searchY(y_pos) == -1):
                break
        mines[i][0] = x_pos
        mines[i][1] = y_pos
        real_board[x_pos][y_pos] = '*'

    for i in range(8):
        for j in range(8):
            text[i][j] = StringVar()
            buttons[i][j] = Button(root, command = lambda i=i, j=j : playMinesUntil(i, j))
            buttons[i][j].config(textvariable = text[i][j], width = 9, height = 5)
            buttons[i][j].grid(row = i, column = j)


def playMines():
    global root
    initialize()
    root.mainloop()

    
def main():
    playMines()
    

if __name__ == "__main__":
    main()