# В этом файле пытались найти какой-то численное решение системы уравнений.
# Ни одного не нашлось. ИИ предложил проверить тривиальные варианты прямой подстановкой.
# Результат: по мнению ИИ вывод rank(J at I) = 16 означает, что есть как минимум одно решение: R=I
# Продолжение в файлах:
#   - pentagon_tensor_2dim_pentagon_involution_find_non_trivial_solution.py
#   - pentagon_tensor_2dim_pentagon_no_involution_find_non_trivial_solution.py


from sage.all import *
import random
from sympy import nsolve

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

# --- вместо R = R^{-1} используем R*R = I ---
RR = R*R
for i in range(4):
    for j in range(4):
        eqns.append(RR[i,j] - Id4[i,j])

# --- условия на P ---
for i in range(Identity.nrows()):
    for j in range(Identity.ncols()):
        eqns.append(P[i,j] - Identity[i,j])

subs = {
  x_11:1,x_12:0,x_13:0,x_14:0,
  x_21:0,x_22:1,x_23:0,x_24:0,
  x_31:0,x_32:0,x_33:1,x_34:0,
  x_41:0,x_42:0,x_43:0,x_44:1
}
print([eq.subs(subs).simplify_full() for eq in eqns])

subs = {
x_11:-1,x_12:0,x_13:0,x_14:0,
x_21:0,x_22:-1,x_23:0,x_24:0,
x_31:0,x_32:0,x_33:-1,x_34:0,
x_41:0,x_42:0,x_43:0,x_44:-1
}
print([eq.subs(subs).simplify_full() for eq in eqns])

exit()

print("Всего уравнений:", len(eqns))

# --- несколько попыток со случайными стартами ---
for attempt in range(10):
    start = [complex(random.uniform(-1,1), random.uniform(-1,1)) for _ in range(16)]
    try:
        sol = nsolve(eqns, vars, start, tol=1e-12, maxsteps=40, prec=40)
        print("\n✅ Найдено решение на попытке", attempt+1)
        break
    except Exception as e:
        print("❌ Попытка", attempt+1, "не сошлась")
else:
    raise RuntimeError("Не удалось найти решение")

# --- вывод ---
subs = dict(zip(vars, sol))
for v in vars:
    print(v, "=", subs[v])

print("\nМаксимальный остаток:")
print(max(abs(eq.subs(subs).n()) for eq in eqns))
