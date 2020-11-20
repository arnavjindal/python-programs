

print("Enter num 1 :")
num1 = input()
print("Enter num 2 :")
num2 = input()
try: # try it else run exception and proceed
    print("Sum of these two numbers is",
          int(num1)+int(num2))
except Exception as e: # here e is just a integer
    print(e)

print("This line is very important")
