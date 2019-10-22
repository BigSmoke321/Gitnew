from tkinter import *
from random import randrange as rnd, choice
import math


global score, antiscore
score = 0
antiscore = 0

root = Tk()
root.geometry('1600x900')

label1 = Label(text=str(score), fg="#eee", bg="#333")
label2 = Label(text=str(antiscore), fg="#eee", bg="#333")
label1.pack()
label2.pack()

c = Canvas(root, bg='white')
c.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'brown', '#99D9EA', '#BE5AA8']

st = [-1, 1]
k = choice(st)
vx = rnd(-5, 6)
vy = k * math.sqrt(25 - vx**2)


def new_ball():
    global x, y, r, clr
    c.delete(ALL)
    x = rnd(100, 1500)
    y = rnd(100, 800)
    r = rnd(30, 50)
    clr = choice(colors)
    c.create_oval(x - r, y - r, x + r, y + r, fill=clr, width=0)
    root.after(20, move_ball)


def move_ball():
    global vx, vy, x, y, r, clr
    if x <= r:
        st = [-1, 1]
        k = choice(st)
        vx = rnd(0, 6)
        vy = k * math.sqrt(25 - vx ** 2)
    elif x >= 1600-r:
        st = [-1, 1]
        k = choice(st)
        vx = rnd(-5, 1)
        vy = k * math.sqrt(25 - vx ** 2)
    elif y <= r:
        vx = rnd(-5, 6)
        vy = math.sqrt(25 - vx ** 2)
    elif y >= 900-r:
        vx = rnd(-5, 6)
        vy = (-1) * math.sqrt(25 - vx ** 2)
    x += vx
    y += vy
    c.delete(ALL)
    c.create_oval(x - r, y - r, x + r, y + r, fill=clr, width=0)
    root.after(20, move_ball)


def click(event):
    global r, score, antiscore
    if ((event.x - x) ** 2 + (event.y - y) ** 2) <= r ** 2:
        score += 1
    else:
        antiscore += 1
    label1['text'] = str(score)
    label2['text'] = str(antiscore)
    if antiscore >= 10:
        exit()


new_ball()
c.bind('<Button-1>', click)
mainloop()