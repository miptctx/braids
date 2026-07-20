from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation


T = sort_triangulation((1,2,4),(1,3,6),(1,4,5),(1,5,6),(2,3,6),(2,4,5),(2,5,6))

t_ij, m_ij = braiding(T, (2,5),(1,4),(5,6),(2,4),(1,5),(4,6))

t_ik, m_ik = braiding(T, (1,5),(2,4),(5,6),(1,4),(2,6),(4,5),(3,6),(2,4),(1,6),(3,4),(1,5),(4,6))

t_jk, m_jk = braiding(T, (2,6),(1,5),(4,5),(3,6),(2,5),(1,6),(3,5),(4,6))


M_1 = m_jk*m_ik*m_ij
M_2 = m_ik*m_ij*m_jk
M_3 = m_ij*m_jk*m_ik

print("is realtion valid: ", M_1 == M_2 and M_2 == M_3)
