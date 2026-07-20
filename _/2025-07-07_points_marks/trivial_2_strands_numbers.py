# This is trefoil on 2 strands

from sage.all import *
from braids import knotting_max, knotting_min, braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty


F=QQ

T = sort_triangulation({1,2,5},{1,3,4},{1,4,5},{2,3,4},{2,4,5})

t, m_12 = braiding(T, (1,4),(2,5), F=F)
t, m_3  = braiding(t, (3,4), F=F)


print_triangles_pretty(T)
print_triangles_pretty(t)

print("Last matrix")
show(m_3)
print("Inverse last matrix")
show(m_3.inverse())

print("Result matrix")
m = m_3 * m_12
show(m)
print("Trace: ", m.trace())
print("Det: ", m.det())
print("Charpoly: ", m.charpoly())
print("Charpoly factor: ", m.charpoly().factor())


m_last = matrix(QQ, [
  [1,0,0,0,0],
  [0,1,0,0,0],
  [0,0,1,0,0],
  [0,0,0,(3-4)/(3-5),-(5-4)/(3-5)],
  [0,0,0,-(2-3)/(3-5),(2-5)/(3-5)]
]).transpose()

print("Last matrix modified")
show(m_last)

print("Result matrix new")
m = m_last * m_12
show(m)
print("Trace: ", m.trace())
print("Det: ", m.det())
print("Charpoly: ", m.charpoly())
print("Charpoly factor: ", m.charpoly().factor())
