from sage.all import *
from braids import knotting_max, knotting_min
from braids.utils import sort_triangulation


PR = PolynomialRing(QQ, 'z_5,z_4,z_3,z_2,z_1')
PR.inject_variables()

F = PR.fraction_field()

P = sort_triangulation({z_1,z_2,z_3})

t, matrix_max = knotting_max(P, {z_1,z_2,z_3}, z_4, F=F)

t, matrix_min = knotting_min(t, z_4, F=F)

assert P == t

matrix_res = matrix_min*matrix_max

show(matrix_res)
