from sage.all import *

A,B,C,D,E = var("A,B,C,D,E")

a,b,c,d,e,x,y = 1,2,3,4,5,6,7 # var("a,b,c,d,e,x,y")

z = (x*d + c*e)/y
t = (b*z + a*c)/x
u = (e*t + a*d)/z
v = (c*u + b*d)/t
w = (a*v + e*b)/u

# 14,24 --> 13,14
M_1 = matrix([
  [0, z],
  [1, 0]
])

# 13,14 --> 13,35
M_2 = matrix([
  [1, 0],
  [0, t]
])

# 13,35 --> 25,35
M_3 = matrix([
  [u, 0],
  [0, 1]
])

# 25,35 --> 24,25
M_4 = matrix([
  [0, v],
  [1, 0]
])

# 24,25 --> 14,24
M_5 = matrix([
  [0, w],
  [1, 0]
])


result = M_5*M_4*M_3*M_2*M_1

show(result)
show(result.det())
