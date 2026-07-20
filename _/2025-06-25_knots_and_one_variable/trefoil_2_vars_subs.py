# This is trefoil on 2 strands

from sage.all import *
from braids import knotting_max, knotting_min, braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

z_9,z_8,z_7,z_6,z_5,z_4,z_3,z_2,z_1=var("z_9,z_8,z_7,z_6,z_5,z_4,z_3,z_2,z_1")

F = SR

P = sort_triangulation({z_1,z_2,z_3})

t, matrix_max_4 = knotting_max(P, {z_1,z_2,z_3}, z_4, F=F)
t, matrix_max_5 = knotting_max(t, {z_1,z_2,z_4}, z_5, F=F)
t, matrix_max_6 = knotting_max(t, {z_1,z_2,z_5}, z_6, F=F)
t, matrix_max_7 = knotting_max(t, {z_1,z_2,z_6}, z_7, F=F)

print_triangles_pretty(t)
print(t)
t, matrix_braid = braiding(t,
                           (z_2,z_5),(z_1,z_6),(z_4,z_5),(z_6,z_7),
                           (z_2,z_4),(z_1,z_6),(z_5,z_6),(z_3,z_4),(z_2,z_6),(z_1,z_4),(z_4,z_5),(z_3,z_6), (z_2,z_4),(z_1,z_6),(z_5,z_6),(z_3,z_4),
                           (z_2,z_5),(z_1,z_4),(z_4,z_6),(z_5,z_7),
                           F=F)

t, matrix_min_7 = knotting_min(t, z_7, F=F)
t, matrix_min_4 = knotting_min(t, z_4, F=F)
t, matrix_min_5 = knotting_min(t, z_5, F=F)
t, matrix_min_6 = knotting_min(t, z_6, F=F)

m = matrix_min_6 * matrix_min_5 * matrix_min_4 * matrix_min_7 \
  * matrix_braid \
  * matrix_max_7 * matrix_max_6 * matrix_max_5 * matrix_max_4

assert P == t

print("Result matrix")
show(m.simplify_full())


t = var("t")

c_1 = z_1 - t*I
c_2 = z_2 - t*I
c_3 = z_3 - t*I
c_4 = z_4 - t*I
c_5 = z_5 - t*I
c_6 = z_6 - t*I
c_7 = z_7 - t*I
c_8 = z_8 - t*I
c_9 = z_9 - t*I

mc = m.subs({z_1: c_1, z_2: c_2, z_3: c_3, z_4: c_4, z_5: c_5, z_6: c_6, z_7: c_7, z_8: c_8, z_9: c_9})
show(mc.simplify_full())
