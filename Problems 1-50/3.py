# Problem 3 - 6/20/17
import math

def checkPrime(n):
	for i in range(2,math.ceil(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True

n = 600851475143
max = 1

for i in range(2,math.ceil(math.sqrt(n))):
	if n%i == 0:
		if checkPrime(n//i):
			max = n//i
			break
		if checkPrime(i):
			max = i
print(max)