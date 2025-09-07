from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty


elements = (complex(1), complex(2), complex(3), complex(4), complex(5))

perms = Permutations(elements)

good_pentagons = 0
bad_pentagons = 0


for z_1, z_2, z_3, z_4, z_5 in perms:

  # P = sort_triangulation({z_1,z_2,z_3}, {z_1,z_3,z_4}, {z_1,z_4,z_5})
  # t, m = braiding(P, {z_1,z_4},{z_1,z_3},{z_3,z_5},{z_2,z_5},{z_2,z_4}, F=CC)
  P = sort_triangulation({z_1,z_2,z_4}, {z_1,z_4,z_5}, {z_2,z_3,z_4})
  t, m = braiding(P, {z_2,z_4},{z_1,z_4},{z_1,z_3},{z_3,z_5},{z_2,z_5}, F=CC)

  assert P == t

  m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
  if m != matrix([[1,0,0],[0,1,0],[0,0,1]]):
    bad_pentagons += 1
    print('################')
    print_triangles_pretty(t)
    print('================')
    print(z_1, z_2, z_3, z_4, z_5)
    show(m)
  else:
    good_pentagons += 1


print("Good pentagons:", good_pentagons)
print("Bad pentagons:", bad_pentagons)
