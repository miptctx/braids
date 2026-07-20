from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation, rotate_tuple

F = CC

for z_1, z_2, z_3, z_4, z_5, z_6, z_7 in Permutations([1,2,3,4,5,6,7]):
  P = sort_triangulation({z_1,z_3,z_4}, {z_2,z_3,z_4},{z_2,z_4,z_6},{z_4,z_5,z_6})

  t_12, m_12 = braiding_ext(P, (rotate_tuple(z_1,z_3,z_2,z_4),(z_3,z_4)), (rotate_tuple(z_2,z_6,z_5,z_4),(z_4,z_6)), F=F)

  t_21, m_21 = braiding_ext(P, (rotate_tuple(z_2,z_6,z_5,z_4),(z_4,z_6)), (rotate_tuple(z_1,z_3,z_2,z_4),(z_3,z_4)), F=F)

  assert t_12 == t_21

  m_12 = m_12.apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
  m_21 = m_21.apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)

  if m_12 != m_21:
    print("Result matrix m_12")
    show(m_12)

    print("Result matrix m_21")
    show(m_21)

    print("Equation satisfied: ", m_12 == m_21)

    quit(-1)


print("All realtions are satisfied")

