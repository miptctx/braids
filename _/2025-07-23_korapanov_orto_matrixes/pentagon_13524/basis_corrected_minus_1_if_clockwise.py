from sage.all import *


def cos_f(i, j, k, l):
  #return sqrt((i-l)*(j-k)/(i-k)/(j-l))
  zeta = ((i-l)*(j-k)) / ((i-k)*(j-l))
  return abs(sqrt(abs(zeta))) * ((1*I) if zeta < 0 else 1)


def sin_f(i, j, k, l):
  #return sqrt((i-j)*(k-l)/(i-k)/(j-l))
  zeta = ((i-j)*(k-l)) / ((i-k)*(j-l))
  return abs(sqrt(abs(zeta))) * ((1*I) if zeta < 0 else 1)


################### Q ######################
# 123,134,145 --> 123,135,345 -- origin
# 135,125,124 --> 135,145,245 -- permutation
# 124,125,134 --> 134,145,245 -- algorithm
# 124,125,135 --> 135,145,245 -- this
Q = -1*matrix([
  [0,               0,              1],
  [ cos_f(1,4,2,5), sin_f(1,4,2,5), 0],
  [-sin_f(1,4,2,5), cos_f(1,4,2,5), 0]
])

print("Q=")
print(Q.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
print("")

################### P ######################
# 124,234,145 --> 123,134,145 -- origin
# 123,235,124 --> 135,125,124 -- permutation
# 123,134,235 --> 125,134,135 -- algorithm
# 123,124,235 --> 124,125,135 -- this
P = -1*matrix([
  [ 0             , 1,               0],
  [ cos_f(1,2,5,3), 0, -sin_f(1,2,5,3)],
  [ sin_f(1,2,5,3), 0,  cos_f(1,2,5,3)]
])

print("P=")
print(P.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
print("")

################### T ######################
# 125,253,345 --> 123,135,345 -- origin
# 134,345,245 --> 135,145,245 -- permutation
# 134,245,345 --> 135,145,245 -- algorithm
# 134,245,345 --> 135,145,245 -- this
T = matrix([
  [ cos_f(1,3,5,4), 0, -sin_f(1,3,5,4)],
  [ sin_f(1,3,5,4), 0,  cos_f(1,3,5,4)],
  [              0, 1,               0]
])

print("T^-1=")
print((T**-1).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
print("")

################### S ######################
# 125,234,245 --> 125,235,345 -- origin
# 134,235,234 --> 134,345,245 -- permutation
# 134,234,235 --> 134,245,345 -- algorithm
# 134,234,235 --> 134,245,345 -- this
S = matrix([
  [1,               0,               0],
  [0,  cos_f(2,4,3,5),  sin_f(2,4,3,5)],
  [0, -sin_f(2,4,3,5),  cos_f(2,4,3,5)]
])

print("S^-1=")
print((S**-1).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
print("")

################### R ######################
# 124,234,145 --> 125,234,245 -- origin
# 123,235,124 --> 134,235,234 -- permutation
# 123,124,235 --> 134,234,235 -- algorithm
# 123,124,235 --> 134,234,235 -- this
R = matrix([
  [ cos_f(1,3,2,4), sin_f(1,3,2,4), 0],
  [-sin_f(1,3,2,4), cos_f(1,3,2,4), 0],
  [              0, 0,              1]
])

print("R^-1=")
print((R**-1).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
print("")

m_l = Q*P
m_r = T*S*R

m_l = m_l.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
m_r = m_r.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)

print("### m left ###")
show(m_l)
print("### m right ###")
show(m_r)
print("")

print("Relation satisfied:", m_l == m_r)

print("")
#m_p = Q*P*(R**-1)*(S**-1)*(T**-1)
#m_p = T*S*R*(Q**-1)*(P**-1)
m_p = (R**-1)*(S**-1)*(T**-1)*Q*P
m_p = m_p.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
print(m_p)

'''
m_test = \
matrix([
  [1.7321*I,     -2.0,      0.0],
  [     2.0, 1.7321*I,      0.0],
  [     0.0,      0.0,      1.0]
]) * \
matrix([
  [     1.0,      0.0,      0.0],
  [     0.0, 1.7321*I,     -2.0],
  [     0.0,      2.0, 1.7321*I]
]) * \
matrix([
  [   1.2247,  0.7071*I,       0.0],
  [      0.0,       0.0,       1.0],
  [-0.7071*I,    1.2247,       0.0]
]) * \
matrix([
  [     0.0,      0.0,      1.0],
  [2.8284*I,      3.0,      0.0],
  [    -3.0, 2.8284*I,      0.0]
]) * \
matrix([
  [      0.0,       1.0,       0.0],
  [   1.2247,       0.0, -0.7071*I],
  [ 0.7071*I,       0.0,    1.2247]
])

print("")
show(m_test.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
'''