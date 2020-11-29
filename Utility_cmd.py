import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "Something went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help="Enter first number. This is a utility for calculation. Please contact harry bhai")

    parser.add_argument('--y', type=float, default=3.0,
                        help="Enter second number. This is a utility for calculation. Please contact harry bhai")

    parser.add_argument('--o', type=str, default="add",
                        help="This is a utility for calculation. Please contact harry bhai for more")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))










#QUIZ ---
#
# import argparse
# import sys
#
# def calc(args):
#     if args.a==45 and args.b==3 and args.operator =="*":
#         return 555
#     elif (args.a==56 or args.a==9) and (args.b==9 or args.b==56) and args.operator =="+":
#         return 77
#     elif args.a==56 and args.b==6 and args.operator =="/":
#      return 4
#     elif args.operator =="+":
#      return args.a+args.b
#     elif args.operator =="-":
#       return args.a -args.b
#     elif args.operator =="*":
#        return args.a *args.b
#     elif args.operator =="**":
#       return args.a **args.b
#     elif args.operator =="%":
#       return args.a % args.b
#
#     else:
#        return "ERROR"
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--a', type=float, default=1.0,
#                         help="Enter first number. This is a utility for calculation. Please contact harry bhai")
#
#     parser.add_argument('--b', type=float, default=3.0,
#                         help="Enter second number. This is a utility for calculation. Please contact harry bhai")
#
#     parser.add_argument('--operator', type=str, default="+",
#                         help="This is a utility for calculation. Please contact harry bhai for more")
#
#     args = parser.parse_args()
#     sys.stdout.write(str(calc(args)))
#


