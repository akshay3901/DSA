str = input('Enter string for remove duplicates :')
str1 = ''
for i in str:
    if i not in str1:
        str1=str1+i
print(str1)
