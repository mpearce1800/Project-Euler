# Problem 2 - 6/20/17

fib = [1,2]
n = 4000000
sum = 2

while fib[-1] <= n:
	fib.append(fib[-1]+fib[-2])
	if fib[-1]%2 == 0:
		sum += fib[-1]
	
print(sum)