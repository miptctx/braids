# В этом файле я проверял, что если A = (Id x R), то A^-2 == (Id x R^-2).
# Результат: это верно.

from sage.all import *

var('a_11,a_12,a_13,a_14')
var('a_21,a_22,a_23,a_24')
var('a_31,a_32,a_33,a_34')
var('a_41,a_42,a_43,a_44')

R = matrix([
  [a_11, a_12, a_13, a_14],
  [a_21, a_22, a_23, a_24],
  [a_31, a_32, a_33, a_34],
  [a_41, a_42, a_43, a_44]
])

Id = matrix([
  [1,0],
  [0,1]
])

A = Id.tensor_product(R)

A_2 = (A**(-2)).simplify_full()
print("A**(-2)")
show(A_2)


R_2 = (R**(-2)).simplify_full()
IdR_2 = Id.tensor_product(R_2)
print("Id x R**(-2)")
show(IdR_2)


print("")
print("Are matrices equal: ", A_2 == IdR_2)
