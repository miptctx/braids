from sage.all import *
from braids.korepanov import braiding
from braids.utils import sort_triangulation

z_1,z_2,z_3,z_4,z_5 = var('z_1 z_2 z_3 z_4 z_5')


assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)
# assume(z_5 < z_1)


P = sort_triangulation({z_1,z_2,z_4}, {z_1,z_4,z_5}, {z_2,z_3,z_4})

t, mp = braiding(P, {z_2,z_4},{z_1,z_4},{z_1,z_3},{z_3,z_5},{z_2,z_5}, F=SR)

assert P == t

print('################')
show(t)
#m = mp.subs({z_1: 1, z_2: 2, z_3: 3, z_4: 4, z_5: 5})
#show(m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
## show(m)
#quit()

# elements = (complex(1), complex(2), complex(3), complex(4), complex(5))
elements = [1,2,3,4,5]

perms = Permutations(elements)

good_pentagons = 0
bad_pentagons = 0

for p_1, p_2, p_3, p_4, p_5 in perms:
  # x_1, x_2, x_3, x_4, x_5 = elements[p_1-1], elements[p_2-1], elements[p_3-1], elements[p_4-1], elements[p_5-1]

  # m = m.subs({z_1: x_1, z_2: x_2, z_3: x_3, z_4: x_4, z_5: x_5})
  m = mp.subs({z_1: p_1, z_2: p_2, z_3: p_3, z_4: p_4, z_5: p_5})
  m = m.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

  if (m != matrix([[1,0,0],[0,1,0],[0,0,1]])):
    bad_pentagons += 1
    print("###############")
    # print(x_1, x_2, x_3, x_4, x_5)
    # print(p_1, p_2, p_3, p_4, p_5)
    # show(m)
  else:
    # print(p_1, p_2, p_3, p_4, p_5)
    good_pentagons += 1


print("Good pentagons:", good_pentagons)
print("Bad pentagons:", bad_pentagons)
