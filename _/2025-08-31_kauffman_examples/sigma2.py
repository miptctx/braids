# This is trefoil on 2 strands

from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation

# z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5,z_6")
z_1,z_2,z_3,z_4,z_5,z_6 = 1,2,3,4,5,6

F = QQ
# F = SR

t_0 = sort_triangulation({z_1,z_2,z_4},{z_1,z_3,z_6},{z_1,z_4,z_5},{z_1,z_5,z_6}, {z_2,z_3,z_6},{z_2,z_4,z_5},{z_2,z_5,z_6})

t_1, A_1 = braiding(t_0, (z_2,z_5), F=F)
t_2, A_2 = braiding(t_1, (z_1,z_4), F=F)
t_3, A_3 = braiding(t_2, (z_5,z_6), F=F)
A = A_3*A_2*A_1

t_4, B_1 = braiding(t_3, (z_2,z_4), F=F)
t_5, B_2 = braiding(t_4, (z_1,z_5), F=F)
t_6, B_3 = braiding(t_5, (z_4,z_6), F=F)
B = B_3*B_2*B_1


def _show(*args):
  # show(latex(*args))
  show(*args)


print("Result matrix A_1")
_show(A_1)
print("Result matrix A_2")
_show(A_2)
print("Result matrix A_3")
_show(A_3)
print("Result matrix A")
_show(A)

print("Result matrix B_1")
_show(B_1)
print("Result matrix B_2")
_show(B_2)
print("Result matrix B_3")
_show(B_3)
print("Result matrix B")
_show(B)

