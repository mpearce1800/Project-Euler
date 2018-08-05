# Problem 19 - 6/26/17

days = [31,28,31,30,31,30,31,31,30,31,30,31]

day, prevDay = 5, 5 #Jan 1, 1901 is a Tuesday, 0 is 1 for modulus
month = 0
year = 1901

count = 0				

while year <= 2000:
	if day == 0:
		count += 1
		
	day = (day+7)%days[month]
	if day < prevDay:
		month = (month+1)%12
		if month == 0:
			year += 1
			if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
				days[1] = 29
			else:
				days[1] = 28
	prevDay = day
				
print(count)