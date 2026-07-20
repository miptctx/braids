# В этом файле проверяем выполнятся уравнение янга бакстера, если фиксировать базис для каждой из триангулций
# и все остальные триангуляяции отождествлять с первоначальной через изоморфизм ротэйшин систем.

from sage.all import *

from braids import braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

var('z_1 z_2 z_3 z_4 z_5 z_6')

F = SR

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)
assume(z_5 < z_6)


t_0 = sort_triangulation({z_1,z_2,z_6}, {z_1,z_3,z_4}, {z_1,z_4,z_5}, {z_1,z_5,z_6}, {z_2,z_3,z_4}, {z_2,z_4,z_5}, {z_2,z_5,z_6})


# Точка 5 вниз
t_15, m_15 = braiding(t_0, {z_1,z_5}, F=F)
show(m_15)

# Точка 5 обходит снизу т. 6.
t_t, m_t = braiding(t_15, {z_2, z_6}, {z_4, z_5}, F=F)

# Точка 6 вниз
t_16, m_16 = braiding(t_t, {z_1, z_6}, F=F)
print()
show(m_16)

# матрица m_15 в которой т. 5 и 6 поменяны местами
m_5_6 = m_15.subs({z_5: z_6, z_6: z_5})
print()
show(m_5_6)

print()
print("equal:", m_16 == m_5_6)

var_dict = {z_1:1,z_2:2,z_3:3,z_4:4,z_5:5,z_6:6}

m = m_15.subs(var_dict)
print()
show(m)
print("jordan form")
m_j1 = m.jordan_form()
show(m_j1.change_ring(CC))

m = m_16.subs(var_dict)
print()
show(m)
print("jordan form")
m_j2 = m.jordan_form()
show(m_j2.change_ring(CC))

print("are jordan forms equal:", m_j1 == m_j2)