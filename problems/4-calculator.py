"""
Practice Exercise 6: Calculator App

Create a simple calculator application using functions:

1. `add(x, y)`: Adds two numbers and returns the result.
2. `subtract(x, y)`: Subtracts the second number from the first and returns the result.
3. `multiply(x, y)`: Multiplies two numbers and returns the result.
4. `divide(x, y)`: Divides the first number by the second and returns the result.

Your program should:

1. Prompt the user for two numbers and an operation (+, -, *, /).
2. Call the appropriate function based on the chosen operation and display the result.
"""


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == "+":
    print(add(num1, num2))
if operator == "-":
    print(subtract(num1, num2))
if operator == "*":
    print(multiply(num1, num2))
if operator == "/":
    print(divide(num1, num2))

