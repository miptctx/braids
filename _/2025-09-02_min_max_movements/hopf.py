# This is trefoil on 3 strands

from sage.all import *
from braids import braiding
from braids.knotting import knotting_max, knotting_min
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

F = QQ

P = sort_triangulation({1,2,3})

t, m_1 = knotting_max(P, {1,2,3}, 4, {1,2,4}, 5, F=F)
t, m_2 = knotting_max(t, {1,2,5}, 6, {1,2,6}, 7, F=F)

t, m_b = braiding(t,
                  (2,5),(1,6),(6,7),(4,5),(2,6),(1,5),(4,6),(5,7),
                  F=F)

t, m_5 = knotting_min(t, 7, 6, F=F)
t, m_6 = knotting_min(t, 5, 4, F=F)

m = m_6*m_5*m_b*m_2*m_1

assert P == t

print("-------------")
print("Result matrix")
show(m)
print("-------------")

show(m_6*m_5*m_b*m_2)
show(m_1)
