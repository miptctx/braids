# This is trefoil on 2 strands

from sage.all import *
from braids import knotting_max, knotting_min, braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

F = QQ

P = sort_triangulation({1,2,6}, {1,3,4},{1,4,5},{1,5,6},{2,3,4},{2,4,5},{2,5,6})

t, s_1 = braiding(P, (2,5),(1,6),(4,5), F=F)

t, s_2 = braiding(P, (1,5),(2,4),(5,6),(3,4), F=F)

m_l = s_1*s_2*s_1
m_r = s_2*s_1*s_2

print("Result matrix m_l")
show(m_l)

print("Result matrix m_r")
show(m_r)

print("Equation satisfied: ", m_l == m_r)
