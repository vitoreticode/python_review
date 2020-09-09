# Manipulate Strings

s = "Interview"

# string slice
s[1:4]

# get char by index
s[3]

# get index of a char on string
s.index('a')

# string case
s.capitalize()
s.lower()
s.upper()

# replace na string
s.replace('i','a')

# string concatenation
s1 = "worn"
s2 = "hole"
s3 = s1 + s2
print(s3)

# list of strings to string
l = ["I","Like","Study"]
s = ' '.join(l)
print(s)

# break a string to list
l = s.split(" ")
print(l)