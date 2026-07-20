from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty


z_1, z_2, z_3, z_4, z_5 = 1, 5, 2, 3, 4

print(z_1, z_2, z_3, z_4, z_5)
print("----------------")

P = sort_triangulation({z_1,z_2,z_4}, {z_1,z_4,z_5}, {z_2,z_3,z_4})

t, m = braiding(P, {z_2,z_4},{z_1,z_4},{z_1,z_3},{z_3,z_5},{z_2,z_5})
print_triangles_pretty(P)
print_triangles_pretty(t)
assert P == t
m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
show(m)
