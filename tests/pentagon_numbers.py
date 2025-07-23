from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty


P = sort_triangulation({1,2,3}, {1,3,4}, {1,4,5})

t, matrix = braiding(P, {1,4},{1,3},{3,5},{2,5},{2,4})

assert P == t

print('################')
print_triangles_pretty(t, justify=4)
print(matrix)
