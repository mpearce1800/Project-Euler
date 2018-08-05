# Problem 17 - 6/23/17

ones = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
tens = {0:0,2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}
teens = {10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8}
hundred = 7

n = 1000

sum = 0
for i in range(n):
	letters = ones[i//100]
	if letters != 0:
		letters += hundred
	
	noHun = i-(i//100)*100
	if noHun == 0:
		sum += letters
		continue
	
	if letters > 0:
		letters += 3
	if noHun < 20 and noHun > 9:
		letters += teens[noHun]
	else:
		letters += tens[noHun//10] + ones[noHun%10]
	sum += letters
	
sum += 11 #1000
print(sum)