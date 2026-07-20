# В этом файле я делал то же самое, что и в файле pentagon_tensor_1dim_pentagon.py,
# только с неединиыной правой частью уравнения. Результат такой же, как и в упомянутом файле.
# Вопрос: верно ли, что R-матрица должна быть размера 1x1?.
# Получается, что любые 5 последовательных флипа (не только в пятиугольнике) дают единицу?

from sage.all import *

var('x')

R = matrix([[x]])

Id = matrix([[1]])

A = Id.tensor_product(R)
B = R.tensor_product(Id)

print("A")
show(A)
print("B")
show(B)

lhs = B*A*B

rhs = Id.tensor_product(R**-2)

print("")
print('lhs')
show(lhs[0][0])
print("")
print('rhs')
show(rhs[0][0])

eqs = [
  lhs[0][0] == rhs[0][0]
]

res = solve(eqs, x)
print("")
show(res)

print("")
print("test pentagon")
P = (A*B*A*B*A).simplify_full().subs({x: 1/4*sqrt(5) + 1/4*I*sqrt(2*sqrt(5) + 10) - 1/4})
print(P[0][0])
