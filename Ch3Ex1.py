"""
Chapter 3, Exercise 1
Student Name: Alejandro Cabrera
Purpose: Compute the following arithmatic progression
         3 + 8 + 13 + ... + 53
"""

sum = 0 #the accumalator

#accumalate the sequence of numbers
for i in range(3,54,5):
    sum += i

#display the total
print("3 + 8 + 13 + ... + 53 =",sum)
