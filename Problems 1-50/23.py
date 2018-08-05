# Problem 23 - 6/28/17
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

n = 28123
abundants = []
for i in range(12,n-12):
	if sum(divisors(i)) > i:
		abundants.append(i)

sieve = [False]*n
for i in range(len(abundants)):
	for j in range(i,len(abundants)):
		if abundants[i]+abundants[j] < n:
			sieve[abundants[i]+abundants[j]] = True
				
print(sum([i for i in range(n) if not(sieve[i])]))