import array as arr
from collections import OrderedDict
dup = arr.array('i',[1,1,2,3,5,5,7,9,9])
for i in range(0,len(dup)):
    for j in range(i+1,len(dup)):
        if(dup[i]==dup[j]):
            print((dup[j]))
result = list(OrderedDict.fromkeys(dup))
print('Array after removing duplicate:'+str(result))