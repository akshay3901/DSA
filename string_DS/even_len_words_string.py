# print even length of string

str = 'python is popular programming language in the world'
s = str.split(' ')
print(s)
for i in s:
    if len(i)%2==0:
        print(i)