"""
Chapter 3, Exercise 4
Student Name: Alejandro Cabrera
Purpose: Compute the following arithmatic progression with a while loop
         53 + 48 + 43 + ... + 3
"""

sum = 0 #the accumalator

i = 53 #Starting the accumalation from 53

#accumalate the sequence of numbers

while i>=3:
    sum += i
    i-=5

"""for i in range(53,2,-5):
    sum += i"""

#display the total
print("53 + 48 + 43 + ... + 3 =",sum)
