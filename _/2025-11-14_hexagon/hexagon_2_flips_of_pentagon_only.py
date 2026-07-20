from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation


PR = PolynomialRing(QQ, 'z_9,z_8,z_7,z_6,z_5,z_4,z_3,z_2,z_1')
PR.inject_variables()

# print(z_1 < z_2)

F = PR.fraction_field()

P = sort_triangulation(
  {z_1,z_2,z_4}, {z_1,z_3,z_6}, {z_1,z_4,z_5}, {z_1,z_5,z_6},
  {z_2,z_3,z_8}, {z_2,z_4,z_9}, {z_2,z_8,z_9},
  {z_3,z_6,z_7}, {z_3,z_7,z_8},
  {z_4,z_5,z_9}, {z_5,z_6,z_7}, {z_5,z_7,z_8}, {z_5,z_8,z_9})

t, matrix = braiding(P, {z_5,z_7},{z_5,z_8},{z_5,z_9},{z_6,z_8},{z_6,z_9},
                        {z_4,z_6},{z_7,z_9},{z_4,z_7},{z_5,z_7},{z_4,z_8},{z_5,z_8},
                        {z_6,z_8},{z_5,z_9},{z_6,z_9},{z_7,z_9},{z_4,z_6},{z_4,z_7},{z_4,z_8}, F=F)

assert P == t

print('################')
show(t)
show(matrix)
