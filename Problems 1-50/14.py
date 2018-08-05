# Problem 14 - 6/22/17

n = 1000000

max, length = 0, 0
for i in range(1,n+1):
	num = i
	count = 1
	while num != 1:
		if num%2 == 0:
			num /= 2
		else:
			num = 3*num + 1
		count += 1
	if count > length:
		max, length = i, count
		
print(max,length)