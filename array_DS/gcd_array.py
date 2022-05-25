import math

m,n=map(int,input('Enter two non-zero numbers: ').split())

g=math.gcd(m,n)

print('GCD of {} and {} is {}.'.format(m,n,g))
