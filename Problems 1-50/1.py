# Problem 1 - 6/20/2017

sum = 0
n = 1000-1
a, b = 3, 5

for i in range(n//a):
	sum += a*(i+1)
for i in range(n//b):
	sum += b*(i+1)
for i in range(n//(a*b)):
	sum -= a*b*(i+1)
	
print(sum)