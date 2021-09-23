import math
from turtle import *
import random

pen = Pen()
pen.color('blue')
pen.width(2)

# construct a square (x,y) with the width w
def square(x,y, w):
    # move to (x,y)
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.speed(0)

    # draw the square
    for i in range(4):
        pen.forward(w)
        pen.left(90)
    # endfor

# end square

def drawing1 (n):
    x = y = 0
    for i in range (n):
        square (x,y,100)
        x = x + 10
        y = y + 10
    # endfor

def drawing2 (n):
    for i in range (n):
        square(0,0,100)
        pen.left(360/n)
    # endfor
# end drawing2

def randomSquare():
    #get some random colors
    r = random.random()
    g = random.random()
    b = random.random()
    pen.color(r,g,b)

    x = random.randint (-300, 300)
    w = random.randint (-400, 400)
    y = random.randint (-300, 300)

    square(x, y, w)
# end randomSquare

def drawing3 (n):
    for i in range (n):

        randomSquare()
        
    #endfor
# end drawing3
