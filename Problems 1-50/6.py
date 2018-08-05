# Problem 6 - 6/21/17

n = 100

sum = 0
for i in range(1,n+1):
	for j in range(i+1,n+1):
		sum += 2*i*j
print(sum)