# This is trefoil on z_2 strands

from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation, rotate_tuple

F = CC

for z_1, z_2, z_3, z_4, z_5, z_6,z_7 in Permutations([1,2,3,4,5,6,7]):
  P = sort_triangulation({z_1,z_2,z_7},{z_1,z_3,z_4},{z_1,z_4,z_5},{z_1,z_5,z_6},{z_1,z_6,z_7},{z_2,z_3,z_4},{z_2,z_4,z_5},{z_2,z_5,z_6},{z_2,z_6,z_7})

  t_ij, m_ij = braiding_ext(P,
                            (rotate_tuple(z_2,z_5,z_6,z_7),(z_2,z_6)),
                            (rotate_tuple(z_1,z_2,z_7,z_6),(z_1,z_7)),
                            (rotate_tuple(z_1,z_6,z_7,z_5),(z_5,z_6)),

                            (rotate_tuple(z_2,z_3,z_4,z_5),(z_2,z_4)),
                            (rotate_tuple(z_1,z_7,z_5,z_4),(z_1,z_5)),
                            (rotate_tuple(z_2,z_5,z_4,z_7),(z_5,z_7)),
                            (rotate_tuple(z_1,z_4,z_5,z_3),(z_3,z_4)),

                            F=F)

  t_ji, m_ji = braiding_ext(P,
                            (rotate_tuple(z_2,z_3,z_4,z_5),(z_2,z_4)),
                            (rotate_tuple(z_1,z_6,z_5,z_4),(z_1,z_5)),
                            (rotate_tuple(z_2,z_5,z_4,z_6),(z_5,z_6)),
                            (rotate_tuple(z_1,z_4,z_5,z_3),(z_3,z_4)),

                            (rotate_tuple(z_2,z_4,z_6,z_7),(z_2,z_6)),
                            (rotate_tuple(z_1,z_2,z_7,z_6),(z_1,z_7)),
                            (rotate_tuple(z_1,z_6,z_7,z_4),(z_4,z_6)),

                            F=F)

  assert t_ij == t_ji

  m_ij = m_ij.apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
  m_ji = m_ji.apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)

  if m_ij != m_ji:
    print("Result matrix m_ij")
    show(m_ij)

    print("Result matrix m_ji")
    show(m_ji)

    print("Equation satisfied: ", m_ij == m_ji)

    quit(-1)


print("All realtions are satisfied")
