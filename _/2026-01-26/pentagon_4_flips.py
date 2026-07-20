# В этом файле я взял уравнение пятиугольника из своей статьи и заменил элементы матриц с дзетами формальными переменными.
# После этого я попытался выразить элементы матрицы пятого флипа через элементы остальных четырех матриц.
# Но оказалось, что такая система не имеет решений.


from sage.all import *

var('a_11 a_12 a_21 a_22')
var('b_11 b_12 b_21 b_22')
var('c_11 c_12 c_21 c_22')
var('d_11 d_12 d_21 d_22')
var('x_11 x_12 x_21 x_22')

m_1 = matrix([
  [1,   0,   0],
  [0,a_11,a_12],
  [0,a_21,a_22]
])

m_2 = matrix([
  [b_11,b_12,0],
  [b_21,b_22,0],
  [0,   0,   1]
])

m_3 = matrix([
  [1,   0,   0],
  [0,c_11,c_12],
  [0,c_21,c_22]
])

m_4 = matrix([
  [d_11,0,d_12],
  [d_21,0,d_22],
  [0,   1,   0]
])

m_5 = matrix([
  [x_11,0, x_12],
  [x_21,0, x_22],
  [0,   1,    0]
])

m = m_5*m_4*m_3*m_2*m_1

print("Pentagon matrix")
show(m)

eqs = [
  m[0][0] == 1,
  m[0][1] == 0,
  m[0][2] == 0,
  m[1][0] == 0,
  m[1][1] == 1,
  m[1][2] == 0,
  m[2][0] == 0,
  m[2][1] == 0,
  m[2][2] == 1
]

print("")
print("eqs")
show(eqs)

result = solve(eqs, x_11, x_12, x_21, x_22)
print("")
print("x_11, x_12, x_21, x_22")
show(result)

result = solve(eqs, a_11, a_12, a_21, a_22)
print("")
print("a_11, a_12, a_21, a_22")
show(result)

result = solve(eqs, b_11, b_12, b_21, b_22)
print("")
print("b_11, b_12, b_21, b_22")
show(result)

result = solve(eqs, c_11, c_12, c_21, c_22)
print("")
print("c_11, c_12, c_21, c_22")
show(result)

result = solve(eqs, d_11, d_12, d_21, d_22)
print("")
print("d_11, d_12, d_21, d_22")
show(result)

exit()

m = m_4*m_3*m_2*m_1
m = m.inverse()
print("")
print("inverse")
show(m)
