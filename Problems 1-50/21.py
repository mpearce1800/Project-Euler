# Problem 21 - 6/28/17
import math

def divisors(n):
	l = [1]
	for i in range(2,math.ceil(math.sqrt(n))):
		if n % i == 0:
			l.append(i)
			l.append(n//i)
	if math.ceil(math.sqrt(n)) == math.sqrt(n):
		l.append(int(math.sqrt(n)))
	return l
	
n = 10000

nums = []
s = 0
for i in range(3,n):
	if not i in nums:
		div = divisors(i)
		j = sum(div)
			
		div2 = divisors(j)
		if sum(div2) == i and i != j:
			s += i
			nums.append(j)
			print(i,j)
		
for num in nums:
	s += num
print(s)