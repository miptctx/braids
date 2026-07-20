# This is trefoil on 2 strands

from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation, rotate_tuple

z_1,z_2,z_3,z_4,z_5,z_6 = 1,2,3,4,5,6
# z_1,z_2,z_3,z_4,z_5,z_6 = 1,4,2,3,5,6

F = CC

t_0 = sort_triangulation({z_1,z_2,z_4},{z_1,z_3,z_6},{z_1,z_4,z_5},{z_1,z_5,z_6}, {z_2,z_3,z_6},{z_2,z_4,z_5},{z_2,z_5,z_6})

t_1, m_1 = braiding_ext(t_0,
                      (rotate_tuple(z_2,z_6,z_5,z_4),(z_2,z_5)),
                      (rotate_tuple(z_1,z_2,z_4,z_5),(z_1,z_4)),
                      (rotate_tuple(z_1,z_5,z_4,z_6),(z_5,z_6)),
                      (rotate_tuple(z_2,z_6,z_4,z_5),(z_2,z_4)),
                      (rotate_tuple(z_1,z_2,z_5,z_4),(z_1,z_5)),
                      (rotate_tuple(z_1,z_4,z_5,z_6),(z_4,z_6)),

                      (rotate_tuple(z_2,z_3,z_6,z_5),(z_2,z_6)),
                      (rotate_tuple(z_1,z_4,z_5,z_6),(z_1,z_5)),
                      (rotate_tuple(z_2,z_5,z_6,z_4),(z_4,z_5)),
                      (rotate_tuple(z_1,z_6,z_5,z_3),(z_3,z_6)),
                      (rotate_tuple(z_2,z_3,z_5,z_6),(z_2,z_5)),
                      (rotate_tuple(z_1,z_4,z_6,z_5),(z_1,z_6)),
                      (rotate_tuple(z_1,z_5,z_6,z_3),(z_3,z_5)),
                      (rotate_tuple(z_2,z_6,z_5,z_4),(z_4,z_6)),

                      (rotate_tuple(z_1,z_4,z_5,z_6),(z_1,z_5)),
                      (rotate_tuple(z_1,z_2,z_5,z_4),(z_2,z_4)),
                      (rotate_tuple(z_2,z_6,z_4,z_5),(z_5,z_6)),
                      (rotate_tuple(z_1,z_5,z_4,z_6),(z_1,z_4)),
                      (rotate_tuple(z_1,z_2,z_4,z_5),(z_2,z_5)),
                      (rotate_tuple(z_2,z_6,z_5,z_4),(z_4,z_6)),
                      F=F)


t_2, m_2 = braiding_ext(t_0,
                      (rotate_tuple(z_2,z_6,z_5,z_4),(z_2,z_5)),
                      (rotate_tuple(z_1,z_2,z_4,z_5),(z_1,z_4)),
                      (rotate_tuple(z_1,z_5,z_4,z_6),(z_5,z_6)),

                      (rotate_tuple(z_2,z_6,z_4,z_5),(z_2,z_4)),
                      (rotate_tuple(z_1,z_4,z_6,z_3),(z_1,z_6)),
                      (rotate_tuple(z_1,z_5,z_6,z_4),(z_4,z_5)),
                      (rotate_tuple(z_2,z_3,z_4,z_6),(z_3,z_6)),

                      (rotate_tuple(z_2,z_4,z_6,z_5),(z_2,z_6)),
                      (rotate_tuple(z_1,z_2,z_5,z_6),(z_1,z_5)),
                      (rotate_tuple(z_1,z_6,z_5,z_4),(z_4,z_6)),
                      (rotate_tuple(z_2,z_4,z_5,z_6),(z_2,z_5)),
                      (rotate_tuple(z_1,z_2,z_6,z_5),(z_1,z_6)),
                      (rotate_tuple(z_1,z_5,z_6,z_4),(z_4,z_5)),

                      (rotate_tuple(z_2,z_3,z_4,z_6),(z_2,z_4)),
                      (rotate_tuple(z_1,z_5,z_6,z_4),(z_1,z_6)),
                      (rotate_tuple(z_1,z_4,z_6,z_3),(z_3,z_4)),
                      (rotate_tuple(z_2,z_6,z_4,z_5),(z_5,z_6)),
                      (rotate_tuple(z_1,z_5,z_4,z_6),(z_1,z_4)),
                      (rotate_tuple(z_1,z_2,z_4,z_5),(z_5,z_2)),
                      (rotate_tuple(z_2,z_6,z_5,z_4),(z_4,z_6)),
                      F=F)

assert t_1 == t_2

m_1 = m_1.apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
show(m_1)
print("")
m_2 = m_2.apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
show(m_2)

print("Braids are same:", m_1 == m_2)

# print((m_1*m_1.transpose()).apply_map(lambda x: round(x.real(), 9) + round(x.imag(), 9) * I))
