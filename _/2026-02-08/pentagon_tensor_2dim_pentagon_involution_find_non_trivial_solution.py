# Здесь пытались найти нетривиальное решение в окрестности тривиального R = I. Ничего не нашлось.
# Решили проверить, есть ли вообще какие-либо еще решения или оно опять только одно?
# Результат: По мнению ИИ вывод rank(J at I) = 16 означает, что есть только одно изолированное решение R=I, а в окрестности решений нет.
# Продолжение в файле pentagon_tensor_2dim_pentagon_no_involution_find_non_trivial_solution.py

from sage.all import *
from sympy import nsolve
import random

var('x_11 x_12 x_13 x_14')
var('x_21 x_22 x_23 x_24')
var('x_31 x_32 x_33 x_34')
var('x_41 x_42 x_43 x_44')

vars = [x_11,x_12,x_13,x_14,
        x_21,x_22,x_23,x_24,
        x_31,x_32,x_33,x_34,
        x_41,x_42,x_43,x_44]

R = matrix([
  [x_11, x_12, x_13, x_14],
  [x_21, x_22, x_23, x_24],
  [x_31, x_32, x_33, x_34],
  [x_41, x_42, x_43, x_44],
])

Id4 = identity_matrix(4)
Id2 = identity_matrix(2)

A = Id2.tensor_product(R)
B = R.tensor_product(Id2)
P = A*B*A*B*A
Identity = Id2.tensor_product(Id2).tensor_product(Id2)

eqns = []

RR = R*R
for i in range(4):
    for j in range(4):
        eqns.append(RR[i,j] - Id4[i,j])

for i in range(Identity.nrows()):
    for j in range(Identity.ncols()):
        eqns.append(P[i,j] - Identity[i,j])

J = jacobian(eqns, vars)

subs_I = {
    x_11:1,x_12:0,x_13:0,x_14:0,
    x_21:0,x_22:1,x_23:0,x_24:0,
    x_31:0,x_32:0,x_33:1,x_34:0,
    x_41:0,x_42:0,x_43:0,x_44:1
}

J0 = J.subs(subs_I).n()
print("rank(J at I) =", J0.rank())

exit()

# --- базовое решение R = I ---
base = [1,0,0,0,
        0,1,0,0,
        0,0,1,0,
        0,0,0,1]

solutions = []

for trial in range(10):
    # маленькое комплексное возмущение
    start = [base[i] + 1e-2*(random.random()+random.random()*I) for i in range(16)]
    try:
        sol = nsolve(eqns, vars, start, tol=1e-12, maxsteps=20, prec=40)
        subs = dict(zip(vars, sol))
        Rsol = matrix(4,4,[subs[v] for v in vars])
        solutions.append(Rsol)
        print(f"✅ Найдено решение {len(solutions)}")
    except:
        print("❌ не сошлось")

# --- вывод ---
print("\nНайденные решения:")
for Rsol in solutions:
    print(Rsol)
    print()
