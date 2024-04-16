"""
Chapter 6, Exercise 3
Student Name: Alejandro Cabrera
Purpose: Compute the Nth element in the Fibonacci sequence recursively
"""

def main():
    """The main function of the program"""

    #prompt for the value of n
    num = int(input("Please enter a positive integer: "))

    #compute the Nth element in the sequence
    element = fib(num)

    #display the result
    print("The element is",element)

def fib(n):
    """Compute the nth element in the sequence recursively"""
    if(n<=2):
        return n-1 #base case
    else:
        return fib(n-2)+fib(n-1) #recursive case
    
#entry point of execution
main()
