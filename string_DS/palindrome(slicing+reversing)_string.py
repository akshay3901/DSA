# check given sring is palindrome or not

a=input("Enter String :")
# slicing / reversing = start value:end value:step value
b=a[-1::-1]
if(a==b):
    print("Palindrome string")
else:
    print("Not palnidrome string")
