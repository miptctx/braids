from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation, get_permutations


# # elements = (complex(1), complex(2), complex(3), complex(4), complex(5))
# elements = [1,2,3,4,5]
# perms = Permutations(elements)
perms = get_permutations()

good_pentagons = 0
bad_pentagons = 0

print("check permutations")
for p_1, p_2, p_3, p_4, p_5 in perms:
  # print(p_1, p_2, p_3, p_4, p_5)
  z_1,z_2,z_3,z_4,z_5 = var('z_1 z_2 z_3 z_4 z_5')
  #str_var = " ".join([f"z_{i}" for i in (p_1, p_2, p_3, p_4, p_5)])
  #z_1,z_2,z_3,z_4,z_5 = var(str_var)

  assume(z_1 < z_2)
  assume(z_2 < z_3)
  assume(z_3 < z_4)
  assume(z_4 < z_5)

  zetas = [z_1,z_2,z_3,z_4,z_5]

  # print(p_1, p_2, p_3, p_4, p_5)

  x_1, x_2, x_3, x_4, x_5 = zetas[p_1-1], zetas[p_2-1], zetas[p_3-1], zetas[p_4-1], zetas[p_5-1]

  #P = sort_triangulation({x_1,x_2,x_3}, {x_1,x_3,x_4}, {x_1,x_4,x_5})
  #t, m = braiding(P, {x_1,x_4},{x_1,x_3},{x_3,x_5},{x_2,x_5},{x_2,x_4}, F=SR)
  P = sort_triangulation({x_1,x_2,x_4}, {x_1,x_4,x_5}, {x_2,x_3,x_4})
  t, m = braiding(P, {x_2,x_4},{x_1,x_4},{x_1,x_3},{x_3,x_5},{x_2,x_5}, F=SR)
  assert P == t

  # m = m.expand()
  # m = m.simplify_full()

  # v_1, v_2, v_3, v_4, v_5 = elements[p_1-1], elements[p_2-1], elements[p_3-1], elements[p_4-1], elements[p_5-1]
  # mp = m.subs({x_1: v_1, x_2: v_2, x_3: v_3, x_4: v_4, x_5: v_5})
  mp = m.subs({x_1: p_1, x_2: p_2, x_3: p_3, x_4: p_4, x_5: p_5})
  mp = mp.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
  #'''
  if mp != matrix([[1,0,0],[0,1,0],[0,0,1]]):
    bad_pentagons += 1
    print('----------------')
    # print(v_1, v_2, v_3, v_4, v_5)
    print(p_1, p_2, p_3, p_4, p_5)
    show(mp)
    print('----------------')
  else:
    good_pentagons += 1
    print(p_1, p_2, p_3, p_4, p_5)
  #'''

  '''
  if p_1 == 1 and p_2 == 2 and p_3 == 5 and p_4 ==3 and p_5 == 4:
  #if p_1 == 3 and p_2 == 1 and p_3 == 2 and p_4 ==5 and p_5 == 4:
    print(x_1, x_2, x_3, x_4, x_5)
    show(mp)
    print("######### m[2][2] #########")
    # print(m[2][2])
    show(latex(m[2][2]))
    quit()
  '''

  #z_1.forget()
  #z_2.forget()
  #z_3.forget()
  #z_4.forget()
  #z_5.forget()

  del z_1
  del z_2
  del z_3
  del z_4
  del z_5

  #x_1.forget()
  #x_2.forget()
  #x_3.forget()
  #x_4.forget()
  #x_5.forget()

print("Good pentagons:", good_pentagons)
print("Bad pentagons:", bad_pentagons)
