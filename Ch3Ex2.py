"""
Chapter 3, Exercise 2
Student Name: Alejandro Cabrera
Purpose: Compute the following arithmatic progression
         53 + 48 + 43 + ... + 3
"""

sum = 0 #the accumalator

#accumalate the sequence of numbers
for i in range(53,2,-5):
    sum += i

#display the total
print("53 + 48 + 43 + ... + 3 =",sum)
