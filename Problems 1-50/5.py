# Problem 5 - 6/20/17
import math

def factor(n):
	factors = factor_l(n)
	
	d = dict()
	for num in factors:
		d[num] = d.get(num, 0) + 1
	return d
	
def factor_l(n):
	if n == 2:
		return [n]
		
	factors = [n]
	
	for i in range(2,math.ceil(math.sqrt(n))+1):
		if n%i == 0:
			factors = factor_l(n//i) + factor_l(i)
			break
			
	return factors
	
n = 20
product = dict()
for i in range(2,n+1):
	factors = factor(i)
	for k in factors:
		product[k] = max(product.get(k,0),factors[k])

p = 1
for k in product:
	p *= k**product[k]
print(p)