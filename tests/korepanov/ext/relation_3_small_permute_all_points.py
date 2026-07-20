from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation, rotate_tuple

F=CC

for z_1, z_2, z_3, z_4, z_5, z_6, z_7 in Permutations([1,2,3,4,5,6,7]):
  T = sort_triangulation((z_1,z_2,z_4),(z_1,z_3,z_7),(z_1,z_4,z_5),(z_1,z_5,z_6),(z_1,z_6,z_7),(z_2,z_3,z_7),(z_2,z_4,z_5),(z_2,z_5,z_6),(z_2,z_6,z_7))

  t_jl, m_jl = braiding_ext(T,
                            (rotate_tuple(z_2,z_6,z_5,z_4),(z_2,z_5)),
                            (rotate_tuple(z_1,z_5,z_6,z_7),(z_1,z_6)),
                            (rotate_tuple(z_1,z_4,z_6,z_5),(z_4,z_5)),
                            (rotate_tuple(z_2,z_7,z_5,z_6),(z_6,z_7)),
                            (rotate_tuple(z_1,z_6,z_5,z_7),(z_1,z_5)),
                            (rotate_tuple(z_2,z_3,z_7,z_5),(z_2,z_7)),
                            (rotate_tuple(z_2,z_5,z_7,z_6),(z_5,z_6)),
                            (rotate_tuple(z_1,z_7,z_5,z_3),(z_3,z_7)),
                            (rotate_tuple(z_2,z_3,z_5,z_7),(z_2,z_5)),
                            (rotate_tuple(z_1,z_6,z_7,z_5),(z_1,z_7)),
                            (rotate_tuple(z_1,z_5,z_7,z_3),(z_3,z_5)),
                            (rotate_tuple(z_1,z_4,z_6,z_5),(z_1,z_6)),
                            (rotate_tuple(z_1,z_5,z_6,z_7),(z_5,z_7)),
                            (rotate_tuple(z_2,z_6,z_5,z_4),(z_4,z_6)),
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
                            F=F)

  t_ik, m_ik = braiding_ext(T,
                            (rotate_tuple(z_1,z_4,z_5,z_6),(z_1,z_5)),
                            (rotate_tuple(z_1,z_2,z_5,z_4),(z_2,z_4)),
                            (rotate_tuple(z_2,z_6,z_4,z_5),(z_5,z_6)),
                            (rotate_tuple(z_1,z_5,z_4,z_6),(z_1,z_4)),
                            (rotate_tuple(z_2,z_7,z_6,z_4),(z_2,z_6)),
                            (rotate_tuple(z_2,z_4,z_6,z_5),(z_4,z_5)),
                            (rotate_tuple(z_1,z_6,z_4,z_7),(z_6,z_7)),
                            (rotate_tuple(z_2,z_7,z_4,z_6),(z_2,z_4)),
                            (rotate_tuple(z_1,z_5,z_6,z_4),(z_1,z_6)),
                            (rotate_tuple(z_1,z_4,z_6,z_7),(z_4,z_7)),
                            (rotate_tuple(z_1,z_2,z_5,z_4),(z_1,z_5)),
                            (rotate_tuple(z_1,z_4,z_5,z_6),(z_4,z_6)),
                            F=F)

  t_jk, m_jk = braiding_ext(T,
                            (rotate_tuple(z_2,z_7,z_6,z_5),(z_2,z_6)),
                            (rotate_tuple(z_1,z_4,z_5,z_6),(z_1,z_5)),
                            (rotate_tuple(z_2,z_5,z_6,z_4),(z_4,z_5)),
                            (rotate_tuple(z_1,z_6,z_5,z_7),(z_6,z_7)),
                            (rotate_tuple(z_2,z_7,z_5,z_6),(z_2,z_5)),
                            (rotate_tuple(z_1,z_4,z_6,z_5),(z_1,z_6)),
                            (rotate_tuple(z_1,z_5,z_6,z_7),(z_5,z_7)),
                            (rotate_tuple(z_2,z_6,z_5,z_4),(z_4,z_6)),
                            F=F)


  assert t_jk == t_kl
  assert t_kl == t_ik
  assert t_ik == t_jk

  lhs = (m_jk*m_ik*m_kl*m_jl).apply_map(lambda x: round(x.real(), 8) + round(x.imag(), 8) * I)
  rhs = (m_jl*m_jk*m_ik*m_kl).apply_map(lambda x: round(x.real(), 8) + round(x.imag(), 8) * I)

  if lhs != rhs:
    print("Result edges m_jk_ik_kl_jl")
    show(lhs)

    print("Result edges e_jl_jk_ik_kl")
    show(rhs)

    print("is relation valid: ", lhs == rhs)

    quit(-z_1)


print("All realtions are satisfied")
