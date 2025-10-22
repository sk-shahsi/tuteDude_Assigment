"""
Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
"""
FirstNumber=int(input("Enter the first number: "))
SecondNumber=int(input("Enter the second number: "))
def addition(FirstNumber,SecondNumber):
    Addition=FirstNumber+SecondNumber
    print("Addition: ",Addition)

def subtraction(FirstNumber,SecondNumber):
    Subtraction=FirstNumber-SecondNumber
    print("Subtraction: ",Subtraction)

def multiplication(FirstNumber,SecondNumber):
    Multiplication=FirstNumber*SecondNumber
    print("Multiplication: ",Multiplication)

def division(FirstNumber,SecondNumber):
    Division=FirstNumber/SecondNumber
    print("Division: ",Division)

addition(FirstNumber,SecondNumber)
subtraction(FirstNumber,SecondNumber)
multiplication(FirstNumber,SecondNumber)
division(FirstNumber,SecondNumber)