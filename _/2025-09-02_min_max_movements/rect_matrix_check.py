from sage.all import *

z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5,z_6")

a,b,c,p,q,r = var("a,b,c,p,q,r")

def _show(*args):
  show(latex(*args))
  #show(*args)

'''
a = p/(z_4-z_2)
b = q/(z_4-z_3)
c = r/(z_4-z_1)

eqs = [
  p+q+r==z_4,
  p*z_1*z_3 + q*z_1*z_2 + r*z_2*z_3 == z_2*z_3*z_4 + z_1*z_2*z_4 + z_1*z_3*z_4 - z_1*z_2*z_3,
  (p+r)*z_3 + (p+q)*z_1 + (q+r)*z_2 == z_4*z_3 + z_1*z_4 + z_2*z_4
]

result = solve(eqs, p,q,r)

show(result)
'''

p = (z_1*z_2*z_3 - z_1*z_3*z_4)/(z_1*z_2 - z_2**2 - (z_1 - z_2)*z_3)
q = -(z_1*z_2*z_3 - z_1*z_2*z_4)/(z_1*z_2 - (z_1 + z_2)*z_3 + z_3**2)
r = -(z_1*z_2*z_3 - z_2*z_3*z_4)/(z_1**2 - z_1*z_2 - (z_1 - z_2)*z_3)

a = p/(z_4-z_2)
b = q/(z_4-z_3)
c = r/(z_4-z_1)

show(a)
show(b)
show(c)

_show(a.simplify_full())
_show(b.simplify_full())
_show(c.simplify_full())


a = -z_1*z_3/(z_1*z_2 - z_2**2 - z_1*z_3 + z_2*z_3)
b = z_1*z_2/(z_1*z_2 - z_1*z_3 - z_2*z_3 + z_3**2)
c = z_2*z_3/(z_1**2 - z_1*z_2 - z_1*z_3 + z_2*z_3)
print("")
_show(a)
_show(b)
_show(c)