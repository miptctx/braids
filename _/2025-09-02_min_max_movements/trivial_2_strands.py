# This is trefoil on 2 strands

from sage.all import *
from braids import braiding
from braids.knotting import knotting_max, knotting_min
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

def _show(*args):
  # show(latex(*args))
  show(*args)

# z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5,z_6")
z_1,z_2,z_3,z_4,z_5,z_6 = 1,2,3,4,5,6

F = QQ
# F = SR

#assume(z_1 < z_2)
#assume(z_2 < z_3)
#assume(z_3 < z_4)
#assume(z_4 < z_5)
#assume(z_5 < z_6)

t_0 = sort_triangulation({z_1,z_2,z_3})

print('######### Trivial with 1/3 twist ##########')
t_1, m_1 = knotting_max(t_0, {z_1,z_2,z_3}, z_4, {z_1,z_3,z_4}, z_5, F=F)
t_2, m_2 = braiding(t_1, (1,4),(3,5), F=F)
t_3, m_3 = knotting_min(t_2, z_5, z_4, F=F)

m = m_3*m_2*m_1

_show(m)
print("Det:", m.det())
print("Trace:", m.trace())
print("Charpoly:", m.charpoly())
print("")

print('######### Trivial with 2/3 twist ##########')
t_1, m_1 = knotting_max(t_0, {z_1,z_2,z_3}, z_4, {z_1,z_3,z_4}, z_5, F=F)
t_2, m_2 = braiding(t_1, (1,4),(3,5),(2,4),(1,5), F=F)
t_3, m_3 = knotting_min(t_2, z_5, z_4, F=F)

m = m_3*m_2*m_1

_show(m)
print("Det:", m.det())
print("Trace:", m.trace())
print("Charpoly:", m.charpoly())
print("")

print('######### Trivial with 2 twists ##########')
t_1, m_1 = knotting_max(t_0, {z_1,z_2,z_3}, z_4, {z_1,z_3,z_4}, z_5, F=F)
t_2, m_2 = braiding(t_1, (1,4),(3,5),(2,4),(1,5),(3,4),(2,5), F=F)
t_3, m_3 = knotting_min(t_2, z_5, z_4, F=F)

m = m_3*m_2*m_1

_show(m)
print("Det:", m.det())
print("Trace:", m.trace())
print("Charpoly:", m.charpoly())
