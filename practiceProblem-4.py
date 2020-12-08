# “The Next Palindrome”
# Problem Statement:-
# A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:
#
# 676, 616, mom, 100001.
#
# You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. Your first input should be the number of test cases and then take all the cases as input from the user.
#
# Input:
# 3
#
# 451
#
# 10
#
# 2133
#
# Output:
# Next palindrome for 451 is 454
#
# Next palindrome for 10 is 11
#
# Next palindrome for 2311 is 2222
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
counter =0
n = int(input("Enter number of test cases: "))
# nums = [i for i in input("Enter numbers separated by ',' ").split(",")]
num = []

for j in range(n):
    num.append(int(input(f"Enter number {j+1} \n")))

for k in num:

    breaker = 0

    while breaker != 1:
        lis = []
        palin = k+counter
        for o in str((palin)):
            lis.append(o)

        for i in range(int((len(lis)+1)/2)):

            if lis[i] == lis[-(i+1)]:

                if i == (int(((len(lis)+1)/2)-1)):
                    print(f"Next palindrome is {palin}")
                    breaker =1
                else:
                    continue

            else:
                break

        counter += 1