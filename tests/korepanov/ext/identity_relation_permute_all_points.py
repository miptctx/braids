from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation, rotate_tuple

F = CC

for z_1, z_2, z_3, z_4, z_5, z_6, z_7 in Permutations([1,2,3,4,5,6,7]):
  P = sort_triangulation({z_1,z_2,z_3}, {z_1,z_3,z_4})

  t_1, m_1 = braiding_ext(P, (rotate_tuple(z_1,z_2,z_3,z_4),(z_1,z_3)), (rotate_tuple(z_1,z_2,z_3,z_4),(z_2,z_4)), F=F)

  m_1 = m_1.apply_map(lambda x: round(x.real(), 10) + round(x.imag(), 10) * I)

  if (m_1 != matrix([[1,0],[0,1]])):
    print("Result matrix m_1")
    show(m_1)
    quit(-1)


print("All realtions are satisfied")
