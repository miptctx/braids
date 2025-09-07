from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation

z_1 = 5
z_2 = 4
z_3 = 2
z_4 = 3
z_5 = 1

z_1 = 1
z_2 = 2
z_3 = 5
z_4 = 3
z_5 = 4


P = sort_triangulation({z_1,z_2,z_3}, {z_1,z_3,z_4}, {z_1,z_4,z_5})

t, matrix = braiding(P, {z_1,z_4},{z_1,z_3},{z_3,z_5},{z_2,z_5},{z_2,z_4}, F=CC)

assert P == t

print('################')
show(t)
show(matrix.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
