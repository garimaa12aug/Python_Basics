'''
Broadcasting Rules

When operating on two arrays, NumPy compares their shapes element-wise. It starts with the trailing dimensions, and works its way forward. Two dimensions are compatible when they are equal, or one of them is 1 

'''

# Lets go for a 2D matrix
c = np.array([[0, 1, 2],[3, 4, 5],[6, 7, 8]])
d = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])

e = np.array([1, 2, 3])

print("Matrix C\n", c)
print("Matrix D\n", d)
print("Matrix E\n", e)

print("Regular matrix addition C+D\n", c + d)

print("Addition using Broadcasting C+E\n", c + e)


'''
output
Matrix C
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
Matrix D
 [[1 2 3]
 [1 2 3]
 [1 2 3]]
Matrix E
 [1 2 3]
Regular matrix addition C+D
 [[ 1  3  5]
 [ 4  6  8]
 [ 7  9 11]]
Addition using Broadcasting C+E
 [[ 1  3  5]
 [ 4  6  8]
 [ 7  9 11]]

In [14]:

M = np.ones((3, 3))
print("Matrix M:\n",M)

Matrix M:
 [[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
'''

