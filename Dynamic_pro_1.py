#totally not an efficent way
#need memoiazation in it

def func(m,n):
    if m==1 or n ==1 :
        return 1
    elif m==0 or n == 0:
        return 0


    a=func(m-1, n)

    b =func(m, n-1)
    return a + b

print(func(18,18))