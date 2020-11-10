
# Iterating a list of lists
list1 = [ ["Arnav", 1], ["Larry", 2],
          ["Carry", 6], ["Marie", 250]]
# for item in list1:
# print(item)
# Output :
# ['Vivek', 1]
# ['Larry', 2]
# ['Carry', 6]
# ['Marie', 250]

# Iterating a dictionary
dict1 = dict(list1)
print(dict1)
for item in dict1:
    print(item) # It will print only keys
# Output :
# Vivek
# Larry
# Carry
# Marie
print(dict1)
print(dict1.items())

for item, lollypop in dict1.items():

    if item[-3:] =="rry":
        print(item,  lollypop)
