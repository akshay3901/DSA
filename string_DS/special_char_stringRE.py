import re

str1 = 'wlecome C@me to !#e Wor%d'
# str2 = 'hi hello'
regex = re.compile('[!@#$%^&*()_+=":?></]')

if(regex.search(str1) == None):
    print('No , special characters present')
else:
    print('Yes ,  it contains special character')
