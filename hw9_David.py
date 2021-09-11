"""
Problem 1

Write a function that gets a set and an item. It returns the set without the item if it was present in the set.
"""

def problem1(p1):
    p1.clear()
    return p1

someset = {"apple", "banana", "cherry"}
print(problem1(someset))


"""
Problem 2

Write a program that gets two sets. If they have the same items it deletes those items from both sets 
and prints them.
"""


thisset1 = {1, 2, 3, 4}
thisset2 = {4, 5, 6, 7}
newset = (list(thisset1) + list(thisset2))
temp_list = []
for i in newset:
    if i not in temp_list:
        temp_list.append(i)
my_list = temp_list
print(my_list)


"""
Problem 3

You have a list of tuples. Remove the tuples that have length 1.
"""


test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
problem3 = [x for x in test_list if len(x) != 1]
print(str(problem3))


"""
Problem 4

You have two tuples.
Create tuples of all combinations of those tuple elements and store them in a list.
"""


tuple1 = (1, 5)
tuple2 = (7, 2)
combination = [(a, b) for a in tuple1 for b in tuple2]
tuple_list = list(combination + [(a, b) for a in tuple2 for b in tuple1])
print(tuple_list)


"""
Problem 5

Convert a tuple to a float data type.
Example: (9, 56) - 9.56
"""

num = (9, 56)

res = float('.'.join(str(x) for x in num))
print(str(res))


"""
Problem 6 

Write a program that will sort tuples by their maximum element.
"""

list1 = [(4, 5, 20, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]

def problem6(sub):
    return max(sub)
list1.sort(key=problem6, reverse=True)

print("Sorted by maximum elements: " + str(list1))
