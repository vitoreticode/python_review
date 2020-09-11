# map single iterator
nums = [1,2,3,4,5]
squares = map(lambda x: x**2, nums)

# map with multiple iterables
num2=[10,20,30,40,50]
mult = map(lambda x,y: x*y, nums, num2)

# filter, iterable
nums = [-3, -2, -1, 0, 1, 2, 3]
fobj = filter(lambda x: x > 0, nums)

# reduce, not iterable
from functools import reduce
nums = [8,1,4,2,9]
robj = reduce(lambda x,y: x if x < y else y, nums)
print(robj)

# using map
"""
Your task is to define your own my_zip() function with *args 
depicting a variable number of Iterables, e.g. lists, strings, tuples etc. 
Rather than a zip object, my_zip() should already return a list of tuples.
"""
def my_zip(*args):
    
    # Retrieve Iterable lengths and find the minimal length
    lengths = list(map(len, args))
    min_length = min(lengths)

    tuple_list = []
    for i in range(0, min_length):
        # Map the elements in args with the same index i
        mapping = map(lambda x: x[i], args)
        # Convert the mapping and append it to tuple_list
        tuple_list.append(tuple(mapping))
        
    return tuple_list

result = my_zip([1, 2, 3], ['a', 'b', 'c', 'd'], 'DataCamp')
print(result)

# using filter
# Exclude all the numbers from nums divisible by 3 or 5
print(nums)
fnums = filter(lambda x: x % 3 != 0 and x % 5 != 0, nums)
print(list(fnums))

# Return the string without its vowels
print(string)
vowels = 'AEIOUaeiou'
fstring = filter(lambda x: x not in vowels, string)
print(''.join(fstring))