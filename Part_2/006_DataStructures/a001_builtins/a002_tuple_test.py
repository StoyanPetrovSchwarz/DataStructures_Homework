'''
TUPLES
'''

'''
Creating a Tuple
'''
car = ("Ford", "Raptor", 2019, "Red")
print(car)

# Length
print(len(car))

# Indexing
print(car[1])

# Slicing
print(car[2:])

'''
Merging Tuples
Tuples can be merged using the + operator
'''

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = hero1 + hero2
print(awesome_team)


'''
Nested Tuples
'''
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero1, hero2)
print(awesome_team)

'''
Search
Check whether an element exists in a tuple by using the in operator
'''
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Moscow" in cities)

'''
The index() function can give us the index of a particular value
'''
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(cities.index("Tokyo"))

'''
Immutability
Since tuples are immutable, we can’t add or delete elements from them. Furthermore, it isn’t possible to append another tuple to an existing tuple.
'''
