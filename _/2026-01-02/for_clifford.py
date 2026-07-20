from sage.all import *


def _show(*args):
  show(latex(*args))


e_1, e_2 = var('e_1,e_2')

k = 1/sqrt(2)

a = k*e_1
b = k*e_2
c = k*e_2
d = k*-e_1

q = matrix([[a,b],[c,d]])
q_2 = q*q
print("q^2")
_show(q_2)
print("")

al_1 = matrix([[a,0,b],[c,0,d],[0,1,0]])
al_2 = matrix([[1,0,0],[0,a,b],[0,c,d]])
ar_1 = matrix([[a,b,0],[0,0,1],[c,d,0]])
ar_2 = matrix([[1,0,0],[0,a,b],[0,c,d]])
ar_3 = matrix([[a,b,0],[b,c,0],[0,0,1]])


lhs = al_2*al_1
rhs = ar_3*ar_2*ar_1

print('lhs')
_show(lhs)
print("")
print('rhs')
_show(rhs)
