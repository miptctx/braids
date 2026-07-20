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
t, m_3 = knotting_max(t, {1,2,7}, 8, {1,2,8}, 9, F=F)


print_triangles_pretty(t)

t, m_b = braiding(t,
                  (2,7),(1,8),(6,7),(8,9),
                  (2,5),(1,6),(1,8),(4,5),(5,6),(7,8),
                  (1,8),(2,6),(2,4),(5,8),(6,8),(3,4),
                  (2,4),(1,6),(4,8),(5,6),
                  (2,8),(1,6),(4,6),(3,8),
                  (2,5),(1,4),(2,7),(4,8),(4,5),(7,9),
                  (2,5),(1,8),(6,8),(5,7),
                  F=F)

t, m_5 = knotting_min(t, 9, 4, F=F)
t, m_6 = knotting_min(t, 7, 8, F=F)
t, m_7 = knotting_min(t, 5, 6, F=F)

m = m_7*m_6*m_5*m_b*m_3*m_2*m_1

assert P == t

print("-------------")
print("Result matrix")
show(m)
print("-------------")

show(m_7*m_6*m_5*m_b*m_3*m_2)
show(m_1)
