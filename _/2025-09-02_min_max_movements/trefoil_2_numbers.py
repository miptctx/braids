# This is trefoil on 2 strands

from sage.all import *
from braids import braiding
from braids.knotting import knotting_max, knotting_min
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

def _show(*args):
  # show(latex(*args))
  show(*args)


F = QQ

T = sort_triangulation({1,2,3})

t, m_1 = knotting_max(T, {1,2,3}, 4, {1,2,4}, 5, F=F)
t, m_2 = knotting_max(t, {1,2,5}, 6, {1,2,6}, 7, F=F)

print_triangles_pretty(t)
t, m_b = braiding(t,
                  (2,5),(1,6),(4,5),(6,7),
                  (2,4),(1,6),(5,6),(3,4),(2,6),(1,4),(4,5),(3,6), (2,4),(1,6),(5,6),(3,4),
                  (2,5),(1,4),(4,6),(5,7),
                  F=F)

'''
m_b_list = list(m_b)
m_b_list[2][2] = m_b[2][2]+17
show(m_b_list)
m_b = matrix(m_b_list)
'''

t, m_4 = knotting_min(t, 7, 4, F=F)
t, m_5 = knotting_min(t, 5, 6, F=F)

m = m_5 * m_4 * m_b * m_2 * m_1

assert T == t

'''
print("matrix maximum 1")
_show(m_1)

print("matrix maximum 2")
_show(m_2)

print("matrix braid")
_show(m_b)

print("matrix minimum 1")
_show(m_4)

print("matrix minimum 2")
_show(m_5)

print("matrix max 1, braid, min 1")
_show(m_4*m_b*m_2)

print("matrix braid, min 1,2")
_show(m_5*m_4*m_b*m_2)
'''

print("Result matrix")
_show(m)