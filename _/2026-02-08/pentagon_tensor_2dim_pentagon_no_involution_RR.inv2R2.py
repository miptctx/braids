# В этом файле нет инволюцию для матрицы R и изменили уравнение пятиугольника добавив обратные матрицы:
# (I⊗R)(R^-1⊗I)(I⊗R^-1)(R⊗I)(I⊗R)=I
# Проверили существование других решений в окрестности изолированого, других решений нет.
# Результат: по мнению ИИ вывод rank(J at I) = 16 означает, что есть только одно изолированное решение R=I

from sage.all import *

# --- переменные ---
var('x_11 x_12 x_13 x_14')
var('x_21 x_22 x_23 x_24')
var('x_31 x_32 x_33 x_34')
var('x_41 x_42 x_43 x_44')

vars = [x_11,x_12,x_13,x_14,
        x_21,x_22,x_23,x_24,
        x_31,x_32,x_33,x_34,
        x_41,x_42,x_43,x_44]

# --- матрица R ---
R = matrix([
  [x_11, x_12, x_13, x_14],
  [x_21, x_22, x_23, x_24],
  [x_31, x_32, x_33, x_34],
  [x_41, x_42, x_43, x_44],
])

Id2 = identity_matrix(2)

# --- операторы ---
A1 = Id2.tensor_product(R)
A2 = R.inverse().tensor_product(Id2)
A3 = Id2.tensor_product(R.inverse())
A4 = R.tensor_product(Id2)
A5 = Id2.tensor_product(R)

P = A1*A2*A3*A4*A5
Identity = Id2.tensor_product(Id2).tensor_product(Id2)

# --- уравнения ---
eqns = []
for i in range(Identity.nrows()):
    for j in range(Identity.ncols()):
        eqns.append(P[i,j] - Identity[i,j])

# --- подстановка R = I ---
subs_I = {
x_11:1,x_12:0,x_13:0,x_14:0,
x_21:0,x_22:1,x_23:0,x_24:0,
x_31:0,x_32:0,x_33:1,x_34:0,
x_41:0,x_42:0,x_43:0,x_44:1
}

# --- якобиан ---
J = jacobian(eqns, vars)
J0 = J.subs(subs_I)

print("rank(J at I) =", J0.rank())
