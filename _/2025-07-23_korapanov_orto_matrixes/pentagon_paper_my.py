from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation

#z_1,z_2,z_3,z_4,z_5 = 1, 2, 4, 5, 3
#z_1,z_2,z_3,z_4,z_5 = 1, 3, 4, 2, 5
z_1,z_2,z_3,z_4,z_5 = 1, 3, 5, 2, 4
# z_1,z_2,z_3,z_4,z_5 = 1, 2, 3, 4, 5
# z_1,z_2,z_3,z_4,z_5 = 3, 4, 5, 1, 2
#z_1,z_2,z_3,z_4,z_5 = 1, 4, 2, 3, 5

print(z_1, z_2, z_3, z_4, z_5)
print("----------------")

P = sort_triangulation({z_1,z_2,z_4}, {z_1,z_4,z_5}, {z_2,z_3,z_4})

t, m = braiding(P, {z_2,z_4},{z_1,z_4},{z_1,z_3},{z_3,z_5},{z_2,z_5}, F=CC, p_k_p_l=True)

assert P == t

print('################')
show(t)

m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
show(m)
