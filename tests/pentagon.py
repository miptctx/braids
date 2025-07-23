from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation


PR = PolynomialRing(QQ, 'z_5,z_4,z_3,z_2,z_1')
PR.inject_variables()

# print(z_1 < z_2)

F = PR.fraction_field()

P = sort_triangulation({z_1,z_2,z_3}, {z_1,z_3,z_4}, {z_1,z_4,z_5})

t, matrix = braiding(P, {z_1,z_4},{z_1,z_3},{z_3,z_5},{z_2,z_5},{z_2,z_4}, F=F)

assert P == t

print('################')
show(t)
show(matrix)
