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
 
#Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["0", "1", "2"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
pokemon = ["dragonite","mewtwo","pikachu"]
for x in pokemon:
  print(x)
  if x == "dragonite":
    break
#  You can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
  thislist = ["gameboy", "gameboycolor", "gameboyA"]
for i in range(len(thislist)):
  print(thislist[i])
  
#  You can loop through the list items by using a while loop.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
  thislist = ["car", "bug", "duck"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#List Comprehension offers the shortest syntax for looping through lists
#A short hand for loop that will print all items in a list
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

thislist = ["g","h","b","y","d","s"]
[print(x) for x in thislist]

#The return value is a new list, leaving the old list unchanged.
newlist = [x for x in fruits if x != "apple"]

newlist = [x for x in fruits if x != "anime"]

#The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(10)]

newlist = [x for x in range(2134)]

#this List objects have a sort() method that will sort the list alphanumerically, ascending, by default
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["blood", "code", "punk", "metal", "king"]
thislist.sort()
print(thislist)

#this will Sort the list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = [9034, 5343, 3334, 4382, 3423]
thislist.sort()
print(thislist)

#the keyword argument "reverse = True" will change descending order
thislist = [11, 55, 66, 88, 22]
thislist.sort(reverse = True)
print(thislist)

#this will roll turn out like this: 88,66,55,22,11

#The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["this", "is", "reverses", "list"]
thislist.reverse()
print(thislist)

#Make a copy of a list with the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["love", "hate", "hope"]
mylist = thislist.copy()
print(mylist)

#Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["change", "guess", "words"]
mylist = list(thislist)
print(mylist)

# the + operator are one several ways to join, or concatenate, two or more lists in Python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["z", "y", "x"]
list2 = [11, 22, 33]

list3 = list1 + list2
print(list3)

#Another way to join two lists is by appending all the items from 1 lists to another is the append function
list1 = ["d", "e" , "f"]
list2 = [4, 5, 6]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["g", "h" , "i"]
list2 = [11, 12, 10]

for x in list2:
  list1.append(x)

print(list1)

#the extend() method, where the purpose is to add elements from one list to another list
list1 = ["lol", "rwar" , "lmao"]
list2 = [10, 20, 30]

list1.extend(list2)
print(list1)

list1 = ["red", "blue" , "colors"]
list2 = [901, 902, 903]

list1.extend(list2)
print(list1)

#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list
# this is just to help me remember most the methods of a list

#Tuples are written with round brackets
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("star", "dust", "sun")
print(thistuple)

#To determine how many items a tuple has, use the len() function
thistuple = ("love", "nana", "charactor")
print(len(thistuple))

#To determine how many items a tuple has, use the len() function
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#From Python's perspective, tuples are defined as objects with the data type 'tuple'
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

mytuple = ("a", "b", "cat")
print(type(mytuple))

#this will Print the second item in the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#this will Print the first item in the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[0])

#Negative indexing means start from the end
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Negative indexing means start from the end on this as well
thistuple = ("apple", "banana", "cherry")
print(thistuple[-2])

#You can specify a range of indexes by specifying where to start and where to end the range
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("m", "a", "n", "g", "o")
print(thistuple[1:4])

#Specify negative indexes if you want to start the search from the end of the tuple
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

thistuple = ("e", "a", "y", "g", "i", "n", "o")
print(thistuple[-5:-2])

#To determine if a specified item is present in a tuple use the in keyword
thistuple = ("p", "a", "r")
if "p" in thistuple:
  print("Yes, 'p' is in the fruits tuple")
  
#You can convert the tuple into a list, change the list, and convert the list back into a tuple
x = ("a", "b", "c")
y = list(x)
y[1] = "k"
x = tuple(y)

print(x)

#Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items, Convert this tuple into a list, remove "apple", and convert it back into a tuple
thistuple = ("tree", "leaf", "bark")
y = list(thistuple)
y.remove("tree")
thistuple = tuple(y)

thistuple = ("car", "bike", "motor")
y = list(thistuple)
y.remove("car")
thistuple = tuple(y)

#The del keyword can delete the tuple completely
thistuple = ("e", "a", "y")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists