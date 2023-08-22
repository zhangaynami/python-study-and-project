# -*- codeing = utf-8 -*-
def tree(branche,t):
    if branche > 5:
        t.forward(branche)
        t.right(20)
        tree(branche - 15 , t)
        t.left(40)
        tree(branche - 10, t)
        t.right(20)
        t.backward(branche)

from turtle import *
t = Turtle()
mywin = t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
t.color("green")
tree(100,t)
mywin.exitonclick()