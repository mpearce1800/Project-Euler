# Problem 26 - 8/4/18

d = 1000
maxLen = 0
maxNum = 0

for i in range(1,d):
	num = 1
	sequence = []
	nums = [num]
	length = 0
	
	while num != 0:
		while num < i:
			num *= 10
		digit = num // i
		sequence.append(digit)
		num = num % i
		
		if num in nums:
			start = nums.index(num)
			length = len(nums[start:])
			if length > maxLen:
				maxLen = length
				maxNum = i
			break
		nums.append(num)
				
	print(str(i) + " " + str(length))
	
print(str(maxNum) + " " + str(maxLen))