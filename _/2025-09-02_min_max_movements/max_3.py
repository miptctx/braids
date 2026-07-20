# This is trefoil on 2 strands

from sage.all import *
from braids import braiding
from braids.knotting import knotting_max
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

def _show(*args):
  # show(latex(*args))
  show(*args)

a_1,a_2,a_3 = var("a_1,a_2,a_3")
b_1,b_2,b_3 = var("b_1,b_2,b_3")
c_1,c_2,c_3 = var("c_1,c_2,c_3")
d_1,d_2,d_3 = var("d_1,d_2,d_3")

#z_1,z_2,z_3,z_4,z_5,z_6,z_11,z_14 = var("z_1,z_2,z_3,z_4,z_5,z_6,z_11,z_14")
z_1,z_2,z_3,z_4,z_5,z_6 = 1,2,3,4,5,6

F = QQ
#F = SR

'''
assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)
assume(z_5 < z_6)
'''

########################
# Triangle 1,4,3
########################
t_0 = sort_triangulation({z_1,z_2,z_4},{z_1,z_3,z_4},{z_2,z_3,z_4})

t_1, m_1 = knotting_max(t_0, {z_1,z_3,z_4}, z_6, {z_1,z_4,z_6}, z_5, F=F)#, vars=(a_1,a_2,a_3))
t_l, m_2 = braiding(t_1, (z_1,z_4), F=F)

m_l = m_2*m_1

print("Result matrix left crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_l)
_show(m_l)
print("")


t_1, m_1 = knotting_max(t_0, {z_1,z_2,z_4}, z_5, {z_1,z_4,z_5}, z_6, F=F)#, vars=(c_1,c_2,c_3))
t_r, m_2 = braiding(t_1, (z_1,z_4), F=F)

#print_triangles_pretty(t_l)
#print_triangles_pretty(t_r)
#print("")

assert t_l == t_r

m_r = m_2*m_1

print("Result matrix right crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_r)
_show(m_r)
print("")


print("Matrix equal:", m_l == m_r)

quit(0)

########################
# Triangle 4,1,3
########################
print("")
print("#####################")

t_0 = sort_triangulation({z_1,z_2,z_3},{z_1,z_2,z_4},{z_1,z_3,z_4})

t_1, m_1 = knotting_max(t_0, {z_1,z_3,z_4}, z_6, F=F, vars=(a_1,a_2,a_3))
t_2, m_2 = knotting_max(t_1, {z_1,z_4,z_6}, z_5, F=F, vars=(b_1,b_2,b_3))

t_l, m_3 = braiding(t_2, (z_1,z_4), F=F)

m_l = m_3*m_2*m_1

print("Result matrix left crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_l)
_show(m_l)
print("")


t_1, m_1 = knotting_max(t_0, {z_1,z_2,z_4}, z_5, F=F, vars=(c_1,c_2,c_3))
t_2, m_2 = knotting_max(t_1, {z_1,z_4,z_5}, z_6, F=F, vars=(d_1,d_2,d_3))

t_r, m_3 = braiding(t_2, (z_1,z_4), F=F)

#print_triangles_pretty(t_l)
#print_triangles_pretty(t_r)
#print("")

assert t_l == t_r

m_r = m_3*m_2*m_1

print("Result matrix right crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_r)
_show(m_r)
print("")


########################
# Triangle 11,14,3
########################
print("")
print("#####################")

t_0 = sort_triangulation({z_14,z_2,z_3},{z_11,z_2,z_14},{z_11,z_3,z_14})

t_1, m_1 = knotting_max(t_0, {z_11,z_3,z_14}, z_6, F=F, vars=(a_1,a_2,a_3))
t_2, m_2 = knotting_max(t_1, {z_11,z_14,z_6}, z_5, F=F, vars=(b_1,b_2,b_3))

t_l, m_3 = braiding(t_2, (z_11,z_14), F=F)

m_l = m_3*m_2*m_1

print("Result matrix left crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_l)
_show(m_l)
print("")


t_1, m_1 = knotting_max(t_0, {z_11,z_2,z_14}, z_5, F=F, vars=(c_1,c_2,c_3))
t_2, m_2 = knotting_max(t_1, {z_11,z_14,z_5}, z_6, F=F, vars=(d_1,d_2,d_3))

t_r, m_3 = braiding(t_2, (z_11,z_14), F=F)

#print_triangles_pretty(t_l)
#print_triangles_pretty(t_r)
#print("")

assert t_l == t_r

m_r = m_3*m_2*m_1

print("Result matrix right crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_r)
_show(m_r)
print("")


########################
# Triangle 14,11,3
########################
print("")
print("#####################")

t_0 = sort_triangulation({z_11,z_2,z_3},{z_11,z_2,z_14},{z_11,z_3,z_14})

t_1, m_1 = knotting_max(t_0, {z_11,z_3,z_14}, z_6, F=F, vars=(a_1,a_2,a_3))
t_2, m_2 = knotting_max(t_1, {z_11,z_14,z_6}, z_5, F=F, vars=(b_1,b_2,b_3))

t_l, m_3 = braiding(t_2, (z_11,z_14), F=F)

m_l = m_3*m_2*m_1

print("Result matrix left crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_l)
_show(m_l)
print("")


t_1, m_1 = knotting_max(t_0, {z_11,z_2,z_14}, z_5, F=F, vars=(c_1,c_2,c_3))
t_2, m_2 = knotting_max(t_1, {z_11,z_14,z_5}, z_6, F=F, vars=(d_1,d_2,d_3))

t_r, m_3 = braiding(t_2, (z_11,z_14), F=F)

#print_triangles_pretty(t_l)
#print_triangles_pretty(t_r)
#print("")

assert t_l == t_r

m_r = m_3*m_2*m_1

print("Result matrix right crossing")
print_triangles_pretty(t_0)
print_triangles_pretty(t_r)
_show(m_r)
print("")

