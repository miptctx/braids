# В этом файле я проверял чему будет равен аннот для матриц из книги Томотада

from sage.all import *

var('A')

n = matrix([[0, A, -A**(-1), 0]])
print("n")
show(n)


R = matrix([
  [A, 0, 0 ,0],
  [0, 0, A**(-1), 0],
  [0, A**(-1), A - A**(-3), 0],
  [0, 0, 0, A]
])
print("")
print("R")
show(R)


m = (n*R).simplify_full()

print("")
print("n*R")
show(m)

print("")
print("-A^(-3)*n")
m = (-A**(-3)*n).simplify_full()
show(m)
