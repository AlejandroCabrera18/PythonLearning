"""
Chapter 6, Exercise 1
Student Name: Alejandro Cabrera
Purpose: Compute the summation of positive integers from 1 to N recursively,
         where N >= 1
"""

def main():
    """The main function of the program"""

    #prompt for the value of n
    num = int(input("Please enter a positive integer: "))

    #compute the sum from 1 to n
    summation = sumOneToN(num)

    #display the result
    print("The sum from 1 to",num,"is",summation)

def sumOneToN(n):
    """Compute the sum from 1 to n recursively"""
    if(n==1):
        return 1 #base case
    else:
        return n+sumOneToN(n-1) #recursive case
    
#entry point of execution
main()
