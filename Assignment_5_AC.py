"""
Chapter 7, Exercise 5
Student Name: Alejandro Cabrera
Purpose: Draw a C shape fractal recursively and
         draws the line segments using random colors.
"""

from turtle import *

from random import *

def line(t, x1, y1, x2, y2):
    """"Draw a line segment from (x1,y1) to (x2,y2)"""
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y2)
    
def cFractal(t, x1, y1, x2, y2, level):
    """Draw a c shape fractal of the even number of levels """
    
    t.pencolor(randint(0,255),randint(0,255),randint(0,255))#randomize colors
    if level == 0:
        line(t, x1, y1, x2, y2) #base case
    else:
        xm = ((x1 + x2) + (y2 - y1)) // 2 #Recursive case
        ym = ((y1 + y2) + (x1 - x2)) // 2
        cFractal(t,x1,y1,xm,ym,level-1)
        cFractal(t,xm,ym,x2,y2,level-1)
        

def main():
    """Main function of the program"""

    #Instantiate a turtle
    myTurtle=Turtle()

    #allows for the RGB randomization
    myTurtle.screen.colormode(255)
    
    #hide the turtle
    myTurtle.hideturtle()

    #prompt for the number of levels
    num = int(input("Please enter the number of levels: "))

    #start drawing
    cFractal(myTurtle, 100, 0, 100,-200,num)
    
#Entry point of the program    
main()




