# supposed to be finder but not yet working

a = "ABCDCDC"
lil= []
for y in a:
    lil.append(y)
    # print(y)

find = []
b = "CDC"
for x in b:
    find.append(x)

counter =0
var = len(find)-2
for i in range(len(lil)):
    if find[0] == lil[i]:
        for j in range((len(find))):
            if i+j <= len(lil)-var:
                break
            if find[j] == lil[i+j]:
                if find[j] == find[-1]:
                    counter += 1
                else:
                    continue
            else:
                break


print(counter)
