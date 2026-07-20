# This is trefoil on 2 strands

from sage.all import *
from braids import braiding, knotting_min
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

def _show(*args):
  # show(latex(*args))
  show(*args)

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
t_0 = sort_triangulation({z_1,z_2,z_5},{z_1,z_3,z_6},{z_1,z_5,z_6}, {z_2,z_3,z_4},{z_2,z_4,z_5}, {z_3,z_4,z_6},{z_4,z_5,z_6})

t_1, m_1 = braiding(t_0, (z_3,z_6), F=F)

t_2, m_2 = knotting_min(t_1, z_6, F=F, vars=(a_1,a_2,a_3))
t_l, m_3 = knotting_min(t_2, z_5, F=F, vars=(b_1,b_2,b_3))

m_l = m_3*m_2*m_1

print("Result matrix left crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_l)
_show(m_l)
print("")


t_1, m_1 = braiding(t_0, (z_2,z_5), F=F)

t_2, m_2 = knotting_min(t_1, z_5, F=F, vars=(c_1,c_2,c_3))
t_r, m_3 = knotting_min(t_2, z_6, F=F, vars=(d_1,d_2,d_3))

assert t_l == t_r

m_r = m_3*m_2*m_1

print("Result matrix right crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_r)
_show(m_r)
print("")

print("Matrix equal:", m_l == m_r)


##############
# Triangle 234
##############
t_0 = sort_triangulation({z_1,z_2,z_3},{z_1,z_2,z_5},{z_1,z_3,z_6},{z_1,z_5,z_6}, {z_2,z_4,z_5},{z_3,z_4,z_6},{z_4,z_5,z_6})

t_1, m_1 = braiding(t_0, (z_3,z_6), F=F)

t_2, m_2 = knotting_min(t_1, z_6, F=F, vars=(a_1,a_2,a_3))
t_l, m_3 = knotting_min(t_2, z_5, F=F, vars=(b_1,b_2,b_3))

m_l = m_3*m_2*m_1

print("Result matrix left crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_l)
_show(m_l)
print("")


t_1, m_1 = braiding(t_0, (z_2,z_5), F=F)

t_2, m_2 = knotting_min(t_1, z_5, F=F, vars=(c_1,c_2,c_3))
t_r, m_3 = knotting_min(t_2, z_6, F=F, vars=(d_1,d_2,d_3))

assert t_l == t_r

m_r = m_3*m_2*m_1

print("Result matrix right crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_r)
_show(m_r)
print("")

print("Matrix equal:", m_l == m_r)


###############
# Triangle 1123
###############
t_0 = sort_triangulation({z_11,z_2,z_5},{z_11,z_3,z_6},{z_11,z_5,z_6}, {z_2,z_3,z_14},{z_2,z_14,z_5}, {z_3,z_14,z_6},{z_14,z_5,z_6})

t_1, m_1 = braiding(t_0, (z_3,z_6), F=F)

t_2, m_2 = knotting_min(t_1, z_6, F=F, vars=(a_1,a_2,a_3))
t_l, m_3 = knotting_min(t_2, z_5, F=F, vars=(b_1,b_2,b_3))

m_l = m_3*m_2*m_1

print("Result matrix left crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_l)
_show(m_l)
print("")


t_1, m_1 = braiding(t_0, (z_2,z_5), F=F)

t_2, m_2 = knotting_min(t_1, z_5, F=F, vars=(c_1,c_2,c_3))
t_r, m_3 = knotting_min(t_2, z_6, F=F, vars=(d_1,d_2,d_3))

assert t_l == t_r

m_r = m_3*m_2*m_1

print("Result matrix right crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_r)
_show(m_r)
print("")

print("Matrix equal:", m_l == m_r)


##############
# Triangle 2314
##############
t_0 = sort_triangulation({z_11,z_2,z_3},{z_11,z_2,z_5},{z_11,z_3,z_6},{z_11,z_5,z_6}, {z_2,z_14,z_5},{z_3,z_14,z_6},{z_14,z_5,z_6})

t_1, m_1 = braiding(t_0, (z_3,z_6), F=F)

t_2, m_2 = knotting_min(t_1, z_6, F=F, vars=(a_1,a_2,a_3))
t_l, m_3 = knotting_min(t_2, z_5, F=F, vars=(b_1,b_2,b_3))

m_l = m_3*m_2*m_1

print("Result matrix left crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_l)
_show(m_l)
print("")


t_1, m_1 = braiding(t_0, (z_2,z_5), F=F)

t_2, m_2 = knotting_min(t_1, z_5, F=F, vars=(c_1,c_2,c_3))
t_r, m_3 = knotting_min(t_2, z_6, F=F, vars=(d_1,d_2,d_3))

assert t_l == t_r

m_r = m_3*m_2*m_1

print("Result matrix right crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_r)
_show(m_r)
print("")

print("Matrix equal:", m_l == m_r)
