from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation


T = sort_triangulation((1,2,4),(1,3,8),(1,4,5),(1,5,6),(1,6,7),(1,7,8),(2,3,8),(2,4,5),(2,5,6),(2,6,7),(2,7,8))

t_ij, m_ij = braiding(T, (2,5),(1,4),(2,6),(4,5),(6,7),(2,4),(1,6),(4,7),(1,5),(4,6))

t_ik, m_ik = braiding(T, (2,5),(1,4),(2,6),(2,7),(4,5),(2,8),(3,8),(4,6),(4,7),(2,4),(1,8),(1,7),(3,4),(1,6),(4,8),(4,7),(1,5),(4,6))

t_jk, m_jk = braiding(T, (2,7),(1,6),(2,8),(5,6),(3,8),(6,7),(2,6),(1,8),(3,6),(1,7),(5,7),(6,8))


M_1 = m_ij*m_ik*m_jk
M_2 = m_jk*m_ij*m_ik
M_3 = m_ik*m_jk*m_ij

print("is realtion valid: ", M_1 == M_2 and M_2 == M_3)
