# The file contains calculation for the trivial loop with deformated second min matrix

from sage.all import *
from braids import braiding
from braids import knotting_max, knotting_min
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

def _show(*args):
  # show(latex(*args))
  show(*args)


# var('A')

# F = QQ

PR = PolynomialRing(QQ, 'A')
PR.inject_variables()

F = PR.fraction_field()

# Deformation
d = -A**2 - A**(-2)
min_vars = [d, d, d]
# min_vars = [1, 1, 1]

z_1 = 1/1
z_2 = 2/1
z_3 = 3/1
z_4 = 4/1
z_5 = 5/1
z_6 = 6/1
z_7 = 7/1

T = sort_triangulation({z_1,z_2,z_3})

t, m_1 = knotting_max(T, {z_1,z_2,z_3}, z_4, F=F)
t, m_2 = knotting_max(t, {z_1,z_2,z_4}, z_5, F=F)
t, m_3 = knotting_max(t, {z_1,z_2,z_5}, z_6, F=F)
t, m_4 = knotting_max(t, {z_1,z_2,z_6}, z_7, F=F)

t, m_b = braiding(t,
                  (z_2,z_5),(z_1,z_6),(z_4,z_5),(z_6,z_7),
                  (z_2,z_4),(z_1,z_6),(z_5,z_6),(z_3,z_4),(z_2,z_6),(z_1,z_4),(z_4,z_5),(z_3,z_6), (z_2,z_4),(z_1,z_6),(z_5,z_6),(z_3,z_4),
                  (z_2,z_5),(z_1,z_4),(z_4,z_6),(z_5,z_7),
                  F=F)

t, m_5 = knotting_min(t, z_7, F=F)
t, m_6 = knotting_min(t, z_4, vars=min_vars, F=F)
t, m_7 = knotting_min(t, z_5, F=F)
t, m_8 = knotting_min(t, z_6, vars=min_vars, F=F)

m = m_8 * m_7 * m_6 * m_5 * m_b * m_4 * m_3 * m_2 * m_1

assert T == t

bracket = m[0][0]

print("d:", d)
print("trefoil bracket:", bracket)
print("trefoil bracket A=1:", bracket.substitute({A: 1}))
