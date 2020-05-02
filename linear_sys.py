import numpy as np
from datetime import datetime

a = np.array([[1, 2, 2], 
	       [2, 7, 3],
	       [-1, 7, -3]],float)
	      
b = np.array([3, 1, -14], float)

num_elements = len(b)

x = np.zeros(num_elements, float)

# Elimination

start_time = datetime.now()
# Go through the fixed rows
for i in range(num_elements-1):

# Take the rows under the fixed row, row by row inorder to apply the row operations
	for j in range(i + 1, num_elements):
		factor = a[i, i] / a[j, i]
		b[j] = b[i] - factor*b[j]
		# element subtraction
		for k in range(i, num_elements):
			a[j, k] = a[i, k] - factor*a[j, k]

# Back Substitution

# Start with last row
x[num_elements - 1] = b[num_elements - 1] / a[num_elements - 1, num_elements - 1]
for i in range(num_elements - 2, -1, -1):
	# Summation of terms
	terms = 0
	for j in range(i + 1, num_elements):
		terms += a[i, j] * x[j]
	x[i] = (b[i] - terms) / a[i, i]
total_time = datetime.now() - start_time
print(f'It took {total_time.microseconds} microseconds to solve the system.')
print('Solution saved to file')

# Save to file
np.savetxt('linear_sysFile.txt', x, fmt='%4.8f', delimiter=' ')

