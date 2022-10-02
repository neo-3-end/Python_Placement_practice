x = int(3)
y = float(3)
print(x) #Prints 3.
print(y) #Prints 3.0
print('------------')
print('Unpacking Wxample')
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print('Global Variables Example')
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)