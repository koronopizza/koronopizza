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

#this Gets the character at position 1
a = "Hello, World!"
print(a[1])

#strings are arrays
#Since strings are arrays, we can loop through the characters in a string
for x in "william":
  print(x)
  
#W
#i
#l
#l
#i
#a
#m

txt = "The best things in life are hotdogs and bacon!"
if "free" in txt:
  print("Yes, 'free' is present.")
else:
  print("not here")  

#To concatenate, or combine, two strings you can use the + operator.  
z = "Hello"
y = "World"
x = z + y
print(x)

#When you compare two values, the expression is evaluated and Python returns the Boolean answer
print(10 > 9)
print(10 == 9)
print(10 < 9)

#values, such as (), [], {}, "", the number 0 evaluates to False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first
print((6 + 3) - (6 + 3))

print((4/4)+(17+22))

#To determine how many items a list has, use the len() function
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

thislist = ["cat","dog","bird"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list4 = ["tree","rock","sun"]
list5 = [3,43,2,565,6,345,55,67,3]
list6 = ["t,f,t,f,,t,f,t,f,t"]

#List items are indexed and you can access them by referring to the index number
thislist = ["apple", "banana", "cherry"]
print(thislist[2])

thislist = ["dragon","bear","flying"]
print(thislist[0])

#The insert() method inserts an item at the specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

blackblood = ["anime","watching","withyou"]
blackblood.insert(0, "friend")
print(blackblood)

# You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
thislist = ["will", "jojo", "john"]
for x in thislist:
  print(x)  
 
#  