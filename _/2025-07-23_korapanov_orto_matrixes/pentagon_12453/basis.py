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
# 124,135,145 --> 124,134,345
Q = matrix([
  [1,              0,              0],
  [0, cos_f(1,3,5,4), sin_f(1,3,5,4)],
  [0,-sin_f(1,3,5,4), cos_f(1,3,5,4)]
])

print("Q=")
print(Q.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
print("")

################### P ######################
# 125,135,245 --> 124,135,145
P = matrix([
  [ cos_f(1,2,4,5), 0, -sin_f(1,2,4,5)],
  [ 0             , 1,               0],
  [ sin_f(1,2,4,5), 0,  cos_f(1,2,4,5)]
])

print("P=")
print(P.apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
print("")

################### T ######################
# 123,234,345 --> 124,234,345
T = matrix([
  [ cos_f(1,2,4,3), -sin_f(1,2,4,3), 0],
  [ sin_f(1,2,4,3),  cos_f(1,2,4,3), 0],
  [              0, 0,               1]
])

print("T^-1=")
print((T**-1).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
print("")

################### S ######################
# 123,235,245 --> 123,234,345
S = matrix([
  [1,               0,               0],
  [0,  cos_f(2,3,5,4),  sin_f(2,3,5,4)],
  [0, -sin_f(2,3,5,4),  cos_f(2,3,5,4)]
])

print("S^-1=")
print((S**-1).apply_map(lambda x: round(x.real(), 4) + round(x.imag(), 4) * I))
print("")

################### R ######################
# 125,135,245 --> 123,235,245
R = matrix([
  [ cos_f(1,2,5,3), sin_f(1,2,5,3), 0],
  [-sin_f(1,2,5,3), cos_f(1,2,5,3), 0],
  [              0, 0,              1],
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
