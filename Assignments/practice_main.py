from email.mime import base
import math
# purpose is to practice writing functions and main functions

# area of a triangle, circle, rectangle


def main():
    area_triangle = units_triangle()
    print(area_triangle)

    area_circle = units_circle(5) #putting a five here makes the radius variable in the function equal to 5
    print (area_circle)
   
    area_rectangle = units_rectangle()
    print(area_rectangle)
    


def units_triangle ():
    base = float(input('What is the base of the triangle? '))
    height = float (input('What is the height of the triangle? '))
    area_triangle = (base * height)/2

    return area_triangle

def units_circle (radius):
    area_circle = math.pi *(radius **2)

    return area_circle

def units_rectangle ():
    base = float(input('What is the base of the rectangle? '))
    height = float(input('What is the height of the rectangle? '))
    area_rectangle = base*height
    return area_rectangle

# the variables you put into the parentheses of functions have to be from previously defined variables.
main()