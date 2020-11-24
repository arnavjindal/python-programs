#perfect Solution - https://www.geeksforgeeks.org/python-cloning-copying-list/
#Best Way ---------
li1 = [4, 8, 2, 10, 15, 18]
li_copy = li1[:]


#2ns Best Way -----
li_copy = []
li_copy.extend(li1)


#Total 10 Ways
#Refer Link For Solution