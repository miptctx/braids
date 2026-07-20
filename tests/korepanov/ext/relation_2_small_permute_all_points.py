from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation, rotate_tuple

F=CC


for z_1, z_2, z_3, z_4, z_5, z_6 in Permutations([1,2,3,4,5,6]):
  T = sort_triangulation((z_1,z_2,z_4),(z_1,z_3,z_6),(z_1,z_4,z_5),(z_1,z_5,z_6),(z_2,z_3,z_6),(z_2,z_4,z_5),(z_2,z_5,z_6))

  t_ij, m_ij = braiding_ext(T,
                            (rotate_tuple(z_2,z_6,z_5,z_4),(z_2,z_5)),
                            (rotate_tuple(z_1,z_2,z_4,z_5),(z_1,z_4)),
                            (rotate_tuple(z_1,z_5,z_4,z_6),(z_5,z_6)),
                            (rotate_tuple(z_2,z_6,z_4,z_5),(z_2,z_4)),
                            (rotate_tuple(z_1,z_2,z_5,z_4),(z_1,z_5)),
                            (rotate_tuple(z_1,z_4,z_5,z_6),(z_4,z_6)),
                            F=F)

  t_ik, m_ik = braiding_ext(T,
                            (rotate_tuple(z_1,z_4,z_5,z_6),(z_1,z_5)),
                            (rotate_tuple(z_1,z_2,z_5,z_4),(z_2,z_4)),
                            (rotate_tuple(z_2,z_6,z_4,z_5),(z_5,z_6)),
                            (rotate_tuple(z_1,z_5,z_4,z_6),(z_1,z_4)),
                            (rotate_tuple(z_2,z_3,z_6,z_4),(z_2,z_6)),
                            (rotate_tuple(z_2,z_4,z_6,z_5),(z_4,z_5)),
                            (rotate_tuple(z_1,z_6,z_4,z_3),(z_3,z_6)),
                            (rotate_tuple(z_2,z_3,z_4,z_6),(z_2,z_4)),
                            (rotate_tuple(z_1,z_5,z_6,z_4),(z_1,z_6)),
                            (rotate_tuple(z_1,z_4,z_6,z_3),(z_3,z_4)),
                            (rotate_tuple(z_1,z_2,z_5,z_4),(z_1,z_5)),
                            (rotate_tuple(z_1,z_4,z_5,z_6),(z_4,z_6)),
                            F=F)

  t_jk, m_jk = braiding_ext(T,
                            (rotate_tuple(z_2,z_3,z_6,z_5),(z_2,z_6)),
                            (rotate_tuple(z_1,z_4,z_5,z_6),(z_1,z_5)),
                            (rotate_tuple(z_2,z_5,z_6,z_4),(z_4,z_5)),
                            (rotate_tuple(z_1,z_6,z_5,z_3),(z_3,z_6)),
                            (rotate_tuple(z_2,z_3,z_5,z_6),(z_2,z_5)),
                            (rotate_tuple(z_1,z_4,z_6,z_5),(z_1,z_6)),
                            (rotate_tuple(z_1,z_5,z_6,z_3),(z_3,z_5)),
                            (rotate_tuple(z_2,z_6,z_5,z_4),(z_4,z_6)),
                            F=F)

  M_1 = (m_jk*m_ik*m_ij).apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
  M_2 = (m_ik*m_ij*m_jk).apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)
  M_3 = (m_ij*m_jk*m_ik).apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)

  if (M_1 != M_2) or (M_2 != M_3):
    show(M_1)
    print("")
    show(M_2)
    print("")
    show(M_3)

    print("is realtion valid: ", M_1 == M_2 and M_2 == M_3)

    quit(-z_1)


print("All realtions are satisfied")
