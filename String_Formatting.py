#very usefull things
#advance string formatting
# REFERENCE =  http://zetcode.com/python/fstring/
# another explaination of .format tool - https://overiq.com/python-101/numbers-in-python/#format-function

# Python f-string dictionaries

user = {'name': 'John Doe', 'occupation': 'gardener'}
print(f"{user['name']} is a {user['occupation']}")





# Python f-string debug
# Python 3.8 introduced the self-documenting expression with the = character.
import math

x = 0.8

print(f'{math.cos(x) = }')
print(f'{math.sin(x) = }')


# Python f-string objects-
class User:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def __repr__(self):
        return f"{self.name} is a {self.occupation}"

u = User('John Doe', 'gardener')

print(f'{u}')


# Python f-string format datetime
import datetime

now = datetime.datetime.now()

print(f'{now:%Y-%m-%d %H:%M}')


# Python f-string format floats-
val = 12.3
print(f'{val:.2f}')
print(f'{val:.5f}')


# Python f-string format width-
for x in range(1, 11):
    print(f'{x:02} {x*x:3} {x*x*x:$^5}')


#Python f-string justify string
s1 = 'a'
s2 = 'ab'
s3 = 'abc'
s4 = 'abcd'

print(f'{s1:>10}')
print(f'{s2:>10}')
print(f'{s3:>10}')
print(f'{s4:>10}')



# Python f-string numeric notations
# Numbers can have various numeric notations, such as decadic or hexadecimal.
# Type codes d, b, o, x can be used to format in decimal, binary, octal and hexadecimal respectively.
# Remember that while formatting integers only width is allowed not precision.

a = 300

# hexadecimal
print(f"{a:x}")

# octal
print(f"{a:o}")

# scientific
print(f"{a:e}")