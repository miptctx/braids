from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation

F=CC

T = sort_triangulation((1,2,4),(1,3,8),(1,4,5),(1,5,6),(1,6,7),(1,7,8),(2,3,8),(2,4,5),(2,5,6),(2,6,7),(2,7,8))

t_1, m_ij = braiding(T, (1,5),(2,4),(1,6),(1,7),(4,5),(4,6),(7,8),(2,8),(1,4),(3,8),(4,7),(2,4),(1,8),(1,7),(3,4),(1,6),(4,8),(4,7),(1,5),(4,6), F=F)

t_2, m_kl = braiding(T, (2,5),(1,6),(4,5),(6,7),(1,5),(2,7),(5,6),(7,8),(2,5),(1,7),(1,6),(5,8),(5,7),(4,6), F=F)

A_1 = (m_ij*m_kl).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
A_2 = (m_kl*m_ij).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

show(A_1)
print("")
show(A_2)

print("is realtion valid: ", A_1 == A_2)
