from sage.all import *


def cos_f(i, j, k, l):
  #return sqrt((i-l)*(j-k)/(i-k)/(j-l))
  zeta = ((i-l)*(j-k)) / ((i-k)*(j-l))
  return abs(sqrt(abs(zeta))) * ((-1*I) if zeta < 0 else 1)


def sin_f(i, j, k, l):
  #return sqrt((i-j)*(k-l)/(i-k)/(j-l))
  zeta = ((i-j)*(k-l)) / ((i-k)*(j-l))
  return abs(sqrt(abs(zeta))) * ((-1*I) if zeta < 0 else 1)


################### Q ######################
# 123,125,134 --> 124,125,234
Q = matrix([
  [ cos_f(1,2,3,4), 0, sin_f(1,2,3,4)],
  [0,               1,              0],
  [-sin_f(1,2,3,4), 0, cos_f(1,2,3,4)]
])

print("Q=")
print(Q.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
print("")

################### P ######################
# 134,135,235 --> 123,125,134
P = matrix([
  [ 0, cos_f(1,3,2,5), -sin_f(1,3,2,5)],
  [ 0, sin_f(1,3,2,5),  cos_f(1,3,2,5)],
  [ 1             , 0,               0]
])

print("P=")
print(P.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
print("")

################### T ######################
# 145,234,245 --> 124,125,234
T = matrix([
  [ cos_f(1,4,2,5), 0, -sin_f(1,4,2,5)],
  [ sin_f(1,4,2,5), 0,  cos_f(1,4,2,5)],
  [              0, 1,               0]
])

print("T^-1=")
print((T**-1).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
print("")

################### S ######################
# 145,235,345 --> 145,234,245
S = matrix([
  [1,               0,               0],
  [0,  cos_f(2,3,4,5),  sin_f(2,3,4,5)],
  [0, -sin_f(2,3,4,5),  cos_f(2,3,4,5)]
])

print("S^-1=")
print((S**-1).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
print("")

################### R ######################
# 134,135,235 --> 145,235,345
R = matrix([
  [ cos_f(1,4,3,5), sin_f(1,4,3,5), 0],
  [              0, 0,              1],
  [-sin_f(1,4,3,5), cos_f(1,4,3,5), 0],
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
print("Det:", m_l.det())
print("Trace:", m_l.trace())
print("### m right ###")
show(m_r)
print("Det:", m_r.det())
print("Trace:", m_r.trace())
print("")

print("Relation satisfied:", m_l == m_r)

print("")
#m_p = Q*P*(R**-1)*(S**-1)*(T**-1)
#m_p = T*S*R*(Q**-1)*(P**-1)
m_p = (R**-1)*(S**-1)*(T**-1)*Q*P
m_p = m_p.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I)
print(m_p)
