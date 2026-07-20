from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation

F = CC

P = sort_triangulation({1,2,4},{1,3,6},{1,4,5},{1,5,6}, {2,3,6},{2,4,5},{2,5,6})

t_1, s_1 = braiding_ext(P,
                        ((2,6,5,4),(2,5)),
                        ((1,2,4,5),(1,4)),
                        ((1,5,4,6),(5,6)),
                        F=F)

t_2, s_2 = braiding_ext(t_1,
                        ((2,6,4,5),(2,4)),
                        ((1,2,5,4),(1,5)),
                        ((1,4,5,6),(4,6)),
                        F=F)

assert P == t_2

s_1 = s_1.apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
s_2 = s_2.apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)

print("sigma 1.1")
show(s_1)
print("sigma 1.2")
show(s_2)

print("Sigmas equal:", s_1 == s_2)
