from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation


P = sort_triangulation({1,2,3}, {1,3,4}, {1,4,5})

t, matrix = braiding(P, {1,4},{1,3},{3,5},{2,5},{2,4}, F=CC)

assert P == t

print('################')
show(t)
show(matrix.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
