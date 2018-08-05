# Problem 10 - 6/21/17
import math

primes = [2,3,5]
def checkPrime(n):
	global primes
	i = 0
	while primes[i] <= math.ceil(math.sqrt(n)):
		if n%primes[i] == 0:
			return False
		i += 1
	primes.append(n)
	return True

n = 2000000
sum = 10

for i in range(6,n):
	if checkPrime(i):
		sum += i
		
print(sum)