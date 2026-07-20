from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation

F = CC

P = sort_triangulation({1,2,3}, {1,3,4})

t_1, m_1 = braiding(P, (1,3),(2,4), F=F)

m_1 = m_1.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
print("Result matrix m_1")
show(m_1)
