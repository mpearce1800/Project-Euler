# Problem 12 - 6/22/17
import math
	
n = 500

tNum, count = 0, 1
numFactors = 0
while numFactors <= n:
	tNum += count
	count += 1
	
	numFactors = 2
	for i in range(2,math.ceil(math.sqrt(tNum))):
		if tNum % i == 0:
			numFactors += 2
	if math.ceil(math.sqrt(tNum))**2 == tNum:
		numFactors += 1
		
print(tNum)
print(numFactors)
