from sage.all import *

F = SR

var('n_00, n_01, n_10, n_11, u_00, u_01, u_10, u_11')

n = matrix(F, [n_00, n_01, n_10, n_11])
u = matrix(F, [
  [u_00],
  [u_01],
  [u_10],
  [u_11]
])

id = matrix(F, [[1,0], [0,1]])

m_l = id.tensor_product(u)
m_r = n.tensor_product(id)

show(m_l)
print("")
show(m_r)
print("")

m = m_r*m_l
show(m)
print("")
print("")


m_l = u.tensor_product(id)
m_r = id.tensor_product(n)

show(m_l)
print("")
show(m_r)
print("")

m = m_r*m_l
show(m)