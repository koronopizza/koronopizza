if 5 > 2:
  #print is an output function
  print("Five is greater than two!")
  # Python uses indentation to indicate a block of code.
  
x = "hello"
y = "world"
print(x)
print(y)
# A variable is created the moment you first assign a value to it.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

sandwich = ["bacon","lettuce","tomato"]
x,y,z = sandwich
print(x)
print(y)
print(z)
#ex showed my work

x = 5
y = "tree"
z = 5.5
print(type(x)) 
print(type(y)) 
print(type(z)) 
x = ("ant", "bug", "worm")
#tuple

#display x:
print(x)

#display the data type of x:
print(type(x)) 
x = {"name" : "jojo", "age" : 32}
#dict
#display x:
print(x)

#display the data type of x:
print(type(x)) 
x = True

#display x:
print(x)

#display the data type of x:
print(type(x)) 
#these are examples of python data types

#---------------------------------------05-1-2024
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))
#ex
a = int(4.5)

print(a)

import random

print(random.randrange(1, 1000))
