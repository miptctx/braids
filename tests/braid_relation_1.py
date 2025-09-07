# This is trefoil on 2 strands

from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation

F = QQ

P = sort_triangulation({1,2,7}, {1,3,4},{1,4,5},{1,5,6},{1,6,7},{2,3,4},{2,4,5},{2,5,6},{2,6,7})

t_ij, m_ij = braiding(P, (2,6),(1,7),(5,6), (2,4),(1,5),(5,7),(3,4), F=F)

t_ji, m_ji = braiding(P, (2,4),(1,5),(5,6),(3,4), (2,6),(1,7),(4,6), F=F)

assert t_ij == t_ji

print("Result matrix m_ij")
show(m_ij)

print("Result matrix m_ji")
show(m_ji)

print("Equation satisfied: ", m_ij == m_ji)
