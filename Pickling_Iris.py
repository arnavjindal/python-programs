import pickle,requests

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = requests.get(url)

lil,pikle_content = [],[]
with open("Iris_Data.txt" , "r+") as f:
    f.truncate(0)
    f.write(data.text)
    fa= f.readlines()

for j in fa:
    pikle_content.append([j.split('\n')[0]])
pikle_content.pop(150)
my_pkl_file = "Iris_Data.pkl"
with open(my_pkl_file , 'wb') as pkl_f:
    pickle.dump(pikle_content,pkl_f)
with open(my_pkl_file , 'rb') as pkl_f:
    var =pickle.load(pkl_f)
    print(var)