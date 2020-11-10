

print("Enter num 1 :")
num1 = input()
print("Enter num 2 :")
num2 = input()
try: # try it else run exception and proceed
    print("Sum of these two numbers is",
          int(num1)+int(num2))
except Exception as e:
    print(e)

print("This line is very important")
