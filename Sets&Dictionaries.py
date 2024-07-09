#Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)
#Loop through the set, and print the values:
for x in thisset:
    print(x)
#Add an item to a set, using the add() method:
thisset.add("orange")
print(thisset)
#Add elements from tropical into thisset:
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#Join Sets
#Union
#The union() method returns a new set with all items from both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)
#Use | to join two sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x | y
print(z)
#Join multiple sets with the union() method:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "appl"}
z = {"facebook", "pple", "amazon"}
set1 = x.union(y, z)
print(set1)
#Join a Set and a Tuple
x1 = {"a", "b", "c"}
y1 = (1, 2, 3)
z1 = x1.union(y1)
print(z1)
#Dictionary Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#Get the value of the "model" key:
x = thisdict["model"]
print(x)
#Add a new item to the original dictionary, and see that the keys list gets updated as well:
thisdict["color"] = "red"
print(thisdict)
#Update the "year" of the thisdict by using the update() method:
thisdict.update({"year": 2020})
#The pop() method removes the item with the specified key name:
thisdict.pop("model")
print(thisdict)
#You can also use the values() method to return values of a dictionary:
for x2 in thisdict.values():
    print(x2)
#You can use the keys() method to return the keys of a dictionary:
for x3 in thisdict.keys():
    print(x3)
#Loop through both keys and values, by using the items() method:
for x4, x5 in thisdict.items():
    print(x4, x5)
#Nested Dictionaries

child1 = {
    "name" : "Emil",
    "year" : 2004
  }
child2 = {
    "name" : "Tobias",
    "year" : 2007
  }
child3 = {
    "name" : "Linus",
    "year" : 2011
  }
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
#Print the name of child 2:
print(myfamily["child2"]["name"])
#Loop through the keys and values of all nested dictionaries:
for key, value in myfamily.items():
    print(key, value)
for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])