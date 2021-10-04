#Init

import turtle
import random

t=turtle.Turtle()
t.left(90)

#Func

def randomDot():
    t.begin_fill()
    t.color("Red")
    t.circle(120)
    t.end_fill

#Main
randomDot()
