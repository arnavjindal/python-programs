import datetime

today = datetime.datetime.today()
print(f"{today:%B %d, %M %m %Y %y}")

# print(today)


import time

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)  ##### WOW thats really Complex

print(time_string)
print(named_tuple)

first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"
print(("Hello, {first_name} {last_name}. You are {age}. " +
       "You are a {profession}. You were a member of {affiliation}.") \
      .format(first_name=first_name, last_name=last_name, age=age, \
              profession=profession, affiliation=affiliation))
