from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation, rotate_tuple

F=CC

T = sort_triangulation((1,2,4),(1,3,6),(1,4,5),(1,5,6),(2,3,6),(2,4,5),(2,5,6))

t_ij, m_ij = braiding_ext(T,
                          (rotate_tuple(2,6,5,4),(2,5)),
                          (rotate_tuple(1,2,4,5),(1,4)),
                          (rotate_tuple(1,5,4,6),(5,6)),
                          (rotate_tuple(2,6,4,5),(2,4)),
                          (rotate_tuple(1,2,5,4),(1,5)),
                          (rotate_tuple(1,4,5,6),(4,6)),
                          F=F)

t_ik, m_ik = braiding_ext(T,
                          (rotate_tuple(1,4,5,6),(1,5)),
                          (rotate_tuple(1,2,5,4),(2,4)),
                          (rotate_tuple(2,6,4,5),(5,6)),
                          (rotate_tuple(1,5,4,6),(1,4)),
                          (rotate_tuple(2,3,6,4),(2,6)),
                          (rotate_tuple(2,4,6,5),(4,5)),
                          (rotate_tuple(1,6,4,3),(3,6)),
                          (rotate_tuple(2,3,4,6),(2,4)),
                          (rotate_tuple(1,5,6,4),(1,6)),
                          (rotate_tuple(1,4,6,3),(3,4)),
                          (rotate_tuple(1,2,5,4),(1,5)),
                          (rotate_tuple(1,4,5,6),(4,6)),
                          F=F)

t_jk, m_jk = braiding_ext(T,
                          (rotate_tuple(2,3,6,5),(2,6)),
                          (rotate_tuple(1,4,5,6),(1,5)),
                          (rotate_tuple(2,5,6,4),(4,5)),
                          (rotate_tuple(1,6,5,3),(3,6)),
                          (rotate_tuple(2,3,5,6),(2,5)),
                          (rotate_tuple(1,4,6,5),(1,6)),
                          (rotate_tuple(1,5,6,3),(3,5)),
                          (rotate_tuple(2,6,5,4),(4,6)),
                          F=F)


M_1 = (m_jk*m_ik*m_ij).apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
M_2 = (m_ik*m_ij*m_jk).apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
M_3 = (m_ij*m_jk*m_ik).apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)

show(M_1)
print("")
show(M_2)
print("")
show(M_3)


print("is realtion valid: ", M_1 == M_2 and M_2 == M_3)
