from sage.all import *
from braids import knotting_max, knotting_min, braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

q,z_9,z_8,z_7,z_6,z_5,z_4,z_3,z_2,z_1 = var('q,z_9,z_8,z_7,z_6,z_5,z_4,z_3,z_2,z_1')

F = SR

P = sort_triangulation({z_1,z_2,z_3})

p_1 = e**(q)

t, matrix_max_4 = knotting_max(P, {z_1,z_2,z_3}, z_4, F=F, param=p_1)
t, matrix_max_5 = knotting_max(t, {z_1,z_2,z_4}, z_5, F=F, param=p_1)
t, matrix_max_6 = knotting_max(t, {z_1,z_2,z_5}, z_6, F=F, param=p_1)
t, matrix_max_7 = knotting_max(t, {z_1,z_2,z_6}, z_7, F=F, param=p_1)

print_triangles_pretty(t)
print(t)
t, matrix_braid = braiding(t, (z_2,z_6),(z_1,z_5),(z_4,z_5),(z_2,z_7),(z_5,z_6), (z_2,z_7),(z_1,z_6),(z_4,z_6),(z_5,z_7), F=F)

p_2 = e**(-q)

t, matrix_min_5 = knotting_min(t, z_5, F=F, param=p_2)
t, matrix_min_6 = knotting_min(t, z_6, F=F, param=p_2)
t, matrix_min_7 = knotting_min(t, z_7, F=F, param=p_2)
t, matrix_min_4 = knotting_min(t, z_4, F=F, param=p_2)

m = matrix_min_4 * matrix_min_7 * matrix_min_6 * matrix_min_5 \
  * matrix_braid \
  * matrix_max_7 * matrix_max_6 * matrix_max_5 * matrix_max_4

assert P == t

print("Result matrix")
show(m)
