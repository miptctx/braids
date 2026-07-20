# This is trefoil on 2 strands

from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation

# z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5")
z_1,z_2,z_3,z_4,z_5 = 1,2,3,4,5

F = QQ
# F = SR

t_0 = sort_triangulation({z_1,z_2,z_5},{z_1,z_3,z_4},{z_1,z_4,z_5},{z_2,z_3,z_4},{z_2,z_4,z_5})

t_1, m = braiding(t_0, (z_2,z_4),(z_1,z_5),(z_3,z_4),(z_2,z_5),(z_1,z_4),(z_3,z_5), F=F)


def _show(*args):
  # show(latex(*args))
  show(*args)


print("Result matrix")
_show(m)

print("Det:", m.det())
print("Trace:", m.trace())
print("Charpoly:", m.charpoly().factor())

print("")
m = m*m
print("Result matrix m^2")
_show(m)

print("Det:", m.det())
print("Trace:", m.trace())
print("Charpoly:", m.charpoly().factor())
