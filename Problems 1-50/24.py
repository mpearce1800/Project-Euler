# Problem 24 - 6/29/17
import math

s = [0,1,2,3,4,5,6,7,8,9]
n = 1000000
res = []

for i in range(len(s)-1,0,-1):
	f = math.factorial(i)
	print(f, end=' ')
	dig = 0
	while n > f:
		n -= f
		dig += 1
	print(dig, end=' ')
	res.append(s[dig])
	print(res)
	s.remove(s[dig])
res.append(s[0])
	
print(''.join([str(a) for a in res]))