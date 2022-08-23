'''
DICTIONARIES

'''

'''
A dictionary stores key-value pairs, where each unique key is an index which holds the value associated with it.
Information is stored in pairs of words and meanings
Dictionaries are unordered because the entries are not stored in a linear structure.
The dictionary’s content is inside curly brackets, {}

A key-value pair is written in the following format:
key:value

Since the dictionary is an unordered data structure, the order of the output will not necessarily match the order in which we wrote the entries. Key-value pairs are accessed in a random or unordered manner.
'''

'''
Creating a Dictionary
'''
empty_dict = {}  # Empty dictionary
print(empty_dict)

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

'''
The dict() Constructor#
As the name suggests, the dict() constructor can be used to construct a dictionary. Think of the “constructor” as an operation that gives us a dictionary.

If our keys are simple strings without special characters, we can create entries in the constructor. In that case, values will be assigned to keys using the = operator.

A popular practice is to create an empty dictionary and add entries later.

The keys and values can have any of the basic data types or structures.

Two keys can have the same value. However, it is crucial that all keys are unique.
'''
empty_dict = dict()  # Empty dictionary
print(empty_dict)

phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# Keys will automatically be converted to strings
print(phone_book)

# Alternative approach
phone_book = dict([('Batman', 468426),
                   ('Cersei', 237734),
                   ('Ghostbusters', 44678)])
print(phone_book)

'''
Accessing Values
'''

'''
we can access a value by enclosing its key in square brackets, []. This is more meaningful than the integer indices we use for tuples and lists.
we can use the get() method as follows:

a_dictionary.get(key)
'''
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book["Cersei"])
print(phone_book.get("Ghostbusters"))

'''
Adding/Updating Entries
We can add new entries in a dictionary by simply assigning a value to a key. 
Python automatically creates the entry.
If a value already exists at this key, it will be updated
'''
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

phone_book["Godzilla"] = 46394  # New entry
print(phone_book)

phone_book["Godzilla"] = 9000  # Updating entry
print(phone_book)

'''
Removing Entries
To delete an entry, we can use the del keyword:
'''
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

'''
To delete elements, the pop() or popitem() methods would work better
'''
phone_book = {"Ivan": 468426,
              "Petar": 237734,
              "Maya": 44678}
print(phone_book)

maya = phone_book.pop("Maya")
print(phone_book)
print(maya)

# Removes and returns the last inserted pair, as a tuple
# In Python versions before 3.7, popitem() removes and returns the random item
lastAdded = phone_book.popitem()
print(lastAdded)

del phone_book["Petar"]
print(phone_book)

'''
Calculate length of dictionary with len()
'''
phone_book = {"Ivan": 468426,
              "Petar": 237734,
              "Maya": 44678}
print(len(phone_book))

'''
Check existence with in keyword
'''
phone_book = {"Ivan": 468426,
              "Petar": 237734,
              "Maya": 44678}
print("Ivan" in phone_book)
print("Godzilla" in phone_book)

'''
Copying Contents
To copy the contents of one dictionary to another, we can use the update() operation
'''
phone_book = {"Ivan": 468426,
              "Petar": 237734,
              "Maya": 44678}

second_phone_book = {"Harry": 67423, "Jaime": 237734, "Godzilla": 37623}

# Add secondphone_book to phone_book
phone_book.update(second_phone_book)
print(phone_book)

'''
Dictionary Comprehension
to iterate the dictionary, we’ll use the dict.items() operation which turns a dictionary into a list of (key, value) tuples
'''
houses = {1: "House1", 2: "House2", 3: "House3", 4: "House4"}
new_houses = {n**2: house + "!" for (n, house) in houses.items()}
print(houses)
print(new_houses)