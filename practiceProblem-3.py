# “Foods and Calories.”
# Problem Statement:-
# You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. You have to reserve this list of food items containing calories.
#
# You have to use the following three methods to reserve a list:
#
# 1). In build method of python
# 2). List name [::-1] slicing trick
# 3). Swap the first element with the last one and second element with second last one and so on like,
# [6 7 8 34 5] -> [5 34 8 7 6]
#
# Input:
# Take a list as an input from the user
#
# [5, 4, 1]
#
# Output:
# [1, 4, 5]
#
# [1, 4, 5]
#
# [1, 4, 5]
#
# All three methods give the same results!
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# taking input from user ---
# cal_lis = [i for i in input("enter list of Calories separated by ',' in ascending order :\n").split(",")]

cal_lis = [1200,156,55,20,10,9,4] # Hardcore list

cal_lis_copy = cal_lis[:]
cal_lis_copy1 = cal_lis[:]
# method 1
cal_lis_copy.reverse()
print(f'{cal_lis_copy} reversed by method 1')

# method 2
print(f'{cal_lis[::-1]} reversed by method 2 ')

# method 3
for i in range(int((len(cal_lis_copy1)+1)/2)):
    cal_lis_copy1[i],cal_lis_copy1[-(i+1)] = cal_lis_copy1[-(i+1)],cal_lis_copy1[i]
print(f'{cal_lis_copy1} reversed by method 3\n')

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
if cal_lis_copy == cal_lis[::-1] == cal_lis_copy1:
    print("All three methods give the same results!\n")
