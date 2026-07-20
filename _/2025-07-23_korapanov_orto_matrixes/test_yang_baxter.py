# This is trefoil on 2 strands

from sage.all import *
from braids.korepanov import braiding_ext as braiding
from braids.utils import sort_triangulation, rotate_tuple

F = CC

t_0 = sort_triangulation({1,2,6}, {1,3,4},{1,4,5},{1,5,6},{2,3,4},{2,4,5},{2,5,6})

t, s_1 = braiding(t_0,
                  (rotate_tuple(2,4,5,6),{2,5}),
                  (rotate_tuple(1,2,6,5),{1,6}),
                  (rotate_tuple(1,5,6,4),{4,5}),
                  F=F)

t, s_2 = braiding(t_0,
                  (rotate_tuple(1,6,5,4),(1,5)),
                  (rotate_tuple(2,3,4,5),(2,4)),
                  (rotate_tuple(2,5,4,6),(5,6)),
                  (rotate_tuple(1,4,5,3),(3,4)),
                  F=F)

m_l = (s_1*s_2*s_1).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
m_r = (s_2*s_1*s_2).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

print("Result matrix m_l")
show(m_l)

print("Result matrix m_r")
show(m_r)

print("Equation satisfied: ", m_l == m_r)
