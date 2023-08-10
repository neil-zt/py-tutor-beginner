"""
Practice Exercise 3: BMI Calculator

Design a Python program with a function:

`calculate_bmi(weight, height)`: 
    Accepts weight in kilograms and height in meters, and returns the calculated Body Mass Index (BMI).

Your program should:

1. Prompt the user for their weight and height.
2. Call the calculate_bmi function to calculate the BMI.
3. Display the calculated BMI along with a corresponding health category (e.g., underweight, normal weight, overweight, etc.).
"""

# Write your code here

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight, height)

if bmi < 18.5:
    print("underweight")
if 18.5 <= bmi < 25:
    print("normal weight")
if 25 <= bmi < 30:
    print("overweight")

    