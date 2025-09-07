from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation

F = CC

P = sort_triangulation({1,2,7},{1,3,4},{1,4,5},{1,5,6},{1,6,7},{2,3,4},{2,4,5},{2,5,6},{2,6,7})

t_12, m_12 = braiding(P, (1,6),(2,5), F=F)

t_21, m_21 = braiding(P, (2,5),(1,6), F=F)

assert t_12 == t_21

m_12 = m_12.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
print("Result matrix m_12")
show(m_12)

m_21 = m_21.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
print("Result matrix m_21")
show(m_21)

print("Equation satisfied: ", m_12 == m_21)
