import numpy as np

# Convert List to 1D Array

vector = [1,2,3,4,5,6]
print("The list is",vector)
vector = np.array(vector)
print("The array is",vector)

# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

vector = np.arange(2,11,1).reshape(3,3)
print(vector)

# 4. Null Vector (10) & Update Sixth Value

vector = np.zeros(10)

print("Original Vector",vector)

vector[6] = 11

print("Appended Vector",vector)

#  Array from 12 to 38

vector = np.arange(12,39)
print(vector)
print(vector[::-1])

# 7. Convert Array to Float Type

vector = np.arange(12,39,dtype=float)
print(vector)

# 8. 2D Array (Border 1, Inside 0)

x = np.ones((5, 5))

x[1:-1,1:-1] = 0
print(x)

# Add Border to Array (0s)

x =  np.ones((5,5))

x[0:4,0:4] = 0
print(x)