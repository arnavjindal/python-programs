
############ Open(), Read() & Readline() For Reading File #########

# file pointer(here f) returned by open function is used to read/write in file
# "rt" is default mode so it is optional to write
# Below is same as f = open("24. Tutorial.txt")

f = open("TUT_File_Reading.txt", "rt")
content = f.read()
print(content)
f.close()
# Good practice to close opened files
# Technically it is to frees/release all the resources
# using by file when it is open.



## Reading in binary mode
f = open("TUT_File_Reading.txt", "rb")
content = f.read()
print(content)
f.close()




## Reading fixed length of characters
f = open("TUT_File_Reading.txt", "rt")
content = f.read(4)
print(content)

content = f.read(4)
print(content)
f.close()


# Reading more than available characters
f = open("TUT_File_Reading.txt", "rt")
content = f.read(344555)
# It will print till available character
print("1 :",content)

content = f.read(344555)
# Nothing left to read now
print("2 :",content)

f.close()




## Printing character by character in each line

f = open("TUT_File_Reading.txt", "rt")
content = f.read()
for line in content:
    print(line)
f.close()
# Output :
# W
# e

# a
# r
# e

# o
# n
# ...............

## Printing line by line using itreater in file

f = open("TUT_File_Reading.txt", "rt")
content = f.read()
for line in f:
    print(line)
f.close()
# Output : Nothing because content has already read the file

f = open("TUT_File_Reading.txt", "rt")
# content = f.read()
for line in f:
    print(line)
f.close()
# Output : (print by default give a backslash end character and file also have new line charcter when we write next line in file)
# We are on a mission to transform and Optimize World with Indian Technologies.

# We will work hard.

# We will win.

f = open("TUT_File_Reading.txt", "rt")
# content = f.read()
for line in f:
    print(line,end="")
f.close()
# Output : (print bydefault give a backslash end character)
# We are on a mission to transform and Optimize World with Indian Technologies.
# We will work hard.
# We will win.






##### readline function to read one line a time

f = open("TUT_File_Reading.txt", "rt")
print(f.readline())
f.close()
# Output :
# We are on a mission to transform and Optimize World with Indian Technologies.

f = open("TUT_File_Reading.txt", "rt")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()





########## Readlines Function to get list of lines.

f = open("TUT_File_Reading.txt", "rt")
print(f.readlines())
f.close()

