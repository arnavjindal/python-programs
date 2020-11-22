import os
def soldier(path,Cap_file , renumbering_format):
    os.chdir(path)
    liss = os.listdir(path)
    liss_1 =liss.copy()
    list__22 =[]
    for j in Cap_file:
        if j in liss:
            liss.remove(j)
        else:
            pass
        f = open(j,"r+")
        list_1 = f.readlines()
        f.truncate(0)
        f.close()

        for k in list_1:
            f = open(j,"a")
            f.write(k.capitalize())

    for i in liss:
        os.rename(i,i.capitalize())

    for l in liss_1:
        var =  l.split(".")
        try:
            if var[1] == renumbering_format:
                list__22.append(l)
        except:
            pass
    for index,m in enumerate(list__22, 1):

        os.rename(m,f"{index}.{renumbering_format}")


path = "F:\AJ\Codin\Python\OH! soldier prettify my folder_Testing"
Cap_file = ["new Text Document.txt"]
renumbering_format = "png"
soldier(path,Cap_file,renumbering_format)

# if  __name__ == '__main__':
#     soldier(input('Enter the directory: '), input('Enter the dictionary file: '), input('Enter the extension: '))