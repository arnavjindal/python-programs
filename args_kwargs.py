# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

def funargs(normal, *argsrohan, **kwargsbala):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam": "Cook"}
funargs(normal, *har, **kw)


"""***************************************(copied from programiz)can also be used as-  ***************************************"""

def adder(*num):
    sum = 0

    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print(f"{key} is {value}")

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)

"""***************************************(copied from RealPython)can also be used as-  ***************************************"""

my_list = [1, 2, 3]
print(*my_list)  #Note that * And ** is just a unpacking operator

#Also
def my_sum(a, b, c):
    print(a + b + c)




my_list = [1, 2, 3]
my_sum(*my_list)




def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2, *list3))



my_list = [1, 2, 3, 4, 5, 6]
a, *b, c = my_list
print(a)
print(b)
print(c)



my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)
"""sameway the *args can be merged   refer-"https://realpython.com/python-kwargs-and-args/" for more """


a = [*"RealPython"]
print(a)
#string to list

*a, = "RealPython"   #Same as above
print(a)
""" the comma does a very neat work i.e.  Python requires that your resulting variable is either a list or a tuple.
                With the trailing comma, you have actually defined a tuple with just one named variable a."""























