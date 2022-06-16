string = "PythonDataStructure"
print(len(string))
print(string.upper())
print(string.lower())
print(string.count('t'))

# indexing
print(string)
print(string[1:10])
print(string[6:-1])

# updating = updation or deletion of characters from a String is not allowed.
# immutable.Only new strings can be reassigned to the same name.

# deleting = Deletion of the entire string is possible with the use of del keyword.
# Further, if we try to print the string,this will produce an error because String is deleted and is unavailable to be printed.


# Formatting = format() method.{}
# 1.default
string = "{} {} {}".format('i','love','python')
print(string)

# 2.positional
string = "{1} {0} {2}".format('i','love','python')
print(string)

# 3.keyword
string = "{i} {l} {p}".format(i='i',l='love',p='python')
print(string)


# Write a program to print every character of a string entered by user in a new line using loop.
a = input('Enter string')
for i in a:
    print(i)

# Write a program to find the length of the string "refrigerator" without using len function.
str = 'refrigerator'
count = 0
for i in str:
    count=count+1
print(count)

# Write a program to check if the letter 'e' is present in the word 'Umbrella'
str = 'Umbrella'
if 'e' in str:
    print('Present')
else:
    print('Absent')

# Write a program to check if the word 'orange' is present in the "This is orange juice".
str = 'This is orange juice'
a = str.split()
if 'orange' in a:
   print('present')
else:
   print('absent')

# Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is.
# For example, if your name is Robert Brett Roser, then the output should be R.B.Roser.
a = 'Robert Brett Roser'
op = a[0]+'.'+a[7]+'.'+a[13:18]
print(op)

