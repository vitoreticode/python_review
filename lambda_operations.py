squared = lambda x: x**2
print(squared(4))

def function_with_callback(num, callback):
    return callback(num)

print(function_with_callback(2, squared))