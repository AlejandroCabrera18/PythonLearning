"""
Chapter 5, Exercise 2
Student Name: Alejandro Cabrera
Purpose: create a square function that will be called by the main function to
         to compute the square of a given number
"""

def main():
    """The main function of the program"""

    #prompt for a number
    number = float(input("Enter a number: "))

    #compute the square of the number
    result = square(number)

    #display the result
    print("The square of", number, "is", result)
    print("The cube of", number, "is", cube(number))

def square(num):
    """Returns the square of num"""
    return num*num

def cube(num):
    """Returns the cube of num"""
    return num**3




#the entry point of program execution
main()
