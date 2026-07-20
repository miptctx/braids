# В этом файле я проверял уравнение пятиугольника с тензорами для матриц размера 1х1
# Результат: нашлось 3 нетривиальных значения, которые удовлетворяют требуемому тождеству.
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

P = A*B*A*B*A

print("")
print('P')
show(P)

Identity = Id.tensor_product(Id).tensor_product(Id)
print("")
print("Identity")
show(Identity)

eqs = [
  P[0][0] == Identity[0][0]
]

print("")
print("eqs")
show(eqs)

res = solve(eqs, x)
print("")
show(res)

print("")
print("test pentagon")
P = (A*B*A*B*A).simplify_full().subs({x: 1/4*sqrt(5) + 1/4*I*sqrt(2*sqrt(5) + 10) - 1/4})
print(P[0][0])
