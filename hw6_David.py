"""
Problem 1

Create a file manually with some text in it like "My favourite fruits are:".
Then write a program to append the file with the fruits that you love.
"""


file = open(r'C:\Users\davel\homework\problem1.txt', "a")
file.write("My favourite fruits are: ")
fav_fruits = input("Enter your favourite fruits: ")
file.write(fav_fruits)
file.close()


"""
Problem 2

Create a file that has 5 or more lines of text.
Write a program to store each line in a variable.
"""


with open(r'C:\Users\davel\homework\lines.txt', "r") as lines:
    q = (lines.readline())
    w = (lines.readline())
    e = (lines.readline())
    r = (lines.readline())
    t = (lines.readline())
print(q)
print(w)
print(e)
print(r)
print(t)


"""
Problem 3

Find the longest word in the file pr3.txt.

"""


f = open(r"C:\Users\davel\homework\pr3.txt")
s = f.read()
lst = s.split()
print(max(lst, key=len))
file.close()

"""
Problem 4

Create a list of names of all our group members.
Loop over the list and create files (filename = name).
Each file should contain the name of a person repeated as many times as the characters of the name.

for example: file -> Ani.txt
              text - > Ani
                       Ani
                       Ani
Ani is repeated 3 times as it has 3 characters.
"""


members = ['Ani',"David","Arsen","Arthur","Alik"]
for x in members:
    cr = open(rf"C:\Users\davel\homework\{x}.txt", "a")
    for i in x:
        print(cr.write(x + "\n"))
file.close()

"""
Problem 5

After writing Problem 4 write a function that gets this list and checks if files with these names exist. 
If a file exists return True, otherwise False.
"""

new_names = ['Ani', 'Armen', 'Aren', 'Argishti', 'Arsen', 'Alik', 'Anahit', 'Anna']

def problem5():
    for x in new_names:
        if x in members:
            print(x + " True")
        else:
            print(x + " False")

problem5()


"""
Problem 6

Write a function that gets a file path and calculates how many upper case letters are in the text.
Hint: use isupper() method.
"""

def count():
    file = open(r"C:\Users\davel\homework\pr6.txt")
    data = file.read()
    count = 0
    for letter in data:
        if letter.isupper():
            count += 1
    print(count)
    file.close()

count()


"""
Problem 7 (OPTIONAL)

Write a program to show the frequency(how many times a word appears in the text) of each word. 
Hint: set()
"""

p7 = open(r"C:\Users\davel\homework\pr7.txt")
str = (p7.read())

def freq(str):
    str_list = str.split()
    unique_words = set(str_list)
    for words in unique_words:
        print('Frequency of', words, str_list.count(words), "times")

freq(str)
