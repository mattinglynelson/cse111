import math

def calculate_circle_area(radius):
    return math.pi * radius **2  # return ends the execution of the current function

area = calculate_circle_area(5) # 5 gives radius its value

print (f'The area is: {area:.2f}')