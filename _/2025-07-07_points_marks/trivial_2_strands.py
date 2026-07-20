# This is trefoil on 2 strands

from sage.all import *
from braids import knotting_max, knotting_min, braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty


z_5,z_4,z_3,z_2,z_1 = var("z_5,z_4,z_3,z_2,z_1")

F = SR

T = sort_triangulation({z_1,z_2,z_5},{z_1,z_3,z_4},{z_1,z_4,z_5},{z_2,z_3,z_4},{z_2,z_4,z_5})

t, m = braiding(T, (z_1,z_4),(z_2,z_5),(z_3,z_4), F=F)

print("Result matrix")
# print_triangles_pretty(T)
# print_triangles_pretty(t)
print(T)
print(t)
show(m)


z_1 = 1/1
z_2 = 2/1
z_3 = 3/1
z_4 = 4/1
z_5 = 5/1

# Original matrix
m = matrix(QQ, [
  [                           (z_2 - z_4)/(z_2 - z_5),                                                  0,                                                  0,                                                  0,                           -(z_1 - z_2)/(z_2 - z_5)],
  [                                                 0,                            (z_1 - z_5)/(z_1 - z_4),                            (z_1 - z_3)/(z_1 - z_4),                                                  0,                                                  0],
  [                           (z_4 - z_5)/(z_2 - z_5),                                                  0,                                                  0,                                                  0,                            (z_1 - z_5)/(z_2 - z_5)],
  [                                                 0,  (z_2 - z_3)*(z_4 - z_5)/((z_1 - z_4)*(z_3 - z_4)),                           -(z_2 - z_3)/(z_1 - z_4),                            (z_3 - z_5)/(z_3 - z_4),                                                  0],
  [                                                 0, -(z_2 - z_4)*(z_4 - z_5)/((z_1 - z_4)*(z_3 - z_4)),                            (z_2 - z_4)/(z_1 - z_4),                           -(z_4 - z_5)/(z_3 - z_4),                                                  0]
])

show(m)
print("Det: ", m.det())
print("Trace: ", m.trace())
print("Charpoly: ", m.charpoly())
print("Charpoly factor: ", m.charpoly().factor())
print("Inverse matrix:")
show(m.inverse())
print("")


# Matrix with replaced variables
m = matrix(QQ, [
  [                           (z_2 - z_5)/(z_2 - z_4),                                                  0,                                                  0,                                                  0,                           -(z_1 - z_2)/(z_2 - z_4)],
  [                                                 0,                            (z_1 - z_4)/(z_1 - z_5),                            (z_1 - z_3)/(z_1 - z_5),                                                  0,                                                  0],
  [                           (z_5 - z_4)/(z_2 - z_4),                                                  0,                                                  0,                                                  0,                            (z_1 - z_4)/(z_2 - z_4)],
  [                                                 0,  (z_2 - z_3)*(z_5 - z_4)/((z_1 - z_5)*(z_3 - z_5)),                           -(z_2 - z_3)/(z_1 - z_5),                            (z_3 - z_4)/(z_3 - z_5),                                                  0],
  [                                                 0, -(z_2 - z_5)*(z_5 - z_4)/((z_1 - z_5)*(z_3 - z_5)),                            (z_2 - z_5)/(z_1 - z_5),                           -(z_5 - z_4)/(z_3 - z_5),                                                  0]
])

show(m)
print("Det: ", m.det())
print("Trace: ", m.trace())
print("Charpoly: ", m.charpoly())
print("Charpoly factor: ", m.charpoly().factor())
