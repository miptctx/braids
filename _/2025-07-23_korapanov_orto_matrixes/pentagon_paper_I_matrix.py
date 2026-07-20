from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty


#z_1, z_2, z_3, z_4, z_5 = 1, 2, 3, 4, 5
#z_1, z_2, z_3, z_4, z_5 = 9, 2, 3, 4, 5
#z_1, z_2, z_3, z_4, z_5 = 1, 2, 3, 5, 4
#z_1, z_2, z_3, z_4, z_5 = 1, 2, 4, 3, 5
#z_1, z_2, z_3, z_4, z_5 = 1, 2, 4, 7, 5
#z_1, z_2, z_3, z_4, z_5 = 8, 2, 4, 5, 3
#z_1, z_2, z_3, z_4, z_5 = 1, 2, 4, 5, 3
#z_1, z_2, z_3, z_4, z_5 = 5, 4, 2, 3, 1
#z_1, z_2, z_3, z_4, z_5 = 1, 3, 2, 5, 4
#z_1, z_2, z_3, z_4, z_5 = 1, 3, 4, 2, 5
#z_1, z_2, z_3, z_4, z_5 = 1, 3, 2, 4, 5
z_1, z_2, z_3, z_4, z_5 = 1, 3, 5, 2, 4
#z_1, z_2, z_3, z_4, z_5 = 1, 4, 2, 3, 5
#z_1, z_2, z_3, z_4, z_5 = 2, 3, 5, 1, 4

print(z_1, z_2, z_3, z_4, z_5)
print("----------------")

P = sort_triangulation({z_1,z_2,z_4}, {z_1,z_4,z_5}, {z_2,z_3,z_4})

t, m = braiding(P, {z_2,z_4},{z_1,z_4},{z_1,z_3},{z_3,z_5},{z_2,z_5})
print_triangles_pretty(P)
print_triangles_pretty(t)
assert P == t
m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
show(m)
print('#################')

unique_indexes = set()

good_pentagons = 0
bad_pentagons = 0

for s_1 in range(0,2):
  t_1, m_1 = braiding(P, {z_2,z_4})
  for s_2 in range(0,2):
    t_2, m_2 = braiding(t_1, {z_1,z_4})
    for s_3 in range(0,2):
      t_3, m_3 = braiding(t_2, {z_1,z_3})
      for s_4 in range(0,2):
        t_4, m_4 = braiding(t_3, {z_3,z_5})
        for s_5 in range(0,2):
          t_5, m_5 = braiding(t_4, {z_2,z_5})

          m = (((-1)**s_5)*m_5) * (((-1)**s_4)*m_4) * (((-1)**s_3)*m_3) * (((-1)**s_2)*m_2) * (((-1)**s_1)*m_1)
          #m = (((I)**s_5)*m_5) * (((I)**s_4)*m_4) * (((I)**s_3)*m_3) * (((I)**s_2)*m_2) * (((I)**s_1)*m_1)
          assert P == t_5
          m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
          if m == matrix([[1,0,0],[0,1,0],[0,0,1]]):
            print("#################")
            print(s_1, "|", s_2, "|", s_3, "|", s_4, "|", s_5)
            good_pentagons += 1
          else:
            bad_pentagons += 1


print("bad pentagond:", bad_pentagons)
print("good pentagond:", good_pentagons)
