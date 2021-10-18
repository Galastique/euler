#I dont know what to call these
"""
list = ["apple", "banana", "cherry"]               (allows duplicates) 
tuple = ("apple", "banana", "cherry")
set = {"apple", "banana", "cherry"}                (does not allow duplicates)
dictionary = {"name": "apple", "color": "green"}
"""

#Bind variables
"""
x, y, z = "Orange", "Banana", "Cherry"      (assign multiple variables at the same time)
x = y = z = "Orange"                        (assign value to multiple variables)
print(type(x))                              (get the type of variable)

(from inside function)
global x                (makes variables available anywhere in the code)
x = "fantastic"


fruits = ["apple", "banana", "cherry"]      (unpack a list into variables)
x, y, z = fruits
"""

#Basic programming operations
"""
if x > y:           (if statement)
elif x > y:         (else if)
else:               (else)
while x > y:        (while loop)
for x in y:         (for loop)

pass        (avoids errors for empty statements)
break       (exits out of loop)
continue    (goes back to start of loop (I think))

and         (both conditions must be true)
or          (only one of the conditions must be true)
not(if x > y):         (similar to ! in js)

is          (both objects must be the same)
is not      (both objects must not be the same)

in          (searches for something in list)
not in

def myfunc():                   (define function)
  print("Hello world")          (set of commands)

myfunc()                        (executes function)
"""

#Data types
"""
Text Type:	    str
Numeric Types:	int, float, complex         (int will be floored if decimal)
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""

#Random
"""
import random

print(random.randrange(1, 10))
"""

#Specific characters from variable/list
"""
https://www.w3schools.com/python/python_lists_comprehension.asp

print(len(x))       (returns how many characters are in the variables)
print(x[1])         (returns second character)
print(x[-1])        (returns last character)
print(x[2:5])       (returns characters from 2 to 5)
print(x[:5])        (returns characters from start to 5)
print(x[2:])        (returns characters from 2 to end)
print(x[-5:-2])     (returns characters from -5 to -2 (count backwards from the end))

print(len(thislist))    (returns amount of items in list)
print(thislist[1])      (returns second item from list)
print(thislist[-1])     (returns last item from list)
print(thislist[2:5])    (returns items 2 to 5)
print(thislist[:5])     (returns items from start to 5)
print(thislist[2:])     (returns items from the second to the end)
print(thislist[-5:-2])  (returns items from -5 to -2 (count backwards from the end))

thislist[1] = "orange"                      (replaces second item with "orange")
thislist[1:3] = ["orange", "watermelon"]    (replaces item 2 and 3)
thislist.insert(2, "watermelon")            (inserts "watermelon" as third item)
thislist.append("orange")                   (adds to list)
thislist.remove("banana")                   (removes "banana")
del thislist[0]                             (removes first item)
thislist.pop()                              (removes last item)
thislist.pop(1)                             (removes second item)

del thislist                                (deletes list)
thislist.clear()                            (removes all items from list)

thislist.extend(thislist2)                  (combines two lists together)
thislist.extend(thistuple)                  (adds tuple to list)

set1.update(set2)                           (adds set to another set)
set3 = set1.union(set2)                     (creates new set with 2 other sets)


thisdict = {              (dictionary example)
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"])          (get value)
x = thisdict["model"]             (assign key to variable)
thislist["color"] = "white"       (assign new key)
thisdict.update({"year": 2020})   (change value)
del thisdict["model"]             (remove key)
thisdict.clear()                  (empty dictionary)

https://www.w3schools.com/python/python_dictionaries_nested.asp     (multiple dics)
https://www.w3schools.com/python/python_dictionaries_methods.asp

x = thisdict.keys()       (get the "types" of values)


https://www.w3schools.com/python/python_sets_methods.asp

https://www.w3schools.com/python/python_lists_methods.asp

for x in "banana":  (returns every character one by one)
  print(x)

for x in thislist:  (returns every item one by one)
  print(x)

txt = "The best things in life are free!"       (searches for something specific in string)
print("free" in txt)

txt = "The best things in life are free!"       (same thing but if its not there)
print("expensive" not in txt)
"""

#Changes variables
"""
https://www.w3schools.com/python/python_strings_methods.asp

print(x.upper())                (returns string in uppercase)
print(x.lower())                (returns string in lowercase)
print(x.strip())                (will remove whitespaces from start and end of string)
print(x.replace("H", "J"))      (will replace every "H" with "J")
print(x.split(","))             (will split string into substrings if it finds ",")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))                  (changes int into a string)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."     (you can add numbers in the brackets to make sure they use the right variables)
print(myorder.format(quantity, itemno, price))              (like above, but with multiple variables)

thislist.sort()                   (sort list in alphabetical order)
thislist.sort(reverse = True)     (sort list in reverse alphabetical order)
mylist = list(thislist)           (creates copy of a list)
list3 = list1 + list2             (combines multiple lists)
list1.extend(list2)               (other way to combine lists)
"""

#While loops
"""
i = 0
while i < len(thislist):    (runs once for every item in list)
  print(thislist[i])
  i = i + 1


"""

#For loops
"""
newlist = [<expression> for <item> in <iterable> if <condition> == True]        (syntax)

thislist = ["apple", "banana", "cherry"]    (runs once for every item in list)
[print(x) for x in thislist]

range(2, 30, 3)       (numbers from 2 to 29, in increments of 3)
----
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:        (for each item in list)
  if "a" in x:          (if item has "a")
    newlist.append(x)   (add item to other list)
----


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]               (adds every item from "fruits" to "newlist" if they arent "apple")

newlist = [x for x in range(10)]    (creates a list of numbers from 1 to 10)

"""
x = 5
y = 1

while x > y:  
    print("Hello there")
    x = x-1