
"""
Problem 1
You have two strings. Put one in the middle of the other one.

Example: s1 = "Environment", s2 = "Earth", result should be "EnviroEarthnment"
"""


s1 = "University"
s2 = "Earth"
new_txt = s1[:6] + s2 + s1[6:]
print(new_txt)


"""
Problem 2

You have five strings. Create two strings, 1 containing all the beginning letters of the five strings,
and 1 containing all the ending letter of the 5 strings.
"""


t1 = "qwerty"
t2 = "asdfg"
t3 = "tyu"
t4 = "1234"
t5 = "p"

beginning = t1[:1] + t2[:1] + t3[:1] + t4[:1] + t5[:1]
print(beginning)
ending = t1[-1:] + t2[-1:] + t3[-1:] + t4[-1:] + t5[-1:]
print(ending)


"""
Problem 3

Create a function that gets a name. If the length of the name is odd (կենտ) it returns the name all in upper case.
If the length of the name is even (զույգ) just return it.
"""


def problem3(name):

    if (len(name)) % 2 == 0:
        return name
    else:
        print(name.upper())

problem3("David")


"""
Problem 4

You have a CNN article. You want to find out how many time the words 'university', 'vaccine', 
'student' (but not 'students') appear in the text. 
You also want to find out how many numbers from 1 to 5 can be found in the text.
"""
article = """ (CNN)The University of Virginia has disenrolled 238 students for its fall semester on Friday for not 
complying with the university's Covid-19 vaccine mandate, according to a university spokesperson.
UVA requires "all students who live, learn, or work in person at the university" to be fully vaccinated 
for the upcoming 2021-2022 academic year, according to current university Covid-19 policies.
Out of the 238 incoming Fall semester students, only 49 of them were actually enrolled in classes, and the remaining 
189 "may not have been planning to return to the university this fall at all," UVA spokesperson Brian Coy told CNN.
"Disenrolled means you're not eligible to take courses," Coy said. 
He added that students who were enrolled at the university on Wednesday still have a week to update their status 
at which point they can re-enroll.
"""

x = str(article.count('university'))
z = str(article.count('vaccine'))
y = (article.count('student')) - (article.count('students'))

print("Word university - " + x)
print("Word vaccine - " + z)
print("Word student - " + str(y))

print("Numbers from 1 to 5 founded in the text" , article.count("1") + article.count("2") + article.count("3") + article.count("4") + article.count("5") , "times")


"""
Problem 5

Find out if there is '2021-2022' string in the article and slice it. 
"""


a = article.find("2021-2022")
b = len("2021-2022")
print(article[a:a + b])


"""
Problem 6 

Create a function that gets a string and returns the same string but the half of it UPPERCASE.
(It's okay if the string has odd number of characters and half is not the exact half)
"""


def problem6(text):
    str_len = len(text)
    poqr = text.lower()
    mec = text.upper()
    half = str_len - int(str_len / 2)
    printstr = poqr[:half] + mec[half:]
    return(printstr)

print(problem6("muradyan"))


"""
Problem 7 

Write a function that takes a name and a (future) profession and returns the sentence
"I am Ani Amirjanyan and I am a backend developer.".
Use .format or f" "
"""


def problem7 ():
    name = "David Muradian"
    profession = "backend developer"

    txt = "I am {0} and I am a {1}".format(name, profession)
    txt1 = f"I am {name} and I am a {profession}"

    print(txt)
    print(txt1)

problem7()


"""
Problem 8

Create a function that takes a 3 digit number (can't take more or less digits) and returns the reverse number.
Example: take "987" return 789. (It is okay if the result starts with 0)
"""

def reverse():
    l = list(input("please enter a 3 digit numbers = "))
    print(l[2], l[1], l[0])

reverse()