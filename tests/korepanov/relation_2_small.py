from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation

F=CC

T = sort_triangulation((1,2,4),(1,3,6),(1,4,5),(1,5,6),(2,3,6),(2,4,5),(2,5,6))

t_ij, m_ij = braiding(T, (2,5),(1,4),(5,6),(2,4),(1,5),(4,6), F=F)

t_ik, m_ik = braiding(T, (1,5),(2,4),(5,6),(1,4),(2,6),(4,5),(3,6),(2,4),(1,6),(3,4),(1,5),(4,6), F=F)

t_jk, m_jk = braiding(T, (2,6),(1,5),(4,5),(3,6),(2,5),(1,6),(3,5),(4,6), F=F)


#M_1 = (m_ij*m_ik*m_jk).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
#M_2 = (m_jk*m_ij*m_ik).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
#M_3 = (m_ik*m_jk*m_ij).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

M_1 = (m_jk*m_ik*m_ij).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
M_2 = (m_ik*m_ij*m_jk).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
M_3 = (m_ij*m_jk*m_ik).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

show(M_1)
print("")
show(M_2)
print("")
show(M_3)


print("is realtion valid: ", M_1 == M_2 and M_2 == M_3)
