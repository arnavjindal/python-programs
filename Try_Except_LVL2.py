

try:
    f = open("does2.txt")

except EOFError as e:
    print("Print eof error aa gaya hai", e)

except IOError as e:
    print("Print IO error aa gaya hai", e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")

print("Important stuff")


"""
Try         Not running     Running
Except      Will run        Will not run
Else        Will not run    Will run
Finally     Will run        Will run

"""



