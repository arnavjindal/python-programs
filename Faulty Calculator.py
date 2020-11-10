#45 * 3 = 555, 56+9 = 77, 56/6 = 4

operator = input("enter operator")

a,b =input("enter two numbers").split()
a= int(a)
b= int(b)

print(a,b)


if a==45 and b==3 and operator =="*":
    print(555)
elif (a==56 or a==9) and (b==9 or b==56) and operator =="+":
    print(77)
elif a==56 and b==6 and operator =="/":
    print(4)
elif operator =="+":
    print (a+b)
elif operator =="-":
    print (a -b)
elif operator =="*":
    print (a *b)
elif operator =="**":
    print (a **b)
elif operator =="%":
    print (a %b)

else:
    print("Error")

