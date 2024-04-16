"""
Chapter 7, Exercise 2
Student Name: Alejandro Cabrera
Purpose: Draw a shape that connects a list or vertices
"""

from turtle import *

def main():
    """The main function"""
    #create (instantiate) a turtle
    fang = Turtle()

    #hide the turtle
    fang.hideturtle()

    #start drawing
    draw(fang,[(10,10),(20,15),(-20,-20)])

def draw(t, vertices):
    """"Draw a shape that connects the given list of vertices"""
    #before drawing
    t.up()

    #go to the last vertice
    t.goto(vertices[-1])

    #about to start drawing
    t.down()

    #connect each vertive
    for (x,y) in vertices:
        t.goto(x,y)

main()




