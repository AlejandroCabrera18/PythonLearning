"""
Chapter 5, Exercise 1
Student Name: Alejandro Cabrera
Purpose: Find and display the median in a set of floating-point numbers that are
         stored in a file
"""

#Open the input file
fileName = input("Please enter a file name: ")
inFile = open(fileName, "r")

#read in the numbers to form a list of numbers
numbers = []
for line in inFile:
    words = line.split()
    for word in words:
        numbers.append(float(word))

#find and display the median
numbers.sort()

midpoint = len(numbers)//2

if len(numbers)%2 == 1:
    median = numbers[midpoint]
else:
    median = (numbers[midpoint]+numbers[midpoint-1])/2
    
print("The median is", median)
