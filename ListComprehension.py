#List Comprehension
fruits = ["naveen", "nivas", "new", "news", "navas"]
newlist = []
for x in fruits:
  if "i" in x:
#   if "a" in x:
#   if "w" in x:
    newlist.append(x)
    print(newlist)
#Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
#With no if statement:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)
#Iterable
# You can use the range() function to create an iterable:
newlist = [x for x in range(100)]
print(newlist)
#Accept only numbers lower than 5:
newlist = [x for x in range(100) if x < -5]
print(newlist)
#Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
print(newlist)
#Set all values in the new list  to 'naveen':
newlist = ['naveen' for x in fruits]
print(newlist)
#Sort Lists
#Sort List Alphanumerically
newlist = sorted(fruits)
print(newlist)
#Sort the list numerically:
newlist = sorted([1, 5, 6, 3, 3])
print(newlist)
#Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#Join Two Lists
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [list2 + list1]
print(list3)
#Append list2 into list1:
for x in list1:
  list2.append(x)
print(list2)
#Extend method to add list2 at the end of list1:
list1.extend(list2)
print(list1)
# Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
# Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double parentheses
print(thistuple)
#Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#Range of Indexes
thistuple =("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
# Update Tuples
#Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#Unpack Tuples
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#Using Asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
#Multiply the fruits tuple
fruits = (2, 2, 55)
mytuple = fruits * 2
print(mytuple)
