# Problem 30 - 8/5/18

n = 5
sum = 0

def getDigits(num):
	digits = []
	while num > 0:
		digits.append(num % 10)
		num = num // 10
	return digits
	
for i in range(2,1000000):
	digits = getDigits(i)
	s = 0
	for digit in digits:
		s += digit**n
	if s == i:
		sum += i
		print(i)
		
print(sum)