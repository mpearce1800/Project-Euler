# Problem 4 - 6/20/17

def checkPalindrome(n):
	l = []
	while n >= 10:
		l.append(n%10)
		n = n//10
	l.append(n)
	
	for i in range(len(l)//2):
		if l[i] != l[-1-i]:
			return False
	return True

n = 999

m = 0
for i in range(n,0,-1):
	for j in range(i,0,-1):
		if checkPalindrome(i*j):
			m = max(i*j,m)
print(m)