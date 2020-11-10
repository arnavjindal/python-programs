# print("'")
#
# # # # # #
# # # # # # #
# # # # # # # mystr = "Harryisagoodboy00"
# # # # # # # # # print(len(mystr))
# # # # # # # # print(mystr[-2:-1])
# # # # # # # #
# # # # # # # # print(mystr.endswith("bdoy"))
# # # # # # # # print(mystr.count("o"))
# # # # # # # # print(mystr.capitalize())
# # # # # # # # print(mystr.replace("is", "are"))
# # # # # # # print(mystr.isalnum())


tup= (1,2,3)

lis= [{"Arnav": "Jindal"},24 ,"@"]

dict= {"Name":["Arnav", "Light"],"Surname":["Jindal",["Wave", "Particle"]]}

# print(tup[2])
# print(lis[0]["Arnav"])
# print(dict["Surname"][1][1])

d3 = dict.copy()
del d3["Surname"]
#print(d3,dict)
# d3 = d2.copy()

# d3["middle name"] = "kumar"
# print(d3)
dict.update({"Class": "XI"})  # USE THIS MORE, INSTEAD OF #31 (Line)
# print(dict)
# d2.update({"Leena":"Toffee"})
# print(d2.keys())
# print(dict.items())



dict2= dict.fromkeys(dict)
print(dict2)
# dict3=dict.values()
# print(dict3)

