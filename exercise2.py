# Matthew wants to know which classes he failed and which classes he passed and the percentage of failed classes.

import numpy as np
print(np.__version__)

num = int(input("How many grades? "))
arr = np.arange(num+1)
i = 1;

while i <= num:
	grade = int(input("Enter a grade between 1 and 10: "))
	arr[i] = grade
	i = i+1

passed = 0
failed = 0

for j in arr:
	if arr[j] >= 7:
		passed = passed + 1
	else:
		failed = failed + 1
if failed > 0:
	print ("Per each class", (passed+failed-1)/failed, "was failed")# Matthew wants to know which classes he failed and which classes he passed and the percentage of failed classes.

import numpy as np
print(np.__version__)

num = int(input("How many grades? "))
arr = np.arange(num+1)
i = 1;

while i <= num:
	grade = int(input("Enter a grade between 1 and 10: "))
	arr[i] = grade
	i = i+1

passed = 0
failed = 0

for j in arr:
	if arr[j] >= 7:
		passed = passed + 1
	else:
		failed = failed + 1
if failed > 0:
	print ("Per each class", (passed+failed-1)/failed, "was failed")
