# I am trying to invent new dzetas here for the pachner 1-3 movement

from sage.all import *
from braids import knotting_max, knotting_min, braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty


# PR = PolynomialRing(QQ, 'a,b,c,p,q,s,z_9,z_8,z_7,z_6,z_5,z_4,z_3,z_2,z_1')
# PR.inject_variables()

a,b,c,p,q,s,z_9,z_8,z_7,z_6,z_5,z_4,z_3,z_2,z_1 = var('a,b,c,p,q,s,z_9,z_8,z_7,z_6,z_5,z_4,z_3,z_2,z_1')

a = p*(z_2-z_1)/(z_4-z_2)
b = q*(z_2-z_3)/(z_4-z_3)
c = s*(z_3-z_1)/(z_4-z_1)

denom = (z_4-z_2)*(z_4-z_3)*(z_4-z_1)

enum_1 = p*(z_2-z_1)*(z_4-z_3)*(z_4-z_1)
enum_2 = q*(z_2-z_3)*(z_4-z_2)*(z_4-z_1)
enum_3 = s*(z_3-z_1)*(z_4-z_3)*(z_4-z_2)

denom = denom.simplify_full()
enum_1 = enum_1.simplify_full()
enum_2 = enum_2.simplify_full()
enum_3 = enum_3.simplify_full()

show(enum_1)
show(enum_2)
show(enum_3)
show(denom)


print("enum")
enum = enum_1+enum_2+enum_3
show(enum)

# exit(0)

'''
eqs = [
  # I)
  #-z_1*z_2*z_3 == -(p*z_1*z_1 - p*z_1*z_2)*z_3,
  #-z_1*z_2*z_3 == q*z_1*z_2*z_2 - q*z_1*z_2*z_3,
  #-z_1*z_2*z_3 == -s*z_1*z_2*z_3 + s*z_2*z_3*z_3
  # II)
  #z_4**3 - z_1*z_2*z_3 == q*z_1*z_2**2 - q*z_1*z_2*z_3 - s*z_1*z_2*z_3 + s*z_2*z_3**2 - (p*z_1**2 - p*z_1*z_2)*z_3
  #-1*(z_1 + z_2 + z_3) == (q*z_2 - q*z_3) - (p*z_1 - p*z_2) - (s*z_1 - s*z_3)
  #(z_1*z_2 + (z_1 + z_2)*z_3) == (p*z_1**2 - p*z_1*z_2 + (p*z_1 - p*z_2)*z_3) - (q*z_1*z_2 + q*z_2**2 - (q*z_1 + q*z_2)*z_3) + (s*z_1*z_2 - s*z_3**2 + (s*z_1 - s*z_2)*z_3)
  #III)
  q*z_1*z_2**2 - q*z_1*z_2*z_3 - s*z_1*z_2*z_3 + s*z_2*z_3**2 - (p*z_1 - p*z_2)*z_4**2 - (s*z_1 - s*z_3)*z_4**2 + (q*z_2 - q*z_3)*z_4**2 - (p*z_1**2 - p*z_1*z_2)*z_3 + (p*z_1**2 - p*z_1*z_2 + (p*z_1 - p*z_2)*z_3)*z_4 - (q*z_1*z_2 + q*z_2**2 - (q*z_1 + q*z_2)*z_3)*z_4 + (s*z_1*z_2 - s*z_3**2 + (s*z_1 - s*z_2)*z_3)*z_4 == -z_1*z_2*z_3 - (z_1 + z_2 + z_3)*z_4**2 + z_4**3 + (z_1*z_2 + (z_1 + z_2)*z_3)*z_4
]

res = solve(eqs, p,q,s)

show(res)

print("Check")

part_1 = q*z_1*z_2**2 - q*z_1*z_2*z_3 - s*z_1*z_2*z_3 + s*z_2*z_3**2 - (p*z_1**2 - p*z_1*z_2)*z_3 + ((q*z_2 - q*z_3) - (p*z_1 - p*z_2) - (s*z_1 - s*z_3))*z_4**2 + ((p*z_1**2 - p*z_1*z_2 + (p*z_1 - p*z_2)*z_3) - (q*z_1*z_2 + q*z_2**2 - (q*z_1 + q*z_2)*z_3) + (s*z_1*z_2 - s*z_3**2 + (s*z_1 - s*z_2)*z_3))*z_4
part_2 = q*z_1*z_2**2 - q*z_1*z_2*z_3 - s*z_1*z_2*z_3 + s*z_2*z_3**2 - (p*z_1 - p*z_2)*z_4**2 - (s*z_1 - s*z_3)*z_4**2 + (q*z_2 - q*z_3)*z_4**2 - (p*z_1**2 - p*z_1*z_2)*z_3 + (p*z_1**2 - p*z_1*z_2 + (p*z_1 - p*z_2)*z_3)*z_4 - (q*z_1*z_2 + q*z_2**2 - (q*z_1 + q*z_2)*z_3)*z_4 + (s*z_1*z_2 - s*z_3**2 + (s*z_1 - s*z_2)*z_3)*z_4

print((part_1 - part_2).simplify_full())
'''
# exit(0)

p = z_2/(z_1 - z_2)
q = -z_3/(z_2 - z_3)
s = z_1/(z_1 - z_3)

#a = p*(z_2-z_1)/(z_4-z_2)
#b = q*(z_2-z_3)/(z_4-z_3)
#c = s*(z_3-z_1)/(z_4-z_1)

a = p*(z_2-z_1)/(-z_2)
b = q*(z_2-z_3)/(-z_3)
c = s*(z_3-z_1)/(-z_1)

res = a+b+c

print("Result")
show(res.simplify_full())


