# This is trefoil on 2 strands

from sage.all import *
from braids import braiding
from braids.knotting import knotting_min
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

def _show(*args):
  show(latex(*args))
  # show(*args)

a_1,a_2,a_3 = var("a_1,a_2,a_3")
b_1,b_2,b_3 = var("b_1,b_2,b_3")
c_1,c_2,c_3 = var("c_1,c_2,c_3")
d_1,d_2,d_3 = var("d_1,d_2,d_3")

z_1,z_2,z_3,z_4,z_5,z_6,z_11,z_14 = var("z_1 z_2 z_3 z_4 z_5 z_6 z_11 z_14")
#z_1,z_2,z_3,z_4,z_5,z_6 = 1,2,3,4,5,6

#F = QQ
F = SR

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)
assume(z_5 < z_6)
assume(z_6 < z_11)
assume(z_11 < z_14)


##############
# Triangle 123
##############
t_0 = sort_triangulation({z_1,z_2,z_6},{z_1,z_3,z_4},{z_1,z_4,z_5},{z_1,z_5,z_6}, {z_2,z_3,z_4},{z_2,z_4,z_6}, {z_4,z_5,z_6})

t_1, m = knotting_min(t_0, z_5, z_6, F=F)#, vars=(a_1,a_2,a_3))

print("Result matrix left crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_1)
_show(m)
print("")

