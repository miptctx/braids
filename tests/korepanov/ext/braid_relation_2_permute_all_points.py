from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation, rotate_tuple

F = CC

for z_1, z_2, z_3, z_4, z_5, z_6,z_7 in Permutations([1,2,3,4,5,6,7]):
  P = sort_triangulation({z_1,z_2,z_6}, {z_1,z_3,z_4},{z_1,z_4,z_5},{z_1,z_5,z_6},{z_2,z_3,z_4},{z_2,z_4,z_5},{z_2,z_5,z_6})

  t_l, m_l = braiding_ext(P,
                          (rotate_tuple(z_2,z_4,z_5,z_6),(z_2,z_5)),
                          (rotate_tuple(z_1,z_2,z_6,z_5),(z_1,z_6)),
                          (rotate_tuple(z_1,z_5,z_6,z_4),(z_4,z_5)),

                          (rotate_tuple(z_1,z_5,z_6,z_4),(z_1,z_6)),
                          (rotate_tuple(z_2,z_3,z_4,z_6),(z_2,z_4)),
                          (rotate_tuple(z_2,z_6,z_4,z_5),(z_5,z_6)),
                          (rotate_tuple(z_1,z_4,z_6,z_3),(z_3,z_4)),

                          (rotate_tuple(z_2,z_6,z_4,z_5),(z_2,z_4)),
                          (rotate_tuple(z_1,z_2,z_5,z_4),(z_1,z_5)),
                          (rotate_tuple(z_1,z_4,z_5,z_6),(z_4,z_6)),
                          F=F)

  t_r, m_r = braiding_ext(P,
                          (rotate_tuple(z_1,z_6,z_5,z_4),(z_1,z_5)),
                          (rotate_tuple(z_2,z_3,z_4,z_5),(z_2,z_4)),
                          (rotate_tuple(z_2,z_5,z_4,z_6),(z_5,z_6)),
                          (rotate_tuple(z_1,z_4,z_5,z_3),(z_3,z_4)),

                          (rotate_tuple(z_2,z_5,z_4,z_6),(z_2,z_4)),
                          (rotate_tuple(z_1,z_2,z_6,z_4),(z_1,z_6)),
                          (rotate_tuple(z_1,z_4,z_6,z_5),(z_4,z_5)),

                          (rotate_tuple(z_1,z_4,z_6,z_5),(z_1,z_6)),
                          (rotate_tuple(z_2,z_3,z_5,z_6),(z_2,z_5)),
                          (rotate_tuple(z_2,z_6,z_5,z_4),(z_4,z_6)),
                          (rotate_tuple(z_1,z_5,z_6,z_3),(z_3,z_5)),
                          F=F)

  assert t_l == t_r

  m_l = m_l.apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
  m_r = m_r.apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)

  if m_l != m_r:
    print("Result matrix m_l")
    show(m_l)

    print("Result matrix m_r")
    show(m_r)

    print("Equation satisfied: ", m_l == m_r)

    quit(-1)


print("All realtions are satisfied")

