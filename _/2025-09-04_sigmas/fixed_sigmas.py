# This is trefoil on 2 strands

from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation

def _show(*args):
  # show(latex(*args))
  show(*args)

# z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5")
z_1,z_2,z_3,z_4,z_5,z_6 = 1,2,3,4,5,6

F = QQ
# F = SR

t_0 = sort_triangulation({z_1,z_2,z_6},{z_1,z_3,z_4},{z_1,z_4,z_5},{z_1,z_5,z_6}, {z_2,z_3,z_4},{z_2,z_4,z_5},{z_2,z_5,z_6})

# sigma_2 depends on sigma_1
print("sigma_2 depends on sigma_1")
t_1, sig_1 = braiding(t_0, (z_2,z_5),(z_1,z_6),(z_4,z_5), F=F)
t_2, sig_2 = braiding(t_1, (z_1,z_6),(z_2,z_4),(z_5,z_6),(z_3,z_4), F=F)

lhs = sig_1*sig_2*sig_1
rhs = sig_2*sig_1*sig_2

print("Result matrix left")
_show(lhs)
print("Det:", lhs.det())
print("Trace:", lhs.trace())
print("Charpoly:", lhs.charpoly().factor())


print("")
print("Result matrix right")
_show(rhs)
print("Det:", rhs.det())
print("Trace:", rhs.trace())
print("Charpoly:", rhs.charpoly().factor())

print("")
print("Are matrices same:", lhs == rhs)


# sigma_2 depends on sigma_1
print("##################################")
print("sigma_2 does not depend on sigma_1")
t_1, sig_1 = braiding(t_0, (z_2,z_5),(z_1,z_6),(z_4,z_5), F=F)
t_2, sig_2 = braiding(t_0, (z_1,z_5),(z_2,z_4),(z_5,z_6),(z_3,z_4), F=F)

lhs = sig_1*sig_2*sig_1
rhs = sig_2*sig_1*sig_2

print("Result matrix left")
_show(lhs)
print("Det:", lhs.det())
print("Trace:", lhs.trace())
print("Charpoly:", lhs.charpoly().factor())


print("")
print("Result matrix right")
_show(rhs)
print("Det:", rhs.det())
print("Trace:", rhs.trace())
print("Charpoly:", rhs.charpoly().factor())

print("")
print("Are matrices same:", lhs == rhs)