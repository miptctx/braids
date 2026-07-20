# В этом файле я проверял уравнение пятиугольника для триангуляции пятиугольника.
# Треугльникам триангуляций сопоставлены двумерные векторные пространства V,
# а всей триангуляции пятиугольников - тензорное произведение этих пространств: V x V x V.
# Инволюцию пока закоментировал...
# Результат: пока неизвестен, т.к. алгоритм падает из-за недостатка памяти.

from sage.all import *

maxima.eval("lisp (room)")

var('x_11, x_12, x_13, x_14')
var('x_21, x_22, x_23, x_24')
var('x_31, x_32, x_33, x_34')
var('x_41, x_42, x_43, x_44')

R = matrix([
  [x_11, x_12, x_13, x_14],
  [x_21, x_22, x_23, x_24],
  [x_31, x_32, x_33, x_34],
  [x_41, x_42, x_43, x_44],
])

print("R")
show(R)

#print("")
#print('P')
#show(P)

#Identity = Id.tensor_product(Id).tensor_product(Id)
#print("")
#print("Identity")
#show(Identity)

eqs = []

#R_inv = R.inverse()
#R_check = (R*R_inv).simplify_full()
#print("")
#print("R_check:")
#show(R_check)

# Involution requirement
#R_sqrt = R*R
#for i in range(R.nrows()):
#  for j in range(R.ncols()):
#    # eqs.append(R[i][j] == R_inv[i][j])
#    if i == j:
#      eqs.append(R_sqrt[i][j] == 1)
#    else:
#      eqs.append(R_sqrt[i][j] == 0)


Id = matrix([[1, 0], [0, 1]])

A = Id.tensor_product(R)
B = R.tensor_product(Id)

print()
print("A")
show(A)
print("")
print("B")
show(B)

P = A*B*A*B*A

# Pentagon requirement
#for i in range(Identity.nrows()):
#  for j in range(Identity.ncols()):
#    eqs.append(P[i][j] == Identity[i][j])
for i in range(P.nrows()):
  for j in range(P.ncols()):
    if i == j:
      eqs.append(P[i][j] == 1)
    else:
      eqs.append(P[i][j] == 0)


print("")
print(f"eqs length: {len(eqs)}:")
show(eqs)

print()
print("solving...")
res = solve(eqs, x_11, x_12, x_13, x_14, x_21, x_22, x_23, x_24, x_31, x_32, x_33, x_34, x_41, x_42, x_43, x_44, solution_dict=True)
print("")
show(res)

#exit()

#print("")
#print("test pentagon")
#P = (A*B*A*B*A).simplify_full().subs({x: 1/4*sqrt(5) + 1/4*I*sqrt(2*sqrt(5) + 10) - 1/4})
#print(P[0][0])
