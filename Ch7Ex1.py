"""
Chapter 7, Exercise 1
Student Name: Alejandro Cabrera
Purpose: Draw a square in which the length of each side is 100 pixels
"""

from turtle import *

#create (instantiate) a turtle
t = Turtle()

#set the pen color
t.pencolor("blue")

#raise the pen
t.up()

#go the starting location, assume it is at (200,300)
t.goto(200,300)

#put down the pen
t.down()
t.hideturtle()
#draw the 4 sides of the square
for i in range(4):
    t.right(90)
    t.forward(100)



