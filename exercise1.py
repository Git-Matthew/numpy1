# Matthew is bad at remembering multiplication tables from 1 to 12 and he needs a python program to calculate them all.

import numpy as np
print(np.__version__)
np.set_printoptions(threshold=12)

num = int(input("Number:"))
arr = np.arange(13)
arr2 = np.arange(num+1)

print("Multiplication table for number", end = ' ')
print(num)
print('X', end = ' ')

for n in arr2:
	print(arr2[n], end = ' ')
print("\n")

for i in arr:
		print(arr[i], end = ' ')
		for j in arr2:
			print(arr[i]*arr2[j], end = ' ')
		print("\n")
