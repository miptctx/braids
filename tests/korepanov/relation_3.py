from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation


F=CC


T = sort_triangulation((1,2,4),(1,3,8),(1,4,5),(1,5,6),(1,6,7),(1,7,8),(2,3,8),(2,4,5),(2,5,6),(2,6,7),(2,7,8))

t_jl, m_jl = braiding(T, (2,6),(1,5),(2,7),(2,8),(4,5),(3,8),(5,6),(5,7),(1,8),(2,5),(1,7),(3,5),(1,6),(5,8),(4,6),(5,7), F=F)

t_kl, m_kl = braiding(T, (1,7),(2,8),(3,8),(6,7),(2,7),(1,8),(3,7),(6,8), F=F)

t_ik, m_ik = braiding(T, (2,5),(1,4),(2,6),(2,7),(4,5),(4,6),(7,8),(2,4),(1,7),(4,8),(1,6),(4,7),(1,5),(4,6), F=F)

t_jk, m_jk = braiding(T, (1,5),(2,6),(2,7),(4,5),(5,6),(7,8),(2,5),(1,7),(1,6),(5,8),(5,7),(4,6), F=F)

M_1 = (m_jk*m_ik*m_kl*m_jl).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
M_2 = (m_jl*m_jk*m_ik*m_kl).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

show(M_1)
print("")
show(M_2)

print("is relation valid: ", M_1 == M_2)
