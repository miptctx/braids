from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation, rotate_tuple

F=CC

T = sort_triangulation((1,2,4),(1,3,7),(1,4,5),(1,5,6),(1,6,7),(2,3,7),(2,4,5),(2,5,6),(2,6,7))

print("m_jl")
t_jl, m_jl = braiding_ext(T,
                          ((2,6,5,4),(2,5)),
                          ((1,5,6,7),(1,6)),
                          ((1,4,6,5),(4,5)),
                          ((2,7,5,6),(6,7)),
                          ((1,6,5,7),(1,5)),
                          ((2,3,7,5),(2,7)),
                          ((2,5,7,6),(5,6)),
                          ((1,7,5,3),(3,7)),
                          ((2,3,5,7),(2,5)),
                          ((1,6,7,5),(1,7)),
                          ((1,5,7,3),(3,5)),
                          ((1,4,6,5),(1,6)),
                          ((1,5,6,7),(5,7)),
                          ((2,6,5,4),(4,6)),
                          F=F)

print("m_kl")
t_kl, m_kl = braiding_ext(T,
                          ((2,3,7,6),(2,7)),
                          ((1,5,6,7),(1,6)),
                          ((2,6,7,5),(5,6)),
                          ((1,7,6,3),(3,7)),
                          ((2,3,6,7),(2,6)),
                          ((1,5,7,6),(1,7)),
                          ((1,6,7,3),(3,6)),
                          ((2,7,6,5),(5,7)),
                          F=F)

print("m_ik")
t_ik, m_ik = braiding_ext(T,
                          ((1,4,5,6),(1,5)),
                          ((1,2,5,4),(2,4)),
                          ((2,6,4,5),(5,6)),
                          ((1,5,4,6),(1,4)),
                          ((2,7,6,4),(2,6)),
                          ((2,4,6,5),(4,5)),
                          ((1,6,4,7),(6,7)),
                          ((2,7,4,6),(2,4)),
                          ((1,5,6,4),(1,6)),
                          ((1,4,6,7),(4,7)),
                          ((1,2,5,4),(1,5)),
                          ((1,4,5,6),(4,6)),
                          F=F)

print("m_jk")
t_jk, m_jk = braiding_ext(T,
                          ((2,7,6,5),(2,6)),
                          ((1,4,5,6),(1,5)),
                          ((2,5,6,4),(4,5)),
                          ((1,6,5,7),(6,7)),
                          ((2,7,5,6),(2,5)),
                          ((1,4,6,5),(1,6)),
                          ((1,5,6,7),(5,7)),
                          ((2,6,5,4),(4,6)),
                          F=F)


assert t_jk == t_kl
assert t_kl == t_ik
assert t_ik == t_jk

lhs = (m_jk*m_ik*m_kl*m_jl).apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
rhs = (m_jl*m_jk*m_ik*m_kl).apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)

print("Result edges m_jk_ik_kl_jl")
show(lhs)

print("Result edges e_jl_jk_ik_kl")
show(rhs)

print("is relation valid: ", lhs == rhs)

#print("is M_1 unitary:", lhs*lhs.conjugate_transpose() == identity_matrix(lhs.nrows()))
# show(lhs.conjugate_transpose())
#print("is ermitova:", lhs == lhs.conjugate_transpose())

