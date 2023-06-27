import numpy as np

# Create a matrix 2x2

matrix = np.array([[1,2],[3,4]])

#populate matrix

print(matrix)

#insert numbers in all matrix positions using for

for i in range(2):
    for j in range(2):
        matrix[i,j] = 50

print(matrix)

