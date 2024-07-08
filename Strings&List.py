#slicing strings
b = "Im naveen"
print(b[2:8])

b = "I'm, naveen"
print(b[-5:-2])

#modify string
#uppercase
a = "hello, world!"
print(a.upper())
#lowecase
a = "Hello, World!"
print(a.lower())
#format string
age = 26
txt = f"My name is naveen, I am {age}"
print(txt)
#multipilication
txt = f"The price is {10 * 50} Rupees"
print(txt)
#boolean
x = "value"
y = 15
z = ''
print(bool(x))
print(bool(y))
print(bool(z))
#Access List Items
 #Access the first item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[0])
#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi","melon", "mango"]
print(thislist[2:5])
#Negative Indexing
thislist = ["apple", "banana", "cherry", "orange", "kiwi","melon", "mango"]
print(thislist[-4:-1])
#Change List Items
thislist = ["apple", "banana", "cherry", "orange", "kiwi","melon", "mango"]
thislist[1] = "blackcurrant"
print(thislist)
#Add List Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "orange")
print(thislist)
#Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#Remove List Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#Remove Specified Index
#Remove the first item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(0)
print(thislist)
#Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#Delete the entire list:
# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist)
#Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#Loop Lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
#Loop Through the Index Numbers.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
#Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
