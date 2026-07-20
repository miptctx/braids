from sage.all import *

A = var('A')

M = Matrix([[0, sqrt(-1)*A], [-sqrt(-1)*A**(-1), 0]])

MxM = M.tensor_product(M)

show(MxM)
