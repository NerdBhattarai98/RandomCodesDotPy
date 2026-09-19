import numpy as np

num_vectors = int(input("Enter the number of vectors you want: "))
size = int(input("Enter the size of each vector: "))

all_vector = []

for i in range(num_vectors):
    one_vector = []

    print(f"\nVector {i + 1}")

    for j in range(size):
        component = int(input(f"Enter component {j + 1}: "))
        one_vector.append(component)

    all_vector.append(one_vector)

all_vector = np.array(all_vector)


def show_vectors(all_vector):
    print("AVAILABLE VECTORS")

    for i in range(len(all_vector)):
        print(f"Vector {i + 1}: {all_vector[i]}")


def choose_two_vectors(all_vector):
    show_vectors(all_vector)

    vector_1 = int(input("\nEnter the index of Vector A: "))
    vector_2 = int(input("Enter the index of Vector B: "))

    vector_a = all_vector[vector_1 - 1]
    vector_b = all_vector[vector_2 - 1]

    return vector_a, vector_b


def vector_add(all_vector):
    vector_a, vector_b = choose_two_vectors(all_vector)

    result = vector_a + vector_b

    print("\nVector A:", vector_a)
    print("Vector B:", vector_b)
    print("A + B =", result)


def vector_subtract(all_vector):
    vector_a, vector_b = choose_two_vectors(all_vector)

    result = vector_a - vector_b

    print("\nVector A:", vector_a)
    print("Vector B:", vector_b)
    print("A - B =", result)


def scalar_multiplication(all_vector):
    show_vectors(all_vector)

    vector_number = int(input("\nChoose a vector: "))
    scalar = float(input("Enter the scalar: "))

    vector = all_vector[vector_number - 1]

    result = scalar * vector

    print(f"\n{scalar} × Vector {vector_number}:")
    print(result)


def scalar_division(all_vector):
    show_vectors(all_vector)

    vector_number = int(input("\nChoose a vector: "))
    scalar = float(input("Enter the scalar: "))

    if scalar == 0:
        print("Cannot divide by zero.")
        return

    vector = all_vector[vector_number - 1]

    result = vector / scalar

    print(f"\nVector {vector_number} / {scalar}:")
    print(result)


def negative_vector(all_vector):
    show_vectors(all_vector)

    vector_number = int(input("\nChoose a vector: "))

    vector = all_vector[vector_number - 1]

    result = -vector

    print("\nNegative Vector:")
    print(result)


def component_wise_multiplication(all_vector):
    vector_a, vector_b = choose_two_vectors(all_vector)

    result = vector_a * vector_b

    print("\nA * B =", result)


def component_wise_division(all_vector):
    vector_a, vector_b = choose_two_vectors(all_vector)

    if np.any(vector_b == 0):
        print("Cannot divide by zero component.")
        return

    result = vector_a / vector_b

    print("\nA / B =", result)


def magnitude(all_vector):
    show_vectors(all_vector)

    vector_number = int(input("\nChoose a vector: "))

    vector = all_vector[vector_number - 1]

    result = np.linalg.norm(vector)

    print(f"\nMagnitude of Vector {vector_number}: {result}")


def direction(all_vector):
    show_vectors(all_vector)

    vector_number = int(input("\nChoose a vector: "))

    vector = all_vector[vector_number - 1]

    if len(vector) != 2:
        print("Direction is currently implemented only for 2D vectors.")
        return

    x = vector[0]
    y = vector[1]

    angle_radians = np.arctan2(y, x)
    angle_degrees = np.degrees(angle_radians)

    print(f"\nDirection of Vector {vector_number}:")
    print(f"{angle_degrees:.2f}°")


def unit_vector(all_vector):
    show_vectors(all_vector)

    vector_number = int(input("\nChoose a vector: "))

    vector = all_vector[vector_number - 1]

    magnitude_value = np.linalg.norm(vector)

    if magnitude_value == 0:
        print("Zero vector does not have a unit vector.")
        return

    result = vector / magnitude_value

    print(f"\nUnit Vector of Vector {vector_number}:")
    print(result)


def inspect_vector(all_vector):
    show_vectors(all_vector)

    vector_number = int(input("\nChoose a vector: "))

    vector = all_vector[vector_number - 1]

    print("VECTOR INSPECTOR")
    print("Vector:", vector)
    print("Shape:", vector.shape)
    print("Size:", vector.size)
    print("NumPy dimensions:", vector.ndim)
    print("Data type:", vector.dtype)
    print("First component:", vector[0])
    print("Last component:", vector[-1])

    if len(vector) > 1:
        print("Slice [1:]:", vector[1:])


while True:
    
    print("VECTOR LAB")
    print("Interactive Linear Algebra")
   

    print("\nVECTOR INFORMATION")
    print("1. Show Vectors")
    print("2. Inspect Vector")

    print("\nVECTOR OPERATIONS")
    print("3. Addition")
    print("4. Subtraction")
    print("5. Scalar Multiplication")
    print("6. Scalar Division")
    print("7. Negative Vector")
    print("8. Component-wise Multiplication")
    print("9. Component-wise Division")

    print("\nVECTOR MATHEMATICS")
    print("10. Magnitude")
    print("11. Direction / Angle")
    print("12. Unit Vector")

    print("\n0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_vectors(all_vector)

    elif choice == "2":
        inspect_vector(all_vector)

    elif choice == "3":
        vector_add(all_vector)

    elif choice == "4":
        vector_subtract(all_vector)

    elif choice == "5":
        scalar_multiplication(all_vector)

    elif choice == "6":
        scalar_division(all_vector)

    elif choice == "7":
        negative_vector(all_vector)

    elif choice == "8":
        component_wise_multiplication(all_vector)

    elif choice == "9":
        component_wise_division(all_vector)

    elif choice == "10":
        magnitude(all_vector)

    elif choice == "11":
        direction(all_vector)

    elif choice == "12":
        unit_vector(all_vector)

    elif choice == "0":
        print("\nExiting Vector Lab...")
        break

    else:
        print("\nInvalid choice. Please try again.")