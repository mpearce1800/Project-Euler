# Problem 7 - 6/21/17
import math

def checkPrime(n):
	for i in range(2,math.ceil(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True

n = 10001

numPrimes = 1
i = 3

while numPrimes < n:
	if checkPrime(i):
		numPrimes += 1
	i += 1
	
print(i-1)