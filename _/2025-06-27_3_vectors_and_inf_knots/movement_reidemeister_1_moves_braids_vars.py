# This is trefoil on 3 strands

from sage.all import *
from braids import knotting_max, knotting_min, braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

PR = PolynomialRing(QQ, 'z_9,z_8,z_7,z_6,z_5,z_4,z_3,z_2,z_1')
PR.inject_variables()

F = PR.fraction_field()

T = sort_triangulation({z_1,z_2,z_4},{z_1,z_3,z_4},{z_2,z_3,z_4})

#### First movement ####

t_1, m_1 = knotting_max(T, {z_2,z_3,z_4}, z_5, F=F)

t_2, m_2 = knotting_max(t_1, {z_3,z_4,z_5}, z_6, F=F)

t_3, m_3 = braiding(t_2, {z_2,z_4},{z_4,z_5},{z_3,z_6},{z_1,z_5},{z_1,z_4}, F=F)

t_4, m_4 = knotting_min(t_3, z_4, F=F)

t_5, m_5 = knotting_min(t_4, z_5, F=F)

m_1_5 = m_5 * m_4 * m_3 * m_2 * m_1

print("Result matrix of one move")
print(m_1_5)
print('Trace of first move:', m_1_5.trace())
print('Poly: ', m_1_5.charpoly())
# print('Det of first moves:', m_1_5.det())

#### Second movement ####

assert T == t_5

t_6, m_6 = knotting_max(t_5, {2,3,6}, 5)

t_7, m_7 = knotting_max(t_6, {3,5,6}, 4)

t_8, m_8 = braiding(t_7, {3,6},{4,5},{2,6},{1,6},{1,5})

t_9, m_9 = knotting_min(t_8, 6)

t_10, m_10 = knotting_min(t_9, 5)

m_1_10 = m_10 * m_9 * m_8 * m_7 * m_6 * m_1_5
print("Result matrix of two moves")
print(m_1_5)
print('Trace of first move:', m_1_5.trace())
print('Det of first moves:', m_1_5.det())

m_1_20 = m_1_10 * m_1_10
print("Result matrix of 4 moves")
print(m_1_5)
print('Trace of first move:', m_1_5.trace())
print('Det of first moves:', m_1_5.det())

m_1_30 = m_1_10 * m_1_10 * m_1_10
print("Result matrix of 6 moves")
print(m_1_5)
print('Trace of first move:', m_1_5.trace())
print('Det of first moves:', m_1_5.det())

m_1_40 = m_1_10 * m_1_10 * m_1_10 * m_1_10
print("Result matrix of 8 moves")
print(m_1_5)
print('Trace of first move:', m_1_5.trace())
print('Det of first moves:', m_1_5.det())
