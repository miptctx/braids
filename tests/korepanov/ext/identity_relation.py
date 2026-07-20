from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation

F = CC

P = sort_triangulation({1,2,3}, {1,3,4})

t_1, m_1 = braiding_ext(P, ((1,2,3,4),(1,3)), ((1,2,3,4),(2,4)), F=F)

m_1 = m_1.apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
print("Result matrix m_1")
show(m_1)
