# Problem 29 - 8/5/18

from math import pow

n = 101
nums = {}

for a in range(2,n):
	for b in range(2,n):
		try:
			nums[pow(a,b)] += 1
		except:
			nums[pow(a,b)] = 1
			
print(len(nums))