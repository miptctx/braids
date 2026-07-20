################################################################
from sage.all import *
from braids import braiding
from braids.knotting import knotting_max, knotting_min
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty


#var('c_1,c_2,c_3,d_1,d_2,d_3')
#var('e_1,e_2,e_3,f_1,f_2,f_3')
var("A")

d = -A**2 - A**(-2)

z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5,z_6")
# z_1,z_2,z_3,z_4,z_5,z_6 = 1,2,3,4,5,6

# F = QQ
F = SR

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)
assume(z_5 < z_6)

t_0 = sort_triangulation({z_1,z_2,z_3})
print("Initial triangulation")
print_triangles_pretty(t_0)


var('c_1,c_2,e_1,e_2')
t_1, m_1 = knotting_max(t_0, {z_1,z_2,z_3}, z_4, {z_1,z_2,z_4}, z_5, vars=[c_1,c_2,0,0,0], F=F)
print("")
print("Matrix of maximum")
print_triangles_pretty(t_1)
show(m_1)

t_2, m_2 = knotting_min(t_1, z_5, z_4, vars=[e_1,e_2,0,0,0], F=F)
print("")
print("Matrix of minimum")
print_triangles_pretty(t_2)
show(m_2)

m = m_2*m_1
print("")
print("Normal result")
print(m[0][0], '=', d)


print("")
print("########################")
print("##### Deformation ######")
print("########################")

c_1 = I*A
c_2 = -I*A**(-1)
e_1 = I*A
e_2 = -I*A**(-1)

t_1, m_1 = knotting_max(t_0, {z_1,z_2,z_3}, z_4, {z_1,z_2,z_4}, z_5, vars=[c_1,c_2,0,0,0], F=F)
print("")
print("Matrix of maximum")
show(m_1)

t_2, m_2 = knotting_min(t_1, z_5, z_4, vars=[e_1,e_2,0,0,0], F=F)
print("")
print("Matrix of minimum")
show(m_2)

m = m_2*m_1
print("")
print("Deformated result")
print(m[0][0], '=', d)
print("")
print("is equal: ", bool(m[0][0] == d))

exit()



print("")
print("### Deformation ###")

m_0 = matrix([
  [c_1],
  [c_2],
  [c_3]])
m_1 = matrix([
  [1,0,0],
  [0,1,0],
  [0,0,d_1],
  [0,0,d_2],
  [0,0,d_3]
])
m_2 = matrix([
  [1,0,0,0,0],
  [0,e_1,e_2,0,e_3],
  [0,0,0,1,0]
])
m_3 = matrix([[f_1,f_2,f_3]])

m = m_3*m_2*m_1*m_0
print(m, '=', '-A^2 - A^(-2)')
print(m.simplify_full(), '=', '-A^2 - A^(-2)')
