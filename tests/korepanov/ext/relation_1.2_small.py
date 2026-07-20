from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation, rotate_tuple


T = sort_triangulation((1,2,4),(1,3,7),(1,4,5),(1,5,6),(1,6,7),(2,3,7),(2,4,5),(2,5,6),(2,6,7))

print("############## First braid ##############")

t_1, m_ij = braiding_ext(T,
                        ((1,4,5,6),(1,5)),
                        ((1,2,5,4),(2,4)),
                        ((1,4,6,7),(1,6)),
                        ((1,5,6,4),(4,5)),
                        ((2,7,4,6),(6,7)),
                        ((1,6,4,7),(1,4)),
                        ((2,3,7,4),(2,7)),
                        ((2,4,7,6),(4,6)),
                        ((1,7,4,3),(3,7)),
                        ((2,3,4,7),(2,4)),
                        ((1,6,7,4),(1,7)),
                        ((1,5,6,4),(1,6)),
                        ((1,4,7,3),(3,4)),
                        ((1,4,6,7),(4,7)),
                        ((1,2,5,4),(1,5)),
                        ((1,4,5,6),(4,6)),
                        F=CC)

print("b_ij")
print(latex(m_ij.apply_map(lambda x: round(x.real(), 5) + round(x.imag(), 5))))

print("############## Second braid ##############")

t_2, m_kl = braiding_ext(T,
                        ((2,7,6,5),(2,6)),
                        ((1,4,5,6),(1,5)),
                        ((2,5,6,4),(4,5)),
                        ((1,6,5,7),(6,7)),
                        ((2,7,5,6),(2,5)),
                        ((1,4,6,5),(1,6)),
                        ((1,5,6,7),(5,7)),
                        ((2,6,5,4),(4,6)),
                        F=CC)

print("b_kl")
print(latex(m_kl.apply_map(lambda x: round(x.real(), 5) + round(x.imag(), 5))))

assert t_1 == t_2

print("Result lhs")
lhs = (m_kl*m_ij).apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
show(lhs)

print("Result rhs")
rhs = (m_ij*m_kl).apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
show(rhs)

show(latex(lhs.apply_map(lambda x: round(x.real(), 5) + round(x.imag(), 5))))

print("is realtion valid: ", lhs == rhs)
