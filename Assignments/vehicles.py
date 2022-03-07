def main():
    # Create a dictionary that contains data about six vehicles.
    # The key for each vehicle in the dictionary is the vehicle's
    # identification number (VIN). The value for each vehicle is
    # a list that contains the year, manufacturer, model, color,
    # engine design, and engine displacement.
    vehicles= [
        # VIN: [year, manufacturer, model, color, eng_design, eng_displace]
        {'vin_number': "1J4GL48K4UF993861" ,'year':2002, 'manufacturer':"Jeep",'model': "Liberty", 'color':"blue", 'eng_design':"V6", 'engine displacement':3.7},
        {'vin_number': "1YVGF22C8AN381568" ,'year':2002, 'manufacturer':"Mazda",'model': "626", 'color':"white", 'eng_design':"I4", 'engine displacement':2.0},
        {'vin_number': "WP0AA0926HG410293" ,'year':1987, 'manufacturer':"Porsche",'model': "924S", 'color':"red", 'eng_design':"I4", 'engine displacement':2.5},
        {'vin_number': "5TDZA23CXTU102983" ,'year':2006, 'manufacturer':"Toyota",'model': "Sienna", 'color':"gold", 'eng_design':"V6", 'engine displacement':3.3},
        {'vin_number': "1GKKVRED5ZL382610" ,'year':2011, 'manufacturer':"GMC",'model': "Acadia", 'color':"charcoal", 'eng_design':"V6", 'engine displacement':3.5},
        {'vin_number': "2T3BF4DV9QR146782" ,'year':2012, 'manufacturer':"Toyota",'model': "RAV 4", 'color': "green", 'eng_design':"I4", 'engine displacement':2.5,}
    ]

    # MANUFACTURER_INDEX = 1
    # MODEL_INDEX = 2
    # COLOR_INDEX = 3

    # Ask the user for a vehicle identification number (VIN).
    vin = input("Please enter a VIN: ")

    # Check if the vin is a key that is in the vehicles dictionary.
    if  vehicles['vin_number']== vin :

        preferred_info = input('What info whould you like on the car? ')

        # Find the data for the vehicle that the user wants.
        print(vehicles[f'{preferred_info}'])
        
        # Print the manufacturer, model, and color of the vehicle.
        print(vehicles['manufacturer','model','color'])

        # Don't print the year, engine design, or displacement.

    else:
        # Print a message stating that the VIN entered
        # by the user is not in the dictionary.
        print(f"{vin} is not in the dictionary.")


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
