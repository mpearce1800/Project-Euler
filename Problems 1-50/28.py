# Problem 28 - 8/5/18

n = 1001
sideLen = 3
sum = 1
curVal = 1

while sideLen <= n:
	for i in range(4):
		curVal += sideLen - 1
		sum += curVal
	sideLen += 2
	
print(sum)