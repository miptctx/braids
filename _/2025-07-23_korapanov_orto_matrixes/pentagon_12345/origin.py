from sage.all import *


def cos_f(i, j, k, l):
  #return sqrt((i-l)*(j-k)/(i-k)/(j-l))
  zeta = ((i-l)*(j-k)) / ((i-k)*(j-l))
  return abs(sqrt(abs(zeta))) * ((1*I) if zeta < 0 else 1)


def sin_f(i, j, k, l):
  #return sqrt((i-j)*(k-l)/(i-k)/(j-l))
  zeta = ((i-j)*(k-l)) / ((i-k)*(j-l))
  return abs(sqrt(abs(zeta))) * ((1*I) if zeta < 0 else 1)



Q = matrix([
  [1,               0,              0 ],
  [0,  cos_f(1,3,4,5),  sin_f(1,3,4,5)],
  [0, -sin_f(1,3,4,5),  cos_f(1,3,4,5)]
])

P = matrix([
  [ cos_f(1,2,3,4), -sin_f(1,2,3,4), 0],
  [ sin_f(1,2,3,4),  cos_f(1,2,3,4), 0],
  [              0,               0, 1]
])

T = matrix([
  [ cos_f(1,2,3,5), -sin_f(1,2,3,5), 0],
  [ sin_f(1,2,3,5),  cos_f(1,2,3,5), 0],
  [              0,               0, 1]
])

S = matrix([
  [1,               0,               0],
  [0,  cos_f(2,3,4,5),  sin_f(2,3,4,5)],
  [0, -sin_f(2,3,4,5),  cos_f(2,3,4,5)]
])

R = matrix([
  [ cos_f(1,2,4,5), 0,  sin_f(1,2,4,5)],
  [              0, 1,               0],
  [-sin_f(1,2,4,5), 0,  cos_f(1,2,4,5)]
])

m_l = Q*P
m_r = T*S*R

m_l = m_l.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
m_r = m_r.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

show(m_l)
print("")
show(m_r)
print("")

print("Relation satisfied:", m_l == m_r)
