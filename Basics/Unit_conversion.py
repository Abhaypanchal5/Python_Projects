class unit_conversion:                         # Define a class for unit conversion
    def __init__(self, value):                 # Initialize the class with a value to convert
        self.value = value
    # Define methods for various unit conversions(You can add more conversions as needed)
    def celsius_to_fahrenheit_1(self):
        return (self.value * 9/5) + 32

    def fahrenheit_to_celsius_2(self):
        return (self.value - 32) * 5/9

    def kilometers_to_miles_3(self):
        return self.value * 0.621371

    def miles_to_kilometers_4(self):
        return self.value / 0.621371

    def kilograms_to_pounds_5(self):
        return self.value * 2.20462

    def pounds_to_kilograms_6(self):
        return self.value / 2.20462
    
    def kilograms_to_grams_7(self):
        return self.value * 1000
    
    def grams_to_kilograms_8(self):
        return self.value / 1000
#get user input for the value to convert and the type of conversion   
value = float(input("Enter the value to convert: "))
converter = unit_conversion(value)

print("Select the conversion type:")  # Display a menu of conversion options for the user to choose from
# You can add more conversion options to this menu as needed, and implement the corresponding methods in the unit_conversion class to perform those conversions.
print("1. Celsius to Fahrenheit")  
print("2. Fahrenheit to Celsius")
print("3. Kilometers to Miles")
print("4. Miles to Kilometers")
print("5. Kilograms to Pounds")
print("6. Pounds to Kilograms")
print("7. Kilograms to Grams")
print("8. Grams to Kilograms")
conversion = input("Enter the conversion type (1-8): ") 
# Based on the user's selection, call the appropriate method from the unit_conversion class to perform the conversion and display the result.
if conversion == '1':
    print(f"{value} Celsius is equal to {converter.celsius_to_fahrenheit_1()} Fahrenheit.")
elif conversion == '2':
    print(f"{value} Fahrenheit is equal to {converter.fahrenheit_to_celsius_2()} Celsius.")
elif conversion == '3':
    print(f"{value} Kilometers is equal to {converter.kilometers_to_miles_3()} Miles.")
elif conversion == '4':
    print(f"{value} Miles is equal to {converter.miles_to_kilometers_4()} Kilometers.")
elif conversion == '5':
    print(f"{value} Kilograms is equal to {converter.kilograms_to_pounds_5()} Pounds.")
elif conversion == '6':
    print(f"{value} Pounds is equal to {converter.pounds_to_kilograms_6()} Kilograms.")
elif conversion == '7':
    print(f"{value} Kilograms is equal to {converter.kilograms_to_grams_7()} Grams.")
elif conversion == '8':
    print(f"{value} Grams is equal to {converter.grams_to_kilograms_8()} Kilograms.")
else:
    print("Invalid conversion type.")