from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation

F = CC

P = sort_triangulation({1,2,6}, {1,3,4},{1,4,5},{1,5,6},{2,3,4},{2,4,5},{2,5,6})

t_l, m_l = braiding_ext(P,
                        ((2,4,5,6),(2,5)),
                        ((1,2,6,5),(1,6)),
                        ((1,5,6,4),(4,5)),

                        ((1,5,6,4),(1,6)),
                        ((2,3,4,6),(2,4)),
                        ((2,6,4,5),(5,6)),
                        ((1,4,6,3),(3,4)),

                        ((2,6,4,5),(2,4)),
                        ((1,2,5,4),(1,5)),
                        ((1,4,5,6),(4,6)),
                        F=F)

t_r, m_r = braiding_ext(P,
                        ((1,6,5,4),(1,5)),
                        ((2,3,4,5),(2,4)),
                        ((2,5,4,6),(5,6)),
                        ((1,4,5,3),(3,4)),

                        ((2,5,4,6),(2,4)),
                        ((1,2,6,4),(1,6)),
                        ((1,4,6,5),(4,5)),

                        ((1,4,6,5),(1,6)),
                        ((2,3,5,6),(2,5)),
                        ((2,6,5,4),(4,6)),
                        ((1,5,6,3),(3,5)),
                        F=F)

assert t_l == t_r

m_l = m_l.apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
print("Result matrix m_l")
show(m_l)

m_r = m_r.apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
print("Result matrix m_r")
show(m_r)

print("Equation satisfied: ", m_l == m_r)
