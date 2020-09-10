# list comprehension
l = [ 2 * num for num in range(0,10)]

# list comprehension with condition
nums_new = [num for num in range(1, 11) if num % 2 == 0]

text = "list COMPREHENSION is A way TO create LISTS"

output = [len(word) for word in text.split()]
output = [len(word) for word in text.split() if word.islower()]

numbers = [1,2,3]
letters = ['a','b','c']

pairs = [(n,l) for n in numbers for l in letters]
print(pairs)
pairs = [[(n,l) for n in numbers] for l in letters]

"""
Find spam
"""
# Convert the text to lower case and create a word list
words = create_word_list(spam.lower())
# Create a set storing only unique words
word_set = set(words)
# Create a dictionary that counts each word in the list
tuples = [(word, words.count(word)) for word in word_set]
word_counter = dict(tuples)
# Printing words that appear more than once
for (key, value) in word_counter.items():
    if value > 1:
        print("{}: {}".format(key, value))

"""
Is prime
"""
def is_prime(n):
    # Define the initial check
    if n < 2:
       return False
    # Define the loop checking if a number is not prime
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
# Filter prime numbers into the new list
primes = [num for num in cands if is_prime(num)]
print("primes = " + str(primes))