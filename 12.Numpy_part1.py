# Load library
import numpy as np

# Create row vector
vector = np.array([1, 2, 3, 4, 5, 6])
print("Vector:",vector)

# Select second element
print("Element 2 in Vector is",vector[1])




# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Matrix\n",matrix)

# Select second row
print("Second row of Matrix\n",matrix[1,:])
print("Third coloumn of Matrix\n",matrix[:,2])

'''
output
Vector: [1 2 3 4 5 6]
Element 2 in Vector is 2
Matrix
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
Second row of Matrix
 [4 5 6]
Third coloumn of Matrix
 [3 6 9]

'''
