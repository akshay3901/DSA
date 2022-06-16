str = input("Enter string :")
bn = {'0,1'}

if str == bn or str == '0' or str == '1':
    print('Yes,{} it is binary string'.format(str))
elif '1' in str or '0' in str:
    print('Yes,{} it is binary string'.format(str))
else:
    print('No,{} it is Not binary string'.format(str))

