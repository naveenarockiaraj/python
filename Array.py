# Arrays
#Get the value of the first array item
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
#Modify the value of the first array
cars[0] = "Toyota"
print(cars[0])
print(cars)
#Print each item in the cars array:
for x in cars:
    print(x)
#Adding Array Elements
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)
#Removing Array Elements
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
cars.pop(1)
print(cars)
#Create an object.
# class Car:
#     def __init__(self, name, color, kind):
#         self.name = name
#         self.color = color
#         self.kind = kind
# n1 = Car("swift", "black", "sidan")
# print(n1.color)
# print(n1.kind)
# print(n1.name)
#string representation of an object WITH the __str__() function
# class Car:
#     def __init__(self, name, color, kind):
#         self.name = name
#         self.color = color
#         self.kind = kind
#     def __str__(self):
#         return f"{self.color}{self.name}{self.kind}"
# n1 = Car("swift", "black", "sedan")
# print(n1)
#Object Methods
# class Car:
#     def __init__(self, name, color, kind):
#         self.name = name
#         self.color = color
#         self.kind = kind
#     def __str__(self):
#         return f"{self.color}{self.name}{self.kind}"
#     def display(self):
#         print(f"{self.color}{self.name}{self.kind}")
# n1 = Car("swift", "black", "sedan")
# n1.display()
#self Parameter
# class Car:
#     def __init__(Myobject, name, color, kind):
#         Myobject.name = name
#         Myobject.color = color
#         Myobject.kind = kind
#     def display(Myobject):
#         print(f"{Myobject.color}{Myobject.name}{Myobject.kind}")
# n1 = Car("swift", "black", "sedan")
# n1.display()
#Modify Object Properties
class Car:
    def __init__(self, name, color, kind):
        self.name = name
        self.color = color
        self.kind = kind
    def display(self):
        print(f"{self.color}{self.name}{self.kind}")
n1 = Car("swift","black","sedan")
n1.display()
n1.color = "red "
n1.display()
n1.name="inova "
n1.display()
n1.kind="suv "
n1.display()
#Delete Object Properties
class Car:
    def __init__(self, name, color, kind):
        self.name = name
        self.color = color
        self.kind = kind
    def display(self):
        color = self.color if hasattr(self, 'color') else 'Unknown'
        name = self.name if hasattr(self, 'name') else 'Unknown'
        kind = self.kind if hasattr(self, 'kind') else 'Unknown'
        print(f"{color} {name} {kind}")

n1 = Car("swift", "black", "sedan")
n1.display()
del n1.color
n1.display()
del n1.name
n1.display()
del n1.kind
n1.display()