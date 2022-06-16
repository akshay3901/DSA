from collections import Counter

str = 'phir hera pheri'
print(str)

# Counter works for hashable objects they are accessed using a key.
# We can get the Key using the get() method.
result = Counter(str)
result = max(result , key=result.get)

print('Least frequent character is :',result)