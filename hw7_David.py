"""
Problem 1

Write a function that will multiply all the list items.
"""


list_of_numbers_2 = [3, 5, 15, 2, 9, 11, 10]
def multiply(numbers):
    y = 1
    for x in numbers:
        y *= x
    return y
print(multiply((list_of_numbers_2)))


"""
Problem 2

Write a program that removes duplicates from a list. DO NOT use set().
"""


list_with_duplicates = ['a', 'b', 'ab', 'a', 'c', 'ab', 'd', 'hh', 'k', 'hh']
new_list = []
for i in list_with_duplicates:
       if i not in new_list:
          new_list.append(i)
print(new_list)


"""
Problem 3

Write a program that will find the second smallest number of the list.
"""


#jnjenq dublikatnery
ls = [3, 5, 88, -1, 0, -1, 3, -7, -10, 3, 3, -7, 5, -10, 1]
new_list1 = []
for i in ls:
       if i not in new_list1:
          new_list1.append(i)
#hashvenq 2rd amenapoqr tivy
def second_smallest(numbers):
    m1 = m2 = float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

print(second_smallest(new_list1))


"""
Problem 4

Write a program that will add the string 'AAA' before every item of the list.
"""


the_list = ['chrome', 'opera', 'mozilla', 'explorer']
string = "AAA"
new_list = [string + s for s in the_list]
print(new_list)


"""
Problem 5

Try to divide a number by 0. Use try, except as a backup. 
"""


x = 12
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("ZeroDivisionError!!!")
except:
    print("something else has happened")
else:
    print("nothing went wrong")


"""
Problem 6

Make a list and then try to access an index that doesn't exist. Use try and except. 
"""


some_list = ["RAM", "CPU", "GPU", "HDD", "SSD"]
try:
    some_list[8]
except IndexError:
    print("Index doesn't exist!")


"""
Problem 7 (OPTIONAL)

1. You have a list of lists. You need to flatten the list. (Make 1 list of all the items in all lists.)
2. Do the same thing with list comprehension.
"""

#1
list_of_list = [['anna', 'bob'], ['john', 'peter'], ['sarah', 'jess', 'ben'], ['ross']]
flat_list = []
for item in list_of_list:
    flat_list += item
print(flat_list)

#2
list_of_list = [['anna', 'bob'], ['john', 'peter'], ['sarah', 'jess', 'ben'], ['ross']]
newlist = [i for s in list_of_list for i in s]
print(newlist)