from sage.all import *
from braids.utils import get_permutations


z_1,z_2,z_3,z_4,z_5 = var('z_1 z_2 z_3 z_4 z_5')

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)


def cos_f(i, j, k, l, i_cos=0):
  # return sqrt(((i-l)*(j-k))/((i-k)*(j-l)))
  zeta = ((i-l)*(j-k)) / ((i-k)*(j-l))
  return ((-1)**i_cos)*abs(sqrt(abs(zeta))) * ((1*I) if zeta < 0 else 1)


def sin_f(i, j, k, l, i_sin=0):
  # return sqrt(((i-j)*(k-l))/((i-k)*(j-l)))
  zeta = ((i-j)*(k-l)) / ((i-k)*(j-l))
  return ((-1)**i_sin)*abs(sqrt(abs(zeta))) * ((1*I) if zeta < 0 else 1)


q = matrix([
  [1,                       0,                      0],
  [0,  cos_f(z_1,z_3,z_4,z_5), sin_f(z_1,z_3,z_4,z_5)],
  [0, -sin_f(z_1,z_3,z_4,z_5), cos_f(z_1,z_3,z_4,z_5)]
])
p = matrix([
  [cos_f(z_1,z_2,z_3,z_4), -sin_f(z_1,z_2,z_3,z_4), 0],
  [sin_f(z_1,z_2,z_3,z_4),  cos_f(z_1,z_2,z_3,z_4), 0],
  [0,                   0,                          1]
])

m_l = q*p

t = matrix([[cos_f(z_1,z_2,z_3,z_5), -sin_f(z_1,z_2,z_3,z_5), 0], [sin_f(z_1,z_2,z_3,z_5), cos_f(z_1,z_2,z_3,z_5), 0], [0, 0, 1]])
s = matrix([[1, 0, 0], [0, cos_f(z_2,z_3,z_4,z_5), sin_f(z_2,z_3,z_4,z_5)], [0, -sin_f(z_2,z_3,z_4,z_5), cos_f(z_2,z_3,z_4,z_5)]])
r = matrix([[cos_f(z_1,z_2,z_4,z_5), 0, sin_f(z_1,z_2,z_4,z_5)], [0, 1, 0], [-sin_f(z_1,z_2,z_4,z_5), 0, cos_f(z_1,z_2,z_4,z_5)]])

m_r = t*s*r

'''
print("product order")
print("")
show(latex(r.transpose()))
print("")
show(latex(s.transpose()))
print("")
show(latex(t.transpose()))
print("")
show(latex(q))
print("")
show(latex(p))
'''


#m_p = r.transpose()*s.transpose()*t.transpose()*q*p
m_p = p*r.transpose()*s.transpose()*t.transpose()*q
#m_p = q*p*r.transpose()*s.transpose()*t.transpose()
#m_p = t.transpose()*q*p*r.transpose()*s.transpose()
#m_p = s.transpose()*t.transpose()*q*p*r.transpose()
# show(latex(m_p))



# # elements = (complex(1), complex(2), complex(3), complex(4), complex(5))
perms = Permutations([1,2,3,4,5])
# perms = get_permutations()

good_pentagons = 0
bad_pentagons = 0

for p_1, p_2, p_3, p_4, p_5 in perms:
  # x_1, x_2, x_3, x_4, x_5 = elements[p_1-1], elements[p_2-1], elements[p_3-1], elements[p_4-1], elements[p_5-1]

  # _m_l = m_l.subs({z_1: x_1, z_2: x_2, z_3: x_3, z_4: x_4, z_5: x_5})
  _m_l = m_l.subs({z_1: p_1, z_2: p_2, z_3: p_3, z_4: p_4, z_5: p_5})
  _m_l = _m_l.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

  # _m_r = m_r.subs({z_1: x_1, z_2: x_2, z_3: x_3, z_4: x_4, z_5: x_5})
  _m_r = m_r.subs({z_1: p_1, z_2: p_2, z_3: p_3, z_4: p_4, z_5: p_5})
  _m_r = _m_r.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

  # m_p = m_p.subs({z_1: x_1, z_2: x_2, z_3: x_3, z_4: x_4, z_5: x_5})
  _m_p = m_p.subs({z_1: p_1, z_2: p_2, z_3: p_3, z_4: p_4, z_5: p_5})
  _m_p = _m_p.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

  if (_m_l != _m_r):
  # if (_m_p != matrix([[1,0,0],[0,1,0],[0,0,1]])):
    bad_pentagons += 1
    # print("###############")
    # # print(x_1, x_2, x_3, x_4, x_5)
    print(p_1, p_2, p_3, p_4, p_5)
    show(_m_l)
    print("")
    show(_m_r)
    # show(_m_p)
  else:
    # print(p_1, p_2, p_3, p_4, p_5)
    good_pentagons += 1


print("Good pentagons:", good_pentagons)
print("Bad pentagons:", bad_pentagons)
