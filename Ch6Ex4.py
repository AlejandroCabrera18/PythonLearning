"""
Chapter 6, Exercise 4
Student Name: Alejandro Cabrera
Purpose: raise x to the nth recursively
"""

def main():
    """The main function of the program"""

    #prompt for the base, i.e., x
    base = int(input("Please enter the base: "))

    #prompt for the value of the exponent, i.e., n
    exp = int(input("Please enter the exponent: "))

    #compute the Nth element in the sequence
    result = power(base,exp)

    #display the result
    print(base,"to the", exp,"th power is",result)

def power(x,n):
    """Raise x to the nth power recursively"""
    if(n==0):
        return 1 #base case
    else:
        return x * power(x,n-1) #recursive case
    
#entry point of execution
main()
