import math
from turtle import *

pen = Pen()
pen.color('brown')
pen.speed(0)
pen.width(2)

pen.penup()
pen.setx(-500)
pen.pendown()

def tree2(n, l):
    '''
    draws a binary tree or order n and length l
    uses a turtle pen
    direction must be preserved
    '''
    #termination
    if n == 0 or l < 2:
        return
    #endif
    pen.forward(l)
    pen.left(45)
    tree2(n-1, l/2)
    pen.right(90)
    tree2(n-1, l/2)
    pen.left(45)
    pen.backward(l)

#end tree2

def tree4(n, l):
    '''
    draws a binary tree or order n and length l
    uses a turtle pen
    direction must be preserved
    '''
    #termination
    if n == 0 or l < 2:
        return
    #endif
    pen.forward(l)
    pen.left(90)
    tree4(n-1, l/2)
    pen.right(60)
    tree4(n-1, l/2)
    pen.right(60)
    tree4(n-1, l/2)
    pen.right(60)
    tree4(n-1, l/2)
    pen.left(90)
    pen.backward(l)

#end tree4

def koch(n,l):
    '''
    draws the koch curve as part of a snowflake
    uses turtle pen
    preserve direction

    '''
    if n == 0 or l <2:
        pen.forward(l)
        return
    #endif
    koch(n-1, l/3)
    pen.left(60)
    koch(n-1, l/3)
    pen.right(120)
    koch(n-1, l/3)
    pen.left(60)
    koch(n-1, l/3)
#end koch

def flake (n, l):
    for i in range(3):
        koch(n, l)
        pen.right(120)

    # endfor
#end flake
