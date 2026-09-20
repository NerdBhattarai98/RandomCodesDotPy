# Write a fresh program yourself that:

# Takes the vector size from the user.
# Takes the vector components.
# Converts it to a NumPy array.
# Calculates:
# L1
# L2
# L∞
# Prints all three.

import numpy as np

size = int(input("Enter the size of vector: "))
vector = []

for i in range(size):

    value = int(input(f"Enter the component {i+1}: "))
    vector.append(value)

vector = np.array(vector)

print("The L1 of the Following vector is: ",np.linalg.norm(vector,ord=1))
print("The L2 of the Following vector is: ",np.linalg.norm(vector,ord=2))
print("The Linf of the Following vector is: ",np.linalg.norm(vector,ord=np.inf))


