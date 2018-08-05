# Problem 15 - 6/22/17

def numLatticePaths(n,m):
	global buffer
	if buffer[n-1][m-1] > 0:
		return buffer[n-1][m-1]
	elif n == 1 and m == 1:
		return 2
	elif n == 1:
		buffer[n-1][m-1] = 1 + numLatticePaths(n,m-1)
	elif m == 1:
		buffer[n-1][m-1] = 1 + numLatticePaths(n-1,m)
	else:
		buffer[n-1][m-1] = numLatticePaths(n-1,m) + numLatticePaths(n,m-1)
	buffer[m-1][n-1] = buffer[n-1][m-1]
	return buffer[n-1][m-1]
		
n = 20
buffer = [[0]*n for i in range(n)]

print(numLatticePaths(n,n))