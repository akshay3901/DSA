# To check if a string has at least one letter and one number

def string_check(str):

    flag_1 = False      # initialize flag variable
    flag_2 = False

    for i in str:
        if i.isalpha():
            flag_1 = True
        if i.isdigit():
            flag_2 = True
    return flag_1 and flag_2

print(string_check('weare25'))
print(string_check('namay'))
print(string_check('a46'))