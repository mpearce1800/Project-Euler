# Problem 27 - 8/5/18

import math

# b must be prime (and positive?)
maxA = 1000
maxB = maxA + 1
maxPrimes = 0
A = 0
B = 0

def isPrime(num):
	if num < 2:
		return False
	for i in range(2, int(math.floor(math.sqrt(num)))):
		if num % i == 0:
		    return False
	return True

for a in range(-1*maxA+1, maxA):
	for b in range(2, maxB):
		n = 0
		while isPrime(n*n + a*n + b):
			n += 1
		if n > maxPrimes:
			maxPrimes = n
			A = a
			B = b
			
print(str(A) + " " + str(B) + " " + str(A*B) + " " + str(maxPrimes))
	
