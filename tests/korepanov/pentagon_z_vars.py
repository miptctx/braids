from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation

# z_1,z_2,z_3,z_4,z_5 = var('z_5,z_4,z_3,z_2,z_1')
z_1,z_2,z_3,z_4,z_5 = var('z_1 z_2 z_3 z_4 z_5')

# PR = PolynomialRing(CC, 'z_5,z_4,z_3,z_2,z_1')
# PR.inject_variables()

# F = PR.fraction_field()
F = SR

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)


P = sort_triangulation({z_1,z_2,z_3}, {z_1,z_3,z_4}, {z_1,z_4,z_5})

t, matrix = braiding(P, {z_1,z_4},{z_1,z_3},{z_3,z_5},{z_2,z_5},{z_2,z_4}, F=F)

assert P == t

print('################')
show(t)
show(matrix)


print('################')
show(matrix[2][2])
