# replace = replace substring in a string with another substring
# split = split or break string into pieces
# join = join strings into one string

# str = 'datta meghe'
# new_string=str.replace('datta','khatta')
# print(new_string)

# str = "datta meghe college of engineering"
# new_string=str.split(' ')
# print(new_string)

# str = ['how','are','you']
# new_string = '_'.join(str)
# print(new_string)

# To reverse words in a given string  (for reverse word use = split + join , for reverse character use slice)
string = input('Enter string for reverse :')
# reversing words in a given string
s = string.split()[-1::-1]
l = []
for i in s:
# appending reversed words to l
    l.append(i)
# printing reverse words
print(" ".join(l))

