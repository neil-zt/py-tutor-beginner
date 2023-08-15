"""
Practice Exercise 1: Temperature Converter

Create a Python program that includes two functions:

1. `celsius_to_fahrenheit(celsius)`: 
    Accepts a temperature in Celsius and returns the equivalent temperature in Fahrenheit.
2. `fahrenheit_to_celsius(fahrenheit)`: 
    Accepts a temperature in Fahrenheit and returns the equivalent temperature in Celsius.

Your program should:

1. Prompt the user for a temperature and a unit (Celsius or Fahrenheit).
2. Call the appropriate function to convert the temperature to the other unit.
3. Display the converted temperature.
"""


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temp_type = input("Enter the type of temperature you are entering (C or F): ")
temp = float(input("Enter the temperature: "))

if temp_type == "C":
    print(celsius_to_fahrenheit(temp))
if temp_type == "F":
    print(fahrenheit_to_celsius(temp))

