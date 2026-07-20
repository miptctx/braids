# This is trefoil on 2 strands

from sage.all import *
from braids import braiding, knotting_max, knotting_min
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

def _show(*args):
  # show(latex(*args))
  show(*args)

z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5,z_6")
# z_1,z_2,z_3,z_4,z_5,z_6 = 1,2,3,4,5,6

# F = QQ
F = SR

t_0 = sort_triangulation({z_1,z_2,z_4},{z_1,z_3,z_4},{z_2,z_3,z_4})

t_1, m_1 = knotting_max(t_0, {z_1,z_3,z_4}, z_6, F=F)
t_2, m_2 = knotting_max(t_1, {z_1,z_4,z_6}, z_5, F=F)

t_3, m_3 = braiding(t_2, (z_4,z_6),(z_1,z_5),(z_1,z_4),   F=F)

t_4, m_4 = knotting_min(t_3, z_5, F=F)
t_5, m_5 = knotting_min(t_4, z_4, F=F)

m = m_5*m_4*m_3*m_2*m_1

print("Result matrix left crossing")
# _show(m.simplify_full())
_show(m)
print("")

print("m[0][2]")
show(m[2][0])

print("")
print_triangles_pretty(t_0)
print_triangles_pretty(t_5)
