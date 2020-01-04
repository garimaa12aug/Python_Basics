
#Unvectorized vs Vectorized Implementations¶


# Importing libraries
import numpy as np

# Defining matrices
mat_a = [[6, 7, 8],[5, 4, 5],[1, 1, 1]]
mat_b = [[1, 2, 3],[1, 2, 3],[1, 2, 3]]

# Getting a row from matrix
def get_row(matrix, row):
    return matrix[row]

# Getting a coloumn from matrix
def get_column(matrix, column_number):
    column = []
 
    for i in range(len(matrix)):
        column.append(matrix[i][column_number])
 
    return column

# Multiply a row with coloumn
def unv_dot_product(vector_one, vector_two):
    total = 0
 
    if len(vector_one) != len(vector_two):
        return total
 
    for i in range(len(vector_one)):
        product = vector_one[i] * vector_two[i]
        total += product
 
    return total

# Multiply two matrixes
def matrix_multiplication(matrix_one, matrix_two):
    m_rows = len(matrix_one)
    p_columns = len(matrix_two[0])
    result = []
    
    for i in range(m_rows):
        row_result = []
 
        for j in range(p_columns):
            row = get_row(matrix_one, i)
            column = get_column(matrix_two, j)
            product = unv_dot_product(row, column)
            
            row_result.append(product) 
        result.append(row_result)
        
    return result

print("Matrix A: ", mat_a,"\n")
print("Matrix B: ", mat_b,"\n")

print("Unvectorized Matrix Multiplication\n",matrix_multiplication(mat_a,mat_b),"\n")

'''
output
Matrix A:  [[6, 7, 8], [5, 4, 5], [1, 1, 1]] 

Matrix B:  [[1, 2, 3], [1, 2, 3], [1, 2, 3]] 

Unvectorized Matrix Multiplication
 [[21, 42, 63], [14, 28, 42], [3, 6, 9]] 
'''



# Vectorized Implementation
npm_a = np.array(mat_a)
npm_b = np.array(mat_b)

print("Vectorized Matrix Multiplication\n",npm_a.dot(npm_b),"\n") 
# A.dot(B) is a numpy built-in function for dot product

'''
output
Vectorized Matrix Multiplication
 [[21 42 63]
 [14 28 42]
 [ 3  6  9]] 

Tip:¶

    Vectorization reduces number of lines of code
    Always prefer libraries and avoid coding from scratch 
'''


