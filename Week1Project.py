import numpy as np

num_vectors = int(input("Enter the number of vectors you want: "))




all_vector = [] #Every vector is stored in this list
size = int(input("Enter the size of elements in the vector: "))

for i in range(num_vectors):
            
    one_vector = []
    print(f"vector{i + 1}")

    for j in range(size):

        component = int(input(f"Enter the component{j + 1}:"))
        one_vector.append(component)
            
    all_vector.append(one_vector)


def vector_add(all_vector):
    sum = np.zeros(size)

    for i in range(num_vectors):


        sum += all_vector[i]
    print("The Sum of the two vectors are: ",sum)

vector_add(all_vector)

def vector_subtract(all_vector):
    diff  = np.zeros(size)

    for i in range(num_vectors):
        diff -= all_vector[i]
    print("The Difference of two vectors are:",diff)

vector_subtract(all_vector)
