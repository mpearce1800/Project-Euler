# Problem 13 - 6/22/17

n = 50

nums = []
with open('13_input.txt','r') as file:
	for line in file:
		nums.append([int(line[a]) for a in range(n)])
		
carry = 0
final = []
for dig in range(-1,-n-1,-1):
	sum = carry
	for num in nums:
		sum += num[dig]
	carry = sum//10
	final.append(sum%10)
final.append(carry)
	
for i in final[-1::-1]:
	print(i,end='')