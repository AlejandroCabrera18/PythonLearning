"""
Chapter 5, Exercise 3
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
    
    #the mapping between hexadecimal digits and their binary values
    mapTable = {'0':'0000','1':'0001','2':'0010','3':'0011',
                '4':'0100','5':'0101','6':'0110','7':'0111',
                '8':'1000','9':'1001','A':'1010','B':'1011',
                'C':'1100','D':'1101','E':'1110','F':'1111',}

    #convert the num digit by digit
    binary=""

    for digit in hexNumber:
        binary = binary + mapTable[digit]

    return binary

#entry point of execution
main()
