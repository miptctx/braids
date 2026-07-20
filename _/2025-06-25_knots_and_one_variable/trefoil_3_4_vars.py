# This is trefoil on z_3 strands calculated with variables

from sage.all import *
from braids import knotting_max, knotting_min, braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty


PR = PolynomialRing(QQ, 'z_9,z_8,z_7,z_6,z_5,z_4,z_3,z_2,z_1')
PR.inject_variables()

F = PR.fraction_field()

P = sort_triangulation({z_1,z_2,z_3})

t, matrix_max_4 = knotting_max(P, {z_1,z_2,z_3}, z_4, F=F)
t, matrix_max_5 = knotting_max(t, {z_1,z_2,z_4}, z_5, F=F)
t, matrix_max_6 = knotting_max(t, {z_1,z_2,z_5}, z_6, F=F)
t, matrix_max_7 = knotting_max(t, {z_1,z_2,z_6}, z_7, F=F)
t, matrix_max_8 = knotting_max(t, {z_1,z_2,z_7}, z_8, F=F)
t, matrix_max_9 = knotting_max(t, {z_1,z_2,z_8}, z_9, F=F)

print_triangles_pretty(t)
print(t)
t, matrix_braid = braiding(t,
                           (z_2,z_7),(z_1,z_8),(z_6,z_7),(z_8,z_9),
                           (z_2,z_5),(z_1,z_6),(z_1,z_8),(z_4,z_5),(z_5,z_6),(z_7,z_8),
                           (z_1,z_8),(z_2,z_6),(z_2,z_4),(z_5,z_8),(z_6,z_8),(z_3,z_4),
                           (z_2,z_4),(z_1,z_6),(z_4,z_8),(z_5,z_6),
                           (z_2,z_8),(z_1,z_6),(z_4,z_6),(z_3,z_8),
                           (z_2,z_5),(z_1,z_4),(z_2,z_7),(z_4,z_8),(z_4,z_5),(z_7,z_9),
                           (z_2,z_5),(z_1,z_8),(z_6,z_8),(z_5,z_7),
                           F=F)

t, matrix_min_9 = knotting_min(t, z_9, F=F)
t, matrix_min_4 = knotting_min(t, z_4, F=F)
t, matrix_min_7 = knotting_min(t, z_7, F=F)
t, matrix_min_8 = knotting_min(t, z_8, F=F)
t, matrix_min_5 = knotting_min(t, z_5, F=F)
t, matrix_min_6 = knotting_min(t, z_6, F=F)

m = matrix_min_6 * matrix_min_5 * matrix_min_8 * matrix_min_7 * matrix_min_4 * matrix_min_9 \
  * matrix_braid \
  * matrix_max_9 * matrix_max_8 * matrix_max_7 * matrix_max_6 * matrix_max_5 * matrix_max_4

assert P == t

print("Result matrix")
show(m)
