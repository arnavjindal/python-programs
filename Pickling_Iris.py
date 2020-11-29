import pickle,requests

#-WRONG APPROACH AND WRONGLY UNDERSTOOD THE EXCERCISE
#-MEANS THIS CODE NOT WRONG

# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# data = requests.get(url).text
#
# lil,pikle_content = [],[]
# with open("Iris_Data.txt" , "r+") as f:
#     # f.truncate(0)
#     # f.write(data)
#     fa= f.readlines()
#
# for j in fa:
#     pikle_content.append([j.split('\n')[0]])
# pikle_content.pop(150)
# my_pkl_file = "Iris_Data.pkl"
# with open(my_pkl_file , 'wb') as pkl_f:
#     pickle.dump(pikle_content,pkl_f)
# with open(my_pkl_file , 'rb') as pkl_f:
#     var =pickle.load(pkl_f)
#     print(var)

#PERFECT APPROACH AND SOLUTION =======================

# pickle
# Use requests module to download the iris dataset

import requests
import pickle

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# print(data)

# l1 = data.split("\n")
# print(l1)

l2 =[item.split(",") for item in data.split("\n") if len(item)!=0]
# print(l2)

with open("myiris.pkl", "wb") as f:
    pickle.dump(l2, f)


# To read this pickle file you can use this code
# import pickle
# with open("myiris.pkl", "rb") as f:
#     print(pickle.load(f))
