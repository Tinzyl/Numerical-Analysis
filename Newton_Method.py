from math import *

x0 = 1.0 

for i in range(1, 101):
	x1 = x0 - (x0**2 - sin(x0)) / (2*x0 - cos(x0)) 

	# Check for convergence criterion
	if abs(x1 - x0) <= 1.0E-8:
		break
	x0 = x1

print(f'Root: {round(x1, 8)}')
print(f'Number of iterations: {i}')



