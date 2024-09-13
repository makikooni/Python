import numpy as np
 
# Exercise 1: Array Operations
arr1 = np.arange(1, 11)
arr2 = np.arange(11, 21)
 
sum_result = arr1 + arr2
multiply_result = arr1 * 3
sqrt_result = np.sqrt(arr2)

# Exercise 2: Indexing and Slicing
matrix = np.random.rand(3, 6)
print(matrix)
second_row = matrix[1, :]
last_element_first_column = matrix[-1, 0]
sub_matrix = matrix[:2, -2:]


# Exercise 3: Statistical Operations
random_array = np.random.randint(1, 100, 20)
print(random_array)
mean_val = np.mean(random_array)
median_val = np.median(random_array)
std_dev_val = np.std(random_array)
max_index = np.argmax(random_array)
min_index = np.argmin(random_array)
normalized_array = (random_array - mean_val) / std_dev_val
print(normalized_array)


# Exercise 4: Linear Algebra
matrix1 = np.random.rand(3, 3)
print(matrix1)
matrix2 = np.random.rand(3, 3)
print(matrix2)
matrix_product = np.dot(matrix1, matrix2)
determinant = np.linalg.det(matrix_product)
eigenvalues, eigenvectors = np.linalg.eig(matrix1)


# Exercise 5: Boolean Indexing
random_array_bool = np.random.rand(15)
values_gt_05 = random_array_bool[random_array_bool > 0.5]
random_array_bool[random_array_bool > 0.5] = 1
random_array_bool[random_array_bool <= 0.5] = 0


# Exercise 6: Reshaping
array_1d = np.arange(16)
matrix_4x4 = array_1d.reshape(4, 4)
array_flattened = matrix_4x4.flatten()


# Exercise 7: Broadcasting
#It subtracts the mean along the 0-axis (columns) from each element in the array.
#This is a common operation in machine learning for centering the data. Subtracting the mean helps in removing any bias or offset in the data.

array_broadcast = np.random.rand(4, 3)
array_broadcast -= np.mean(array_broadcast, axis=0)



# Exercise 8: File I/O
random_matrix = np.random.rand(5, 5)
np.savetxt('random_matrix.txt', random_matrix)
loaded_matrix = np.loadtxt('random_matrix.txt')


# Displaying results (optional)
print("Exercise 1:")
print("Sum:", sum_result)
print("Multiply:", multiply_result)
print("Square Root:", sqrt_result)
 
print("\nExercise 2:")
print("Matrix:\n", matrix)
print("Second Row:", second_row)
print("Last Element First Column:", last_element_first_column)
print("Sub-Matrix:\n", sub_matrix)
 
print("\nExercise 3:")
print("Random Array:", random_array)
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev_val)
print("Max Index:", max_index)
print("Min Index:", min_index)
print("Normalized Array:", normalized_array)

print("\nExercise 4:")
print("Matrix Product:\n", matrix_product)
print("Determinant:", determinant)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
 

print("\nExercise 5:")
print("Values > 0.5:", values_gt_05)
print("Modified Array:", random_array_bool)


print("\nExercise 6:")
print("1D Array:", array_1d)
print("Reshaped Matrix:\n", matrix_4x4)
print("Flattened Array:", array_flattened)

print("\nExercise 7:")
print("Broadcasted Array:\n", array_broadcast)

print("\nExercise 8:")
print("Saved Matrix:\n", random_matrix)
print("Loaded Matrix:\n", loaded_matrix)

