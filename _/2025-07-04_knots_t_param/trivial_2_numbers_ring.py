from sage.all import *
from braids import knotting_max, knotting_min, braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

PR = PolynomialRing(QQ, 'q')
PR.inject_variables()

F = PR.fraction_field()

P = sort_triangulation({1,2,3})

t, matrix_max_4 = knotting_max(P, {1,2,3}, 4, F=F, param=q)
t, matrix_max_5 = knotting_max(t, {1,2,4}, 5, F=F, param=q)
t, matrix_max_6 = knotting_max(t, {1,2,5}, 6, F=F, param=q)
t, matrix_max_7 = knotting_max(t, {1,2,6}, 7, F=F, param=q)

print_triangles_pretty(t)
print(t)
t, matrix_braid = braiding(t, (2,5),(1,6),(4,5),(1,7),(5,6), (2,7),(1,6),(4,6),(5,7), F=F)

t, matrix_min_5 = knotting_min(t, 5, F=F, param=1/q)
t, matrix_min_6 = knotting_min(t, 6, F=F, param=1/q)
t, matrix_min_7 = knotting_min(t, 7, F=F, param=1/q)
t, matrix_min_4 = knotting_min(t, 4, F=F, param=1/q)

m = matrix_min_4 * matrix_min_7 * matrix_min_6 * matrix_min_5 \
  * matrix_braid \
  * matrix_max_7 * matrix_max_6 * matrix_max_5 * matrix_max_4

assert P == t

print("Result matrix")
show(m)
