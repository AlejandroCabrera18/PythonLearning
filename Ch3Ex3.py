"""
Chapter 3, Exercise 3
Student Name: Alejandro Cabrera
Purpose: Converting a numeric score into a letter grade based on the following scale:
        >= 90 --> A
        80 - 89 --> B
        70 - 79 --> C
        <= 69 --> F
"""
#prompt user to enter a score
score = int(input("Please enter a score (0-100): "))

#assign a letter grade
if score>=90: #above 89
    letter = "A"
elif score>=80: #between 80 and 89
    letter = "B"
elif score>=70: #between 70 and 79
    letter = "C"
else: #below 70
    letter="F"

#output the grade
print("The student got this grade:",letter)
