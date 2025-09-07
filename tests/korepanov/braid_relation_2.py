from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation

F = CC

P = sort_triangulation({1,2,6}, {1,3,4},{1,4,5},{1,5,6},{2,3,4},{2,4,5},{2,5,6})

t_l, m_l = braiding(P,
                  (2,5),(1,6),(4,5),
                  (1,6),(2,4),(5,6),(3,4),
                  (2,4),(1,5),(4,6),
                  F=F)

t_r, m_r = braiding(P,
                  (1,5),(2,4),(5,6),(3,4),
                  (2,4),(1,6),(4,5),
                  (1,6),(2,5),(4,6),(3,5),
                  F=F)

assert t_l == t_r

m_l = m_l.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
print("Result matrix m_l")
show(m_l)

m_r = m_r.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
print("Result matrix m_r")
show(m_r)

print("Equation satisfied: ", m_l == m_r)
