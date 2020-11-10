'''INTRO TO GLOBAL LOCAL VARIABLES'''

# l = 10 # Global
#
# def function1(n):
#     # l = 5 #Local
#     m = 8 #Local
#     global l
#     l = l + 45
#     print(l, m)

# # print(m)


def harry():
    x = 20
    def rohan():
        global x # CHANGES GLOBALLY MEANS CHANGES OUTSIDE OF ALL FUNCTIONS MEANS EVEN OUTSITE "HARRY".
        x = 88
    # print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

harry()
print(x)


