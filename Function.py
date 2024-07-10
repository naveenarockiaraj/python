# Creating a Function
def my_function():
    print("Hello from a function")
my_function()
# Creating a Function with Parameters
def my_function_with_parameters(name):
    print("This"+" "+"is"+" "+ name)
my_function_with_parameters("John")
#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
#If the number of keyword arguments is unknown, add a ** before the parameter name:
def my_function(**kid):
    print("His last name is " + kid["fname"])
my_function(fname="Tobias", lname="Refsnes")
#Recursion Example
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
tri_recursion(8)
#Lambda
x = lambda a : a + 10
print(x(5))
#Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
#use the same function definition to make both functions, in the same program:
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))


