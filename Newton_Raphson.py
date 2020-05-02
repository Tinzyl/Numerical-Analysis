from math import *
x = 10
for iteration in range(1, 101):
	xnew = x - (x**2 + cos(x)**2 -4*x)/(2*(x - cos(x)*sin(x) - 2)) # The newton-Raphsons Formula
	if abs(xnew - x) < 0.000001:
		break
	x = xnew
print('The root : %0.5f' % xnew)
print('Thhe number of iterations : %d' % iteration)