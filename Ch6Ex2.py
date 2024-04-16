"""
Chapter 6, Exercise 2
Student Name: Alejandro Cabrera
Purpose: Compute the factorial recursively
"""

def main():
    """The main function of the program"""

    #prompt for the value of n
    num = int(input("Please enter a positive integer: "))

    #compute n!
    factorialResult = factorial(num)

    #display the result
    print("The factorial of",num,"is",factorialResult)

def factorial(n):
    """Compute n! recursively"""
    if(n==0):
        return 1 #base case
    else:
        return n*factorial(n-1) #recursive case
    
#entry point of execution
main()
