from datetime import datetime

import math
customer = input('Enter first and last name of customer: ')
width = int(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))


volume = (math.pi*(width*width)*aspect_ratio*((width*aspect_ratio)+(2540*diameter))) / 10000000000



datetime = datetime.now()


print(f'The approximate volume is {volume:.2f} liters. ')
print(datetime)

with open('volumes.txt', 'at' ) as volumes_file:
    print(f'\nDate: {datetime}, Customer: {customer}, Width of tire: {width}, Aspect Ratio: {aspect_ratio}, Diameter: {diameter}, Volume: {volume}', file = volumes_file)
   

