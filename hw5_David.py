"""
Problem 1

You have a list, you want to iterate over it and return the numbers that are divisible by 5.
If you iterate over a number larger than 500, stop the loop.
"""


list = [5, 11, 30, 45, 175, 99, 106, 300, 490, 512, 890, 1000]

N = 5
for num in list:
	if(num%N==0 and num <= 500):
		print (num)


"""
Problem 2

Create a loop to print the reverse of a list. 
"""
list1 = [1, 2, 3, 4, 5]

for i in range(len(list1) // 2):
    list1[i], list1[-1 - i] = list1[-1 - i], list1[i]

print(list1)


"""
Problem 3

Write a function to get a number and return the factorial of the number. Use loops. 
ex. factorial of 5 is 1*2*3*4*5
You can't count factorial of negative numbers, and the factorial of 0 is 1. 
"""

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

n = int(input("Enter a number: "))

"""
Problem 4

Write a code that would print list items that are at even positions. 
ex. in list = [10, 11, 12], 10 is at index 0, 11 - index 1 (odd), 12 - index 2 (even)
Use loops.
"""


test_list = [10, 11, 12, 13, 14, 15, 16]

odd = []
even = []
for i in range(0, len(test_list)):
    if i % 2:
        even.append(test_list[i])
    else:
        odd.append(test_list[i])

res1 = odd
res2 = even
print("Odd numbers list: " + str(res1))
print("Even numbers list: " + str(res2))


"""
Problem 5

Write a function that gets a list of names and returns the ones that start with A.
Notice that some list items begin and end with spaces, or start with @. Get rid of space and @ before printing the name.
"""


def problem5(names):
    for x in names:
        num1 = (x.replace("@"," "))
        num2 = (num1.strip())
        for y in num2:
            if y[0] == "A":
                print(num2)

names = [' Anna', "Lily", " Anahit ", "@Bob", "@Ani@", " Luiza@", "@@Armen"]

problem5(names)
"""
Problem 6

Write a program that checks if a number is prime (պարզ) or not. Try not to google. :) 
"""


num = int(input("Enter the number to checks if it's prime or not: "))
if num > 1:
    for i in range(2, num//2):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
            print(num, "is a prime number")


"""
Problem 7 (OPTIONAL)

Write a loop that will print this pattern.

* 
* * 
* * * 
* * * * 
* * * * *

Hint: print("\r") -> for printing on a new line, 
      print('*', end=' ') -> for printing on the same line

"""

tox = 5
for i in range(0, tox):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")