#Basic python
print('naveen')

#operator
meaning = 1
print('')

# if meaning > 10: 
#     print('Right on!')
# else:
#     print('not today')

# trnary operator
print('Right on!') if meaning > 10 else print('Not today')

#creating variables
x = 5
y = "John"
print(x)
print(y)
print(x , y)


#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


#casting the variable
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

#get the data type of a variable with the type() function
x = 5
y = "John"
z = 3.0
print(type(x))
print(type(y))
print(type(z))

#String variables can be declared either by using single or double quotes
x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)


#Multiple Variables
x, y, z = "Inova", "Swift", "Thar"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)


#unpacking collection
Cars = ["Swift", "Inova", "Thar"]
x, y, z = Cars 
print(x)
print(y)
print(z)

#mathematical operator
x = 5.5
y = 10
print(x + y + x - y)

#Global variable
B = "Engineer"

def myfunc():
  B = "Developer"
  print("I'm a" + " " + B)

myfunc()
print("I'm a " + B)

