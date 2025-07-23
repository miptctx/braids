from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation


T = sort_triangulation((1,2,4),(1,3,8),(1,4,5),(1,5,6),(1,6,7),(1,7,8),(2,3,8),(2,4,5),(2,5,6),(2,6,7),(2,7,8))

t_ij, m_ij = braiding(T, (2,5),(1,4),(5,6),(2,4),(1,5),(4,6))

t_kl, m_kl = braiding(T, (2,8),(1,7),(3,8),(6,7),(2,7),(1,8),(3,7),(6,8))

A_1 = m_ij*m_kl
A_2 = m_kl*m_ij

print("is realtion valid: ", A_1 == A_2)
