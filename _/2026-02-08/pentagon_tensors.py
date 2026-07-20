from sage.all import *

var('q')

"""
# Матрица Хекке
R = matrix([
  [q,0,        0,0],
  [0,0,        1,0],
  [0,1,q-q**(-1),0],
  [0,0,        0,q]
])
"""

"""
# Семейство Белавина–Дринафельда
R = matrix([
  [1,   0,   0, 0],
  [0,   q, 1-q, 0],
  [0, 1+q,  -q, 0],
  [0,   0,   0, 1]
])
"""

"""
# Антисимметрическое (суперсимметрическое) решение
R = matrix([
  [1, 0, 0,0],
  [0, 0,-1,0],
  [0,-1, 0,0],
  [0, 0, 0,1]
])
"""

"""
# Джордановское нетривиальное решение
R = matrix([
  [1, 0, 0, 0],
  [0, 1, 1, 0],
  [0, 0, 1, 0],
  [0, 0, 0, 1]
])
"""

'''
# Оператор перестановки
R = matrix([
  [1, 0, 0, 0],
  [0, 0, 1, 0],
  [0, 1, 0, 0],
  [0, 0, 0, 1]
])
'''


print("R^2")
R_2 = (R*R)#.simplify_full()
show(R_2)


Id = matrix([
  [1,0],
  [0,1]
])

m_1 = Id.tensor_product(R)
m_2 = R.tensor_product(Id)


#print("")
#print("m_1")
#show(m_1)

#print("")
#print("m_2")
#show(m_2)

m = m_1*m_2*m_1*m_2*m_1

#m = m.simplify_full()

print("")
print("pentagon matrix")
show(m)

#"pentagon matrix q = 1"
#show(m.subs({q:1}))
