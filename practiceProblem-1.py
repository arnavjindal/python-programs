"""YOUR AGE IN 2090"""


# Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).
#
# Here are a few instructions that you must have to follow:
#
# Do not use any type of modules like DateTime or date utils. (-5 points)
# Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
# Your code should handle all sort of errors like:                       (2 points)
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible!

#My Solution
yob_age = input("enter your YOB or age: ")

if len(yob_age) == 4:
    year_born =int(yob_age)
    age_present = 2020-int(year_born)
    if age_present>150:
        print("you seems to be the oldest person alive")
    if int(yob_age)>2020:
        print("Hey you lil bastard who is still in production !!")
    else:
        print("its a YOB ")
        year_born =int(yob_age)
        print(f"your present age is {age_present}" if age_present!=0  else "welcome to the world boiii")
        print(f"you will turn 100 in the year: {year_born+100}")

elif len(yob_age) in (1,2,3):
    year_born = 2020-int(yob_age)
    if 2020-year_born>150:
        print("you seems to be the oldest person alive")
    if int(year_born)>2020:
        print("Hey you lil bastard who is still in production !!")

    else:
        print("its an age")
        print(f'you were born in {year_born}' if year_born !=2020  else "welcome to the world boiii" )
        print(f"you will turn 100 in the year :{year_born+100}")

while True:
    opo =input("enter the year yo wanna check out age of your self else enter Quit(q)")
    if  len(opo) in (4,5):
        opo =int(opo)
        print(f"your age in {opo} is {opo-year_born}")
    else:
        print("breaking the loop")
        break





# Solution that is just perfect you say--------------------------.

yearAge = int(input("What is your Age/Year of birth\n"))
isAge = False
isYear = False

if len(str(yearAge)) == 4:
    isYear = True

else:
    isAge = True

if(yearAge<1900 and isYear):
    print("You seem to be the oldest person alive")
    exit()

if(yearAge>2019):
    print("You are not yet born")
    exit()

if isAge:
    yearAge = 2019 - yearAge

print(f"You will be 100 years old in {yearAge + 100}")

interestedYear = int(input("Enter the year you want to know your age in\n"))

print(f"You will be {interestedYear - yearAge} years old in {interestedYear}")



