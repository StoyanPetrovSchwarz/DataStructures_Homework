start_first = ["Start", "First", 30]
print(start_first)

# Indexing
print(start_first[0])

# Length
print(len(start_first))

'''
Lists are mutable. Not bound to to one type of data
'''

print(start_first[2])
start_first[2] += 3
print(start_first[2])


'''
Using range()#
A range can further be converted into a list by using the list() casting.
'''

num_seq = range(0, 10)  # A sequence from 0 to 9
num_list = list(num_seq)  # The list() method casts the sequence into a list
print(num_list)

num_seq = range(3, 20, 3)  # A sequence from 3 to 19 with a step of 3
print(list(num_seq))

'''
List-Ception!
The nested lists do not even need to be of the same size! This is not something we can find in many other languages.
'''
world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners)

'''
Sequential Indexing
To access the elements of a list or a string which exists inside another list, we can use the concept of sequential indexing.
Each level of indexing takes us one step deeper into the list, allowing us to access any element in a complex list.
'''
world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners[1])
print(world_cup_winners[1][1])  # Accessing 'Spain'
print(world_cup_winners[1][1][0])  # Accessing 'S'

'''
Merging Lists
'''
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
merged_list = part_A + part_B
print(merged_list)

'''
Use the extend() property of a list to add the elements of one list at the end of another
'''
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
part_A.extend(part_B)
print(part_A)

'''
Adding Elements
'''

'''
The append() method can be used to add a new element at the end of a list.
'''
num_list = []  # Empty list
num_list.append(1)
num_list.append(2)
num_list.append(3)
print(num_list)

'''
To add an element at a particular index in the list, we can use the insert() method.
aList.insert(index, newElement)
'''
num_list = [1, 2, 3, 5, 6]
num_list.insert(3, 4)  # Inserting 4 at the 3rd index. 5 and 6 shifted ahead
print(num_list)

'''
Removing Elements
'''

'''
The counterpart of append() is the pop() operation which removes the last element from the list.
'''
houses = ["first", "second", "third", "forth"]
last_house = houses.pop()
print(last_house)
print(houses)

'''
If we need to delete a particular value from a list, we can use the remove() method by following this template:
aList.remove(element_to_be_deleted)
'''
houses = ["first", "second", "third", "forth"]
print(houses)
houses.remove("forth")
print(houses)

# For nested lists
populations = [["Winterfell", 10000], ["King's Landing", 50000],
               ["Iron Islands", 5000]]
print(populations)
populations.remove(["King's Landing", 50000])
print(populations)

'''
List Slicing
List slicing is the term used for obtaining a portion of a list given the start and end indices.
'''
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list[2:5])
print(num_list[0::2])

'''
Index Search
With lists its really easy to access a value through its index. However, the opposite operation is also possible where we can find the index of a given value.

For this, we’ll use the index() method
'''
cities = ["London", "Paris", "Los Angeles", "Beirut"]
print(cities.index("Los Angeles"))  # It is at the 2nd index

'''
To verify the existence of an element in a list, we can use the -- in -- operator
'''

cities = ["London", "Paris", "Los Angeles", "Beirut"]
print("London" in cities)
print("Moscow" not in cities)

'''
List Sort
A list can be sorted in ascending order using the sort() method. 
Sorting can be done alphabetically or numerically depending on the content of the list
'''

num_list = [20, 40, 10, 50.4, 30, 100, 5]
num_list.sort()
print(num_list)

'''
List Comprehension
List comprehension is a technique that uses a for loop and a condition to create a new list from an existing one.
'''
nums = [10, 20, 30, 40, 50]
nums_double = []

for n in nums:
    nums_double.append(n * 2)
print(nums)
print(nums_double)
'''
The expression is equivalent to -- n * 2 -- since it’s used to create each value in the new list.
Our for loop is -- for n in nums --, where -- n -- is the iterator.
An if condition doesn’t exist in this case.
'''
nums = [10, 20, 30, 40, 50]

# List comprehension
nums_double = [n * 2 for n in nums]

print(nums)
print(nums_double)

'''
Adding a Condition
'''
nums = [10, 20, 30, 40, 50]

# List comprehension
nums_double = [n * 2 for n in nums if n % 4 == 0]

print(nums)
print(nums_double)

'''
Using Multiple Lists
List comprehension can also be performed on more than one list. 
The number of for loops in the comprehension will correspond to the number of lists we’re using.
'''
list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

print(sum_list)
