# This is trefoil on 3 strands

from sage.all import *
from braids import knotting_max, knotting_min, braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

F = QQ

T = sort_triangulation({1,2,4},{1,3,4},{2,3,4})

#### First movement ####

t_1, m_1 = knotting_max(T, {2,3,4}, 5, F=F)

t_2, m_2 = knotting_max(t_1, {3,4,5}, 6, F=F)

t_3, m_3 = braiding(t_2, {2,4},{4,5},{3,6},{1,5},{1,4}, F=F)

t_4, m_4 = knotting_min(t_3, 4, F=F)

t_5, m_5 = knotting_min(t_4, 5, F=F)

m_1_5 = m_5 * m_4 * m_3 * m_2 * m_1

#### Second movement ####

# assert T == t_5

t_6, m_6 = knotting_max(t_5, {2,3,6}, 5)

t_7, m_7 = knotting_max(t_6, {3,5,6}, 4)

t_8, m_8 = braiding(t_7, {3,6},{4,5},{2,6},{1,6},{1,5})

t_9, m_9 = knotting_min(t_8, 6)

t_10, m_10 = knotting_min(t_9, 5)

print("Result matrix of one move")
print(m_1_5)
print('Trace of first move:', m_1_5.trace())
print('Det of first moves:', m_1_5.det())

m_1_5_opposite = m_10 * m_9 * m_8 * m_7 * m_6
print("Result matrix of opposite move")
print(m_1_5_opposite)
print('Trace of first move:', m_1_5_opposite.trace())
print('Det of first moves:', m_1_5_opposite.det())

m_1_10 = m_1_5_opposite * m_1_5
print("Result matrix of two moves")
print(m_1_10)
print('Trace of first move:', m_1_10.trace())
print('Det of first moves:', m_1_10.det())

m_1_20 = m_1_10 * m_1_10
print("Result matrix of 4 moves")
print(m_1_20)
print('Trace of first move:', m_1_20.trace())
print('Det of first moves:', m_1_20.det())

m_1_30 = m_1_10 * m_1_10 * m_1_10
print("Result matrix of 6 moves")
print(m_1_30)
print('Trace of first move:', m_1_30.trace())
print('Det of first moves:', m_1_30.det())

m_1_40 = m_1_10 * m_1_10 * m_1_10 * m_1_10
print("Result matrix of 8 moves")
print(m_1_40)
print('Trace of first move:', m_1_40.trace())
print('Det of first moves:', m_1_40.det())
