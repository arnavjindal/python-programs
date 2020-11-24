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


"""PERFECT SOLUTION FOR IT --------------"""

# Oh soldier Prettify my Folder

# path, dictionary file, format

# def soldier("C://", "harry.txt", "jpg")

import os
def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i +=1

soldier(r"C:\Users\Haris\Desktop\testing",
        r"C:\Users\Haris\PycharmProjects\PythonTuts\ext.txt", ".png" )




