#Class Polymorphism
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Drive!")
class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Sail!")
class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Fly!")
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")
# boat1.move()
# plane1.move()
# for x in (car1, boat1, plane1):
#   x.move()
car1.move()

# Inheritance Class Polymorphism
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Move!")
class Car(Vehicle):
  pass
class Boat(Vehicle):
  def move(self):
    print("Sail!")
class Plane(Vehicle):
  def move(self):
    print("Fly!")
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")
for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

#Scope
x = 300#global variable
def myfunc():
  x = 200#Function variable
  print(x)
myfunc()
print(x)
#
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)
#Nonlocal is belong to outer variable
def myfunc1():
  x = "OTA"
  def myfunc2():
    nonlocal x
    x = "naveen"
  myfunc2()
  return x
print(myfunc1())

