from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty


F = SR

var('x_1,x_2,x_3,x_4,x_5')

assume(x_1 < x_2)
assume(x_2 < x_3)
assume(x_3 < x_4)
assume(x_4 < x_5)


var('z_1,z_2,z_3,z_4,z_5')

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)


P = sort_triangulation({x_1,x_2,x_3}, {x_1,x_3,x_4}, {x_1,x_4,x_5})
t, m_x = braiding(P, {x_1,x_4},{x_1,x_3},{x_3,x_5},{x_2,x_5},{x_2,x_4}, F=F)

#for z_1, z_2, z_3, z_4, z_5 in Permutations([1,2,3,4,5]):
for z_1, z_2, z_3, z_4, z_5 in Permutations([z_1,z_2,z_3,z_4,z_5]):
  print()
  print('################')
  print("permutation:", z_1, z_2, z_3, z_4, z_5)

  m = m_x.subs({x_1: z_1, x_2:z_2, x_3:z_3, x_4:z_4, x_5:z_5})
  print(m[0][0])
  m = m.simplify_full()

  assert P == t

  #print_triangles_pretty(P)
  #print_triangles_pretty(t)
  show(m)
