from sage.all import *
from braids.korepanov import braiding_ext
from braids.utils import sort_triangulation, get_permutations


a_1,a_2,a_3,a_4,a_5 = var('a_1,a_2,a_3,a_4,a_5')

perms = Permutations([a_1,a_2,a_3,a_4,a_5])
#perms = get_permutations()

print("traverse all cycles")

good_pentagons = 0
bad_pentagons = 0


def rotate_tuple(*t):
    if len(t) != 4 or len(set(t)) != 4:
        raise ValueError(f"Кортеж должен содержать 4 попарно различных числа, len={len(t)}, set={set(t)}")

    min_val = min(t)
    min_idx = t.index(min_val)

    result = t[min_idx:] + t[:min_idx]

    return tuple(result)

print("check rotate_tuple function")
print(rotate_tuple(3, 5, 1, 7))
print(rotate_tuple(3, 7, 1, 5))
print(rotate_tuple(7, 3, 5, 1))
print(rotate_tuple(4, 2, 9, 1))
print(rotate_tuple(10, 5, 30, 20))
print(rotate_tuple(10, 20, 30, 5))

F = SR

for z_1, z_2, z_3, z_4, z_5 in perms:
  t_0 = sort_triangulation({z_1,z_2,z_4}, {z_1,z_4,z_5}, {z_2,z_3,z_4})

  print(z_1, z_2, z_3, z_4, z_5)

  assume(z_1 < z_2)
  assume(z_2 < z_3)
  assume(z_3 < z_4)
  assume(z_4 < z_5)

  t_1, m_1 = braiding_ext(t_0, (rotate_tuple(z_1, z_2, z_3, z_4),{z_2,z_4}), F=F)
  t_2, m_2 = braiding_ext(t_1, (rotate_tuple(z_1, z_3, z_4, z_5),{z_1,z_4}), F=F)
  t_3, m_3 = braiding_ext(t_2, (rotate_tuple(z_1, z_2, z_3, z_5),{z_1,z_3}), F=F)
  t_4, m_4 = braiding_ext(t_3, (rotate_tuple(z_2, z_3, z_4, z_5),{z_3,z_5}), F=F)
  t_5, m_5 = braiding_ext(t_4, (rotate_tuple(z_1, z_2, z_4, z_5),{z_2,z_5}), F=F)

  assert t_0 == t_5

  #m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
  #show(m)

  m = m_5*m_4*m_3*m_2*m_1

  m_00 = m[0][0]
  # print(m_00 == 1)
  #print(m_00)
  #m_00 = m_00.simplify_full()
  #print(m_00)
  #m_00 = m_00.subs({a_1: 1, a_2: 2, a_3: 3, a_4: 4, a_5: 5})
  #print(m_00)
  #print(float(m_00))

  quit()

  # m = m.simplify_full()
  m_max = m._maxima_()

  #m_1_max = m_1._maxima_()
  #m_2_max = m_2._maxima_()
  #m_3_max = m_3._maxima_()
  #m_4_max = m_4._maxima_()
  #m_5_max = m_5._maxima_()

  #m_max = m_5.dot(m_4).dot(m_3).dot(m_2).dot(m_1)

  #print(m_max)
  #print('###########')

  maxima(f"assume({a_1} > {a_2});")
  maxima(f"assume({a_2} > {a_3});")
  maxima(f"assume({a_3} > {a_4});")
  maxima(f"assume({a_4} > {a_5});")

  # m_max = m_max.fullratsimp()
  m_simpl = maxima(f"fullmap(fullratsimp, {m_max.name()});")
  # print(m_max)

  print('###########')
  # m = m_max.sage()
  m = m_simpl.sage()
  print(m)

  if m == matrix([[1,0,0],[0,1,0],[0,0,1]]):
    good_pentagons += 1
  else:
    bad_pentagons += 1

  #print("#####################")
  #print("")

  forget()

print("good:", good_pentagons)
print("bad:", bad_pentagons)
