# This task consists of a total of 10 points to evaluate your performance.
#
# Problem Statement:-
# Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute the apples. These “n” number of apples is provided to harry by his friends, and he can request for few more or few less apples.
#
# You need to print whether a number is in range mn to mx, is a divisor of “n” or not.
#
# Input:
#
# Take input n, mn, and mx from the user.
#
# Output:
# Print whether the numbers between mn and mx are divisor of “n” or not. If mn=mx, show that this is not a range, and mn is equal to mx. Show the result for that number.
#
# Example:
# If n is 20 and mn=2 and mx=5
#
# 2 is a divisor of20
#
# 3 is not a divisor of 20
#
# …
#
# 5 is a divisor of 20

try:
    a, mn, mx = input("enter n, mn, mx seperated by space: ").split()

    a,mn,mx =int(a),int(mn),int(mx)
except ValueError:
    print("enter integer values only")
    exit()
if mn == mx or a<0:
    print("enter a valid range")
    exit()

if mn >mx:
    print("enter mx greater than mn")
for i in range(mn,mx+1):

    if a%i==0:
        print(f'{i} is a divisor of {a}')
    else:
        print(f'{i} is not a divisor of {a}')


