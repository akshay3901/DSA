from array import *
arr = array('i',[])
n = int(input("Enter the Length of elements :"))
for i in range(n):
    x = int(input("Enter the elements :"))
    arr.append(x)
print(arr)

#print("Minimum value is :",min(arr))
#print("Minimum value is :",max(arr))

max = arr[0]
for i in range(n):
    if arr[i] > max:
        max = arr[i]
print("Maximum value is :",max)

min = arr[0]
for i in range(n):
    if arr[i] < min:
        min = arr[i]
print("Minimum value is :",min)

