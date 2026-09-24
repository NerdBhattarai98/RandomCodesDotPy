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

# vector = []
# size = int(input("Enter the size of vector: "))

# for i in range(size):

#     value = int(input("Enter the necessary value: "))
#     vector.append(value)

# vector = np.array(vector)
# print(vector)
# print(type(vector))

# print("The L1 Norm of the vector is",np.linalg.norm(vector,ord = 1))
# print("The L2 Norm of the vector is",np.linalg.norm(vector,ord = 2))
# print("The Linf Norm of the vector is",np.linalg.norm(vector,ord = np.inf))

#Distance and norm

# A = np.array([3,4])
# B = np.array([2,3])

# difference = A-B
# L2 = np.linalg.norm(difference,ord = 2)
# L1 = np.linalg.norm(difference,ord = 1)

# print(difference)
# print(L1)
# print(L2)

#Dot Product of the Vectors

u = np.array([10,2,0])
v = np.array([20,4,0])
w = np.array([3,3,3])

dotp1 = np.dot(u,v)
print(dotp1)

dotp2 = np.dot(v,w)
print(dotp2)

dotp3 = np.dot(u,w)
print(dotp3)

umag = np.linalg.norm(u)
vmag = np.linalg.norm(v)
wmag = np.linalg.norm(w)

cosineuv  =dotp1/(umag*vmag)
cosinevw  =dotp2/(vmag*wmag)
cosineuw  =dotp3/(umag*wmag)

print(cosineuv)
print(cosinevw)
print(cosineuw)