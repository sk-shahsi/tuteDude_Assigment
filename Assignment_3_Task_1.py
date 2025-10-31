"""
Task 1: Calculate Factorial Using a Function


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
"""
input_number = int(input("Enter a number: "))
def factorial(input_number):
    if input_number == 0:
        return 1
    else:
        return input_number * factorial(input_number-1)

print(f"factorial of {input_number} is: {factorial(input_number)}")

