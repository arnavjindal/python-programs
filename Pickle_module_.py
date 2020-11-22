import pickle

# Pickling a python object
cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
cars2 = ("Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki")
file = "mycar.pkl"
fileobj = open(file, 'wb')
pickle.dump([cars,cars2], fileobj)
fileobj.close()

file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))







