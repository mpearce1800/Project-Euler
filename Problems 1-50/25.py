# Problem 25 - 7/11/17

fib = [1,1]
n = 1000
i = 2

while fib[-1]//(10**(n-1)) < 1:
	i += 1
	fib[0],fib[1] = fib[1],sum(fib)
	
print(i, fib[-1])