"""
Chapter 5, Exercise 4
Student Name: Alejandro Cabrera
Purpose: Create a convert function that is called by the main function
         to convert a hexadecimal number into an equivalent binary num
"""

def main():
    """The main function of this program"""
    #prompt the user for a hexadecimal
    hexNum = input("Please enter a hexadecimal number: ")

    #convert the hexadecimal num into an equivalent binary num
    binNum = convert(hexNum)
    
    #display the result
    print("The hexadecimal number",hexNum,"is converted into",binNum)

def convert(hexNumber):
    """Convert the hexdecimal number into a binary number"""
    

    #convert the num digit by digit
    binary=""

    for digit in hexNumber:
        if digit == '0':
            binary = binary + "0000"
        elif digit == '1':
            binary = binary + "0001"
        elif digit == '2':
            binary = binary + "0010"
        elif digit == '3':
            binary = binary + "0011"
        elif digit == '4':
            binary = binary + "0100"
        elif digit == '5':
            binary = binary + "0101"
        elif digit == '6':
            binary = binary + "0110"
        elif digit == '7':
            binary = binary + "0111"
        elif digit == '8':
            binary = binary + "1000"
        elif digit == '9':
            binary = binary + "1001"
        elif digit == 'A':
            binary = binary + "1010"
        elif digit == 'B':
            binary = binary + "1011"
        elif digit == 'C':
            binary = binary + "1100"
        elif digit == 'D':
            binary = binary + "1101"
        elif digit == 'E':
            binary = binary + "1110"
        elif digit == 'F':
            binary = binary + "1111"
            

    return binary

#entry point of execution
main()
