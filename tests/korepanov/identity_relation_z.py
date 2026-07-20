from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation

z_1 = 4
z_2 = 5
z_3 = 3
z_4 = 1

'''
z_1 = 1
z_2 = 4
z_3 = 5
z_4 = 3
'''

P = sort_triangulation({z_1,z_2,z_3}, {z_1,z_3,z_4})

t_1, m_1 = braiding(P, (z_1,z_3),(z_2,z_4))

m_1 = m_1.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
print("Result matrix m_1")
show(m_1)
