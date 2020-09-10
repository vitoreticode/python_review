squared = lambda x: x**2
print(squared(4))

def function_with_callback(num, callback):
    return callback(num)

print(function_with_callback(2, squared))

odd_or_even = lambda num: 'even'if num % 2 == 0 else 'odd'
odd_or_even(3)

# Returns a dictionary counting charaters in a string
lambda2 = lambda s: dict([(c, s.count(c)) for c in set(s)])
print(func2('DataCamp'))
print(lambda2('DataCamp'))
