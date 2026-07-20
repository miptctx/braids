from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

var('z_1,z_2,z_3,z_4')

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)

t_0 = sort_triangulation({z_1,z_2,z_3}, {z_1,z_3,z_4})

t_1, m_1 = braiding(t_0, {z_2,z_4}, F=QQ)
