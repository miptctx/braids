from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation, get_permutations

GF2 = GF(2)

# perms = Permutations([1,2,3,4,5])
perms = get_permutations()

very_good_pentagons = 0

all_sign_vectors = set()

print("traverse all cycles")

good_pentagons = 0
bad_pentagons = 0

for z_1, z_2, z_3, z_4, z_5 in perms:
  P = sort_triangulation({z_1,z_2,z_4}, {z_1,z_4,z_5}, {z_2,z_3,z_4})

  print(z_1, z_2, z_3, z_4, z_5)

  t, m = braiding(P, {z_2,z_4},{z_1,z_4},{z_1,z_3},{z_3,z_5},{z_2,z_5})
  assert P == t
  m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
  show(m)

  if m == matrix([[1,0,0],[0,1,0],[0,0,1]]):
    good_pentagons += 1
  else:
    bad_pentagons += 1

  print("#####################")
  print("")

print("good:", good_pentagons)
print("bad:", bad_pentagons)
