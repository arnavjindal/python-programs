# def print_formatted(number):
#     for i in range (1,(number+1)):
#         print(f"{i:>2} {oct(i).split('o')[1]:>2} {hex(i).split('x')[1].capitalize():>2} {bin(i).split('b')[1]:>2}")



# def print_formatted(number):
#     binary_len = len('{:b}'.format(number))
#     for _ in range(1, number+1):
#         for base in 'doXb':
#             print('{0:{width}{base}}'.format(_, base=base, width=binary_len), end=' ')
#         print()
#
#
#
#
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)
#
# n = int(input())
# width = len("{0:b}".format(n))
# print (width)
# for i in range(1,n+1):
#     print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

for i in range(5):
    for j in range(3):
        print(i,j)
        break