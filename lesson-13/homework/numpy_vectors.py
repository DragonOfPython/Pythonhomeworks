import numpy as np

# Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)
print("Vector with values ranging from 10 to 49:")
print(vector)

# Create a 3x3 matrix with values ranging from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print("\n3x3 Matrix with values ranging from 0 to 8:")
print(matrix_3x3)

# Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print("\n3x3 Identity Matrix:")
print(identity_matrix)

# Create a 3x3x3 array with random values
random_array = np.random.rand(3, 3, 3)
print("\n3x3x3 Array with random values:")
print(random_array)

# Create a 10x10 array with random values and find the minimum and maximum values
random_array_10x10 = np.random.rand(10, 10)
print("\n10x10 Array with random values:")
print(random_array_10x10)
print("\nMinimum value:", np.min(random_array_10x10))
print("Maximum value:", np.max(random_array_10x10))

# Create a random vector of size 30 and find the mean value
random_vector_30 = np.random.rand(30)
print("\nRandom Vector of size 30:")
print(random_vector_30)
print("\nMean value:", np.mean(random_vector_30))

# Normalize a 5x5 random matrix
random_matrix_5x5 = np.random.rand(5, 5)
normalized_matrix = (random_matrix_5x5 - np.mean(random_matrix_5x5)) / np.std(random_matrix_5x5)
print("\nNormalized 5x5 Random Matrix:")
print(normalized_matrix)

# Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
matrix_5x3 = np.random.rand(5, 3)
matrix_3x2 = np.random.rand(3, 2)
matrix_product = np.dot(matrix_5x3, matrix_3x2)
print("\nMatrix Product of a 5x3 and a 3x2 matrix:")
print(matrix_product)

# Create two 3x3 matrices and compute their dot product
matrix_A = np.random.rand(3, 3)
matrix_B = np.random.rand(3, 3)
dot_product = np.dot(matrix_A, matrix_B)
print("\nDot Product of two 3x3 matrices:")
print(dot_product)

# Given a 4x4 matrix, find its transpose
matrix_4x4 = np.random.rand(4, 4)
transpose_matrix = np.transpose(matrix_4x4)
print("\nTranspose of a 4x4 matrix:")
print(transpose_matrix)

# Create a 3x3 matrix and calculate its determinant
matrix_3x3_det = np.random.rand(3, 3)
determinant = np.linalg.det(matrix_3x3_det)
print("\nDeterminant of a 3x3 matrix:")
print(determinant)

# Create two matrices (A) (3x4) and (B) (4x3), and compute the matrix product (A * B)
matrix_A = np.random.rand(3, 4)
matrix_B = np.random.rand(4, 3)
matrix_product_AB = np.dot(matrix_A, matrix_B)
print("\nMatrix Product of two matrices A and B:")
print(matrix_product_AB)

# Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product
matrix_3x3 = np.random.rand(3, 3)
vector_3 = np.random.rand(3, 1)
matrix_vector_product = np.dot(matrix_3x3, vector_3)
print("\nMatrix-Vector Product of a 3x3 matrix and a 3-element column vector:")
print(matrix_vector_product)

# Solve the linear system (Ax = b) where (A) is a 3x3 matrix, and (b) is a 3x1 column vector
A = np.random.rand(3, 3)
b = np.random.rand(3, 1)
x = np.linalg.solve(A, b)
print("\nSolution to the linear system Ax = b:")
print(x)

# Given a 5x5 matrix, find the row-wise and column-wise sums
matrix_5x5 = np.random.rand(5, 5)
row_sums = np.sum(matrix_5x5, axis=1)
col_sums = np.sum(matrix_5x5, axis=0)
print("\nRow-wise sums of the 5x5 matrix:")
print(row_sums)
print("\nColumn-wise sums of the 5x5 matrix:")
print(col_sums)