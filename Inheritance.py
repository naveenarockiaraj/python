#Inheritance
# create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
            print(self.firstname, self.lastname)
X = Person('NAVEEN', 'ARO')
X.printname()
#Add the __init__() Function
# Add a __init__() function to the Person class:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.lastname, self.firstname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Aro", "Allen")
x.printname()
#Python also has a super() function
# that will make the child class inherit all the methods and properties from its parent:
class Person:
    def __init__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname
def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Mike", "Olsen", 2019)
x.welcome()

#Iterators
mytple = ("apple", "banana", "cherry")
myit = iter(mytple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "apple"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#Create an iterator that returns numbers,
# starting with 1 and each sequence will increase by one until stops.
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#StopIteration
class MyNumbers:
    def __iter__(self):
        self.a = 10
        return self
    def __next__(self):
        if self.a <= 50:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
  
#
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 100:
            x = self.a
            self.a += 10
            return x
        else:
            raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
        