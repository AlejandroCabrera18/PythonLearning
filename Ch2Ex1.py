"""
Chapter 2, Exercise 1
Student Name: Alejandro Cabrera
Purpose: Computing the average velocity of a moving object
        and tounding it to 2 decimal places
        Assume that at time 1 the object is at location 1
        and at time 2 that object is at location 2
"""

#get time1, Location1, time2, and location2
time1 = float(input("Enter the time 1: "))
location1 = float(input("Enter the location 1: "))
time2 = float(input("Enter the time 2: "))
location2 = float(input("Enter the location 2: "))

#Compute the average velocity
avgVelocity = (location2 - location1) / (time2-time1)

#round the average velocity to 2 decimal places
avgVelocity = round(avgVelocity,2)

#display the average velocity
print("The average velocity is", avgVelocity)
