# В этом файле я проверял уравнение пятиугольника для триангуляции пятиугольника.
# Треугльникам триангуляций сопоставлены двумерные векторные пространства V,
# а всей триангуляции пятиугольников - тензорное произведение этих пространств: V x V x V.
# Переменные использованы из кольца многочленов от 16 переменных.
# Результат: Переменные не могут быть с кольца, они должны быть объявлены через var(),
# поэтому программа некорректна: https://doc.sagemath.org/html/en/tutorial/tour_algebra.html

from sage.all import *

#var('x_11, x_12, x_13, x_14')
#var('x_21, x_22, x_23, x_24')
#var('x_31, x_32, x_33, x_34')
#var('x_41, x_42, x_43, x_44')

#R = matrix([
#  [x_11, x_12, x_13, x_14],
#  [x_21, x_22, x_23, x_24],
#  [x_31, x_32, x_33, x_34],
#  [x_41, x_42, x_43, x_44],
#])

PR = PolynomialRing(QQ, 16, "x_")

PR.inject_variables()

R = matrix([
  [x_0, x_1,  x_2,  x_3],
  [x_4, x_5,  x_6,  x_7],
  [x_8, x_9,  x_10, x_11],
  [x_12, x_13, x_14, x_15],
])

Id = matrix([[1, 0], [0, 1]])

A = Id.tensor_product(R)
B = R.tensor_product(Id)

print("A")
show(A)
print("")
print("B")
show(B)

P = A*B*A*B*A

#print("")
#print('P')
#show(P)

Identity = Id.tensor_product(Id).tensor_product(Id)
print("")
print("Identity")
show(Identity)

eqs = []

R_inv = R.inverse()

R_check = (R*R_inv)#.simplify_full()
print("")
print("R_check:")
show(R_check)

for i in range(R.nrows()):
  for j in range(R.ncols()):
    eqs.append(R[i][j] == R_inv[i][j])

for i in range(Identity.nrows()):
  for j in range(Identity.ncols()):
    eqs.append(P[i][j] == Identity[i][j])


print("")
print("eqs")
show(eqs)

res = solve(eqs, x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9, x_10, x_11, x_12, x_13, x_14, x_15)
print("")
show(res)

exit()
print("")
print("test pentagon")
# P = (A*B*A*B*A).simplify_full().subs({x: 1/4*sqrt(5) + 1/4*I*sqrt(2*sqrt(5) + 10) - 1/4})
# print(P[0][0])
P = A*B*A*B*A
show(P)
