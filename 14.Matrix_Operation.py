matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("Flattened Matrix\n",matrix.flatten())
print("Reshaping Matrix\n",matrix.reshape(9,1))
print("Transposed Matrix\n",matrix.T)




# Create matrix
matrix_a = np.array([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 2]])

# Create matrix
matrix_b = np.array([[1, 3, 1],
                     [1, 3, 1],
                     [1, 3, 8]])

print("Matrix Addition\n",np.add(matrix_a, matrix_b))
print("Scalar Multiplication\n",np.multiply(matrix_a, matrix_b))
print("Matrix Multiplication\n",np.dot(matrix_a, matrix_b))


'''
output
Flattened Matrix
 [1 2 3 4 5 6 7 8 9]
Reshaping Matrix
 [[1]
 [2]
 [3]
 [4]
 [5]
 [6]
 [7]
 [8]
 [9]]
Transposed Matrix
 [[1 4 7]
 [2 5 8]
 [3 6 9]]
Matrix Addition
 [[ 2  4  2]
 [ 2  4  2]
 [ 2  4 10]]
Scalar Multiplication
 [[ 1  3  1]
 [ 1  3  1]
 [ 1  3 16]]
Matrix Addition
 [[ 3  9 10]
 [ 3  9 10]
'''
