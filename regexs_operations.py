# Any character
.

# Any alphanumeric
\w

# Any digits
\d

# Any whitespace
\s

# Square braquets
[aAbB] # a, b, A, B
[a-z]  # a,b,c...
[A-Z]  # A,B,C...
[0-9]  # 0,1,2,3...

# Repetitions
# No character or it repeats an undefined number of times
a* # '','a','aa','aaa'
# At least once
a+ # 'a','aa','aaa'
# The char exists or not
a? # '', 'a'
# Character present from N to M times
a{2,4} # 'aa','aaa','aaaa'

