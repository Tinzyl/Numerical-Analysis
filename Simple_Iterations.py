from math import sqrt

x = 1.6 #the initial guess

for iteration in range(1, 101):
	xnew = sqrt((5*x-3)/2)
	print(iteration, x)
	if abs(xnew - x) < 0.000001:
		break
	x = xnew
print('The root : %0.5f' % xnew)
print('The number of iterations : %d' % iteration)