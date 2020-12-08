# for x in range(1, 11):
#     print(f'{x:5b} {x*x:3} ${x*x*x:<5}')
# print(float("nan"))
# print('%c' % 197)


# down=0
# right =0
# def func(m,n):
#     if m==1 | n ==1 :
#         return 1
#     down =+ func(m,n-1)
#     right =+ func(m-1,n)

def memoize_coordinates(f):
    memory = {}

    # This inner function has access to memory
    # and 'f'
    def inner(m,n):
        if (m,n) not in memory:
            memory[(m,n)] = f((m,n))
        return memory[(m,n)]

    return inner

@memoize_coordinates
def func(m,n):
    if m==1 or n ==1 :
        return 1
    elif m==0 or n == 0:
        return 0


    a=func(m-1, n)

    b =func(m, n-1)
    return a + b

print(func(18,18))
#2333606220