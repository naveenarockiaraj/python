#If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")
  #Elif statement:
  if b < a:
    print("b is less than a")
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 30
b = 3
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
elif b < a:
  print("b is less than a")
#One line if else statement, with 3 conditions:
a = 332
b = 331
print("A Greater") if a > b else print("A is lesset") if a == b else print("B is greater")
#The and keyword is a logical operator, and is used to combine conditional statements:
a1 = 33
b1 = 200
if a1 < 1 and b1 > 2:
    print("Both conditions are True")
#The or keyword is a logical operator, and is used to combine conditional statements:
a2 = 200
b2 = 33
if a2 < 1 or b2 > 4:
    print("At least one of the conditions is True")
#The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
a3 = 33
b3 = 200
if not a3 < b3:
  print("a is NOT greater than b")
else:
  print("a is greater than b")

