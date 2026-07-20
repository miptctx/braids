from sage.all import *
from braids import knotting_max, knotting_min, braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

F = QQ

t = sort_triangulation({1,2,5}, {1,3,4}, {1,4,5}, {2,3,5}, {3,4,5})

print_triangles_pretty(t)

t, m_0 = knotting_min(t, 4, F=F)

t, m_1 = knotting_max(t, {1,2,5}, 4, F=F)

t, m_2 = braiding(t, (2,5), F=F)

m_l = m_2*m_1*m_0

print("Result matrix")
show(m_l)

print("")


t = sort_triangulation({1,2,5}, {1,3,4}, {1,4,5}, {2,3,5}, {3,4,5})

print_triangles_pretty(t)

t, m_0 = knotting_min(t, 4, F=F)

t, m_1 = knotting_max(t, {2,3,5}, 4, F=F)

t, m_2 = braiding(t, (2,5), F=F)

m_r = m_2*m_1*m_0

print("Result matrix")
show(m_r)

print("Matrix eqal: ", m_l == m_r)
