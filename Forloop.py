# Python For Loops
# Loop through the letters in the word "Naveen"
for letter in "Naveen":
    print(letter)
#The break Statement
# Use a break statement to exit a for loop
for letter in "Navien":
    if letter == "e":
        break
    print(letter)
#break comes after the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
#break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#Using the range() function:
for N in range(6):
  print(N)
#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
   print(x)
#Break the loop when x is 3, and see what happens with the else block:
for x1 in range(2, 30):
   if x1 == 8:
      break
   print(x1)
#Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruit = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruit:
    print(x, y)
# Functions
# Creating a Function
def my_function():
   print("Hello from a function")
my_function()
# Passing Arguments
def my_function(fname):
   print(fname + " Refsnes")
my_function("Tobias")
my_function("Emil")
my_function("Linus")