title = 'TMNT'

villains = ['Shredder', 'Krang', 'Bebop', 'Rock']
turtles = {
    'Raphael': 'Sai', 
    'Mich': 'Nunchaku',
    'Leonardo': 'Katana', 
    'Dona':'Bo'
}
result = zip(title, villains, turtles)
print(result)

for item in result:
    print(item)

result = zip(title, villains, turtles)
tuples = list(result)
print(tuples)

turtle_masks = [
    ('raphael','red'),
    ('leonardo','blue'),
    ('michelangelo','orange'),
    ('donatello','purple')
]

result = zip(*turtle_masks)
print(result)
for item in result:
    print(item)

keys = ['movie','year','director']
values = [
    ['forest gump','goodfelas','seven'],
    [1994,1990,1995],
    ['r zemikas','m scorsee', 'd fincher']
]

movies = dict(zip(keys, values))
print(movies)

# Define a function searching for the longest word
def get_longest_word(words):
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

# Create a list of the lengths of each list in wlist
lengths = [len(item) for item in wlist]
# Create a list of the longest words in each list in wlist
words = [get_longest_word(item) for item in wlist]
# Combine the resulting data into one iterable object
for item in zip(wlist,lengths,words):
    print(item)