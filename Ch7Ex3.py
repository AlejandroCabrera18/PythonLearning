"""
Chapter 7, Exercise 3
Student Name: Alejandro Cabrera
Purpose: Walking randomly
"""

from turtle import *
from random import *



def walk(t, turns = 30, distance = 40):
    """"A random walk function"""
    #hide the turtle
    t.hideturtle
    
    #start walking based on the number of turns, heading direction and distance
    #after each turn
    for i in range(turns):
        t.setheading(randint(0,360))#heading a random direction
        t.pencolor(randint(0,255),randint(0,255),randint(0,255))
        t.forward(distance) #Move forward to the destination
    
#Start walking    
walk(Turtle(), 50, 20)




