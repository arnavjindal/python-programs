# l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]
#
# # i = 1
# # for item in l1:
# #     if i%2 is not 0:
# #         print(f"Jarvis please buy {item}")
# #     i += 1
#
# for index, item in enumerate(l1):
#     if index%2==0:
#         print(f"Jarvis please buy {item}")



#                     -----------------------------------------------PROGRAMIZ--------------------------------------------------------

#                                                       Example 1: How enumerate() works in Python?

grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))



#                                                     Example 2: Looping Over an Enumerate object

grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
    print(item)

print('\n')
for count, item in enumerate(grocery):
    print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
    print(count, item)