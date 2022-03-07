
'''
Mattingly Nelson
1/18/22
Function Practice
'''
import math


start_odometer = float(input('What is the starting value of the odometer in miles? '))

end_odometer = float(input('What is the ending odometer value in miles? '))

fuel_input = float(input('How much fuel in gallons was used? '))



def miles_per_gallon():
    start_miles = start_odometer
    end_miles = end_odometer
    amount_gallons = fuel_input

    mpg = (end_miles-start_miles)/amount_gallons
    lpk100k = 233.215/mpg
    print(f'{mpg} miles per gallon')
    print(f'{lpk100k} liters per 100 km')
    return mpg





def main():
    miles_per_gallon()


main()