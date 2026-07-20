# This is trefoil on 2 strands

from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation, rotate_tuple

# z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5")
# z_1,z_2,z_3,z_4,z_5,z_6 = 1,2,3,4,5,6
# z_1,z_2,z_3,z_4,z_5,z_6 = 1,2,3,4,5,6
z_1,z_2,z_3,z_4,z_5,z_6 = 1,4,2,3,5,6

F = CC

t_0 = sort_triangulation({z_1,z_2,z_4},{z_1,z_3,z_6},{z_1,z_4,z_5},{z_1,z_5,z_6}, {z_2,z_3,z_6},{z_2,z_4,z_5},{z_2,z_5,z_6})

t_1, m = braiding_ext(t_0,
                      (rotate_tuple(z_1,z_4,z_5,z_6),(z_1,z_5)),
                      (rotate_tuple(z_1,z_2,z_5,z_4),(z_2,z_4)),
                      (rotate_tuple(z_2,z_6,z_4,z_5),(z_5,z_6)),

                      (rotate_tuple(z_2,z_3,z_6,z_4),(z_2,z_6)),
                      (rotate_tuple(z_1,z_5,z_4,z_6),(z_1,z_4)),
                      (rotate_tuple(z_2,z_4,z_6,z_5),(z_4,z_5)),
                      (rotate_tuple(z_1,z_6,z_4,z_3),(z_3,z_6)),
                      
                      (rotate_tuple(z_1,z_5,z_6,z_4),(z_1,z_6)),
                      (rotate_tuple(z_1,z_2,z_6,z_5),(z_2,z_5)),
                      (rotate_tuple(z_2,z_4,z_5,z_6),(z_4,z_6)),
                      
                      (rotate_tuple(z_2,z_3,z_4,z_5),(z_2,z_4)),
                      (rotate_tuple(z_1,z_6,z_5,z_4),(z_1,z_5)),
                      (rotate_tuple(z_2,z_5,z_4,z_6),(z_5,z_6)),
                      (rotate_tuple(z_1,z_4,z_5,z_3),(z_3,z_4)),
                      
                      (rotate_tuple(z_1,z_6,z_4,z_5),(z_1,z_4)),
                      (rotate_tuple(z_1,z_2,z_4,z_6),(z_2,z_6)),
                      (rotate_tuple(z_2,z_5,z_6,z_4),(z_4,z_5)),
                      
                      (rotate_tuple(z_2,z_3,z_5,z_6),(z_2,z_5)),
                      (rotate_tuple(z_1,z_4,z_6,z_5),(z_1,z_6)),
                      (rotate_tuple(z_2,z_6,z_5,z_4),(z_4,z_6)),
                      (rotate_tuple(z_1,z_5,z_6,z_3),(z_3,z_5)),
                      F=F)


def _show(*args):
  # show(latex(*args))
  show(*args)


print("Result matrix")
_show(m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))

print("Det:", m.det())
print("Trace:", m.trace())
print("Charpoly:", m.charpoly().factor())

print("")
m = m*m
print("Result matrix m^2")
_show(m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))

print("Det:", m.det())
print("Trace:", m.trace())
print("Charpoly:", m.charpoly().factor())
