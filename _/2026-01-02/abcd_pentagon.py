from sage.all import *

a,b,c,d = var('a,b,c,d')


q = matrix([[a,b],[c,d]])
q_2 = q*q
print("q^2")
print(q_2)
print("")

eqs = [
  q_2[0][0] == 1,
  q_2[0][1] == 0,
  q_2[1][0] == 0,
  q_2[1][1] == 1
]

result = solve(eqs, a,b,c,d)
print(result)

# exit()

al_1 = matrix([[a,0,b],[c,0,d],[0,1,0]])
al_2 = matrix([[1,0,0],[0,a,b],[0,c,d]])
ar_1 = matrix([[a,b,0],[0,0,1],[c,d,0]])
ar_2 = matrix([[1,0,0],[0,a,b],[0,c,d]])
ar_3 = matrix([[a,b,0],[b,c,0],[0,0,1]])


lhs = al_2*al_1
rhs = ar_3*ar_2*ar_1

print(lhs)
print("")
print(rhs)

eqs = [
  lhs[0][0] == rhs[0][0],
  lhs[0][1] == rhs[0][1],
  lhs[0][2] == rhs[0][2],
  lhs[1][0] == rhs[1][0],
  lhs[1][1] == rhs[1][1],
  lhs[1][2] == rhs[1][2],
  lhs[2][0] == rhs[2][0],
  lhs[2][1] == rhs[2][1],
  lhs[2][2] == rhs[2][2]
]

result = solve(eqs, a,b,c,d)

print(result)

'''
diff = lhs - rhs

# переменные
vars = [a, b, c, d]

# матрица коэффициентов (9×4)
A = matrix(SR, [
    diff.apply_map(lambda e: e.derivative(v)).list()
    for v in vars
]).transpose()

# свободные члены
bvec = -vector(SR, diff.subs({a:0, b:0, c:0, d:0}).list())

# решение
solution = A.solve_right(bvec)

print(solution)
'''

'''
print("")
var('x')
result = solve(x*x + 1 == 0, x)
print(result)
'''