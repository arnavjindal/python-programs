def fibonacci_iterative(n):

    num=0
    a=0
    b=1
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        for i in range (n-2):
            num = a+b
            a=b
            b=num

        return num





n=int(input("N: "))
def fibonacci_recursive(n):

    if n ==1:
        return 0
    elif n== 2:
        return 1
    else:
        return fibonacci_recursive(n-2)+fibonacci_recursive(n-1)




print(fibonacci_recursive(n))
print(fibonacci_iterative(n))