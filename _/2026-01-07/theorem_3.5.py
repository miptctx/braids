from sage.all import *

F = SR

var('A')

n = matrix([0, A, -A**(-1), 0])
u = matrix([
  [0],
  [-A],
  [A**(-1)],
  [0]
])

# Tomotada's matrix
R = matrix([
  [A, 0,       0,         0],
  [0, 0,       A**(-1),   0],
  [0, A**(-1), A-A**(-3), 0],
  [0, 0,       0,         A]
])

'''
# Kauffman's matrix
R = matrix([
  [A**(-1), 0,                        0,         0],
  [0,       -A**(-3) + A**(-1),       A,         0],
  [0,       A,                        0,         0],
  [0,       0,                        0,         A]
])
'''

id = matrix(F, [
  [1,0],
  [0,1]
])

m_1 = id.tensor_product(n)
show(m_1)
print("")

m_2 = R.tensor_product(id)
show(m_2)
print("")

m_l = m_1*m_2
show(m_l)



m_1 = n.tensor_product(id)
show(m_1)
print("")

m_2 = id.tensor_product(R**(-1))
show(m_2)
print("")

m_r = m_1*m_2
show(m_r)
print("")

print("is equal?")
print(m_l == m_r)
print("")

nR = n*R
print("n*R")
show(nR)
print("")

nrTest = -A**(-1)*n
print("-A**(-1)*n")
show(nrTest.simplify_full())
print("")

print("is equal", nR == nrTest)
