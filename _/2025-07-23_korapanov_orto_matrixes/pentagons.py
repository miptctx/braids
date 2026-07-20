from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation

'''
z_1 = 4#2#2#2#1#2#2#2#1
z_2 = 2#1#1#1#2#3#3#1#2
z_3 = 3#4#5#4#4#4#1#3#3
z_4 = 1#5#3#3#3#1#4#4#4
z_5 = 5#3#4#5#5#5#5#5#5
'''

elements = (1, 2, 3, 4, 5)

perms = Permutations(elements)

good_pentagons = 0
bad_pentagons = 0

for z_1, z_2, z_3, z_4, z_5 in perms:
  P = sort_triangulation({z_1,z_2,z_3}, {z_1,z_3,z_4}, {z_1,z_4,z_5})

  t, m = braiding(P, {z_1,z_4},{z_1,z_3},{z_3,z_5},{z_2,z_5},{z_2,z_4}, F=CC)

  assert P == t
  m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
  if m != matrix([[1,0,0],[0,1,0],[0,0,1]]):
    bad_pentagons += 1
    print('################')
    print(z_1, z_2, z_3, z_4, z_5)
    show(m)
  else:
    good_pentagons += 1

print("Good pentagons:", good_pentagons)
print("Bad pentagons:", bad_pentagons)
