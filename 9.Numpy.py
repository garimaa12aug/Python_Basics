'''
NumPy¶

    Numpy is the fundamental package for numerical computing with Python. It contains among other things:
    a powerful N-dimensional array object
    sophisticated (broadcasting) functions
    tools for integrating C/C++ and Fortran code
    useful linear algebra, Fourier transform, and random number capabilities 
'''

import numpy as np   # Importing libraries

a = np.array([0, 1, 2])
b = np.array([5, 5, 5])

print("Matrix A\n", a)
print("Matrix B\n", b)

print("Regular matrix addition A+B\n", a + b)

print("Addition using Broadcasting A+5\n", a + 5)

'''
output
Matrix A
 [0 1 2]
Matrix B
 [5 5 5]
Regular matrix addition A+B
 [5 6 7]
Addition using Broadcasting A+5
 [5 6 7]

'''
