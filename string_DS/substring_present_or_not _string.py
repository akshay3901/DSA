# check if a substring is there in the given string or not.

#str = input('Enter string :')
#sub_str = input('Enter substring for check :')

#s = str.split()
#print(s)

#if sub_str in str:
#    print('yes , substring is present')
#else:
#    print('No, substring is not present')



def check(str,sub_str):
    if(str.find(sub_str) == -1):
        print('No,substring not present')
    else:
        print('yes,substring present')

str = input('Enter string :')
sub_str=input('Enter substring :')
check(str,sub_str)


