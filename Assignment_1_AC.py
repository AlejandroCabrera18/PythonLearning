"""
Assignment 1
Student Name: Alejandro Cabrera
Purpose: This is a program that takes the
radius of a sphere (a floating-point number) as
input and outputs the sphere's diameter, circumference,
surface area, and volume
"""

from math import pi

#get the radius of the sphere
radius = float(input("Enter the radius of the sphere: "))

#calculate the diameter, circumference, surface area, and volume of the sphere
diameter = 2*radius
circumference = 2*radius*pi
surfaceArea = 4*pi*(radius**2)
volume = (4/3)*pi*(radius**3)

#display the diameter, circumference, surface area, and volume of the sphere
print("The diameter of the sphere with radius",radius,"is:", round(diameter,2))
print("The circumference of the sphere with radius",radius,"is:", round(circumference,2))
print("The surface are of the sphere with radius",radius,"is:", round(surfaceArea,2))
print("The volume of the sphere with radius",radius,"is:", round(volume,2))
