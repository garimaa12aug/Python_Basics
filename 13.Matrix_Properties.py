# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Matrix Shape:",matrix.shape)
print("Number of elements:",matrix.size)
print("Number of dimentions:",matrix.ndim)
print("Average of matrix:",np.mean(matrix))
print("Maximum number:",np.max(matrix))
print("Coloumn with minimum numbers:",np.min(matrix, axis=1))
print("Diagnol of matrix:",matrix.diagonal())
print("Determinant of matrix:",np.linalg.det(matrix))

'''
output
Matrix Shape: (3, 3)
Number of elements: 9
Number of dimentions: 2
Average of matrix: 5.0
Maximum number: 9
Coloumn with minimum numbers: [1 4 7]
Diagnol of matrix: [1 5 9]
Determinant of matrix: 0.0

'''
