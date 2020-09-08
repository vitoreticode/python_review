# -*- coding: utf-8 -*-

"""
Data Structure
	It is a specialized format to organize and store data

	Python main data structures:
		- list
		- tuple
		- set
		- dictionary
"""

"""
List - Is a ordered mutable sequence of items(numbers, strings, etc)
"""

# creating a list
my_list = [1,2,3,4,5]

# find element
1 in my_list

# accessing list elements
print(my_list)
print(my_list[2])
print(my_list[1:4])

# add element on last position
my_list.append(6)

# remove element
my_list.remove(1)
print(my_list)

# remove the last item from a list and return its values
my_list.pop()

# count the amount of a item in a list
my_list.count(2)

"""
Tuple - An ordered immutable sequence of items(numbers, strings, etc)
	  - Modifying a tuple its not possible
"""
my_tuple = (1, 'apple', 2, 'banana')

# find element
1 in my_tuple

"""
Set - An unordered collection with no duplicate items(numbers, strings, etc)
"""

# creating a set
my_set = (my_list)
my_set2 = ([3,4,5,6,7])

# add element
my_set.add(7)

# remove element
my_set.remove(7)

# find element
5 in my_set

# operation on sets
my_set.union(my_set2)
my_set.intersection(my_set2)
my_set.difference(my_set2)

"""
Dictonary - Collection of key-value pairs where keys are unique and immutable
"""

fruits = {'apple':10, 'orange':20, 'banana': 30}
print(fruits)

fruits = dict([('apple',10),('orange',20),('banana',30)])
print(fruits['apple'])

fruits['apple'] = 20
fruits['grapefruit'] = 40

fruits.items()
fruits.values()
fruits.keys()

fruits.popitem('banana')
'apple' in fruits