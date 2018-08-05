# Problem 9 - 6/21/17

n = 1000

for a in range(n//3):
	for b in range(a+1,(n-a)//2):
		c = n-a-b
		if a**2 + b**2 == c**2:
			print(a*b*c)