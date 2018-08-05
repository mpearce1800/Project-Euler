# Problem 16 - 6/22/17

res = str(2**1000)

sum = 0
for i in range(len(res)):
	sum += int(res[i])
	
print(sum)
