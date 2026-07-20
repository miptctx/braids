from sage.all import *
from braids.korepanov import braiding_ext as braiding
from braids.utils import sort_triangulation, get_permutations, rotate_tuple
from braids.prints import print_triangles_pretty


a_1,a_2,a_3,a_4,a_5 = var('a_1,a_2,a_3,a_4,a_5')

assume(a_1 > 0)
assume(a_1 < a_2)
assume(a_2 < a_3)
assume(a_3 < a_4)
assume(a_4 < a_5)

permutations = list(get_permutations(var_list=[a_1,a_2,a_3,a_4,a_5]))
print(permutations)

forget()

for z_1, z_2, z_3, z_4, z_5 in permutations:

  print(z_1, z_2, z_3, z_4, z_5)

  assume(z_1 > 0)
  assume(z_1 < z_2)
  assume(z_2 < z_3)
  assume(z_3 < z_4)
  assume(z_4 < z_5)

  P = sort_triangulation({z_1,z_2,z_4}, {z_1,z_4,z_5}, {z_2,z_3,z_4})
  t, m = braiding(P,
                  (rotate_tuple(z_1, z_2, z_3, z_4),{z_2,z_4}),
                  (rotate_tuple(z_1, z_3, z_4, z_5),{z_1,z_4}),
                  (rotate_tuple(z_1, z_2, z_3, z_5),{z_1,z_3}),
                  (rotate_tuple(z_2, z_3, z_4, z_5),{z_3,z_5}),
                  (rotate_tuple(z_1, z_2, z_4, z_5),{z_2,z_5}),
                  F=SR)

  print_triangles_pretty(P)
  print_triangles_pretty(t)

  assert P == t

  '''
  for a in assumptions():
    maxima(f"assume({a})")

  print(maxima('facts()'))

  m_00 = m[0][0]._maxima_().fullratsimp()

  print(m_00.sage())
  '''

  print(f"simplify({m[0][0].simplify_full()}) assuming {z_1} > 0, {z_1} < {z_2}, {z_2} < {z_3}, {z_3} < {z_4}, {z_4} < {z_5};\n")
  print(f"simplify({m[0][1].simplify_full()}) assuming {z_1} > 0, {z_1} < {z_2}, {z_2} < {z_3}, {z_3} < {z_4}, {z_4} < {z_5};\n")
  print(f"simplify({m[0][2].simplify_full()}) assuming {z_1} > 0, {z_1} < {z_2}, {z_2} < {z_3}, {z_3} < {z_4}, {z_4} < {z_5};\n")
  print(f"simplify({m[1][0].simplify_full()}) assuming {z_1} > 0, {z_1} < {z_2}, {z_2} < {z_3}, {z_3} < {z_4}, {z_4} < {z_5};\n")
  print(f"simplify({m[1][1].simplify_full()}) assuming {z_1} > 0, {z_1} < {z_2}, {z_2} < {z_3}, {z_3} < {z_4}, {z_4} < {z_5};\n")
  print(f"simplify({m[1][2].simplify_full()}) assuming {z_1} > 0, {z_1} < {z_2}, {z_2} < {z_3}, {z_3} < {z_4}, {z_4} < {z_5};\n")
  print(f"simplify({m[2][0].simplify_full()}) assuming {z_1} > 0, {z_1} < {z_2}, {z_2} < {z_3}, {z_3} < {z_4}, {z_4} < {z_5};\n")
  print(f"simplify({m[2][1].simplify_full()}) assuming {z_1} > 0, {z_1} < {z_2}, {z_2} < {z_3}, {z_3} < {z_4}, {z_4} < {z_5};\n")
  print(f"simplify({m[2][2].simplify_full()}) assuming {z_1} > 0, {z_1} < {z_2}, {z_2} < {z_3}, {z_3} < {z_4}, {z_4} < {z_5};\n")

  forget()

  print("#################")

  # quit()
