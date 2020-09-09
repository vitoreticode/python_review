# list comprehension
l = [ 2 * num for num in range(1,6)]
print(l)

# list comprehension with condition
nums_new = [num for num in range(1, 11) if num % 2 == 0]
print(nums_new)