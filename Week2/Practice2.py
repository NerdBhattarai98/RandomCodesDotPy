import numpy as np

vector1 = []
vector2 = []

size = int(input("Enter the size of the vector: "))

print("----------Value for Vector 1---------- ")

for i in range(size):
    value = int(input("Enter the value: "))
    vector1.append(value)

vector1 = np.array(vector1)


print("----------Value for Vector 2---------- ")

for i in range(size):
    value = int(input("Enter the value: "))
    vector2.append(value)

vector2 = np.array(vector2)

print(vector1)
print(vector2)
print(type(vector1))

dotp = vector1 @ vector2
Magnitude1 = np.linalg.norm(vector1)
Magnitude2 = np.linalg.norm(vector2)

CosineSim = dotp/(Magnitude1*Magnitude2)
CosineDist = 1- CosineSim

print("The Dot Products of Vector are: ",dotp)
print("The Magnitude of Vector 1 is: ",Magnitude1)
print("The Magnitude of Vector 2 is: ",Magnitude2)
print("The Cosine Similarity is:",round(CosineSim,4))
print("The Cosine Distance is: ",round(CosineDist,4))