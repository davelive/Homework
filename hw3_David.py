"""
Problem 1

Write a function that gets a name and a salary and prints 'Employee named --- earns ---.'
If no salary is passed to the function, print the default salary which is 100.000.
"""


def person(name,salery = "100.000"):
    print("Employee named " + name + "earns " + salery)

person("David ", "800.000")
person("Jacob ")


"""
Problem 2

Create a function that gets 3 numbers then checks if the first number falls between the 2nd and 3rd numbers.
"""

def falls(num1, num2, num3):
    if num2 < num1 and num1 < num3:
        print(str(num1) + " is falls between the 2nd and 3rd numbers")
    else:
        print(str(num1) + " is not falls between the 2nd and 3rd numbers")
falls(10,5,50)


"""
Problem 3

Create a function that gets 3 numbers and returns the biggest of them.
Hint: You can use a function inside a function. 
"""


def biggest(num1,num2,num3):
    if (num1 > num2) and (num1 > num3):
        biggestnum = num1
    elif (num2 > num1) and (num2 > num3):
        biggestnum = num2
    else:
        biggestnum = num3
    print("The biggest number is", biggestnum)

biggest(20,80,30)


"""
Problem 4

Write a function that will return the volume (ծավալ) of a cylinder (գլան). 
You can pass the radius and the height to the function. 
Google how to calculate the volume of the cylinder.
You are going to need sqrt(square root, արմատ) and pi (I show those below)
"""

import math

def cylinder_volume (height, radius):
    pi = math.pi
    volume = height * pi * radius ** 2
    print(volume)
    return volume

cylinder_volume(1, 5)


"""
Problem 5 (Calculator)

Write a function that accepts 3 variables -> number1, number2, operation.
operation can be +, -, *, /
The function should return the result of the operation with the two number.

Example: calculator(9, 3, '+') -> result is 12
In case of division, if the second number is 0, say that the operation cannot be completed.
"""

def calc(num1, num2, operation):
    if operation == '+':
        print(num1 + num2)

    elif operation == '-':
        print(num1 - num2)

    elif operation == '*':
        print(num1 * num2)
    elif operation == '/' and num2 == 0:
        print("Operation cannot be completed")
    elif operation == '/':
        print(num1 / num2)
    else:
        print("Some error text")

calc(9,3,"+")