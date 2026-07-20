from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation


T = sort_triangulation((1,2,4),(1,3,7),(1,4,5),(1,5,6),(1,6,7),(2,3,7),(2,4,5),(2,5,6),(2,6,7))

t_jl, m_jl = braiding(T, (2,5),(1,6),(4,5),(6,7),(1,5),(2,7),(5,6),(3,7),(2,5),(1,7),(3,5),(1,6),(5,7),(4,6))

t_kl, m_kl = braiding(T, (2,7),(1,6),(5,6),(3,7),(2,6),(1,7),(3,6),(5,7))

t_ik, m_ik = braiding(T, (1,5),(2,4),(5,6),(1,4),(2,6),(4,5),(6,7),(2,4),(1,6),(4,7),(1,5),(4,6))

t_jk, m_jk = braiding(T, (2,6),(1,5),(4,5),(6,7),(2,5),(1,6),(5,7),(4,6))

M_1 = m_jk*m_ik*m_kl*m_jl
M_2 = m_jl*m_jk*m_ik*m_kl

print("is relation valid: ", M_1 == M_2)

print("is M_1 unitary:", M_1*M_1.conjugate_transpose() == identity_matrix(M_1.nrows()))

#print("det m_jk", m_jk.det())
#print("det m_jl", m_jl.det())
#print("det m_kl", m_kl.det())
