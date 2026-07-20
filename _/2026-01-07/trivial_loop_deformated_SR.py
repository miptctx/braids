# The file contains calculation for the trivial loop with deformated second min matrix

from sage.all import *
from braids import braiding
from braids import knotting_max, knotting_min
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

def _show(*args):
  # show(latex(*args))
  show(*args)


z_1,z_2,z_3,z_4,z_5,z_6,z_7 = var("z_1 z_2 z_3 z_4 z_5 z_6 z_7")
var('A')

F = SR

# Deformation
d = -A**2 - A**(-2)
min_vars = [d, d, d]

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)
assume(z_5 < z_6)
assume(z_6 < z_7)

T = sort_triangulation({z_1,z_2,z_3})

t, m_1 = knotting_max(T, {z_1,z_2,z_3}, z_4, F=F)
t, m_2 = knotting_max(t, {z_1,z_2,z_4}, z_5, F=F)

print_triangles_pretty(t)
#t, m_b = braiding(t,
#                  (z_2,z_5),(z_1,z_6),(z_4,z_5),(z_6,z_7),
#                  (z_2,z_4),(z_1,z_6),(z_5,z_6),(z_3,z_4),(z_2,z_6),(z_1,z_4),(z_4,z_5),(z_3,z_6), (z_2,z_4),(z_1,z_6),(z_5,z_6),(z_3,z_4),
#                  (z_2,z_5),(z_1,z_4),(z_4,z_6),(z_5,z_7),
#                  F=F)

t, m_4 = knotting_min(t, z_5, F=F)
t, m_5 = knotting_min(t, z_4, vars=min_vars, F=F)
print_triangles_pretty(t)

# m = m_5 * m_4 * m_b * m_2 * m_1
m = m_5 * m_4 * m_2 * m_1

assert T == t

bracket = m[0].simplify_full()

print("bracket:", bracket)
print("d:", d)
