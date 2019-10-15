from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('1920x1200')



c=Canvas(root, bg='white')
c.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'brown']
def new_ball():
    global x, y, r, x2, y2, r2
    c.delete(ALL)
    x = rnd(100, 1820)
    y = rnd(100, 1100)
    r = rnd(30, 50)
    x2 = rnd(0, 1920)
    y2 = rnd(0, 1200)
    r2 = rnd(1, 100)
    c.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0)
    c.create_oval(x2-r2, y2-r2, x2+r2, y2+r2, fill=choice(colors), width=0)
    root.after(1000, new_ball)


def click(event):
    print(x, y, r, '   ', x2, y2, r2)

new_ball()
c.bind('<Button-1>', click)
mainloop()