from sage.all import *

from braids.korepanov import braiding_ext as braiding
from braids.utils import sort_triangulation, rotate_tuple

F = CC

z_1, z_2, z_3, z_4, z_5, z_6 = 1,2,3,4,5,6


t_0 = sort_triangulation({1,2,6},{1,3,4},{1,4,5},{1,5,6},{2,3,4},{2,4,5},{2,5,6})


t_1, m_1 = braiding(t_0,
                    (rotate_tuple(2,4,5,6),{2,5}),
                    (rotate_tuple(1,2,6,5),{1,6}),
                    (rotate_tuple(1,5,6,4),{4,5}),
                    F=F)

t_2, m_2 = braiding(t_1,
                    (rotate_tuple(2,4,6,5),{2,6}),
                    (rotate_tuple(1,2,5,6),{1,5}),
                    (rotate_tuple(1,6,5,4),{4,6}),
                    F=F)

assert t_2 == t_0

print("is matrices same:", m_1 == m_2)

print("----------")
print(m_1)
print("----------")
print(m_2)
