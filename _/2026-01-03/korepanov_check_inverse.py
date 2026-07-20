from sage.all import *
from braids.korepanov import braiding_ext as braiding
from braids.utils import sort_triangulation, rotate_tuple
from braids.prints import print_triangles_pretty

z_1 = 1#/1
z_2 = 2#/1
z_3 = 3#/1
z_4 = 4#/1
z_5 = 5#/1
z_6 = 6#/1

t_0 = sort_triangulation(
  {z_1,z_2,z_6}, {z_1,z_3,z_4}, {z_1,z_4,z_6},
  {z_2,z_3,z_4}, {z_2,z_4,z_5}, {z_2,z_5,z_6},
  {z_4,z_5,z_6})

t_1, m_1 = braiding(t_0, (rotate_tuple(z_2,z_3,z_4,z_5),{z_2,z_4}))
m_1_inv = m_1.inverse().apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
m_1_trs = m_1.transpose().apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
m_1 = m_1.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

print_triangles_pretty(t_0)
print_triangles_pretty(t_1)

print('################')
show(m_1)
print('inverse matrix')
show(m_1_inv)
print('transpose matrix')
show(m_1_trs)
print('inverse == transpose:', m_1_inv == m_1_trs)

t_2, m_2 = braiding(t_1, (rotate_tuple(z_2,z_3,z_4,z_5),{z_3,z_5}))
m_2_inv = m_2.inverse().apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
m_2_trs = m_2.transpose().apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
m_2 = m_2.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
print('')
print_triangles_pretty(t_1)
print_triangles_pretty(t_2)

print('################')
show(m_2)
print('inverse matrix')
show(m_2_inv)
print('transpose matrix')
show(m_2_trs)
print('inverse == transpose:', m_2_inv == m_2_trs)
