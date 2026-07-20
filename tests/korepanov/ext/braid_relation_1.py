# This is trefoil on 2 strands

from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation

F = CC

P = sort_triangulation({1,2,7},{1,3,4},{1,4,5},{1,5,6},{1,6,7},{2,3,4},{2,4,5},{2,5,6},{2,6,7})

t_ij, m_ij = braiding_ext(P,
                          ((2,5,6,7),(2,6)),
                          ((1,2,7,6),(1,7)),
                          ((1,6,7,5),(5,6)),

                          ((2,3,4,5),(2,4)),
                          ((1,7,5,4),(1,5)),
                          ((2,5,4,7),(5,7)),
                          ((1,4,5,3),(3,4)),

                          F=F)

t_ji, m_ji = braiding_ext(P,
                          ((2,3,4,5),(2,4)),
                          ((1,6,5,4),(1,5)),
                          ((2,5,4,6),(5,6)),
                          ((1,4,5,3),(3,4)),

                          ((2,4,6,7),(2,6)),
                          ((1,2,7,6),(1,7)),
                          ((1,6,7,4),(4,6)),

                          F=F)

assert t_ij == t_ji

m_ij = m_ij.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

print("Result matrix m_ij")
show(m_ij)

m_ji = m_ji.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

print("Result matrix m_ji")
show(m_ji)

print("Equation satisfied: ", m_ij == m_ji)
