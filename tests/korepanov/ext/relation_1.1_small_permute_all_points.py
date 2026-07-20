from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation, rotate_tuple

F=CC

for z_1, z_2, z_3, z_4, z_5, z_6, z_7 in Permutations([1,2,3,4,5,6,7]):
  T = sort_triangulation((z_1,z_2,z_4),(z_1,z_3,z_7),(z_1,z_4,z_5),(z_1,z_5,z_6),(z_1,z_6,z_7),(z_2,z_3,z_7),(z_2,z_4,z_5),(z_2,z_5,z_6),(z_2,z_6,z_7))

  t_ij, m_ij = braiding_ext(T,
                            (rotate_tuple(z_2,z_6,z_5,z_4),(z_2,z_5)),
                            (rotate_tuple(z_1,z_2,z_4,z_5),(z_1,z_4)),
                            (rotate_tuple(z_1,z_5,z_4,z_6),(z_5,z_6)),
                            (rotate_tuple(z_2,z_6,z_4,z_5),(z_2,z_4)),
                            (rotate_tuple(z_1,z_2,z_5,z_4),(z_1,z_5)),
                            (rotate_tuple(z_1,z_4,z_5,z_6),(z_4,z_6)),
                            F=F)

  t_kl, m_kl = braiding_ext(T,
                            (rotate_tuple(z_2,z_3,z_7,z_6),(z_2,z_7)),
                            (rotate_tuple(z_1,z_5,z_6,z_7),(z_1,z_6)),
                            (rotate_tuple(z_2,z_6,z_7,z_5),(z_5,z_6)),
                            (rotate_tuple(z_1,z_7,z_6,z_3),(z_3,z_7)),
                            (rotate_tuple(z_2,z_3,z_6,z_7),(z_2,z_6)),
                            (rotate_tuple(z_1,z_5,z_7,z_6),(z_1,z_7)),
                            (rotate_tuple(z_1,z_6,z_7,z_3),(z_3,z_6)),
                            (rotate_tuple(z_2,z_7,z_6,z_5),(z_5,z_7)),
                            F=CC)

  assert t_ij == t_kl

  lhs = (m_kl*m_ij).apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
  rhs = (m_ij*m_kl).apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)

  if lhs != rhs:
    print("lhs")
    print(lhs)

    print("rhs")
    print(rhs)

    print("is realtion valid: ", lhs == rhs)

    quit(-1)


print("All realtions are satisfied")
