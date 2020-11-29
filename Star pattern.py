Row = int(input("Enter number of rows: "))
bool_ = int(input("enter 0/1: "))
if bool_ ==0:
    bool_ = False
else:
    bool_ = True

if bool_ :
    for i in range(Row+1) :
        for i in range ((i)):
            print("*",end= "")
        print()
elif bool_ == False:
    for j in range(Row,0 ,-1) :
        for i in range (j):
            print("*",end= "")
        print()




