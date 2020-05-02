'''
@ author: Tinotenda Mhlanga
@ program: Trapezoidal Rule

'''

from math import sin, pi, exp, factorial
import scipy.integrate

f = lambda x: exp(-x)

mac_series = 0
x1 = 1
a = 0
b = 1
n = 100 # number of divisions
h = (b - a) / n # step size
S = 0.5 * (f(a) + f(b))

# Trapezoidal Rule
for i in range(1, n):
	# Summation
	S += f(a + i*h)

I = h * S

# Maclaurin Expansion
for i in range(1, 8):
	if i % 2 == 0:
		mac_series -= x1**i/(i * factorial(i - 1))
	else:
		mac_series += x1**i/(i * (factorial(i - 1)))

# Exact Value
exact_value = scipy.integrate.quad(f, 0, 1)

print(f'\nExact Value: {round(exact_value[0], 12)}')
print(f'\nResult Using Trapezoidal Rule: {round(I, 12)}')
print(f'\nResult Using Maclaurins Expansion: {round(mac_series, 12)}')
