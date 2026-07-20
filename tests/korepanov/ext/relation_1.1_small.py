from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation, rotate_tuple

F=CC

T = sort_triangulation((1,2,4),(1,3,7),(1,4,5),(1,5,6),(1,6,7),(2,3,7),(2,4,5),(2,5,6),(2,6,7))

t_ij, m_ij = braiding_ext(T,
                          ((2,6,5,4),(2,5)),
                          ((1,2,4,5),(1,4)),
                          ((1,5,4,6),(5,6)),
                          ((2,6,4,5),(2,4)),
                          ((1,2,5,4),(1,5)),
                          ((1,4,5,6),(4,6)),
                          F=F)

t_kl, m_kl = braiding_ext(T,
                          ((2,3,7,6),(2,7)),
                          ((1,5,6,7),(1,6)),
                          ((2,6,7,5),(5,6)),
                          ((1,7,6,3),(3,7)),
                          ((2,3,6,7),(2,6)),
                          ((1,5,7,6),(1,7)),
                          ((1,6,7,3),(3,6)),
                          ((2,7,6,5),(5,7)),
                          F=CC)

assert t_ij == t_kl

lhs = (m_kl*m_ij).apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
rhs = (m_ij*m_kl).apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)

print("lhs")
print(lhs)

print("rhs")
print(rhs)

print("is realtion valid: ", lhs == rhs)
