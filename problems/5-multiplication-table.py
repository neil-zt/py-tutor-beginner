"""
Practice Exercise 5: Multiplication Table Generator

Create a program that generates multiplication tables using loops and functions:


Your program should:

1. Ask the user for the number of terms they want in the multiplication table.
2. Call the generate_table function to generate the table.
3. Display the generated multiplication table.
"""

num = int(input("Enter a number: "))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(i * j, end=" ")
    print("\n")