# https://pynative.com/python/regex/
# import the RE module
import re

target_string = "Jessa salary is 8000$"

# compile regex pattern
# pattern to match any character
str_pattern = r"\w"
pattern = re.compile(str_pattern)

# match regex pattern at start of the string
res = pattern.match(target_string)
# match character
print(res.group())
# Output 'J'

# search regex pattern anywhere inside string
# pattern to search any digit
res = re.search(r"\d", target_string)
print(res.group())
# Output 8

# pattern to find all digits
res = re.findall(r"\d", target_string)
print(res)
# Output ['8', '0', '0', '0']

# regex to split string on whitespaces
res = re.split(r"\s", target_string)
print("All tokens:", res)
# Output ['Jessa', 'salary', 'is', '8000$']

# regex for replacement
# replace space with hyphen
res = re.sub(r"\s", "-", target_string)
# string after replacement:
print(res)
# Output Jessa-salary-is-8000$