'''
                                                                                            'Learn from Mistakes'


Author: Arnav
Date: 8 Dec 2020
Purpose: Practice problem
'''


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
n = int(input("Enter number of test cases: \n"))
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
                    print(f"Next palindrome is {palin}\n")
                    breaker =1
                else:
                    continue

            else:
                break
        counter += 1

# really poor execution of program
# I forgot to use the three methods he taught in last problem (I picked the hardest Method)
# CWH's execution (Pretty neat):
'''
Author: Harry
Date: 15 April 2019
Purpose: Practice Problem For CodeWithHarry Channel 
'''


def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    n = int(input("Enter the number of test cases\n"))
    numbers = []
    for i in range(n):
        number = int(input("Enter the number:\n"))
        numbers.append(number)

    for i in range(n):
        print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")