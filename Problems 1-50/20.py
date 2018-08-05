# Problem 20 - 6/26/17
import math

n = 100
fact = math.factorial(n)

sum = 0
while fact > 10:
	sum += fact % 10
	fact = fact//10
print(sum+fact)