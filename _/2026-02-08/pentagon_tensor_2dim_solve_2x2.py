# В этом файле я проверял уравнение пятиугольника для триангуляции пятиугольника.
# Треугльникам триангуляций сопоставлены двумерные векторные пространства V,
# а всей триангуляции пятиугольников - тензорное произведение этих пространств: V x V x V.
# Система уравнений решается не с помощью solve(), а с помощью алгоритма groebner.
# Результат: неизвестен, алгоритм падает из-за недостатка памяти внутри библиотеки.

from sage.all import *

# ---- переменные ----
#vars = [
#'x_11','x_12','x_13','x_14',
#'x_21','x_22','x_23','x_24',
#'x_31','x_32','x_33','x_34',
#'x_41','x_42','x_43','x_44'
#]
# var('x_11 x_22 x_23 x_32 x_33')
var('x_11 x_22 x_23 x_32 x_33 x_44')

#Rpoly = PolynomialRing(QQ, vars, order='lex')
#Rpoly.inject_variables()

# ---- матрица R ----
#R = matrix(Rpoly, [
#  [x_11, x_12, x_13, x_14],
#  [x_21, x_22, x_23, x_24],
#  [x_31, x_32, x_33, x_34],
#  [x_41, x_42, x_43, x_44],
#])
R = matrix(SR, [
[x_11, 0, 0, 0],
[0, x_22, x_23, 0],
[0, x_32, x_33, 0],
[0, 0, 0, x_44]
])

Id = matrix(SR, [[1,0],[0,1]])

# ---- тензорные произведения ----
A = Id.tensor_product(R)
B = R.tensor_product(Id)

P = A*B*A*B*A

# ---- формируем полиномиальную систему ----
polys = []

for i in range(int(P.nrows()/1)):
    for j in range(int(P.ncols()/1)):
        if i == j:
            polys.append(P[i,j] == 1)
        else:
            polys.append(P[i,j] == 0)

print("number of equations:", len(polys))
print()
for eq in polys:
  print(eq)



print()
print("solving...")

print()
result = solve(polys, x_11, x_22, x_23, x_32, x_33, x_44)
print(result)

