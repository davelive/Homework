"""
Problem 1

Create 3 dictionaries for your favourite top 3 cars. Dict should contain information like brand, model, year, and color.
Add all those dicts in one dict and print items. 
"""


car1 = {
    "brand": "Audi",
    "model": "R8",
    "year": 2015,
    "colors": ["White"]
}
car2 = {
    "brand": "Chevrolet",
    "model": "Corvette",
    "year": 2009,
    "colors": ["Yellow", 'Black']
}
car3 = {
    "brand": "Mitsubishi",
    "model": "Eclipse",
    "year": 1995,
    "colors": ["Red", 'Green']
}
fav_cars = {**car1, **car2, **car3}
print(list(fav_cars.items()))


"""
Problem 2

You have a list of lists. Each list in the list contains a key and a value. Transform it into a list of dictionaries. 
Use loops.
"""


ls = [['Bob', 45], ['Anna', 4], ['Luiza', 24], ['Martin', 14]]
my_dict = dict()
for i,v in ls:
  my_dict[i] = v
print(my_dict)


"""
Problem 3

Check if value 1000 exists in the dict values. If yes delete all other items except that one.
"""


dt = {'hundred': 100, 'million': 1000000, 'thousand': 1000, 'ten': 10}
if 1000 in dt.values():
    ts = dt['thousand']
    dt.clear()
    dt['thousand'] = ts
print(dt)


"""
Problem 4

Change Narine's salary to 10000
"""


sampleDict = {
     'employee1': {'name': 'Marine', 'salary': 7500},
     'employee2': {'name': 'Karine', 'salary': 8000},
     'employee3': {'name': 'Narine', 'salary': 6500}
}
sampleDict.update({"employee3": {'name': 'Narine', 'salary': 10000}})
print(sampleDict)


"""
Problem 5

Write a function that will get a dict of employees and their salaries. It will return a new dict with 
the same keys (employees) and all values will be the average of their salaries. 
example:  dict1 = {'ann': 3000, 'bob': 4000, 'lily': 5000}
          dict2 = {'ann': 4000, 'bob': 4000, 'lily': 4000}
"""

dict1 = {'ann': 3000, 'bob': 4000, 'lily': 5000, 'molly': 5500, 'david': 500}
def problem5(dict1):
    avr = 0
    for x in dict1.values():
        avr += x // len(dict1.values())
    for i in dict1:
        dict1.update({i: avr})
    return dict1

print(problem5(dict1))


"""
Homework 7 Problem 4

Write a program that will add the string 'AAA' as an item before every item of the list.


"""

the_list = ['chrome', 'opera', 'mozilla', 'explorer']
new_list = [v for s in the_list for v in ('AAA', s)]
print(new_list)