import numpy as np

# #Norms
# vector = np.array([1,2,3])

# #L1 Norm

# L1 = np.linalg.norm(vector,ord=1)
# print(L1)


# #L2 Norm

# L2 = np.linalg.norm(vector,ord=2)
# print(L2)

# #Linfinity Norm

# Linf = np.linalg.norm(vector,ord=np.inf)
# print(Linf)

vector = []
size = int(input("Enter the size of vector: "))

for i in range(size):

    value = int(input("Enter the necessary value: "))
    vector.append(value)

vector = np.array(vector)
print(vector)
print(type(vector))

print("The L1 Norm of the vector is",np.linalg.norm(vector,ord = 1))
print("The L2 Norm of the vector is",np.linalg.norm(vector,ord = 2))
print("The Linf Norm of the vector is",np.linalg.norm(vector,ord = np.inf))