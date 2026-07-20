from sage.all import *
from braids.korepanov import braiding_ext as braiding
from braids.utils import sort_triangulation, get_permutations

GF2 = GF(2)

perms = Permutations([1,2,3,4,5])
#perms = get_permutations()

very_good_pentagons = 0

all_sign_vectors = set()

print("traverse all cycles")

good_pentagons = 0
bad_pentagons = 0


def rotate_tuple(*t):
    if len(t) != 4 or len(set(t)) != 4:
        raise ValueError(f"Кортеж должен содержать 4 попарно различных числа, len={len(t)}, set={set(t)}")

    min_val = min(t)
    min_idx = t.index(min_val)

    '''
    # Определяем соседей в оригинальном кортеже
    left_idx = (min_idx - 1) % 4
    right_idx = (min_idx + 1) % 4
    left = t[left_idx]
    right = t[right_idx]

    # Проверяем условие для реверса
    if left < right:
        result = t[min_idx+1:] + t[:min_idx+1]
        result = reversed(result)
        # result = result[::-1]
    else:
       result = t[min_idx:] + t[:min_idx]
    '''

    result = t[min_idx:] + t[:min_idx]

    return tuple(result)

print("check rotate_tuple function")
print(rotate_tuple(3, 5, 1, 7))
print(rotate_tuple(3, 7, 1, 5))
print(rotate_tuple(7, 3, 5, 1))
print(rotate_tuple(4, 2, 9, 1))
print(rotate_tuple(10, 5, 30, 20))
print(rotate_tuple(10, 20, 30, 5))


for z_1, z_2, z_3, z_4, z_5 in perms:
# for z_1, z_2, z_3, z_4, z_5 in [[1,4,2,3,5]]:
  P = sort_triangulation({z_1,z_2,z_4}, {z_1,z_4,z_5}, {z_2,z_3,z_4})

  print(z_1, z_2, z_3, z_4, z_5)

  t, m = braiding(P,
                  (rotate_tuple(z_1, z_2, z_3, z_4),{z_2,z_4}),
                  (rotate_tuple(z_1, z_3, z_4, z_5),{z_1,z_4}),
                  (rotate_tuple(z_1, z_2, z_3, z_5),{z_1,z_3}),
                  (rotate_tuple(z_2, z_3, z_4, z_5),{z_3,z_5}),
                  (rotate_tuple(z_1, z_2, z_4, z_5),{z_2,z_5}))
  assert P == t
  m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
  show(m)

  if m == matrix([[1,0,0],[0,1,0],[0,0,1]]):
    good_pentagons += 1
  else:
    bad_pentagons += 1

  print("#####################")
  print("")

print("good:", good_pentagons)
print("bad:", bad_pentagons)
