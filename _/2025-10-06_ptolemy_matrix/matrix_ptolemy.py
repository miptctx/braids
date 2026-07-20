import random
from sage.all import *
from sage.matrix.constructor import random_diagonalizable_matrix

'''
A = matrix([3])
B = matrix([7])
C = matrix([6])
D = matrix([4])
E = matrix([1])
X = matrix([2])
Y = matrix([5])
'''

N = 5
matrix_space = sage.matrix.matrix_space.MatrixSpace(QQ, N)

'''
A = random_matrix(QQ, N, num_bound=-10, den_bound=10)
B = random_matrix(QQ, N, num_bound=-10, den_bound=10)
C = random_matrix(QQ, N, num_bound=-10, den_bound=10)
D = random_matrix(QQ, N, num_bound=-10, den_bound=10)
E = random_matrix(QQ, N, num_bound=-10, den_bound=10)
X = random_matrix(QQ, N, num_bound=-10, den_bound=10)
Y = random_matrix(QQ, N, num_bound=-10, den_bound=10)
'''

'''
A = random_diagonalizable_matrix(matrix_space)
B = random_diagonalizable_matrix(matrix_space)
C = random_diagonalizable_matrix(matrix_space)
D = random_diagonalizable_matrix(matrix_space)
E = random_diagonalizable_matrix(matrix_space)
X = random_diagonalizable_matrix(matrix_space)
Y = random_diagonalizable_matrix(matrix_space)
'''

A, _ = random_diagonalizable_matrix(matrix_space).diagonalization()
B, _ = random_diagonalizable_matrix(matrix_space).diagonalization()
C, _ = random_diagonalizable_matrix(matrix_space).diagonalization()
D, _ = random_diagonalizable_matrix(matrix_space).diagonalization()
E, _ = random_diagonalizable_matrix(matrix_space).diagonalization()
X, _ = random_diagonalizable_matrix(matrix_space).diagonalization()
Y, _ = random_diagonalizable_matrix(matrix_space).diagonalization()

'''
A = identity_matrix(QQ, N)
B = identity_matrix(QQ, N)
C = identity_matrix(QQ, N)
D = identity_matrix(QQ, N)
E = identity_matrix(QQ, N)
X = identity_matrix(QQ, N)
Y = identity_matrix(QQ, N)
'''

Z = (E*C + X*D)*(Y**-1)
T = (Z*B + A*C)*(X**-1)
U = (E*T + A*D)*(Z**-1)
V = (D*B + U*C)*(T**-1)
W = (E*B + A*V)*(U**-1)

print("Z =")
print(Z)
print("T =")
print(T)
print("U =")
print(U)
print("V =")
print(V)

print("X =")
print(X)
print("X.det =", X.det())
print("X.trace =", X.trace())

print("Y =")
print(Y)
print("Y.det =", Y.det())
print("Y.trace =", Y.trace())

print("X==W:", X==W)
