# Problem 22 - 6/28/17

f = open("p022_names.txt",'r')
names = f.readline().split('","')
names[0], names[-1] = names[0][1:], names[-1][:-1]

i = 1
total = 0
for name in sorted(names):
	sum = 0
	for j in range(len(name)):
		sum += ord(name[j]) - 0x40 # A is 0x41
	total += sum*i
	i += 1
	
print(total)