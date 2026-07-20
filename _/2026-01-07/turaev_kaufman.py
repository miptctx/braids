from sage.all import *

A = var('A')

F = SR

n = matrix(F, [[0, sqrt(-1)*A, -sqrt(-1)*A**(-1), 0]])

u = n.transpose()

I = matrix(F, [[1, 0], [0, 1]])

m_1 = I.tensor_product(u)
m_2 = n.tensor_product(I)

print("I x u")
show(m_1)


print("")
print("n x I")
show(m_2)


m = m_2*m_1
print("")
print("(n x I)(I x u)")
show(m)
