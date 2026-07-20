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

# Точка 4 вверх
t_24, m_24 = braiding(t_0, {z_2,z_4}, F=F)
# Точка 4 вниз
t_14, m_14 = braiding(t_0, {z_1,z_4}, F=F)

# Точка 5 вверх
t_25, m_25 = braiding(t_0, {z_2,z_5}, F=F)
# Точка 5 вниз
t_15, m_15 = braiding(t_0, {z_1,z_5}, F=F)

# Точка 4 вверх влево
t_24_15, m_24_15 = braiding(t_24, {z_1,z_5}, F=F)

# Точка 5 вверх вправо
t_25_14, m_25_14 = braiding(t_25, {z_1,z_4}, F=F)

# t_24_15 ~ t_25_14

# Точка 5 вниз влево
t_15_26, m_15_26 = braiding(t_15, {z_2,z_6}, F=F)

# t_15_26 ~ t_25

# Точка 4 вниз влево
t_14_25, m_14_25 = braiding(t_14, {z_2,z_5}, F=F)

# Точка 5 вниз вправо
t_15_24, m_15_24 = braiding(t_15, {z_2,z_4}, F=F)

# s_i*s_{i+1}*s_i
print("s_1")
print_triangles_pretty(t_0)
print_triangles_pretty(t_15)
print_triangles_pretty(t_15_26)
print_triangles_pretty(t_25)
print_triangles_pretty(t_0)

#show(m_25)
#print("")
#show(m_25.inverse().simplify_full())

# exit()

s_1 = m_25.inverse()*m_15_26*m_15

print("")
print("s_2")
print_triangles_pretty(t_0)
print_triangles_pretty(t_14)
print_triangles_pretty(t_14_25)
print_triangles_pretty(t_15_24)
print_triangles_pretty(t_15)
print_triangles_pretty(t_0)
s_2 = m_15.inverse()*m_15_24.inverse()*m_14_25*m_14

m_l = s_1*s_2*s_1
m_r = s_2*s_1*s_2

m_l = m_l.subs({z_1: 1/1, z_2: 2/1, z_3: 3/1, z_4: 4/1, z_5: 5/1, z_6: 6/1})
m_r = m_r.subs({z_1: 1/1, z_2: 2/1, z_3: 3/1, z_4: 4/1, z_5: 5/1, z_6: 6/1})

print("")
print("m_l")
show(m_l)

print("")
print("m_r")
show(m_r)

print("equal: ", m_l == m_r)


print("")
print("m_l trace", m_l.trace())
print("m_r trace", m_r.trace())
