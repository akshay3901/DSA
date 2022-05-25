import array as arr
numbers = arr.array('i',[1,2,3,5,7,8,9])
missing_number = set(range(numbers[0],numbers[-1] + 1)) - set(numbers)
print(missing_number)
