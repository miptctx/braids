# This is trefoil on 3 strands

from sage.all import *
from braids import knotting_max, knotting_min, braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

F = QQ

P = sort_triangulation({1,2,3})

t, matrix_max_4 = knotting_max(P, {1,2,3}, 4, F=F)
t, matrix_max_5 = knotting_max(t, {1,2,4}, 5, F=F)
t, matrix_max_6 = knotting_max(t, {1,2,5}, 6, F=F)
t, matrix_max_7 = knotting_max(t, {1,2,6}, 7, F=F)
t, matrix_max_8 = knotting_max(t, {1,2,7}, 8, F=F)
t, matrix_max_9 = knotting_max(t, {1,2,8}, 9, F=F)

print_triangles_pretty(t)
print(t)
t, matrix_braid = braiding(t,
                           (2,7),(1,8),(6,7),(8,9),
                           (2,5),(1,6),(1,8),(4,5),(5,6),(7,8),
                           (1,8),(2,6),(2,4),(5,8),(6,8),(3,4),
                           (2,4),(1,6),(4,8),(5,6),
                           (2,8),(1,6),(4,6),(3,8),
                           (2,5),(1,4),(2,7),(4,8),(4,5),(7,9),
                           (2,5),(1,8),(6,8),(5,7),
                           F=F)

t, matrix_min_9 = knotting_min(t, 9, F=F)
t, matrix_min_4 = knotting_min(t, 4, F=F)
t, matrix_min_7 = knotting_min(t, 7, F=F)
t, matrix_min_8 = knotting_min(t, 8, F=F)
t, matrix_min_5 = knotting_min(t, 5, F=F)
t, matrix_min_6 = knotting_min(t, 6, F=F)

m = matrix_min_6 * matrix_min_5 * matrix_min_8 * matrix_min_7 * matrix_min_4 * matrix_min_9 \
  * matrix_braid \
  * matrix_max_9 * matrix_max_8 * matrix_max_7 * matrix_max_6 * matrix_max_5 * matrix_max_4

assert P == t

print("-------------")
print("Result matrix")
show(m)
print("-------------")

matrix_min = matrix_min_6 * matrix_min_5 * matrix_min_8 * matrix_min_7 * matrix_min_4 * matrix_min_9
matrix_max = matrix_max_9 * matrix_max_8 * matrix_max_7 * matrix_max_6 * matrix_max_5 * matrix_max_4
print("Matrix mins")
show(matrix_min)
print("Matrix braid")
show(matrix_braid)
print("Matrix max")
show(matrix_max)

print("Matrices braids * max")
show(matrix_braid * matrix_max)

print("Matrices min * braids * max")
show(matrix_min * matrix_braid * matrix_max)
