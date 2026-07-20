# Расчет трилистника по формулам новых операторов, с одинаковыми формулами для максимумов и минимумов
# ОЖИДАНИЕ: будет распозноваться регулярная изотопия
# РЕЗУЛЬТАТ: инвариант тривиальный, обычный трилистник соответствует тривиальному узлу.

from sage.all import *
from braids import braiding
from braids.knotting import knotting_max, knotting_min
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty


def _show(*args):
  # show(latex(*args))
  show(*args)


PR = PolynomialRing(CC, 'A')
PR.inject_variables()

F = PR.fraction_field()

# Deformation
var("A")
d = -A**2 - A**(-2)
c_1 = I*A
c_2 = -I*A**(-1)
e_1 = I*A
e_2 = -I*A**(-1)
print("d:", d)

max_vars = [c_1,c_2,0,0,0]
min_vars = [e_1,e_2,0,0,0]

z_1 = 1
z_2 = 2
z_3 = 3
z_4 = 4
z_5 = 5
z_6 = 6
z_7 = 7
z_8 = 8
z_9 = 9


T = sort_triangulation({z_1,z_2,z_3})

t, m_1 = knotting_max(T, {z_1,z_2,z_3}, z_4, {z_1,z_2,z_4}, z_5, vars=max_vars, F=F)
t, m_2 = knotting_max(t, {z_1,z_2,z_5}, z_6, {z_1,z_2,z_6}, z_7, vars=max_vars, F=F)

t, m_b = braiding(t,
                  (z_2,z_5),(z_1,z_6),(z_4,z_5),(z_6,z_7),
                  (z_2,z_4),(z_1,z_6),(z_5,z_6),(z_3,z_4),(z_2,z_6),(z_1,z_4),(z_4,z_5),(z_3,z_6), (z_2,z_4),(z_1,z_6),(z_5,z_6),(z_3,z_4),
                  (z_2,z_5),(z_1,z_4),(z_4,z_6),(z_5,z_7),
                  F=F)

t, m_3 = knotting_min(t, z_7, z_4, vars=min_vars, F=F)
t, m_4 = knotting_min(t, z_5, z_6, vars=min_vars, F=F)

m = m_4 * m_3 * m_b * m_2 * m_1

assert T == t

bracket = m[0][0]

print("trefoil non regular isotopy bracket:", bracket)

#########################################################
t, m_1 = knotting_max(T, {z_1,z_2,z_3}, z_4, {z_1,z_2,z_4}, z_5, vars=max_vars, F=F)
t, m_2 = knotting_max(t, {z_1,z_2,z_5}, z_6, {z_1,z_2,z_6}, z_7, vars=max_vars, F=F)

t, m_b = braiding(t,
                  (z_2,z_5),(z_1,z_6),(z_4,z_5),(z_6,z_7),
                  (z_1,z_5),(z_2,z_7),(z_5,z_6),
                  (z_2,z_6),(z_1,z_7),(z_5,z_7),(z_4,z_6),
                  F=F)

t, m_3 = knotting_min(t, z_5, z_6, vars=min_vars, F=F)
t, m_4 = knotting_min(t, z_7, z_4, vars=min_vars, F=F)

m = m_4 * m_3 * m_b * m_2 * m_1

assert T == t

bracket = m[0][0]

print("trefoil no isotopy bracket:", bracket)
