x1= 1.2
x2 = 1.5
y1 = 2*x1**2 -5*x1 + 3
y2 = 2*x2**2 -5*x2 + 3

# Check for the sign difference between y-values
# If the signs are not opposite, stop
if y1*y2 > 0:
	print('The root is not within the given interval')
	exit

for bisection in range(1, 101): # 100 bisections
	# Calculate the value of x in the half of the interval
	xh = (x1 + x2) / 2
	yh = 2*xh**2 -5*xh + 3
	# Check for the sign difference between the y-values first half interval
	y1 = 2*x1**2 -5*x1 + 3
	if abs(y1) < 1.0E-6:
		break
	
	# If the signs are opposite, let x1 and x2 be the limits of the first half interval
	elif y1 * yh < 0: # If the root is in the first half interval
		x2 = xh
	else:
		x1 = xh
print('The root : %0.5f' % x1)
print('The number of bisections : %d' % bisection)


