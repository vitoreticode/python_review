# Iterables

# enumerate
villains = ['Darth Maul','Palpatine', 'Darth Vader']
enum_villains = enumerate(villains)
list_enum_villains = list(enumerate(villains))

for villain in enum_villains:
	print(villain)

for idx, name in enum_villains:
	print(str(idx) + '-' + name)

# iter()

interval = range(0,5)
interval_iter = iter(interval)
next(interval_iter)

while True:
	try:
		next(interval_iter)
	except StopIteration:
		break


# using enumerate
"""
Let's enumerate! Your task is, given a string, to define the function retrieve_character_indices() that creates a dictionary character_indices, where each key represents a unique character from the string and the corresponding value is a list containing the indices/positions of this letter in the string.

For example, passing the string 'ukulele' to the retrieve_character_indices() function should result in the following output: {'e': [4, 6], 'k': [1], 'l': [3, 5], 'u': [0, 2]}.

For this task, you are not allowed to use any string methods!
"""
def retrieve_character_indices(string):
    character_indices = dict()
    # Define the 'for' loop
    for index, character in enumerate(string):
        # Update the dictionary if the key already exists
        if character in character_indices:
            character_indices[character].append(index)
        # Update the dictionary if the key is absent
        else:
            character_indices[character] = [index]
            
    return character_indices
  
print(retrieve_character_indices('enumerate an Iterable'))
