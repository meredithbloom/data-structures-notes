# METHODS FOR STORING COLLECTIONS OF DATA IN PYTHON
# multiple pieces of information in the same variable



# LIST - ordered, changeable, and can have duplicate items

myfruits = ['apple', 'banana', 'kiwi', 'cherry', 'apple']
mybools = [True, False, False, True]
mynums = [1,2,4,8,444,100,-1,1]

mylist = [True, 'apple', 3, 'kiwi', True, False]

print(type(mylist))

# the list() constructor
newlist = list(('apple', 'kiwi', False))
print(newlist)

# ---------------------------------------
# ---------------------------------------

# SET - unordered, unchangeable, and unindexed. no duplicate members. cannot refer to items by index.
# set items are unchangeable, but you can remove/add items to set

myfruitsset = {'apple', 'banana', 'cherry'}
mynumsset = {1,5,-66,2,6,8}
myboolset = {True, False, False, True}

myset = {'apple', 15, True}

print(len(myset))
print(type(myset))

# the set() constructor
newset = set(('apple', 'banana', 'cherry', 'kiwi'))
print(newset)

# cannot refer to items in a set with an index. have to use "for in" loop
for x in newset:
    print(x)


# ---------------------------------------
# ---------------------------------------

# TUPLE - ordered, indexed, and *unchangeable*. allows duplicate members. cannot add, remove items after tuple has been created.

fruittuple = ("apple", "kiwi", "banana")
numtuple = (5,14,66)
booltuple = (True, False, True, True)

# must include comma if you want to create a tuple with only one item, otherwise python will not recognize as a tuple
oneitemtuple = ('banana',)

mytuple = ('apple', True, 15)

print(type(mytuple))

newtuple = tuple(('apple', 'kiwi', 'cranberry'))
print(newtuple)

# ---------------------------------------
# ---------------------------------------

# DICTIONARY (hash table implementation) - ordered, changeable, does not allow duplicates. key value pairs

mycar = {
    "brand": "Volkswagon",
    "model": "Jetta",
    "year": 2004,
    "color": "green",
    "iscool": True
}

print(len(mycar))
print(type(mycar))









