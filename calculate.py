from math import pi

def house_squarefoot():
    length = int(input("What is the length of your house? "))
    width = int(input("What is the width of your house? "))
    square_foot = length * width
    print(f"The square footage of your house is {square_foot}!")

def circ_circum():
    radius = int(input("What is the radius of your circle? "))
    circum = 2 * pi * radius
    print(f"The circumference of your circle is {circum}!")
